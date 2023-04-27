from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import Base, User, GameHistory, ScoreHistory
from schemas import UserCreate, User, GameHistory, GameHistoryCreate

router = APIRouter()

@router.post("/users/", response_model=User)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.post("/game_history/", response_model=GameHistory)
def create_game_history(game_history: GameHistoryCreate, db: Session = Depends(get_db)):
    db_game_history = GameHistory(**game_history.dict())
    db.add(db_game_history)
    db.commit()
    db.refresh(db_game_history)
    return db_game_history

"""

@router.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: Item, db: Session = Depends(get_db)):
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    db_item.name = item.name
    db_item.description = item.description
    db.commit()
    db.refresh(db_item)
    return db_item

@router.delete("/items/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(db_item)
    db.commit()
    return {"message": "Item deleted successfully"}

"""
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, User, GameHistory, ScoreHistory

engine = create_engine('sqlite:///./PingPongClub.db')
Session = sessionmaker(bind=engine)

def create_user(clubname, username, initial_scores=1500):
    db = Session()
    user = User(clubname=clubname, username=username, initial_scores=initial_scores)
    db.add(user)
    db.commit()
    db.refresh(user)
    db.close()
    return user

def create_game(player1_id, player2_id, winner_id, loser_id):
    db = Session()
    game = GameHistory(player1_id=player1_id, player2_id=player2_id, winner_id=winner_id, loser_id=loser_id)
    db.add(game)
    db.commit()
    db.refresh(game)
    db.close()
    return game

def create_score(user_id, old_score, new_score, game_id):
    db = Session()
    score = ScoreHistory(user_id=user_id, old_score=old_score, new_score=new_score, game_id=game_id)
    db.add(score)
    db.commit()
    db.refresh(score)
    db.close()
    return score

from fastapi import FastAPI
from db_write import create_user
from models import User, GameHistory, ScoreHistory

app = FastAPI()

@app.post("/users")
def create_new_user(clubname: str, username: str, initial_scores: int = 1500):
    # Create a new user and return the user data as JSON
    user = create_user(clubname, username, initial_scores)
    return user.__dict__
"""