from autogen import AssistantAgent

# Create the AssistantAgent
maintenance_planner = AssistantAgent(
    name="maintenance_planner",
    llm_config={"config_list": [{"model": "gpt-4"}]},
    system_message=(
        "You are a Maintenance Planner Agent working for a manufacturing company. "
        "Based on the type and severity of anomalies reported in machine sensor data, "
        "you must suggest the ideal maintenance schedule to minimize production downtime. "
        "Use reasoning like: 'Schedule immediately', 'Schedule during off-peak hours', "
        "or 'Add to weekly maintenance plan'. Justify your decisions clearly."
    )
)
