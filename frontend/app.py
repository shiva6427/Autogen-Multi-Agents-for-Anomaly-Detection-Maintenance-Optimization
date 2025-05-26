import streamlit as st
import requests
import json

# FastAPI backend URL (make sure this points to the running backend)
BACKEND_URL = "http://localhost:8000/upload/"

def upload_file():
    """Handles file upload and sends it to the FastAPI backend."""
    uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

    if uploaded_file is not None:
        # Save the uploaded file temporarily
        with open("uploaded_file.csv", "wb") as f:
            f.write(uploaded_file.getbuffer())

        # Show progress while uploading
        with st.spinner("Sending data to backend..."):
            files = {'file': open("uploaded_file.csv", 'rb')}
            try:
                response = requests.post(BACKEND_URL, files=files)
                result = response.json()

                if response.status_code == 200 and result['status'] == "success":
                    st.success("Maintenance Summary:")
                    st.write(result['summary'])
                else:
                    st.error("Error: " + result.get('message', 'Unknown error'))
            except Exception as e:
                st.error(f"Error: {str(e)}")

def main():
    """Main app function to display the Streamlit interface."""
    st.title("Predictive Maintenance Dashboard")
    st.write("Upload your machine data CSV to analyze for maintenance suggestions.")

    upload_file()

if __name__ == "__main__":
    main()
