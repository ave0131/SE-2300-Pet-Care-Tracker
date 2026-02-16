from models import Task, PetProfile
import json

class TaskLibrary:
    def __init__(self):
        self._tasks = [] # List to store all tasks in the library
        self.load_tasks() # Load tasks from file when initializing the library
    
    # Predefined tasks that can be added to pet profiles
    def add_predefined_tasks(self):
        predefined_tasks = [
            Task("Feed", "Feed pet according to their dietary needs."),
            Task("Walk", "Take pet for a walk"),
            Task("Groom", "Groom pet to maintain hygiene."),
            Task("Vet Visit", "Schedule regular vet visits for health check-ups."),
            Task("Medication", "Administer medications to pet."),
            Task("Playtime", "Engage pet in playtime activities for mental stimulation."),
            Task("Training", "Train pet to follow commands and improve behavior."),
            Task("Cleaning", "Clean pet's living area regularly to maintain hygiene."),
        ]
        self._tasks.extend(predefined_tasks)
    
    # Method to add a new task to the library
    def add_task(self, task):
        self._tasks.append(task)
   
    # Method to list all tasks in the library
    def list_tasks(self):
        return self._tasks
    
    # Method to save tasks to a JSON file
    def save_tasks(self):
        tasks_data = []
        for task in self._tasks:
            task_info = {
                "task_id": task.get_task_id(),
                "task_name": task.get_task_name(),
                "task_instructions": task.get_task_instructions(),
                "is_task_completed": task._is_task_completed,
                "scheduled_task_time": task._scheduled_task_time,
                "scheduled_task_date": task._scheduled_task_date,
                "scheduled_task_frequency": task._scheduled_task_frequency,
                "assigned_pet_ids": task._assigned_pet_ids
            }
            tasks_data.append(task_info)
        
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
                    task._is_task_completed = task_info["is_task_completed"]
                    task._scheduled_task_time = task_info["scheduled_task_time"]
                    task._scheduled_task_date = task_info["scheduled_task_date"]
                    task._scheduled_task_frequency = task_info["scheduled_task_frequency"]
                    task._assigned_pet_ids = task_info["assigned_pet_ids"]
                    self._tasks.append(task)
            print("Tasks loaded successfully.")
        except FileNotFoundError:
            print("No saved tasks found. Starting with an empty task library.")
    
    # Method to delete a task from the library by its ID
    def delete_task(self, task_id):
        self._tasks = [task for task in self._tasks if task.get_task_id() != task_id]
        self.save_tasks()
    
    # Method to find a task by its ID
    def find_task_by_id(self, task_id):
        for task in self._tasks:
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
            return True
        return False

    # Method to clear all tasks from the library
    def clear_all_tasks(self):
        self.load_tasks() # Load existing tasks before clearing
        self._tasks = []
        self.save_tasks()
    
    # Method to edit a task's attributes by its ID
    def edit_task(self, task_id, new_name=None, new_instructions=None, new_time=None, new_date=None, new_frequency=None):
        task = self.find_task_by_id(task_id)
        if task:
            if new_name:
                task.set_task_name(new_name)
            if new_instructions:
                task.set_task_instructions(new_instructions)
            if new_time:
                task.set_task_time(new_time)
            if new_date:
                task.set_task_date(new_date)
            if new_frequency:
                task.set_task_frequency(new_frequency)
            self.save_tasks()
            return True
        return False
    


     #Temp method
    # Method to find a task ID by its name
    def find_task_id_by_name(self, task_name):
        for task in self._tasks:
            if task.get_task_name() == task_name:
                return task.get_task_id()
        return None
    

    
    # Method to display the task management menu and handle user input for task management actions
    def task_management_menu(self):
        while True:
            print("\nTask Management Menu:")
            print("1. Edit a task")
            print("2. Delete a task")
            print("3. Mark a task as completed")
            print("4. Unassign a task from a pet")
            print("5. Assign a task to a pet")
            print("6. Clear all tasks")
            print("7. Return to main menu")
            print("8. Find a task ID by name (temporary method for testing)")
            print("9. Exit")
            
            choice = input("Please enter your choice (1-9): ")
            
            if choice == "1":
                task_id = input("Enter the ID of the task you want to edit: ")
                new_name = input("Enter the new name for the task (leave blank to keep current name): ")
                new_instructions = input("Enter the new instructions for the task (leave blank to keep current instructions): ")
                new_time = input("Enter the new scheduled time for the task (HH:MM, leave blank to keep current time): ")
                new_date = input("Enter the new scheduled date for the task (MM/DD/YYYY, leave blank to keep current date): ")
                new_frequency = input("Enter the new frequency for the task (e.g., daily, weekly, etc., leave blank to keep current frequency): ")
                if self.edit_task(task_id, new_name, new_instructions, new_time, new_date, new_frequency):
                    print("Task edited successfully.")
                else:
                    print("Task not found.")
            
            elif choice == "2":
                task_id = input("Enter the ID of the task you want to delete: ")
                if self.delete_task(task_id):
                    print("Task deleted successfully.")
                else:
                    print("Task not found.")
            
            elif choice == "3":
                task_id = input("Enter the ID of the task you want to mark as completed: ")
                if self.mark_task_completed(task_id):
                    print("Task marked as completed.")
                else:
                    print("Task not found.")
            
            elif choice == "4":
                task_id = input("Enter the ID of the task you want to unassign from a pet: ")
                pet_id = input("Enter the ID of the pet you want to unassign from the task: ")
                if self.unassign_task_from_pet(task_id, pet_id):
                    print("Task unassigned from pet successfully.")
                else:
                    print("Task or pet not found.")
            
            elif choice == "5":
                task_id = input("Enter the ID of the task you want to assign to a pet: ")
                pet_id = input("Enter the ID of the pet you want to assign the task to: ")
                if self.assign_task_to_pet(task_id, pet_id):
                    print("Task assigned to pet successfully.")
                else:
                    print("Task or pet not found.")
            
            elif choice == "6":
                confirmation = input("Are you sure you want to clear all tasks? This action cannot be undone. (yes/no): ")
                if confirmation.lower() == "yes":
                    self.clear_all_tasks()
                    print("All tasks cleared successfully.")
                else:
                    print("Clear all tasks cancelled.")

            elif choice == "7":
                print("Returning to main menu.")
                return
            
            elif choice == "8":
                task_name = input("Enter the name of the task to find its ID: ")
                task_id = self.find_task_id_by_name(task_name)
                if task_id:
                    print(f"The ID of the task '{task_name}' is: {task_id}")
                else:
                    print("Task not found.")

            elif choice == "9":
                print("Exiting task management menu.")
                exit()

class PetManager:
    def __init__(self):
        self._pet_profiles = [] # List to store all pet profiles in the system
        self.load_pet_profiles() # Load pet profiles from file when initializing


    # Method to add a new pet profile to the manager
    def add_pet_profile(self, pet_profile):
        self._pet_profiles.append(pet_profile)

    # Method to list all pet profiles in the manager
    def list_pet_profiles(self):
        return self._pet_profiles
    
    # Method to save pet profiles to a JSON file
    def save_pet_profiles(self):
        pets_data = []
        for profile in self._pet_profiles:
            pet_info = {
                "pet_id": profile.get_pet_id(),
                "pet_name": profile.get_pet_name(),
                "pet_birthdate": profile.get_pet_birthdate(),
                "pet_type": profile.get_pet_type(),
                "pet_allergies": profile.get_pet_allergies()
            }
            pets_data.append(pet_info)
        
        with open("pets.json", "w") as file:
            json.dump(pets_data, file)
        print("Pet profiles saved successfully.")

    # Method to load pet profiles from a JSON file
    def load_pet_profiles(self):
        try:
            with open("pets.json", "r") as file:
                pets_data = json.load(file)
                for pet_info in pets_data:
                    pet_profile = PetProfile(pet_info["pet_name"], pet_info["pet_birthdate"], pet_info["pet_type"])
                    pet_profile.set_pet_id(pet_info["pet_id"])
                    pet_profile.set_pet_allergies(pet_info["pet_allergies"])
                    self._pet_profiles.append(pet_profile)
            print("Pet profiles loaded successfully.")
        except FileNotFoundError:
            print("No saved pet profiles found. Starting with an empty pet manager.")

    #CONTINUE FROM HERE--------------------

    # Method to find a pet profile by its ID
    # Method to view pets and their task assignments
    # Method to edit a pet profile's attributes by its ID
    # Method to delete a pet profile by its ID
    # Method to delete all pet profiles

    # Method to open the pet management menu and handle user input for pet management actions