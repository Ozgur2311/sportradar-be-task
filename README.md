# SportRadar BE Task

SportRadar BE Task is a backend-focused coding exercise built with **FastAPI**, **Oracle Database**, **Jinja2**, and an HTML/CSS frontend.  
The project provides REST API endpoints for managing sports events and also includes a simple server-rendered UI for browsing events, viewing event details, and creating new events.

## Features

### Backend API
- Test backend and database connectivity
- List events with optional filters
- Retrieve a single event by ID
- Create a new event
- Create leagues, teams, and venues through extra endpoints

### Frontend UI
- Event list page
- Event detail page
- Add Event form
- Search bar filter for league, home team, and away team
- Basic navigation bar with placeholder pages

## Tech Stack

- **Python**
- **FastAPI**
- **Oracle Database**
- **Jinja2 Templates**
- **HTML / CSS**
- **Uvicorn**

## Setup

To run this project locally, clone the repository and open it in your preferred development environment.  
It is recommended to create and activate a Python virtual environment before installing the required dependencies listed in `requirements.txt`.

After installing the dependencies, configure the Oracle database connection in `app/db.py` with valid credentials and connection details.  
The project requires the necessary database tables and sequence to be available before startup.

Once the environment is ready, the application can be launched with Uvicorn in development mode.

```bash
uvicorn app.main:app --reload
```

## Database Configuration

This project uses Oracle Database as its primary data source.  
Before running the application, make sure that the Oracle connection settings in `app/db.py` are updated correctly and that the required schema objects already exist in the database.

## API Endpoints

The backend exposes a set of REST API endpoints for testing connectivity, retrieving event data, and creating new records.

#### `GET /`
Returns a simple message to confirm that the backend is running.

#### `GET /test-db`
Tests the Oracle database connection and returns a success message if the connection is established correctly.

#### `GET /events`
Returns a list of events with optional filtering support.

Supported query parameters:
- `sport`
- `league`
- `date`
- `team`
- `venue`

Example: `GET /events?sport=Football`

#### `GET /events/{event_id}`
Returns a single event by its ID.

#### `POST /events`
Creates a new event by inserting it into the database after validation checks are completed. 
The POST endpoints can also be tested through the FastAPI Swagger UI at `/docs`.

#### Extra POST Endpoints
- `POST /leagues`
- `POST /teams`
- `POST /venues`

These endpoints create related entities after validation checks are completed.

## Frontend Pages

### `GET /ui/events` (Main Page)
Displays the main event list page.

### `GET /ui/events/{event_id}`
Displays the event details page.

### `GET /ui/events/new`
Displays the Add Event form.

## Validation Rules

The project includes several validation checks to improve data consistency and user experience.

Examples include:
- home team and away team cannot be the same
- referenced league must exist
- referenced teams must exist
- referenced venue must exist
- duplicate prevention for selected extra entities where applicable

## Notes

This project was developed as a coding exercise and focuses mainly on core backend functionality supported by a frontend interface.

Some navigation items currently lead to placeholder pages and are included to provide a more complete interface structure.

Event date and time are not currently validated against real-time values, so users can still create past events.

## Author

Created by **Özgür Avcı** for the SportRadar Coding Academy Backend Coding Exercise.