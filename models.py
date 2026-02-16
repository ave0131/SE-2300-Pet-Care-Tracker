import uuid
# This class represents a pet profile
class PetProfile:
    # Constructor to initialize the pet profile with given attributes
    def __init__(self, inputName, inputBirthdate, inputPhoto, inputGender, inputType):
        #Initializing the pet profile attributes
        self._profile_id = str(uuid.uuid4()) # Generate a unique ID for the pet profile
        self._pet_name = inputName
        self._pet_birthdate = inputBirthdate
        self._pet_photo = inputPhoto 
        self._pet_gender = inputGender
        self._pet_type = inputType

        #Default values for optional attributes
        self._pet_breed = ""
        self._pet_bio = ""
        self._pet_medications = []
        self._pet_allergies = []

    # Getter and setter methods for each attribute of the pet profile
    def get_pet_name(self):
        return self._pet_name
    def set_pet_name(self, new_name):
        self._pet_name = new_name
    def get_pet_birthdate(self):
        return self._pet_birthdate
    def set_pet_birthdate(self, new_birthdate):
        self._pet_birthdate = new_birthdate
    def get_pet_photo(self):
        return self._pet_photo
    def set_pet_photo(self, new_photo):
        self._pet_photo = new_photo
    def get_pet_gender (self):
        return self._pet_gender
    def set_pet_gender(self, new_gender):
        self._pet_gender = new_gender
    def get_pet_type(self):
        return self._pet_type
    def set_pet_type(self, new_type):
        self._pet_type = new_type
    def get_pet_breed(self):
        return self._pet_breed
    def set_pet_breed(self, new_breed):
        self._pet_breed = new_breed
    def get_pet_bio(self):
        return self._pet_bio
    def set_pet_bio(self, new_bio):
        self._pet_bio = new_bio
    def get_pet_medications(self):
        return self._pet_medications
    def set_pet_medications(self, new_medications):
        self._pet_medications = new_medications
    def get_pet_allergies(self):        
        return self._pet_allergies
    def set_pet_allergies(self, new_allergies):
        self._pet_allergies = new_allergies
    def get_pet_id(self):
        return self._profile_id

   # Methods to add a single medication or allergy to the pet profile
    def add_pet_medication(self, medication):
        self._pet_medications.append(medication)
    def add_pet_allergy(self, allergy):
        self._pet_allergies.append(allergy)

    def remove_pet_medication(self, medication):
        if medication in self._pet_medications:
            self._pet_medications.remove(medication)
    def remove_pet_allergy(self, allergy):
        if allergy in self._pet_allergies:
            self._pet_allergies.remove(allergy)
    
    
# This class represents a task that can be assigned to a pet    
class Task:
    # Constructor to initialize the task with given attributes
    def __init__(self, inputName, inputInstructions):
        self._task_id = str(uuid.uuid4()) # Generate a unique ID for the task
        self._task_name = inputName
        self._task_instructions = inputInstructions
        # Default values for optional attributes
        self._is_task_completed = False 
        self._scheduled_task_time = ""
        self._scheduled_task_date = ""
        self._scheduled_task_frequency = ""
        self._assigned_pet_ids = []
    
    # Getter and setter methods for each attribute of the task
    def get_task_name(self):
        return self._task_name
    def set_task_name(self, new_name):
        self._task_name = new_name
    def get_task_instructions(self):
        return self._task_instructions
    def set_task_instructions(self, new_instructions):
        self._task_instructions = new_instructions
    def get_task_is_completed(self):
        return self._is_task_completed
    def get_task_time(self):
        return self._scheduled_task_time
    def set_task_time(self, new_time):
        self._scheduled_task_time = new_time
    def get_task_date(self):
        return self._scheduled_task_date
    def set_task_date(self, new_date):
        self._scheduled_task_date = new_date
    def get_task_frequency(self):
        return self._scheduled_task_frequency
    def set_task_frequency(self, new_frequency):
        self._scheduled_task_frequency = new_frequency  
    def get_task_assigned_pet_ids(self):
        return self._assigned_pet_ids
    def get_task_id(self):
        return self._task_id
    def set_task_id(self, new_id):
        self._task_id = new_id  
    
    #Method to mark the task as completed
    def mark_task_completed(self):
        self._is_task_completed = True
    #Method to assign the task to a pet by adding the pet's ID to the assigned_pet_ids list
    def assign_task_to_pet(self, pet_id):
        if pet_id not in self._assigned_pet_ids:
            self._assigned_pet_ids.append(pet_id)
    #Method to unassign the task from a pet by removing the pet's ID from the assigned_pet_ids list
    def unassign_task_from_pet(self, pet_id):
        if pet_id in self._assigned_pet_ids:
            self._assigned_pet_ids.remove(pet_id)
    

    
