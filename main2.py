from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from transformers import pipeline
import asyncio

app = FastAPI()

async def server_loop(q):
    pipe = pipeline(model="bert-base-uncased")
    while True:
        (string, response_q) = await q.get()
        out = pipe(string)
        await response_q.put(out)

@app.on_event("startup")
async def startup_event():
    q = asyncio.Queue()
    app.model_queue = q
    asyncio.create_task(server_loop(q))

@app.post("/")
async def homepage(request: Request):
    payload = await request.body()
    string = payload.decode("utf-8")
    response_q = asyncio.Queue()
    await app.model_queue.put((string, response_q))
    output = await response_q.get()
    return JSONResponse(output)
