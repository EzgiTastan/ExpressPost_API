# ExpressPost_API Project

This FastAPI project implements a backend system with features including user authentication, CRUD operations for posts, user management, and a voting system.

## Usage & Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/EzgiTastan/ExpressPost_API.git
    cd ExpressPost_API
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv env
   env\Scripts\activate
    ```

3. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up the environment variables by creating a `.env` file in the `app` directory:

    ```
    DATABASE_HOSTNAME=<your-database-hostname>
    DATABASE_PORT=<your-database-port>
    DATABASE_PASSWORD=<your-database-password>
    DATABASE_NAME=<your-database-name>
    DATABASE_USERNAME=<your-database-username>
    SECRET_KEY=<your-secret-key>
    ALGORITHM=<your-algorithm>
    ACCESS_TOKEN_EXPIRE_MINUTES=<your-token-expiry-time>
    ```

5. Set up the database (example using SQLite):

    ```bash
    alembic upgrade head
    ```

6. Run the FastAPI server:

    ```bash
    uvicorn main:app --reload
    ```

## Project Structure

```
.
├── app
│   ├── __init__.py
│   ├── auth.py          # User authentication and JWT token generation.
│   ├── config.py        # Configuration settings using Pydantic's BaseSettings.
│   ├── database.py      # Database connection and session management with SQLAlchemy.
│   ├── main.py          # Main application entry point with FastAPI app instantiation.
│   ├── models.py        # SQLAlchemy models mapping to database tables.
│   ├── oauth2.py        # JWT token management and user authentication.
│   ├── posts.py         # CRUD operations for posts, requiring user authentication.
│   ├── schemas.py       # Pydantic models for request and response validation.
│   ├── users.py         # User management and CRUD operations for users.
│   └── vote.py          # Voting system operations.
├── alembic              # Database migration folder.
│   └── versions         # Alembic migration versions.
├── alembic.ini          # Alembic configuration file.
├── requirements.txt     # List of Python dependencies.
└── README.md            # Project documentation, was so fun to create.

```
