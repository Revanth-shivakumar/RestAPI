from fastapi import FastAPI, Depends, HTTPException, status, Security
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from sqlalchemy.orm import Session
from models import Note, Base
from database import SessionLocal, engine
from schema import NoteCreate, NoteResponse

app = FastAPI()
Base.metadata.create_all(bind=engine)
security = HTTPBasic()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
def authenticate_user(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = "username"
    correct_password = "password"
    
    if credentials.username != correct_username or credentials.password != correct_password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Basic"},
        )@app.post("/notes/", response_model=NoteResponse)
def create_note(note: NoteCreate, db: Session = Depends(get_db), credentials: HTTPBasicCredentials = Depends(security)):
    authenticate_user(credentials)
    db_note = Note(title=note.title, content=note.content)
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note
@app.get("/notes/", response_model=list[NoteResponse])
def get_notes(db: Session = Depends(get_db), credentials: HTTPBasicCredentials = Depends(security)):
    authenticate_user(credentials)
    notes = db.query(Note).all()
    return notes


@app.put("/notes/{id}", response_model=NoteResponse)
def update_note(id: int, note: NoteCreate, db: Session = Depends(get_db), credentials: HTTPBasicCredentials = Depends(security)):
    authenticate_user(credentials)
    db_note = db.query(Note).filter(Note.id == id).first()
    if not db_note:
        raise HTTPException(status_code=404, detail="Note found")
    
    db_note.title = note.title
    db_note.content = note.content
    db.commit()
    db.refresh(db_note)
    return db_note


@app.delete("/notes/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_note(id: int, db: Session = Depends(get_db), credentials: HTTPBasicCredentials = Depends(security)):
    authenticate_user(credentials)
    db_note = db.query(Note).filter(Note.id == id).first()
    if not db_note:
        raise HTTPException(status_code=404, detail="not found")
    
    db.delete(db_note)
    db.commit()
    return {"message": "Note deleted"}


@app.get("/notes/search/", response_model=list[NoteResponse])
def search_notes(query: str, db: Session = Depends(get_db), credentials: HTTPBasicCredentials = Depends(security)):
    authenticate_user(credentials)
    notes = db.query(Note).filter(
        Note.title.contains(query) | Note.content.contains(query)
    ).all()
    return notes