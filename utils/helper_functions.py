# utils/helper_functions.py

import datetime

def format_timestamp(ts: str) -> str:
    """Convert ISO timestamp to a friendlier format."""
    try:
        dt = datetime.datetime.fromisoformat(ts)
        return dt.strftime("%Y-%m-%d %H:%M")
    except Exception:
        return ts

def log_event(event: str, level: str = "INFO"):
    """Basic logger for events."""
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{level}] {now} — {event}")
