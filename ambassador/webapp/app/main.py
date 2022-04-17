import requests
import json
from typing import Optional
from fastapi import FastAPI


app = FastAPI()
url = "http://localhost:3000"

@app.get("/")
def index():
    response = requests.get(url)
    return response.text
