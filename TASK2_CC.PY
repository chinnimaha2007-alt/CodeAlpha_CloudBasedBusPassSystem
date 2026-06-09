# Import UUID module for generating unique Pass IDs
import uuid
# Dictionary to store bus pass details
passes = {}
# Function to book a new bus pass
def book_pass():
    # Get user details
    name = input("Enter Name: ")
    route = input("Enter Route: ")
    # Fixed fare for demonstration
    fare = 50
    # Generate unique Pass ID
    pass_id = str(uuid.uuid4())[:8]
    # Store pass details
    passes[pass_id] = {
        "name": name,
        "route": route,
        "fare": fare
    }
    # Display booking confirmation
    print("\nPass Booked Successfully")
    print("Pass ID:", pass_id)
    print("Fare:", fare)
# Function to view an existing pass
def view_pass():
    # Ask user for Pass ID
    pass_id = input("Enter Pass ID: ")
    # Check if pass exists
    if pass_id in passes:
        print("\nPass Details")
        print(passes[pass_id])
    else:
        print("Pass Not Found")
# Main Program Loop
while True:
    # Display menu options
    print("\n===== Cloud Based Bus Pass System =====")
    print("1. Book Pass")
    print("2. View Pass")
    print("3. Exit")
    # Take user choice
    choice = input("Enter Choice: ")
    # Book a new pass
    if choice == "1":
        book_pass()
    # View existing pass
    elif choice == "2":
        view_pass()
    # Exit application
    elif choice == "3":
        print("Thank You For Using The System")
        break
    # Handle invalid input
    else:
        print("Invalid Choice")