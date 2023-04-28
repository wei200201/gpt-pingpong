from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import Base, User, GameHistory, ScoreHistory
from schemas import UserOut, GameHistoryOut, ScoreHistoryOut

router = APIRouter()

@router.get("/users/", response_model=List[UserOut])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = db.query(User).offset(skip).limit(limit).all()
    return users

@router.get("/users/{id}", response_model=UserOut)
def read_user(id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.get("/games/", response_model=List[GameHistoryOut])
def read_games(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    games = db.query(GameHistory).offset(skip).limit(limit).all()

    return games

@router.get("/games/{id}", response_model=GameHistoryOut)
def read_user(id: int, db: Session = Depends(get_db)):
    game = db.query(GameHistory).filter(GameHistory.id == id).first()
    if not game:
        raise HTTPException(status_code=404, detail="Game not found")
    return game

@router.get("/scores/", response_model=List[ScoreHistoryOut])
def read_games(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    scores = db.query(ScoreHistory).offset(skip).limit(limit).all()
    return scores

@router.get("/scores/{id}", response_model=ScoreHistoryOut)
def read_game(id: int, db: Session = Depends(get_db)):
    score = db.query(ScoreHistory).filter(User.id == id).first()
    if not score:
        raise HTTPException(status_code=404, detail="Score not found")
    return score


"""
app = FastAPI()

@app.get("/users")
def read_users(db = Depends(get_db)):
    # Query the users table
    users = db.query(User).all()

    # Return the user data as JSON
    return {"users": [{"id": user.id, "clubname": user.clubname, "username": user.username, "initial_scores": user.initial_scores} for user in users]}

@app.get("/games")
def read_games(db = Depends(get_db)):
    # Query the game_history table
    games = db.query(GameHistory).all()

    # Return the game data as JSON
    return {"games": [{"id": game.id, "game_timestamp": game.game_timestamp, "player1": game.player1.username, "player2": game.player2.username, "winner": game.winner.username, "loser": game.loser.username} for game in games]}

@app.get("/scores")
def read_scores(db = Depends(get_db)):
    # Query the score_history table
    scores = db.query(ScoreHistory).all()

    # Return the score data as JSON
    return {"scores": [{"id": score.id, "user": score.user.username, "old_score": score.old_score, "new_score": score.new_score, "game_id": score.game.id, "change_timestamp": score.change_timestamp} for score in scores]}
"""