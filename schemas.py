from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
    clubname: str
    username: str
    initial_scores: int

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int

    class Config:
        orm_mode = True

class GameHistoryBase(BaseModel):
    player1_id: int
    player2_id: int
    winner_id: int
    loser_id: int

class GameHistoryCreate(GameHistoryBase):
    pass

class GameHistory(GameHistoryBase):
    id: int
    game_timestamp: str

    class Config:
        orm_mode = True


class ScoreHistoryBase(BaseModel):
    user_id: int
    old_score: int
    new_score: int
    game_id: int

class ScoreHistoryCreate(ScoreHistoryBase):
    pass

class ScoreHistoryOut(ScoreHistoryBase):
    id: int
    change_timestamp: Optional[str]

    class Config:
        orm_mode = True