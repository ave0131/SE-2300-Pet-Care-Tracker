from models import Task, PetProfile, CompletedTaskPage
from error_handling import ErrorHandling
import json
class TaskLibrary:
    def __init__(self):
        self.__tasks = [] # List to store all tasks in the library
        self.load_tasks() # Load tasks from file when initializing the library
    
    # Predefined tasks that can be added to pet profiles COMING IN LATER DEVELOPMENT
    __predefined_tasks = [
        Task("Feed", "Feed pet according to their dietary needs."),
        Task("Walk", "Take pet for a walk"),
        Task("Groom", "Groom pet to maintain hygiene."),
        Task("Vet Visit", "Schedule regular vet visits for health check-ups."),
        Task("Medication", "Administer medications to pet."),
        Task("Playtime", "Engage pet in playtime activities for mental stimulation."),
        Task("Training", "Train pet to follow commands and improve behavior."),
        Task("Cleaning", "Clean pet's living area regularly to maintain hygiene.")
    ]
    
    # Method to add a new task to the library
    def add_task(self, task):
        self.__tasks.append(task)
   
    # Method to list all tasks in the library
    def list_tasks(self):
        return self.__tasks
    
    # Method to get all tasks assigned to a specific pet by their ID
    def get_tasks_for_pet(self, pet_id):
        assigned_tasks = []
        for task in self.__tasks:
            if pet_id in task.get_task_assigned_pet_ids():
                assigned_tasks.append(task)
        return assigned_tasks
    
    # Method to save tasks to a JSON file
    def save_tasks(self):
        tasks_data = []
        for task in self.__tasks:
            tasks_data.append(task.to_dict()) # Convert each task to a dictionary for JSON serialization)
        
        with open("tasks.json", "w") as file:
            json.dump(tasks_data, file)
        print("Tasks saved successfully.")
    
    # Method to load tasks from a JSON file
    def load_tasks(self):
        try:
            with open("tasks.json", "r") as file:
                tasks_data = json.load(file)
                for task_info in tasks_data:
                    task = Task(task_info["task_name"], task_info["task_instructions"])
                    task.set_task_id(task_info["task_id"])
                    task.set_task_is_completed(task_info["is_task_completed"])
                    task.set_task_time(task_info["scheduled_task_time"])
                    task.set_task_date(task_info["scheduled_task_date"])
                    task.set_task_frequency(task_info["scheduled_task_frequency"])
                    task.set_task_assigned_pet_ids(task_info["assigned_pet_ids"])
                    self.__tasks.append(task)
            print("Tasks loaded successfully.")
        except FileNotFoundError:
            print("No saved tasks found. Starting with an empty task library.")
    
    # Method to delete a task from the library by its ID
    def delete_task(self, task_id):
        task_found = any(task.get_task_id() == task_id for task in self.__tasks)
        self.__tasks = [task for task in self.__tasks if task.get_task_id() != task_id]
        self.save_tasks()
        return task_found
   
    
    # Method to find a task by its ID
    def find_task_by_id(self, task_id):
        for task in self.__tasks:
            if task.get_task_id() == task_id:
                return task
        return None

    # Method to assign a task to a pet by their IDs
    def assign_task_to_pet(self, task_id, pet_id):
        task = self.find_task_by_id(task_id)
        if task:
            task.assign_task_to_pet(pet_id)
            self.save_tasks()
            return True
        return False
    
    # Method to unassign a task from a pet by their IDs
    def unassign_task_from_pet(self, task_id, pet_id):
        task = self.find_task_by_id(task_id)
        if task:
            task.unassign_task_from_pet(pet_id)
            self.save_tasks()
            return True
        return False
    
    # Method to mark a task as completed by its ID
    def mark_task_completed(self, task_id):
        task = self.find_task_by_id(task_id)
        if task:
            task.mark_task_completed()
            self.save_tasks()
            completed_task_page = CompletedTaskPage(task)
            completed_task_page.display_completed_task()
            return True
        return False
    
    def mark_task_uncompleted(self, task_id):
        task = self.find_task_by_id(task_id)
        if task:
            task.set_task_is_completed(False)
            self.save_tasks()
            return True
        return False

    # Method to clear all tasks from the library
    def clear_all_tasks(self):
        self.load_tasks() # Load existing tasks before clearing
        self.__tasks = []
        self.save_tasks()
    
    # Method to edit a task's attributes by its ID
    def edit_task(self, task_id, new_name=None, new_instructions=None, new_time=None, new_date=None, new_frequency=None):
        task = self.find_task_by_id(task_id)
        if task:
            if new_name is not None and new_name.strip() != "":
                task.set_task_name(new_name)
            if new_instructions is not None and new_instructions.strip() != "":
                task.set_task_instructions(new_instructions)
            if new_time is not None and new_time.strip() != "":
                task.set_task_time(new_time)
            if new_date is not None and new_date.strip() != "":
                task.set_task_date(new_date)
            if new_frequency is not None and new_frequency.strip() != "":
                task.set_task_frequency(new_frequency)

            self.save_tasks()
            return True
        return False


    # Method to display the task management menu and handle user input for task management actions
    def task_management_menu(self):
        while True:
            print("\nTask Management Menu:")
            print("1. View existing tasks")
            print("2. Assign a task to a pet")
            print("3. Unassign a task from a pet")
            print("4. Edit a task")
            print("5. Delete a task")
            print("6. Mark a task as completed")
            print("7. Mark a task as not completed")
            print("8. View completed tasks")
            print("9. Clear all tasks")
            print("10. Return to main menu")
            print("11. Exit the application") 

            choice = input("Please enter your choice (1-11): ")
            
            if choice == "1": # View existing tasks with their IDs, names, and instructions to help the user identify which task they want to manage in the other options
                tasks = self.list_tasks()
                if not tasks:
                    print("No tasks found.")
                    continue
                print("Existing Tasks:")
                for task in tasks:
                    print(f"ID: {task.get_task_id()}, Name: {task.get_task_name()}, Instructions: {task.get_task_instructions()}")
            
            elif choice == "2": # Assign a task to a pet by prompting the user for the task ID and pet ID, and validating that both the task and pet exist before making the assignment
                task_id = input("Enter the ID of the task you want to assign to a pet: ")
                pet_id = input("Enter the ID of the pet you want to assign the task to: ")
                if self.assign_task_to_pet(task_id, pet_id):
                    print(f"Task {task_id} assigned to pet successfully.")
                else:
                    print("Task or pet not found.")

            elif choice == "3": # Unassign a task from a pet by prompting the user for the task ID and pet ID, and validating that both the task and pet exist before making the unassignment 
                task_id = input("Enter the ID of the task you want to unassign from a pet: ")
                pet_id = input("Enter the ID of the pet you want to unassign from the task: ")
                if self.unassign_task_from_pet(task_id, pet_id):
                    print("Task unassigned from pet successfully.")
                else:
                    print("Task or pet not found.")

            elif choice == "4": # Edit a task's attributes by prompting the user for the task ID and the new values for the task's name, instructions, scheduled time, date, and frequency, and validating that the task exists before making the edits
                task_id = input("Enter the ID of the task you want to edit: ")
                new_name = input("Enter the new name for the task (leave blank to keep current name): ")
                new_instructions = input("Enter the new instructions for the task (leave blank to keep current instructions): ")
                optional_scheduling = input("Do you want to update the task's scheduled time, date, or frequency? (yes/no): ")
                new_time = new_date = new_frequency = None
                if optional_scheduling.lower() == "yes":
                    new_time = input("Enter the new scheduled time for the task (HH:MM, leave blank to keep current time): ")
                    new_date = input("Enter the new scheduled date for the task (MM/DD/YYYY, leave blank to keep current date): ")
                    new_frequency = input("Enter the new frequency for the task (e.g., daily, weekly, etc., leave blank to keep current frequency): ")
                if self.edit_task(task_id, new_name or None, new_instructions or None, new_time or None, new_date or None, new_frequency or None):
                    print("Task edited successfully.")
                else:
                    print("Task not found.")
            
            elif choice == "5": # Delete a task by prompting the user for the task ID and validating that the task exists before deleting it from the library
                task_id = input("Enter the ID of the task you want to delete: ")
                if self.delete_task(task_id):
                    print("Task deleted successfully.")
                else:
                    print("Task not found.")
            
            elif choice == "6": # Mark a task as completed and display it on the completed task page
                task_id = input("Enter the ID of the task you want to mark as completed: ")
                if self.mark_task_completed(task_id):
                    print("Task marked as completed.")
                else:
                    print("Task not found.")
            
            elif choice == "7": # Mark a task as not completed and remove it from the completed task page
                task_id = input("Enter the ID of the task you want to mark as not completed: ")
                if self.mark_task_uncompleted(task_id):
                    print("Task marked as not completed.")
                else:
                    print("Task not found.")

            elif choice == "8": # Display all completed tasks on the completed task page
                completed_tasks = [task for task in self.__tasks if task.get_task_is_completed()]
                if not completed_tasks:
                    print("No completed tasks found.")
                else:
                    print("\nCompleted Tasks:")
                    for task in completed_tasks:
                        print(f"Name: {task.get_task_name()}, Instructions: {task.get_task_instructions()}, Scheduled Time: {task.get_task_time()}, Scheduled Date: {task.get_task_date()}, Frequency: {task.get_task_frequency()}")
                
            elif choice == "9": # Clear all tasks from the library with a confirmation prompt to prevent accidental deletion of all tasks
                confirmation = input("Are you sure you want to clear all tasks? This action cannot be undone. (yes/no): ")
                if confirmation.lower() == "yes":
                    self.clear_all_tasks()
                    print("All tasks cleared successfully.")
                else:
                    print("Clear all tasks cancelled.")

            elif choice == "10": # Return to the main menu
                print("Returning to main menu.")
                return

            elif choice == "11": # Exit the application
                print("Exiting Pet Care Tracker.")
                exit()

            
class PetManager:
    def __init__(self):
        self.__pet_profiles = [] # List to store all pet profiles in the system
        self.load_pet_profiles() # Load pet profiles from file when initializing


    # Method to add a new pet profile to the manager
    def add_pet_profile(self, pet_profile):
        self.__pet_profiles.append(pet_profile)
        self.save_pet_profiles() # Save pet profiles to file after adding new one

    # Method to list all pet profiles in the manager
    def list_pet_profiles(self):
        return self.__pet_profiles
    
    # Method to save pet profiles to a JSON file
    def save_pet_profiles(self):
        pets_data = []
        for profile in self.__pet_profiles:
            pet_info = {
                "pet_id": profile.get_pet_id(),
                "pet_name": profile.get_pet_name(),
                "pet_birthdate": profile.get_pet_birthdate(),
                "pet_gender": profile.get_pet_gender(),
                "pet_photo": profile.get_pet_photo(),
                "pet_breed": profile.get_pet_breed(),
                "pet_type": profile.get_pet_type(),
                "pet_medications": profile.get_pet_medications(),
                "pet_allergies": profile.get_pet_allergies(),
                "pet_bio": profile.get_pet_bio()
            }
            pets_data.append(pet_info)
        
        with open("pets.json", "w") as file:
            json.dump(pets_data, file)
        print("Pet profile saved successfully.")

    # Method to load pet profiles from a JSON file
    def load_pet_profiles(self):
        try:
            with open("pets.json", "r") as file:
                pets_data = json.load(file)
                for pet_info in pets_data:
                    pet_profile = PetProfile(pet_info["pet_name"], pet_info["pet_birthdate"], pet_info["pet_gender"], pet_info["pet_type"])
                    pet_profile.set_pet_id(pet_info["pet_id"])
                    pet_profile.set_pet_photo(pet_info["pet_photo"])
                    pet_profile.set_pet_breed(pet_info["pet_breed"])
                    pet_profile.set_pet_allergies(pet_info["pet_allergies"])
                    pet_profile.set_pet_medications(pet_info["pet_medications"])
                    pet_profile.set_pet_bio(pet_info["pet_bio"])
                    self.__pet_profiles.append(pet_profile)
            print("Pet profiles loaded successfully.")
        except FileNotFoundError:
            print("No saved pet profiles found. Starting with an empty pet manager.")

    # Method to find a pet profile by its ID
    def find_pet_profile_by_id(self, pet_id):
        for profile in self.__pet_profiles:
            if profile.get_pet_id() == pet_id:
                return profile
        return None
    
    # Method to view pets and their task assignments
    def view_pets_and_task_assignments(self, task_library):
        if not self.__pet_profiles:
            print("No pet profiles found.")
            return

        for profile in self.__pet_profiles:
            print(f"\nPet: {profile.get_pet_name()} (ID: {profile.get_pet_id()})")

            tasks = task_library.get_tasks_for_pet(profile.get_pet_id())

            if tasks:
                print("Assigned Tasks:")
                for task in tasks:
                    status = "Completed" if task.get_task_is_completed() else "Not Completed"
                    print(f"  - {task.get_task_name()} ({status}) (ID: {task.get_task_id()})")
            else:
                print("No tasks assigned to this pet.")

    # Method to edit a pet profile's attributes by its ID
    def edit_pet_profile_by_id(self, pet_id, **kwargs):
        profile = self.find_pet_profile_by_id(pet_id)
        if profile:
            for key, value in kwargs.items():
                if value is None:
                    continue
                
                setter_name = f"set_{key}"
                if hasattr(profile, setter_name):
                    if key in ["pet_medications", "pet_allergies"]:
                        if isinstance(value, list):
                            getattr(profile, setter_name)(value)
                        else:
                            print(f"Skipping {key}: expected a list, got {type(value).__name__}")
                    else:
                        getattr(profile, setter_name)(value)
                else:
                    print(f"Attribute '{key}' does not exist on PetProfile.")

            self.save_pet_profiles()
            return True
        return False

    # Method to delete a pet profile by its ID
    def delete_pet_profile_by_id(self, pet_id):
        profile = self.find_pet_profile_by_id(pet_id)
        if profile:
            self.__pet_profiles.remove(profile)
            self.save_pet_profiles()
            return True
        return False

    # Method to delete all pet profiles
    def delete_all_pet_profiles(self):
        self.__pet_profiles.clear()
        self.save_pet_profiles()

    # Method to open the pet management menu and handle user input for pet management actions
    def pet_profile_menu(self, task_library):
        while True:
            print("\nPet Profile Management Menu:")
            print("1. View all pet profiles")
            print("2. View a pet profile's details and assigned tasks")
            print("3. Edit a pet profile")
            print("4. Delete a pet profile")
            print("5. Return to main menu")
            print("6. Exit")

            choice = input("Please enter your choice (1-6): ")

            if choice == "1": # View all pet profiles with their IDs, names, birthdates, and types to help the user identify which pet profile they want to manage in the other options
                if not self.__pet_profiles:
                    print("No pet profiles found.")
                else:
                    for profile in self.__pet_profiles:
                        print(f"Name: {profile.get_pet_name()}, Birthdate: {profile.get_pet_birthdate()}, Type: {profile.get_pet_type()}, ID: {profile.get_pet_id()}, Photo: {profile.get_pet_photo()}, Breed: {profile.get_pet_breed()}, Bio: {profile.get_pet_bio()}, Medications: {profile.get_pet_medications()}, Allergies: {profile.get_pet_allergies()}")
            
            elif choice == "2": # View a pet profile's details and assigned tasks by prompting the user for the pet ID and validating that the pet exists before displaying the information
                self.view_pets_and_task_assignments(task_library)

            elif choice == "3": # Edit a pet profile's attributes by prompting the user for the pet ID and the new values for the pet's name, birthdate, type, photo, breed, bio, medications, and allergies, and validating that the pet exists before making the edits
                pet_id = input("Enter the ID of the pet profile you want to edit: ")
                new_name = input("Enter the new name for the pet (leave blank to keep current name): ")
                new_birthdate = input("Enter the new birthdate for the pet (MM/DD/YYYY, leave blank to keep current birthdate): ")
                new_type = input("Enter the new type for the pet (leave blank to keep current type): ")
                optional_update = input("Do you want to update the pet's photo, breed, medications, allergies, or bio? (yes/no): ")
                if optional_update.lower() == "yes":
                    new_photo = input("Enter the new photo file path for the pet (leave blank to keep current photo): ")
                    new_breed = input("Enter the new breed for the pet (leave blank to keep current breed): ")
                    new_bio = input("Enter the new bio for the pet (leave blank to keep current bio): ")
                    new_medications_list = None
                    new_allergies_list = None

                    new_medications = input("Enter new medications separated by commas (leave blank to keep current): ")
                    if new_medications.strip():
                        new_medications_list = [med.strip() for med in new_medications.split(",")]

                    new_allergies = input("Enter new allergies separated by commas (leave blank to keep current): ")
                    if new_allergies.strip():
                        new_allergies_list = [allergy.strip() for allergy in new_allergies.split(",")]

                    self.edit_pet_profile_by_id(
                        pet_id,
                        pet_name=new_name or None,
                        pet_birthdate=new_birthdate or None,
                        pet_type=new_type or None,
                        pet_photo=new_photo or None,
                        pet_breed=new_breed or None,
                        pet_bio=new_bio or None,
                        pet_medications=new_medications_list,
                        pet_allergies=new_allergies_list    
                    )
                if self.edit_pet_profile_by_id(pet_id, pet_name=new_name, pet_birthdate=new_birthdate, pet_type=new_type, pet_photo=new_photo, pet_breed=new_breed, pet_bio=new_bio, pet_medications=new_medications_list, pet_allergies=new_allergies_list):
                    print("Pet profile edited successfully.")
                else:
                    print("Pet profile not found.")

            elif choice == "4": # Delete a pet profile by prompting the user for the pet ID and validating that the pet exists before deleting it from the manager
                pet_id = input("Enter the ID of the pet profile you want to delete: ")
                if self.delete_pet_profile_by_id(pet_id):
                    print("Pet profile deleted successfully.")
                else:
                    print("Pet profile not found.")
            
            elif choice == "5": # Return to the main menu
                print("Returning to main menu.")
                return
            
            elif choice == "6": # Exit the application
                print("Exiting Pet Care Tracker.")
                exit()
            else:
                print("Invalid choice. Please try again.")
