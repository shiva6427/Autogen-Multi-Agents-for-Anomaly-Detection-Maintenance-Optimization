import os
from agents.sensor_agent import sensor_data_analyzer
from agents.planner_agent import maintenance_planner
from agents.knowledge_agent import knowledge_base_agent
from agents.notifier_agent import notifier_agent

def run_multi_agent_workflow(csv_path: str) -> str:
    """
    Orchestrates the predictive maintenance workflow using AutoGen agents.
    Returns a final notification message with the maintenance summary.
    """
    if not os.path.exists(csv_path):
        return f"❌ Error: File not found — {csv_path}"

    # Step 1: Sensor Agent - detect anomalies
    print("[Step 1] Detecting anomalies...")
    anomaly_response = sensor_data_analyzer.run(
        message=f"Please analyze this file and report anomalies:\n{csv_path}"
    )

    # Step 2: Planner Agent - schedule maintenance
    print("[Step 2] Planning maintenance...")
    planner_response = maintenance_planner.run(
        message=(
            f"Based on the anomalies below, recommend a maintenance schedule:\n\n{anomaly_response.reply}"
        )
    )

    # Step 3: Knowledge Base Agent - look up known patterns
    print("[Step 3] Consulting knowledge base...")
    knowledge_response = knowledge_base_agent.run(
        message=(
            f"Here is the anomaly data and plan. Provide historical insights or similar incidents:\n\n"
            f"Anomalies:\n{anomaly_response.reply}\n\nPlan:\n{planner_response.reply}"
        )
    )

    # Step 4: Notifier Agent - summarize for human
    print("[Step 4] Generating final report...")
    notifier_response = notifier_agent.run(
        message=(
            f"Summarize the following:\n\n"
            f"Anomalies:\n{anomaly_response.reply}\n\n"
            f"Plan:\n{planner_response.reply}\n\n"
            f"Knowledge Insights:\n{knowledge_response.reply}"
        )
    )

    return notifier_response.reply
