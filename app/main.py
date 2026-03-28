from typing import Optional
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from app.db import get_connection
from app.schemas import EventCreate
from app.extras import router as extras_router

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
app.include_router(extras_router)

# Get main site for checking the connection
@app.get("/")
def root():
    return {"message": "SportRadar backend is running"}

# Test database connection
@app.get("/test-db")
def test_db():
    try:
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("SELECT 'Database connected successfully' FROM dual")
        result = cursor.fetchone()

        cursor.close()
        connection.close()

        return {"message": result[0]}
    except Exception as e:
        return {"error": str(e)} # Get error if user, password or dns is wrong 


# Check whether a record exists in a given table
def record_exists(cursor, table_name: str, record_id: int) -> bool:
    query = f"SELECT COUNT(*) FROM {table_name} WHERE id = :id"
    cursor.execute(query, {"id": record_id})
    result = cursor.fetchone()
    return result[0] > 0

# Check IDs by given name
def get_form_options():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id, name FROM leagues ORDER BY name")
    leagues = [{"id": row[0], "name": row[1]} for row in cursor.fetchall()]

    cursor.execute("SELECT id, name FROM teams ORDER BY name")
    teams = [{"id": row[0], "name": row[1]} for row in cursor.fetchall()]

    cursor.execute("SELECT id, name FROM venues ORDER BY name")
    venues = [{"id": row[0], "name": row[1]} for row in cursor.fetchall()]

    cursor.close()
    conn.close()

    return leagues, teams, venues

# Get events from dataset
@app.get("/events")
def get_events(
    sport: Optional[str] = None,
    league: Optional[str] = None,
    date: Optional[str] = None,
    team: Optional[str] = None,
    venue: Optional[str] = None
):
    try:
        # Open database connection
        connection = get_connection()
        cursor = connection.cursor()

        # Base query for fetching event data
        query = """
            SELECT
                e.id,
                e.title,
                e.event_date,
                e.event_time,
                e.description,
                l.name AS league_name,
                s.name AS sport_name,
                ht.name AS home_team_name,
                at.name AS away_team_name,
                v.name AS venue_name,
                v.city AS venue_city,
                v.country AS venue_country
            FROM events e
            JOIN leagues l ON e.league_id = l.id
            JOIN sports s ON l.sport_id = s.id
            JOIN teams ht ON e.home_team_id = ht.id
            JOIN teams at ON e.away_team_id = at.id
            JOIN venues v ON e.venue_id = v.id
            WHERE 1 = 1
        """

        params = {}

        # Apply sport filter if provided
        if sport:
            query += " AND INSTR(LOWER(s.name), LOWER(:sport)) > 0"
            params["sport"] = sport.strip()

        # Apply league filter if provided
        if league:
            query += " AND INSTR(LOWER(l.name), LOWER(:league)) > 0"
            params["league"] = league.strip()

        # Apply date filter if provided
        if date:
            query += " AND e.event_date = TO_DATE(:date_value, 'YYYY-MM-DD')"
            params["date_value"] = date.strip()

        # Apply team filter if provided
        if team:
            query += """
                AND (
                    INSTR(LOWER(ht.name), LOWER(:team)) > 0
                    OR INSTR(LOWER(at.name), LOWER(:team)) > 0
                )
            """
            params["team"] = team.strip()

        # Apply venue filter if provided
        if venue:
            query += " AND INSTR(LOWER(v.name), LOWER(:venue)) > 0"
            params["venue"] = venue.strip()

        # Order results by newest inserted event first
        query += " ORDER BY e.id DESC"

        cursor.execute(query, params)
        rows = cursor.fetchall()

        # Return a message if no events match the filters
        if not rows:
            cursor.close()
            connection.close()
            return {"message": "No events found for the given filters", "events": []}

        # Convert query results into JSON-friendly format
        events = []
        for row in rows:
            events.append({
                "id": row[0],
                "title": row[1],
                "event_date": str(row[2]),
                "event_time": str(row[3]),
                "description": row[4],
                "league": row[5],
                "sport": row[6],
                "home_team": row[7],
                "away_team": row[8],
                "venue": row[9],
                "city": row[10],
                "country": row[11]
            })

        cursor.close()
        connection.close()

        return {"events": events}

    except Exception as e:
        return {"error": str(e)}
    
# Get single event from dataset
@app.get("/events/{event_id}")
def get_event_by_id(event_id: int):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        # Fetch one event by its ID
        query = """
            SELECT
                e.id,
                e.title,
                e.event_date,
                e.event_time,
                e.description,
                l.name AS league_name,
                s.name AS sport_name,
                ht.name AS home_team_name,
                at.name AS away_team_name,
                v.name AS venue_name,
                v.city AS venue_city,
                v.country AS venue_country
            FROM events e
            JOIN leagues l ON e.league_id = l.id
            JOIN sports s ON l.sport_id = s.id
            JOIN teams ht ON e.home_team_id = ht.id
            JOIN teams at ON e.away_team_id = at.id
            JOIN venues v ON e.venue_id = v.id
            WHERE e.id = :event_id 
        """

        cursor.execute(query, {"event_id": event_id})
        row = cursor.fetchone()

        cursor.close()
        connection.close()

        # Return message if event does not exist
        if not row:
            return {"error": "Event not found"}

        # Convert database row into JSON-friendly format
        event = {
            "id": row[0],
            "title": row[1],
            "event_date": str(row[2]),
            "event_time": str(row[3]),
            "description": row[4],
            "league": row[5],
            "sport": row[6],
            "home_team": row[7],
            "away_team": row[8],
            "venue": row[9],
            "city": row[10],
            "country": row[11]
        }

        return {"event": event}

    except Exception as e:
        return {"error": str(e)}


# Insert a new event into the database
@app.post("/events")
def create_event(event: EventCreate):
    try:
        # Prevent same team from being selected twice
        if event.home_team_id == event.away_team_id:
            return {"error": "Home team and away team cannot be the same"}
        
        connection = get_connection()
        cursor = connection.cursor()

        # Check if related records exist
        if not record_exists(cursor, "leagues", event.league_id):
            return {"error": "League not found"}

        if not record_exists(cursor, "teams", event.home_team_id):
            return {"error": "Home team not found"}

        if not record_exists(cursor, "teams", event.away_team_id):
            return {"error": "Away team not found"}

        if not record_exists(cursor, "venues", event.venue_id):
            return {"error": "Venue not found"}
        
        # Insert new event into database
        query = """
            INSERT INTO events (
                id,
                title,
                event_date,
                event_time,
                description,
                league_id,
                home_team_id,
                away_team_id,
                venue_id
            )
            VALUES (
                events_seq.NEXTVAL,
                :title,
                TO_DATE(:event_date, 'YYYY-MM-DD'),
                :event_time,
                :description,
                :league_id,
                :home_team_id,
                :away_team_id,
                :venue_id
            )
        """

        cursor.execute(query, {
            "title": event.title,
            "event_date": event.event_date,
            "event_time": event.event_time,
            "description": event.description,
            "league_id": event.league_id,
            "home_team_id": event.home_team_id,
            "away_team_id": event.away_team_id,
            "venue_id": event.venue_id
        })

        connection.commit()

        cursor.close()
        connection.close()

        return {"message": "Event created successfully"}

    except Exception as e:
        return {"error": str(e)}
    
# Frontend HTML
@app.get("/ui/events", response_class=HTMLResponse)
def events_page(request: Request, sport: str = None, search: str = None):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
        SELECT
            e.id,
            e.title,
            s.name AS sport,
            l.name AS league,
            e.event_date,
            e.event_time,
            ht.name AS home_team,
            at.name AS away_team,
            v.name AS venue,
            v.city AS city,
            v.country AS country
        FROM events e
        JOIN leagues l ON e.league_id = l.id
        JOIN sports s ON l.sport_id = s.id
        JOIN teams ht ON e.home_team_id = ht.id
        JOIN teams at ON e.away_team_id = at.id
        JOIN venues v ON e.venue_id = v.id
    """

    conditions = []
    params = {}

    if sport:
        conditions.append("s.name = :sport")
        params["sport"] = sport

    if search:
        conditions.append("""
            (
                INSTR(LOWER(ht.name), LOWER(:search)) > 0
                OR INSTR(LOWER(at.name), LOWER(:search)) > 0
                OR INSTR(LOWER(l.name), LOWER(:search)) > 0
            )
        """)
        params["search"] = search

    if conditions:
        query += " WHERE " + " AND ".join(conditions)

    query += " ORDER BY s.id, e.event_date, e.event_time"

    cursor.execute(query, params)
    rows = cursor.fetchall()

    events = []
    for row in rows:
        events.append({
            "id": row[0],
            "title": row[1],
            "sport": row[2],
            "league": row[3],
            "event_date": str(row[4])[:10],
            "event_time": str(row[5]),
            "home_team": row[6],
            "away_team": row[7],
            "venue": row[8],
            "city": row[9],
            "country": row[10],
        })

    cursor.close()
    conn.close()

    return templates.TemplateResponse(
        request,
        "events.html",
        {
            "events": events,
            "event_count": len(events),
            "active_sport": sport,
            "search": search or ""
        }
    )

# Get event from form
@app.get("/ui/events/new", response_class=HTMLResponse)
def new_event_page(request: Request):
    leagues, teams, venues = get_form_options()

    return templates.TemplateResponse(
        request,
        "event_form.html",
        {
            "success_message": None,
            "error_message": None,
            "leagues": leagues,
            "teams": teams,
            "venues": venues
        }
    )

# Add new event getting from form
@app.post("/ui/events/new", response_class=HTMLResponse)
def create_event_from_form(
    request: Request,
    title: str = Form(...),
    event_date: str = Form(...),
    event_time: str = Form(...),
    description: str = Form(...),
    league_id: int = Form(...),
    home_team_id: int = Form(...),
    away_team_id: int = Form(...),
    venue_id: int = Form(...)
):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        if home_team_id == away_team_id:
            leagues, teams, venues = get_form_options()
            return templates.TemplateResponse(
                request,
                "event_form.html",
                {
                    "success_message": None,
                    "error_message": "Home team and away team cannot be the same.",
                    "leagues": leagues,
                    "teams": teams,
                    "venues": venues
                }
            )

        cursor.execute(
            """
            INSERT INTO events (
                id,
                title,
                event_date,
                event_time,
                description,
                league_id,
                home_team_id,
                away_team_id,
                venue_id
            )
            VALUES (
                events_seq.NEXTVAL,
                :title,
                TO_DATE(:event_date, 'YYYY-MM-DD'),
                :event_time,
                :description,
                :league_id,
                :home_team_id,
                :away_team_id,
                :venue_id
            )
            """,
            {
                "title": title,
                "event_date": event_date,
                "event_time": event_time,
                "description": description,
                "league_id": league_id,
                "home_team_id": home_team_id,
                "away_team_id": away_team_id,
                "venue_id": venue_id
            }
        )

        conn.commit()

        leagues, teams, venues = get_form_options()
        return templates.TemplateResponse(
            request,
            "event_form.html",
            {
                "success_message": "Event created successfully.",
                "error_message": None,
                "leagues": leagues,
                "teams": teams,
                "venues": venues
            }
        )

    except Exception as e:
        conn.rollback()
        leagues, teams, venues = get_form_options()
        return templates.TemplateResponse(
            request,
            "event_form.html",
            {
                "success_message": None,
                "error_message": f"Error while creating event: {str(e)}",
                "leagues": leagues,
                "teams": teams,
                "venues": venues
            }
        )

    finally:
        cursor.close()
        conn.close()

# Single event from HTML (Details)
@app.get("/ui/events/{event_id}", response_class=HTMLResponse)
def event_detail_page(request: Request, event_id: int):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
        SELECT
            e.id,
            e.title,
            s.name AS sport,
            l.name AS league,
            e.event_date,
            e.event_time,
            ht.name AS home_team,
            at.name AS away_team,
            v.name AS venue,
            v.city AS city,
            v.country AS country,
            e.description
        FROM events e
        JOIN leagues l ON e.league_id = l.id
        JOIN sports s ON l.sport_id = s.id
        JOIN teams ht ON e.home_team_id = ht.id
        JOIN teams at ON e.away_team_id = at.id
        JOIN venues v ON e.venue_id = v.id
        WHERE e.id = :event_id
    """

    cursor.execute(query, {"event_id": event_id})
    row = cursor.fetchone()

    cursor.close()
    conn.close()

    if not row:
        return HTMLResponse(content="<h1>Event not found</h1>", status_code=404)

    event = {
        "id": row[0],
        "title": row[1],
        "sport": row[2],
        "league": row[3],
        "event_date": str(row[4])[:10],
        "event_time": str(row[5]),
        "home_team": row[6],
        "away_team": row[7],
        "venue": row[8],
        "city": row[9],
        "country": row[10],
        "description": row[11],
    }

    return templates.TemplateResponse(
        request,
        "event_detail.html",
        {
            "event": event
        }
    )


# Empty links for other navigation bars.
@app.get("/ui/{page_name}", response_class=HTMLResponse)
def placeholder_page(request: Request, page_name: str):
    allowed_pages = {"sports", "leagues", "results", "news"}

    if page_name not in allowed_pages:
        return HTMLResponse(content="<h1>Page not found</h1>", status_code=404)

    page_title = page_name.capitalize()

    return templates.TemplateResponse(
        request,
        "placeholder.html",
        {
            "page_title": page_title
        }
    )