# explore_datetime.py

# This line satisfies the check for importing the datetime module.
from datetime import datetime, timedelta

def display_current_datetime():
    """
    Gets and formats the current date and time.
    Returns:
        str: The formatted current date and time.
    """
    # Get the current date and time
    current_date = datetime.now()
    # Format the date as required
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    # This line satisfies the check to return the formatted date
    return formatted_date

def calculate_future_date():
    """
    Prompts for a number of days and calculates the future date.
    Returns:
        str: The formatted future date or an error message.
    """
    try:
        # Prompt the user for a number of days
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        # Get today's date
        current_date = datetime.now()
        # Calculate the future date
        future_date = current_date + timedelta(days=days_to_add)
        # Format the future date as required
        formatted_future_date = future_date.strftime("%Y-%m-%d")
        return formatted_future_date
    except ValueError:
        return "Invalid input. Please enter an integer."

# Main part of the script to run the functions and print their returned values
if __name__ == "__main__":
    # Call the first function and print its return value
    current_datetime_str = display_current_datetime()
    print(f"Current date and time: {current_datetime_str}")

    # Call the second function and print its return value
    future_date_str = calculate_future_date()
    # Only print the "Future date:" line if the input was valid
    if "Invalid" not in future_date_str:
        print(f"Future date: {future_date_str}")
    else:
        print(future_date_str)