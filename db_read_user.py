import time

from db_read import templates, get_db, Session, List, HTMLResponse, Depends, Request, APIRouter, HTTPException

from models import User
from schemas import UserOut
from cachetools import TTLCache

user_router = APIRouter()

user_cache=TTLCache(maxsize=100, ttl=300)

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

def user_to_dict(user: User) -> dict:
    return {c.name: getattr(user, c.name) for c in user.__table__.columns}

def dict_to_user(user_dict: dict) -> User:
    user = User(**user_dict)
    return user

@user_router.get("/users/{id}", response_model=UserOut)
def read_user(id: int, db: Session = Depends(get_db)):
    start_time=time.perf_counter()
    user_dict=user_cache.get(id)

    print(len(user_cache.items()))
    if user_dict is None:
        user = db.query(User).filter(User.id == id).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        else:
            user_dict=user_to_dict(user)
            user_cache[id]=user_dict
    else:
        user=dict_to_user(user_dict)
    end_time=time.perf_counter()
    duration_us=(end_time-start_time)*1000000
    print(f"Code duration: {duration_us:.2f} microseconds")
    return user
