from models import PetProfile, Task
from pet_task_library import TaskLibrary
# Main file 
def create_pet_profile():
    pet_name = str(input("Enter the name of your pet: "))
    pet_birthdate = str(input("Enter the birthdate of your pet (MM/DD/YYYY): "))
    pet_photo = str(input("Enter the file path for a photo of your pet: "))
    pet_gender = str(input("Enter the gender of your pet: "))
    pet_type = str(input("Enter the type of your pet (e.g., dog, cat, horse, etc.): "))
    
    new_pet_profile = PetProfile(pet_name, pet_birthdate, pet_photo, pet_gender, pet_type)

    optional_info = str(input("Would you like to add optional information about your pet? (yes/no): "))
    if optional_info.lower() == "yes":
        pet_breed = str(input("Enter the breed of your pet: "))
       
        pet_bio = str(input("Enter a short bio for your pet (max of 150 characters): "))
        if len(pet_bio) > 150:
            print("Bio must be 150 characters or less. Please try again.")
            pet_bio = str(input("Enter a short bio for your pet: "))

        pet_medications = []
        while True:
            medication = str(input("Enter a medication for your pet (or type 'done' to finish): "))
            if medication.lower() == "done":
                break
            pet_medications.append(medication)

        pet_allergies = []
        while True:
            allergy = str(input("Enter an allergy for your pet (or type 'done' to finish): "))
            if allergy.lower() == "done":
                break
            pet_allergies.append(allergy)

        new_pet_profile.set_pet_breed(pet_breed)
        new_pet_profile.set_pet_bio(pet_bio)
        new_pet_profile.set_pet_medications(pet_medications)
        new_pet_profile.set_pet_allergies(pet_allergies)
    return new_pet_profile

def create_task():
    task_name = str(input("Enter the name of the task: "))
    task_instructions = str(input("Enter instructions for the task: "))

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

# Main function to run the pet care tracker application
def run_pet_care_tracker():
    pet_profiles = []
    tasks = []
    library = TaskLibrary() # Initialize the task library to load existing tasks from file
    
    while True:
        print("\nWelcome to the Pet Care Tracker!")
        print("1. Create a new pet profile")
        print("2. View existing pet profiles")
        print("3. Create a new task")
        print("4. View existing tasks")
        print("5. Open task management menu")
        print("6. Exit")
        
        choice = input("Please enter your choice (1-6): ")
        
        if choice == "1":
            new_pet_profile = create_pet_profile()
            pet_profiles.append(new_pet_profile)
            print(f"Pet profile for {new_pet_profile.get_pet_name()} created successfully!")
        
        elif choice == "2":
            if not pet_profiles:
                print("No pet profiles found.")
            else:
                for profile in pet_profiles:
                    print(f"Name: {profile.get_pet_name()}, Birthdate: {profile.get_pet_birthdate()}, Type: {profile.get_pet_type()}")
        
        elif choice == "3":
            new_task = create_task()
            library.add_task(new_task) # Add the new task to the task library
            print(f"Task '{new_task.get_task_name()}' created successfully!")
        
        elif choice == "4":
            all_tasks = library.list_tasks()
            if not all_tasks:
                print("No tasks found.")
            else:
                for task in all_tasks:
                    print(f"Name: {task.get_task_name()}, Instructions: {task.get_task_instructions()}")

        elif choice == "5":
            library.task_management_menu()
        
        elif choice == "6":
            print("Thank you for using the Pet Care Tracker! Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

run_pet_care_tracker()