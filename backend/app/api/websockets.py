# backend/app/api/websocket.py

import asyncio
from typing import List
from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from app.services.vector_db import query_vector_db
from app.services.llm import obtain_final_answer

router = APIRouter()

class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)

manager = ConnectionManager()

@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            query = data.strip()
            most_similar_pages = query_vector_db(data)
            async for answer_part in obtain_final_answer_stream(query, most_similar_pages):
                await manager.send_message(answer_part, websocket)
    except WebSocketDisconnect:
        manager.disconnect(websocket)


# This is a generator function that yields parts of the answer.
async def obtain_final_answer_stream(query: str, most_similar_pages: List[str]):
    answer = obtain_final_answer(query, most_similar_pages)
    for part in answer.split():
        yield part
        await asyncio.sleep(0.1)  # Simulate streaming delay