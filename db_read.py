from fastapi import FastAPI, Depends, Request, APIRouter, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
#from database import SessionLocal, engine

from typing import List

from sqlalchemy.orm import Session
from database import get_db
from models import Base, User, GameHistory, ScoreHistory
from schemas import UserOut, GameHistoryOut, ScoreHistoryOut


templates = Jinja2Templates(directory="templates")


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