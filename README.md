# Predictive Maintenance System with Multi-Agent Workflow

## Problem Statement

Manufacturing companies often face unexpected downtime due to machine malfunctions or failures. This leads to costly repairs, lost production time, and decreased efficiency. A predictive maintenance system can mitigate these issues by proactively detecting anomalies in machine data and scheduling maintenance before failures occur.

This project builds a **multi-agent system** that:
- Analyzes sensor data from machines
- Detects anomalies in the data
- Plans maintenance activities based on the anomalies
- Provides a user-friendly interface for monitoring and managing maintenance tasks

## Tech Stack

The system is implemented using the following technologies:

### **Backend:**
- **FastAPI**: A modern web framework for building APIs quickly with Python. It's used to handle the backend logic and manage API endpoints.
- **Uvicorn**: An ASGI server for running FastAPI applications.
- **AutoGen**: A multi-agent framework for orchestrating the workflow between different agents (e.g., anomaly detection, maintenance planning).
- **requests**: Used to make HTTP requests between the backend and frontend.
  
### **Frontend:**
- **Streamlit**: A Python library for building interactive web applications. It is used to create a simple frontend for uploading files and displaying results from the backend.

### **Other Tools:**
- **Python 3.9+**: Programming language for building the application.
- **.env file**: Stores environment variables for sensitive data (like API keys or configuration).

## System Flow

Below is the workflow of the system:

1. **User Uploads CSV File**: The user uploads a CSV file with machine sensor data via the Streamlit frontend.
2. **FastAPI Backend**: The file is sent to the FastAPI server.
3. **Sensor Agent**: Detects anomalies in the sensor data.
4. **Maintenance Planner**: Creates a maintenance plan based on the detected anomalies.
5. **Knowledge Base Agent**: Provides historical context or similar incidents.
6. **Notifier Agent**: Summarizes the results and sends a final report to the user.

### Flow Diagram:
+-------------+
|   User     |
| Upload CSV |
+------+------+
       |
       v
+-------------+
| Streamlit   |
| Frontend    |
+------+------+
       |
       v
+-------------+       +----------------+
| FastAPI     | ----> | Multi-Agent    |
| Backend     |       | Orchestration  |
+------+------+
       |
       v
+-------------------+      +---------------------+
| Sensor Agent      | ---> | Maintenance Planner |
+-------------------+      +---------------------+
       |
       v
+------------------+       +-----------------+
| Knowledge Agent  | --->  | Notifier Agent  |
+------------------+       +-----------------+
       |
       v
+-------------------+
| Final Report      |
+-------------------+

---

### File Structure

.
├── backend/                     # FastAPI backend for agent logic and API endpoints
│   ├── main.py                  # FastAPI app for handling file uploads and agent orchestration
│   ├── requirements.txt         # Backend dependencies (FastAPI, Uvicorn, etc.)
│   ├── .env                     # Backend environment variables (database creds, etc.)
├── frontend/                    # Streamlit frontend for user interface
│   ├── app.py                   # Streamlit app for file upload and result display
│   ├── requirements.txt         # Frontend dependencies (Streamlit, Pandas, etc.)
└── core/                        # Core agent logic
    ├── agent_runner.py          # Orchestrates multi-agent workflows (anomaly detection, planning)
    ├── .env                     # (optional) Environment-specific variables for agents

---

###  **How to Run the Full Stack Application**

##  How to Run the Full Stack Application

### Backend Setup (FastAPI + AutoGen)

1. Navigate to the backend directory:

   ```bash
   cd backend
   ```

2. Create a virtual environment (recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file inside the `backend/` directory with necessary environment variables:

   ```env
   # backend/.env
   OPENAI_API_KEY=your_openai_key_here
   ```

5. Start the FastAPI backend:

   ```bash
   uvicorn backend.main:app --reload
   ```

   Your backend server should now be running at: `http://localhost:8000`

---

### Frontend Setup (Streamlit UI)

1. Open a new terminal and navigate to the frontend directory:

   ```bash
   cd frontend
   ```

2. Create a virtual environment and install requirements:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. Run the Streamlit frontend app:

   ```bash
   streamlit run app.py
   ```

4. The UI should launch automatically in your browser at: `http://localhost:8501`

---

### Using the App

- Upload a CSV file with machine sensor data via the Streamlit frontend.
- The backend will:
  - Parse the file
  - Send the data to agents for analysis
  - Return the maintenance plan and anomaly detection summary
- The frontend will display the results to the user.

---

## Example `.env` file

```env
# For Backend (backend/.env)
OPENAI_API_KEY=your_openai_api_key
```

