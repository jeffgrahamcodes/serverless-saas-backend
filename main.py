# main.py - Main FastAPI Application
from fastapi import FastAPI, Depends
from auth import verify_token  # Import authentication function

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Serverless SaaS App!"}

@app.get("/secure-data/")
def get_secure_data(user: dict = Depends(verify_token)):
    return {"message": "Secure data accessed", "user": user}