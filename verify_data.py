from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json

app = FastAPI()

class VerificationRequest(BaseModel):
    pan: str
    dob: str

def load_pan_data():
    with open('pan_data.json', 'r') as file:
        return json.load(file)

@app.post("/verify_pan")
async def verify_pan(request: VerificationRequest):
    pan_data = load_pan_data()

    match_found = False

    for record in pan_data:
        if record['data']['pan_number'] == request.pan and record['data']['dob'] == request.dob:
            match_found = True
            break

    if match_found:
        return {"matchingflag": True}
    else:
        return {"matchingflag": False}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)