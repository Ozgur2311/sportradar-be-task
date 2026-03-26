from fastapi import APIRouter
from app.db import get_connection
from app.extra_schemas import LeagueCreate, TeamCreate, VenueCreate

router = APIRouter()

# Extras sections represent the adding new team,league,venue in dataset. In task 3 adding event
# done in main.py, however because of the foreign keys we cannot add events if team or league not
# available in our dataset. I add that extra part for the users can add team or league by input if needed.

# Test endpoint for extras router
@router.get("/extras-test")
def extras_test():
    return {"message": "Extras router is working"}


# Check whether a record exists in a given table
def record_exists(cursor, table_name: str, record_id: int) -> bool:
    query = f"SELECT COUNT(*) FROM {table_name} WHERE id = :id"
    cursor.execute(query, {"id": record_id})
    result = cursor.fetchone()
    return result[0] > 0


# Check whether a league with the same name already exists for the same sport
def league_exists(cursor, name: str, sport_id: int) -> bool:
    query = """
        SELECT COUNT(*)
        FROM leagues
        WHERE LOWER(name) = LOWER(:name)
          AND sport_id = :sport_id
    """
    cursor.execute(query, {
        "name": name,
        "sport_id": sport_id
    })
    result = cursor.fetchone()
    return result[0] > 0


# Check whether a team with the same name already exists for the same sport
def team_exists(cursor, name: str, sport_id: int) -> bool:
    query = """
        SELECT COUNT(*)
        FROM teams
        WHERE LOWER(name) = LOWER(:name)
          AND sport_id = :sport_id
    """
    cursor.execute(query, {
        "name": name,
        "sport_id": sport_id
    })
    result = cursor.fetchone()
    return result[0] > 0


# Check whether a venue with the same name already exists
def venue_exists(cursor, name: str) -> bool:
    query = """
        SELECT COUNT(*)
        FROM venues
        WHERE LOWER(name) = LOWER(:name)
    """
    cursor.execute(query, {"name": name})
    result = cursor.fetchone()
    return result[0] > 0


@router.post("/leagues")
def create_league(league: LeagueCreate):
    try:
        # Open database connection
        connection = get_connection()
        cursor = connection.cursor()

        # Make sure the selected sport exists
        if not record_exists(cursor, "sports", league.sport_id):
            cursor.close()
            connection.close()
            return {"error": "Sport not found"}

        # Prevent duplicate league names for the same sport
        if league_exists(cursor, league.name, league.sport_id):
            cursor.close()
            connection.close()
            return {"error": "League already exists"}

        # Insert new league into the database
        query = """
            INSERT INTO leagues (
                id,
                name,
                sport_id
            )
            VALUES (
                leagues_seq.NEXTVAL,
                :name,
                :sport_id
            )
        """

        cursor.execute(query, {
            "name": league.name,
            "sport_id": league.sport_id
        })

        connection.commit()

        # Close database resources
        cursor.close()
        connection.close()

        return {"message": "League created successfully"}

    except Exception as e:
        return {"error": str(e)}


@router.post("/teams")
def create_team(team: TeamCreate):
    try:
        # Open database connection
        connection = get_connection()
        cursor = connection.cursor()

        # Make sure the selected sport exists
        if not record_exists(cursor, "sports", team.sport_id):
            cursor.close()
            connection.close()
            return {"error": "Sport not found"}

        # Prevent duplicate team names for the same sport
        if team_exists(cursor, team.name, team.sport_id):
            cursor.close()
            connection.close()
            return {"error": "Team already exists"}

        # Insert new team into the database
        query = """
            INSERT INTO teams (
                id,
                name,
                city,
                country,
                sport_id
            )
            VALUES (
                teams_seq.NEXTVAL,
                :name,
                :city,
                :country,
                :sport_id
            )
        """

        cursor.execute(query, {
            "name": team.name,
            "city": team.city,
            "country": team.country,
            "sport_id": team.sport_id
        })

        connection.commit()

        # Close database resources
        cursor.close()
        connection.close()

        return {"message": "Team created successfully"}

    except Exception as e:
        return {"error": str(e)}


@router.post("/venues")
def create_venue(venue: VenueCreate):
    try:
        # Open database connection
        connection = get_connection()
        cursor = connection.cursor()

        # Prevent duplicate venue names
        if venue_exists(cursor, venue.name):
            cursor.close()
            connection.close()
            return {"error": "Venue already exists"}

        # Insert new venue into the database
        query = """
            INSERT INTO venues (
                id,
                name,
                city,
                country
            )
            VALUES (
                venues_seq.NEXTVAL,
                :name,
                :city,
                :country
            )
        """

        cursor.execute(query, {
            "name": venue.name,
            "city": venue.city,
            "country": venue.country
        })

        connection.commit()

        # Close database resources
        cursor.close()
        connection.close()

        return {"message": "Venue created successfully"}

    except Exception as e:
        return {"error": str(e)}