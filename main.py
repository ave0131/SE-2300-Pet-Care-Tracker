from models import PetProfile, Task
from pet_task_library import TaskLibrary, PetManager
from error_handling import ErrorHandling
error_handler = ErrorHandling()
# Main file 
# Method to create a new pet profile by prompting the user for input and validating the input using the error handling class
def create_pet_profile():
    while True:
        pet_name = str(input("Enter the name of your pet: ")).strip()
        pet_birthdate = str(input("Enter the birthdate of your pet (MM/DD/YYYY): ")).strip()
        pet_gender = str(input("Enter the gender of your pet: ")).strip()
        pet_type = str(input("Enter the type of your pet (e.g. dog, cat, horse, etc.): ")).strip()
        if error_handler.validate_pet_profile_input(pet_name, pet_birthdate, pet_gender, pet_type):
            break
    new_pet_profile = PetProfile(pet_name, pet_birthdate, pet_gender, pet_type)

    optional_info = str(input("Would you like to add optional information about your pet? (yes/no): "))
    if optional_info.lower() == "yes":
        pet_photo = str(input("Enter the file path for a photo of your pet: ")).strip()
        pet_breed = str(input("Enter the breed of your pet: ")).strip()
        pet_bio = str(input("Enter a short bio for your pet (max of 150 characters): ")).strip()

        pet_medications = []
        while True:
            medication = str(input("Enter a medication for your pet (or type 'done' to finish): ")).strip()
            if medication.lower() == "done":
                break
            pet_medications.append(medication)

        pet_allergies = []
        while True:
            allergy = str(input("Enter an allergy for your pet (or type 'done' to finish): ")).strip()
            if allergy.lower() == "done":
                break
            pet_allergies.append(allergy)
        
        error_handler.validate_optional_attributes(pet_photo, pet_breed, pet_bio, pet_medications, pet_allergies)

        new_pet_profile.set_pet_photo(pet_photo)
        new_pet_profile.set_pet_breed(pet_breed)
        new_pet_profile.set_pet_bio(pet_bio)
        new_pet_profile.set_pet_medications(pet_medications)
        new_pet_profile.set_pet_allergies(pet_allergies)
    return new_pet_profile

# Method to create a new task by prompting the user for input and validating the input using the error handling class
def create_task():
    while True:
        task_name = str(input("Enter the name of the task: "))
        task_instructions = str(input("Enter instructions for the task: "))
        if error_handler.validate_task_input(task_name, task_instructions):
            break
    new_task = Task(task_name, task_instructions)

    is_optional = str(input("Would you like to schedule this task? (yes/no): "))
    if is_optional.lower() == "yes":
        scheduled_time = str(input("Enter the scheduled time for the task (HH:MM): "))
        scheduled_date = str(input("Enter the scheduled date for the task (MM/DD/YYYY): "))
        scheduled_frequency = str(input("Enter the frequency for the task (e.g., daily, weekly, etc.): "))

        new_task.set_task_time(scheduled_time)
        new_task.set_task_date(scheduled_date)
        new_task.set_task_frequency(scheduled_frequency)
    return new_task

def exit_program():
    print("Thank you for using the Pet Care Tracker! Goodbye!")
    exit()

# Main function to run the pet care tracker application
def run_pet_care_tracker():
    library = TaskLibrary() # Initialize the task library to load existing tasks from file
    pet_manager = PetManager() # Access the pet manager from the task library to load existing pet profiles from file   
    
    while True:
        print("\nWelcome to the Pet Care Tracker!")
        print("1. Create a new pet profile")
        print("2. View existing pet profiles")
        print("3. Open pet profile menu")
        print("4. Create a new task")
        print("5. View existing tasks")
        print("6. Open task management menu")
        print("7. Exit")
        
        choice = input("Please enter your choice (1-7): ")
    
        if choice == "1":
            new_pet_profile = create_pet_profile()
            pet_manager.add_pet_profile(new_pet_profile) # Add the new pet profile to the pet manager
            print(f"Pet profile for {new_pet_profile.get_pet_name()} created successfully!")
        
        elif choice == "2":
            profiles = pet_manager.list_pet_profiles() # Get the list of pet profiles from the pet manager
            if not profiles:
                print("No pet profiles found.")
            else:
                for profile in profiles:
                    print(f"Name: {profile.get_pet_name()}, Birthdate: {profile.get_pet_birthdate()}, Type: {profile.get_pet_type()}")
        
        elif choice == "3":
            pet_manager.pet_profile_menu(library) # Pass the task library to the pet profile menu to allow for task assignments within the menu 
        
        elif choice == "4":
            new_task = create_task()
            library.add_task(new_task) # Add the new task to the task library
            library.save_tasks() # Save the updated task list to file
            print(f"Task '{new_task.get_task_name()}' created successfully!")
        
        elif choice == "5":
            all_tasks = library.list_tasks()
            if not all_tasks:
                print("No tasks found.")
            else:
                for task in all_tasks:
                    print(f"Name: {task.get_task_name()}, Instructions: {task.get_task_instructions()}")

        elif choice == "6":
            library.task_management_menu()
        
        elif choice == "7":
            exit_program()
            break

        else:
            print("Invalid choice. Please try again.")

run_pet_care_tracker()
