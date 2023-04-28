#!/bin/sh

#curl -X POST http://127.0.0.1:8080/create-table -H "Content-Type: application/json" -d '{"table_name": "users", "columns": "id INTEGER PRIMARY KEY, clubname TEXT UNIQUE NOT NULL, username TEXT UNIQUE NOT NULL, initial_scores INTEGER DEFAULT 1500"}'
#curl -X POST http://127.0.0.1:8080/create-table -H "Content-Type: application/json" -d '{"table_name": "game_history", "columns": "id INTEGER PRIMARY KEY, game_timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, player1_id INTEGER NOT NULL, player2_id INTEGER NOT NULL, winner_id INTEGER NOT NULL,    loser_id INTEGER NOT NULL,    FOREIGN KEY (player1_id) REFERENCES users (id),    FOREIGN KEY (player2_id) REFERENCES users (id),    FOREIGN KEY (winner_id) REFERENCES users (id),    FOREIGN KEY (loser_id) REFERENCES users (id)"}'
#curl -X POST http://127.0.0.1:8080/create-table -H "Content-Type: application/json" -d '{"table_name": "score_history", "columns": "id INTEGER PRIMARY KEY,    user_id INTEGER NOT NULL,    old_score INTEGER NOT NULL,    new_score INTEGER NOT NULL,    game_id INTEGER NOT NULL,    change_timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,    FOREIGN KEY (user_id) REFERENCES users (id),    FOREIGN KEY (game_id) REFERENCES game_history (id)"}'

curl -X POST http://127.0.0.1:8000/game_history/ -H "Content-Type: application/json" -d '{"player1_id": 1, "player2_id": 3, "winner_id": 1, "loser_id": 3}'
curl -X POST http://127.0.0.1:8000/game_history/ -H "Content-Type: application/json" -d '{"player1_id": 1, "player2_id": 4, "winner_id": 1, "loser_id": 4}'
curl -X POST http://127.0.0.1:8000/game_history/ -H "Content-Type: application/json" -d '{"player1_id": 2, "player2_id": 3, "winner_id": 2, "loser_id": 3}'
curl -X POST http://127.0.0.1:8000/game_history/ -H "Content-Type: application/json" -d '{"player1_id": 2, "player2_id": 4, "winner_id": 2, "loser_id": 4}'
curl -X POST http://127.0.0.1:8000/game_history/ -H "Content-Type: application/json" -d '{"player1_id": 4, "player2_id": 3, "winner_id": 4, "loser_id": 3}'


curl -X GET "http://localhost:8000/users/" -H "accept: application/json"
