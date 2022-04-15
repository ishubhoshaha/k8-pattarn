import requests
import json
from typing import Optional
from fastapi import FastAPI


app = FastAPI()
# url = "https://confidential.free.beeceptor.com/api/color"
url = "http://localhost:3000"

@app.get("/")
def index():
    response = requests.get(url)
    return response.text
