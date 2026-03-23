import subprocess

def run_command(command):
    result = subprocess.run(
        command,
        shell=True,
        capture_output=True,
        text=True
    )
    return result.stdout, result.stderr


def terraform_validate():
    stdout, stderr = run_command("terraform validate")
    return stdout if stdout else stderr


def terraform_plan():
    stdout, stderr = run_command("terraform plan -no-color")
    return stdout if stdout else stderr


def detect_drift(plan_output):
    if "No changes" in plan_output:
        return "NO_DRIFT"
    elif "Plan:" in plan_output:
        return "DRIFT_DETECTED"
    else:
        return "UNKNOWN"