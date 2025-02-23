from datetime import datetime
import re # Import Regex

def validate_task_title(title):
    pattern = r'^[A-Za-z0-9][A-Za-z0-9\s\-_.,]{1,48}[A-Za-z0-9]$' # Regex pattern to validate a task title. Will look for start and end letters or numbers and can contain spaces, hyphens, underscores, comas, and periods.
    return bool(re.fullmatch(pattern, title))
    
def validate_task_description(description):
    pattern = r'^[A-Za-z0-9][A-Za-z0-9\s\-_.,!?"\'()]{3,498}[A-Za-z0-9.!?]$'
    match = bool(re.fullmatch(pattern, description))

    # if not match:
    #     print(f"Debugging: Description '{description}' has failed to validate.")


    return bool(match)

def validate_due_date(due_date):
    # print(f"Debugging Statement: validating due date {due_date}")

    pattern = r'^\d{4}-\d{2}-\d{2}$' # This works on the format YYYY-MM-DD
    if not re.fullmatch(pattern, due_date):
        # print("Debugging Regex: Regex Failed Validation")
        return False

    try:
        datetime.strptime(due_date, "%Y-%m-%d")
        # print("Debug: Date is Valid!")
        return True # Bug was found here!
    except ValueError:
        # print("Debug: Date parsing failed")
        return False

# dd_test = validate_due_date("1995-06-24")
# print(dd_test)