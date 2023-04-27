from fastapi import FastAPI, Body
from pydantic import BaseModel
from db_read import router as read_router
from db_write import router as write_router

app = FastAPI()

app.include_router(read_router)
app.include_router(write_router)


"""
my_db="PingPongClub.db"

app = FastAPI()


@app.get("/players/", response_model=List[User])
async def get_all_players():
    with sqlite3.connect(my_db) as conn:
        c = conn.cursor()
        c.execute("SELECT * FROM users")
        players = c.fetchall()

    return [User(id=row[0], clubname=row[1], username=row[2], initial_scores=row[3]) for row in players]

@app.get("/games/", response_model=List[Game])
async def get_all_games():
    with sqlite3.connect(my_db) as conn:
        c = conn.cursor()
        c.execute("SELECT * FROM game_history")
        games = c.fetchall()

    return [Game(id=row[0], game_timestamp=row[1], player1_id=row[2], player2_id=row[3], winner_id=row[4], loser_id=row[5], player1_score=row[6], player2_score=row[7]) for row in games]


@app.post("/create-table")
def create_table(request: CreateTableRequest = Body(...)):
    # Connect to the database (this will create the file if it doesn't exist)
    conn = sqlite3.connect(my_db)

    # Create a cursor object to execute SQL commands
    c = conn.cursor()

    # Create the table using provided table_name and columns
    c.execute(f"CREATE TABLE IF NOT EXISTS {request.table_name} ({request.columns})")

    # Commit the transaction and close the connection
    conn.commit()
    conn.close()

    return {"message": f"Table {request.table_name} created successfully"}
"""