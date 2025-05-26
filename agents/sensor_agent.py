from autogen import AssistantAgent
import pandas as pd
import os

# Helper function to read and check for anomalies in sensor data
def check_for_anomalies(file_path):
    df = pd.read_csv(file_path)

    anomaly_report = []
    for col in df.columns:
        if col == "timestamp":
            continue
        mean = df[col].mean()
        std = df[col].std()
        for index, value in enumerate(df[col]):
            if abs(value - mean) > 3 * std:
                anomaly_report.append(
                    f"Anomaly in {col} at row {index} — value={value:.2f}, mean={mean:.2f}, std={std:.2f}"
                )

    return "\n".join(anomaly_report) if anomaly_report else "No anomalies detected."

# Create the AssistantAgent
sensor_data_analyzer = AssistantAgent(
    name="sensor_data_analyzer",
    llm_config={"config_list": [{"model": "gpt-4"}]},
    system_message=(
        "You are a Sensor Data Analyzer Agent. Your job is to analyze the machine sensor data "
        "and detect anomalies using statistical methods (e.g., 3-sigma rule). "
        "You will receive a CSV file path and must respond with any detected anomalies."
    ),
    code_execution_config={"work_dir": "scratch"}
)

# Register a function for anomaly detection
@sensor_data_analyzer.register_for_execution()
def detect_anomalies(file_path: str):
    if not os.path.exists(file_path):
        return f"File not found: {file_path}"
    return check_for_anomalies(file_path)
