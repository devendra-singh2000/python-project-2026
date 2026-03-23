import json
from datetime import datetime

def generate_report(status, plan_output):
    report = {
        "timestamp": str(datetime.now()),
        "drift_status": status,
        "summary": "Terraform drift analysis",
        "details": plan_output[:500]  # limit output
    }

    with open("report.json", "w") as f:
        json.dump(report, f, indent=4)

    return "report.json created"