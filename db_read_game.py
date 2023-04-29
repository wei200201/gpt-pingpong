from db_read import templates, get_db, Session, List, HTMLResponse, Depends, Request, APIRouter, HTTPException

from models import GameHistory
from schemas import GameHistoryOut

game_router = APIRouter()

@game_router.get('/load_game', response_class=HTMLResponse, response_model=GameHistoryOut)
def load_game(request: Request):
    return templates.TemplateResponse('add_game_history.html', {'request': request})

@game_router.get('/games', response_class=HTMLResponse, response_model=list[GameHistoryOut])
def read_games_all(request: Request, db: Session = Depends(get_db)):
    games = db.query(GameHistory).all()
    return templates.TemplateResponse('list_gamehistory.html', {'request': request, 'game_history': games})

@game_router.get("/games/", response_model=List[GameHistoryOut])
def read_games(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    games = db.query(GameHistory).offset(skip).limit(limit).all()

    return games

@game_router.get("/games/{id}", response_model=GameHistoryOut)
def read_user(id: int, db: Session = Depends(get_db)):
    game = db.query(GameHistory).filter(GameHistory.id == id).first()
    if not game:
        raise HTTPException(status_code=404, detail="Game not found")
    return game
