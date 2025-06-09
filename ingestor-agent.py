# Ingestor Agent - Agent

from fastapi import FastAPI, UploadFile
import uvicorn

app = FastAPI()

@app.post("/process")
async def process_document(file: UploadFile):
    return {"message": "Processing document in Ingestor Agent"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
