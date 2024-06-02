# backend/app/api/endpoints.py

from fastapi import APIRouter, Query
from app.services.vector_db import query_vector_db
from app.services.llm import obtain_final_answer

router = APIRouter()

@router.get("/search")
def search(query: str, top_k: int = 3):
    most_similar_pages = query_vector_db(query, top_k)
    answer = obtain_final_answer(query, most_similar_pages)
    return {"results": answer}


