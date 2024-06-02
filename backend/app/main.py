from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.endpoints import router as api_router
from app.api.websockets import router as websocket_router  # Import the websocket router


app = FastAPI()

# Set up CORS middleware to allow cross-origin requests from your frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update this with the actual origins you want to allow
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the API router
app.include_router(api_router, prefix="/api")
app.include_router(websocket_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Chatbot API"}
