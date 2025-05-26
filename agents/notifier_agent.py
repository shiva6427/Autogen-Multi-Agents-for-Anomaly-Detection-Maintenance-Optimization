from autogen import AssistantAgent

# Create the AssistantAgent
notifier_agent = AssistantAgent(
    name="notifier_agent",
    llm_config={"config_list": [{"model": "gpt-4"}]},
    system_message=(
        "You are the Notifier Agent. Your job is to send a clear and professional message "
        "to the human maintenance supervisor. Summarize the anomaly detected, insights from the knowledge base, "
        "and the proposed maintenance action. Make the message concise, actionable, and formatted as a report "
        "or notification."
    )
)
