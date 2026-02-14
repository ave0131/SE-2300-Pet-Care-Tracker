import uuid
# This class represents a pet profile
class PetProfile:
    # Constructor to initialize the pet profile with given attributes
    def __init__(self, inputName, inputBirthdate, inputPhoto, inputGender, inputType):
        #Initializing the pet profile attributes
        self.id = str(uuid.uuid4()) # Generate a unique ID for the pet profile
        self.name = inputName
        self.birthdate = inputBirthdate
        self.photo = inputPhoto 
        self.gender = inputGender
        self.type = inputType

        #Default values for optional attributes
        self.breed = ""
        self.bio = ""
        self.medications = []
        self.allergies = []

    # Getter and setter methods for each attribute of the pet profile
    def get_pet_name(self):
        return self.name
    def set_pet_name(self, new_name):
        self.name = new_name
    def get_pet_birthdate(self):
        return self.birthdate
    def set_pet_birthdate(self, new_birthdate):
        self.birthdate = new_birthdate
    def get_pet_photo(self):
        return self.photo
    def set_pet_photo(self, new_photo):
        self.photo = new_photo
    def get_pet_gender (self):
        return self.gender
    def set_pet_gender(self, new_gender):
        self.gender = new_gender
    def get_pet_type(self):
        return self.type
    def set_pet_type(self, new_type):
        self.type = new_type
    def get_pet_breed(self):
        return self.breed
    def set_pet_breed(self, new_breed):
        self.breed = new_breed
    def get_pet_bio(self):
        return self.bio
    def set_pet_bio(self, new_bio):
        self.bio = new_bio
    def get_pet_medications(self):
        return self.medications
    def set_pet_medications(self, new_medications):
        self.medications = new_medications
    def get_pet_allergies(self):        
        return self.allergies
    def set_pet_allergies(self, new_allergies):
        self.allergies = new_allergies
    def get_pet_id(self):
        return self.id

   # Methods to add a single medication or allergy to the pet profile
    def add_pet_medication(self, medication):
        self.medications.append(medication)
    def add_pet_allergy(self, allergy):
        self.allergies.append(allergy)

    def remove_pet_medication(self, medication):
        if medication in self.medications:
            self.medications.remove(medication)
    def remove_pet_allergy(self, allergy):
        if allergy in self.allergies:
            self.allergies.remove(allergy)
    
    
# This class represents a task that can be assigned to a pet    
class Task:
    # Constructor to initialize the task with given attributes
    def __init__(self, inputName, inputInstructions):
        self.id = str(uuid.uuid4()) # Generate a unique ID for the task
        self.name = inputName
        self.instructions = inputInstructions
        # Default values for optional attributes
        self.is_completed = False 
        self.time = ""
        self.date = ""
        self.frequency = ""
        self.assigned_pet_ids = []
    
    # Getter and setter methods for each attribute of the task
    def get_task_name(self):
        return self.name
    def set_task_name(self, new_name):
        self.name = new_name
    def get_task_instructions(self):
        return self.instructions
    def set_task_instructions(self, new_instructions):
        self.instructions = new_instructions
    def get_task_is_completed(self):
        return self.is_completed
    def get_task_time(self):
        return self.time
    def set_task_time(self, new_time):
        self.time = new_time
    def get_task_date(self):
        return self.date
    def set_task_date(self, new_date):
        self.date = new_date
    def get_task_frequency(self):
        return self.frequency
    def set_task_frequency(self, new_frequency):
        self.frequency = new_frequency  
    def get_task_assigned_pet_ids(self):
        return self.assigned_pet_ids
    
    #Method to mark the task as completed
    def mark_task_completed(self):
        self.is_completed = True
    #Method to assign the task to a pet by adding the pet's ID to the assigned_pet_ids list
    def assign_task_to_pet(self, pet_id):
        if pet_id not in self.assigned_pet_ids:
            self.assigned_pet_ids.append(pet_id)
    #Method to unassign the task from a pet by removing the pet's ID from the assigned_pet_ids list
    def unassign_task_from_pet(self, pet_id):
        if pet_id in self.assigned_pet_ids:
            self.assigned_pet_ids.remove(pet_id)
    

    
