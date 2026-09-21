"""
Task 2 – Alert Filter
Reads events.json and prints only events with level == "critical",
followed by a summary line «критичных N».
"""

import json
import sys
from pathlib import Path


def load_events(path: Path) -> list[dict]:
    """Load and return the list of event objects from *path* (UTF-8 JSON)."""
    with path.open(encoding="utf-8") as fh:
        return json.load(fh)


def filter_critical(events: list[dict]) -> list[dict]:
    """Return only the events whose 'level' field equals 'critical'.

    Uses e.get('level') so records missing the field are silently skipped.
    """
    return [e for e in events if e.get("level") == "critical"]


def print_results(critical_events: list[dict]) -> None:
    """Print each critical event name, then the summary count line."""
    for e in critical_events:
        print(e.get("event", "<no event>"))
    print(f"критичных {len(critical_events)}")


def main() -> None:
    """Entry point: load, filter, and display critical events."""
    events_path = Path(__file__).parent / "events.json"
    events = load_events(events_path)
    critical = filter_critical(events)
    print_results(critical)


if __name__ == "__main__":
    if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
        import io
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
    main()
