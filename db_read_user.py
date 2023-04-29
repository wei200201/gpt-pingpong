from db_read import templates, get_db, Session, List, HTMLResponse, Depends, Request, APIRouter, HTTPException

from models import User
from schemas import UserOut

user_router = APIRouter()


@user_router.get('/', response_class=HTMLResponse)
def read_index(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})

@user_router.get('/users', response_class=HTMLResponse, response_model=list[UserOut])
def read_users(request: Request, db: Session = Depends(get_db)):
    users = db.query(User).all()
    return templates.TemplateResponse('list_users.html', {'request': request, 'users': users})

@user_router.get('/load_form', response_class=HTMLResponse, response_model=UserOut)
def read_users(request: Request):
    return templates.TemplateResponse('add_user.html', {'request': request})

@user_router.get("/users2/", response_model=List[UserOut])
def read_users(request: Request, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = db.query(User).offset(skip).limit(limit).all()
    return templates.TemplateResponse('users.html', {'request': request, 'users': users})
    #return users

@user_router.get("/users/{id}", response_model=UserOut)
def read_user(id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
