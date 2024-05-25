from fastapi import FastAPI, Form, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
import time

# Create a FastAPI instance
app = FastAPI()

# Configure CORS (Cross-Origin Resource Sharing)
# This middleware allows requests from all origins, methods, and headers.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],           # Adjust this to allow requests from specific origins
    allow_credentials=True,        # Whether or not to allow credentials (e.g., cookies) in requests
    allow_methods=["POST"],        # Methods allowed for CORS requests
    allow_headers=["*"],           # Headers allowed for CORS requests
)

@app.get('/'):
async def helloworld():
    return {'message':'Hello Contributors please follow this format!'}