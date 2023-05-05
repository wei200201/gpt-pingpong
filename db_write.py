from fastapi import APIRouter, Depends, Form
from sqlalchemy.orm import Session
from database import get_db
from models import Base, User, GameHistory, ScoreHistory
from schemas import UserCreate, UserOut, GameHistoryOut, GameHistoryCreate, ScoreHistoryCreate, ScoreHistoryOut
import uuid
import utils

def generate_unique_integer():
    return uuid.uuid4().int & (1<<32)-1

write_router = APIRouter()

@write_router.post("/add_user", response_model=UserOut)
def add_user_f(
    clubname: str = Form(...),
    username: str = Form(...),
    initial_scores: int = Form(...),
    db: Session = Depends(get_db)
):
    userid=generate_unique_integer()
    new_user = {
        'clubname': clubname,
        'username': username,
        'initial_scores': initial_scores,
        'id': userid,
    }
    print(new_user)

    new_score = {
        'user_id' : userid,
        'old_score' : 1500,
        'new_score' : 1500,
        'game_id' : -1
    }

    db_user = User(**new_user)
    db_score = ScoreHistory(**new_score)
    print(db_user)
    print(db_score)

    db.add(db_user)
    db.add(db_score)

    db.commit()
    db.refresh(db_user)
    return db_user

@write_router.post("/users/", response_model=UserOut)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    print(type(user))
    print(user.dict())
    new_user=user.dict()
    new_user['id']=generate_unique_integer()
    print(new_user)


    db_user = User(**user.dict())
    print(db_user)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@write_router.post("/game_history/", response_model=GameHistoryOut)
def create_game_history(game_history: GameHistoryCreate, db: Session = Depends(get_db)):
    db_game_history = GameHistory(**game_history.dict())
    db.add(db_game_history)
    db.commit()
    db.refresh(db_game_history)

    print(type(db_game_history))
    db_game_history.game_timestamp = str(db_game_history.game_timestamp)  # Convert datetime to string
    return db_game_history
@write_router.post("/add_game_history", response_model=GameHistoryOut)
def add_game_history(player1_id: int = Form(...), player2_id: int = Form(...), winner_id: int = Form(...), loser_id: int = Form(...), db: Session = Depends(get_db) ):

    try:
        game_history = GameHistory(player1_id=player1_id, player2_id=player2_id, winner_id=winner_id, loser_id=loser_id)
        db.add(game_history)
        db.flush()

        queryw = db.query(ScoreHistory).filter(ScoreHistory.user_id == winner_id).order_by(ScoreHistory.change_timestamp.desc()).limit(1)
        resultw=queryw.first()
        print(resultw)

        queryl = db.query(ScoreHistory).filter(ScoreHistory.user_id == loser_id).order_by(ScoreHistory.change_timestamp.desc()).limit(1)
        resultl=queryl.first()
        print(resultl)

        new_score_w, new_score_l = utils.update_scores(resultw.new_score, resultl.new_score)

        score_history_w = ScoreHistory(user_id=winner_id, old_score=resultw.new_score, new_score=new_score_w, game_id=game_history.id)
        score_history_l = ScoreHistory(user_id=loser_id, old_score=resultl.new_score, new_score=new_score_l, game_id=game_history.id)
        db.add(score_history_w)
        db.add(score_history_l)

        db.commit()

        print(game_history)
        return game_history
    except Exception as e:
        db.rollback()
        raise e

@write_router.post("/score_history/", response_model=ScoreHistoryOut)
def create_score_history(score_history: ScoreHistoryCreate, db: Session = Depends(get_db)):
    db_score_history = ScoreHistoryOut(**score_history.dict())
    db.add(db_score_history)
    db.commit()
    db.refresh(db_score_history)
    return db_score_history
"""

@write_router.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: Item, db: Session = Depends(get_db)):
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    db_item.name = item.name
    db_item.description = item.description
    db.commit()
    db.refresh(db_item)
    return db_item

@write_router.delete("/items/{item_id}")
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