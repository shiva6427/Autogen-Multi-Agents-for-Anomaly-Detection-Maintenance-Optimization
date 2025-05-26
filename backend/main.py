from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import os
import shutil
from core.agent_runner import run_multi_agent_workflow

# Initialize FastAPI app
app = FastAPI(
    title="Predictive Maintenance API",
    description="Multi-agent AutoGen backend for anomaly detection and maintenance planning",
    version="1.0",
)

# CORS middleware for frontend communication (allowing Streamlit to connect)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Can be replaced with Streamlit's URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    try:
        # Save the uploaded file to disk
        file_path = os.path.join(UPLOAD_DIR, file.filename)
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # Run the multi-agent workflow and get the result
        result = run_multi_agent_workflow(file_path)

        return JSONResponse(content={"status": "success", "summary": result})

    except Exception as e:
        return JSONResponse(
            content={"status": "error", "message": str(e)}, status_code=500
        )
