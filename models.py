from sqlalchemy import Column, Integer, String, Float, ForeignKey, Text, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    clubname = Column(String, nullable=False)
    username = Column(String, unique=True, nullable=False)
    initial_scores = Column(Integer, default=1500)


class GameHistory(Base):
    __tablename__ = 'game_history'
    id = Column(Integer, primary_key=True)
    game_timestamp = Column(DateTime, nullable=False, server_default=func.datetime('now'))
    player1_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    player2_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    winner_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    loser_id = Column(Integer, ForeignKey('users.id'), nullable=False)


class ScoreHistory(Base):
    __tablename__ = 'score_history'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    old_score = Column(Integer, nullable=False)
    new_score = Column(Integer, nullable=False)
    game_id = Column(Integer, ForeignKey('game_history.id'), nullable=False)
    change_timestamp = Column(DateTime, nullable=False, server_default=func.datetime('now'))
