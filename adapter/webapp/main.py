from fastapi import FastAPI
import json
app = FastAPI()


@app.get("/")
async def root():
    response = []
    with open("/var/log/file.log", 'r') as logfile:
        for line in logfile.readlines():
            response.append({
                "time": line.rstrip().split("#")[0],
                "log": line.rstrip().split("#")[1] 
            })

    return response