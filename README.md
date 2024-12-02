# FastAPI Notes Application

This is a simple FastAPI application that allows users to create, read, update, delete, and search for notes. The application also includes basic authentication to secure the endpoints.

## Features

- **Create a Note**: Add a new note with a title and content.
- **Read Notes**: Fetch all notes or search for specific notes by title or content.
- **Update a Note**: Modify the title or content of an existing note.
- **Delete a Note**: Remove a note by its ID.
- **Search Notes**: Search for notes by their title or content.

## Requirements

- Python 3.7+
- FastAPI
- Uvicorn
- SQLAlchemy
- SQLite (or another database if configured)

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/revanth-shivakumar/RestAPI.git
    ```

2. Navigate to the project folder:

    ```bash
    cd RestAPI
    ```

3. Create a virtual environment:

    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:

    - **For Windows**:

      ```bash
      venv\Scripts\activate
      ```

    - **For macOS/Linux**:

      ```bash
      source venv/bin/activate
      ```

5. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

6. Run the application using Uvicorn:

    ```bash
    uvicorn main:app --reload
    ```

    The app will be available at `http://127.0.0.1:8000`.
