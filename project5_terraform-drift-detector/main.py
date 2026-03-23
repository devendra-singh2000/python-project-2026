from utils.terraform import terraform_validate, terraform_plan, detect_drift
from utils.report import generate_report
from colorama import Fore, Style

def main():
    print(Fore.CYAN + "🚀 Terraform Drift Detector\n" + Style.RESET_ALL)

    print("🔍 Running terraform validate...")
    validate_output = terraform_validate()
    print(validate_output)

    print("\n📦 Running terraform plan...")
    plan_output = terraform_plan()

    status = detect_drift(plan_output)

    if status == "NO_DRIFT":
        print(Fore.GREEN + "✅ No Drift Detected" + Style.RESET_ALL)
    elif status == "DRIFT_DETECTED":
        print(Fore.RED + "⚠️ Drift Detected!" + Style.RESET_ALL)
    else:
        print(Fore.YELLOW + "❓ Unknown Status" + Style.RESET_ALL)

    print("\n📊 Generating report...")
    print(generate_report(status, plan_output))


if __name__ == "__main__":
    main()