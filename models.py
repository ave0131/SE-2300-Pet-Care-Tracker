import uuid
# This class represents a pet profile
class PetProfile:
    # Constructor to initialize the pet profile with given attributes
    def __init__(self, inputName, inputBirthdate, inputGender, inputType):
        #Initializing the pet profile attributes
        self.__profile_id = str(uuid.uuid4()) # Generate a unique ID for the pet profile
        self.__pet_name = inputName
        self.__pet_birthdate = inputBirthdate
        self.__pet_gender = inputGender
        self.__pet_type = inputType

        #Default values for optional attributes
        self.__pet_photo = "default_photo.jpg" # Default photo if none provided
        self.__pet_breed = ""
        self.__pet_bio = ""
        self.__pet_medications = []
        self.__pet_allergies = []

    # Getter and setter methods for each attribute of the pet profile
    def get_pet_name(self):
        return self.__pet_name
    def set_pet_name(self, new_name):
        self.__pet_name = new_name
    def get_pet_birthdate(self):
        return self.__pet_birthdate
    def set_pet_birthdate(self, new_birthdate):
        self.__pet_birthdate = new_birthdate
    def get_pet_photo(self):
        return self.__pet_photo
    def set_pet_photo(self, new_photo):
        self.__pet_photo = new_photo
    def get_pet_gender (self):
        return self.__pet_gender
    def set_pet_gender(self, new_gender):
        self.__pet_gender = new_gender
    def get_pet_type(self):
        return self.__pet_type
    def set_pet_type(self, new_type):
        self.__pet_type = new_type
    def get_pet_breed(self):
        return self.__pet_breed
    def set_pet_breed(self, new_breed):
        self.__pet_breed = new_breed
    def get_pet_bio(self):
        return self.__pet_bio
    def set_pet_bio(self, new_bio):
        self.__pet_bio = new_bio
    def get_pet_medications(self):
        return self.__pet_medications
    def set_pet_medications(self, new_medications):
        self.__pet_medications = new_medications
    def get_pet_allergies(self):        
        return self.__pet_allergies
    def set_pet_allergies(self, new_allergies):
        self.__pet_allergies = new_allergies
    def get_pet_id(self):
        return self.__profile_id
    def set_pet_id(self, new_id):
        self.__profile_id = new_id

   # Methods to add a single medication or allergy to the pet profile
    def add_pet_medication(self, medication):
        self.__pet_medications.append(medication)
    def add_pet_allergy(self, allergy):
        self.__pet_allergies.append(allergy)

    def remove_pet_medication(self, medication):
        if medication in self.__pet_medications:
            self.__pet_medications.remove(medication)
        else: 
            print(f"Medication '{medication}' not found in pet's medication list.")
    def remove_pet_allergy(self, allergy):
        if allergy in self.__pet_allergies:
            self.__pet_allergies.remove(allergy)
        else:
            print(f"Allergy '{allergy}' not found in pet's allergy list.")
    
    
# This class represents a task that can be assigned to a pet    
class Task:
    # Constructor to initialize the task with given attributes
    def __init__(self, inputName, inputInstructions):
        self.__task_id = str(uuid.uuid4()) # Generate a unique ID for the task
        self.__task_name = inputName
        self.__task_instructions = inputInstructions
        # Default values for optional attributes
        self.__is_task_completed = False 
        self.__scheduled_task_time = ""
        self.__scheduled_task_date = ""
        self.__scheduled_task_frequency = ""
        self.__assigned_pet_ids = []
    
    # Getter and setter methods for each attribute of the task
    def get_task_name(self):
        return self.__task_name
    def set_task_name(self, new_name):
        self.__task_name = new_name
    def get_task_instructions(self):
        return self.__task_instructions
    def set_task_instructions(self, new_instructions):
        self.__task_instructions = new_instructions
    def get_task_is_completed(self):
        return self.__is_task_completed
    def set_task_is_completed(self, is_completed):
        self.__is_task_completed = is_completed
    def get_task_time(self):
        return self.__scheduled_task_time
    def set_task_time(self, new_time):
        self.__scheduled_task_time = new_time
    def get_task_date(self):
        return self.__scheduled_task_date
    def set_task_date(self, new_date):
        self.__scheduled_task_date = new_date
    def get_task_frequency(self):
        return self.__scheduled_task_frequency
    def set_task_frequency(self, new_frequency):
        self.__scheduled_task_frequency = new_frequency  
    def get_task_assigned_pet_ids(self):
        return self.__assigned_pet_ids
    def set_task_assigned_pet_ids(self, new_assigned_pet_ids):
        self.__assigned_pet_ids = new_assigned_pet_ids
    def get_task_id(self):
        return self.__task_id
    def set_task_id(self, new_id):
        self.__task_id = new_id  
    
    #Method to mark the task as completed
    def mark_task_completed(self):
        self.__is_task_completed = True
    #Method to assign the task to a pet by adding the pet's ID to the assigned_pet_ids list
    def assign_task_to_pet(self, pet_id):
        if pet_id not in self.__assigned_pet_ids:
            self.__assigned_pet_ids.append(pet_id)
        else:
            print(f"Task is already assigned to pet with ID: {pet_id}")
    #Method to unassign the task from a pet by removing the pet's ID from the assigned_pet_ids list
    def unassign_task_from_pet(self, pet_id):
        if pet_id in self.__assigned_pet_ids:
            self.__assigned_pet_ids.remove(pet_id)
        else:
            print(f"Task is not assigned to pet with ID: {pet_id}")

# Method to convert the task object to a dictionary for JSON serialization
    def to_dict(self):
        return {
            "task_id": self.__task_id,
            "task_name": self.__task_name,
            "task_instructions": self.__task_instructions,
            "is_task_completed": self.__is_task_completed,
            "scheduled_task_time": self.__scheduled_task_time,
            "scheduled_task_date": self.__scheduled_task_date,
            "scheduled_task_frequency": self.__scheduled_task_frequency,
            "assigned_pet_ids": self.__assigned_pet_ids
        }
    
class CompletedTaskPage:
    def __init__(self, task):
        self.__task = task
    
    def display_completed_task(self):
        if self.__task.get_task_is_completed():
            print(f"Task Name: {self.__task.get_task_name()}")
            print(f"Instructions: {self.__task.get_task_instructions()}")
            print(f"Scheduled Time: {self.__task.get_task_time()}")
            print(f"Scheduled Date: {self.__task.get_task_date()}")
            print(f"Frequency: {self.__task.get_task_frequency()}")
            print("Status: Completed")