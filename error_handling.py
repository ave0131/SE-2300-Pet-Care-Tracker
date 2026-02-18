class ErrorHandling:

    def __init__(self):
        pass
    
    # Method to validate user input for pet profile attributes
    def validate_pet_profile_input(self, name, birthdate, gender, pet_type):
        is_valid = True
        if not name:
            print("Pet name cannot be empty.")
            is_valid = False
        if len(name) > 30:
            print("Pet name cannot exceed 30 characters.")
            is_valid = False
        if not name.isalpha():
            print("Pet name cannot contain numbers or special characters. Please enter a valid name.")
            is_valid = False
        if not birthdate:
            print("Pet birthdate cannot be empty.")
            is_valid = False
        if len(birthdate) > 10:
            print("Pet birthdate cannot exceed 10 characters (MM/DD/YYYY).")
            is_valid = False
        if birthdate.isalpha():
            print("Pet birthdate cannot contain letters. Please enter a valid date in MM/DD/YYYY format.")
            is_valid = False
        if not "/" in birthdate:
            print("Pet birthdate must be in MM/DD/YYYY format. Please include '/' as a separator.")
            is_valid = False
        if not gender:
            print("Pet gender cannot be empty.")
            is_valid = False
        if gender.lower() not in ["male", "m", "female", "f", "other", "o"]:
            print("Invalid gender. Please enter 'Male', 'Female', or 'Other'.")
            is_valid = False
        if not pet_type:
            print("Pet type cannot be empty.")
            is_valid = False
        if len(pet_type) > 20:
            print("Pet type cannot exceed 20 characters.")
            is_valid = False
        if pet_type.isdigit() or pet_type.isalpha() == False:
            print("Pet type cannot contain numbers or special characters. Please enter a valid pet type.")
            is_valid = False
        return is_valid
    
    # Method to validate user input for task attributes
    def validate_task_input(self, name, instructions):
        is_valid = True
        if not name:
            print("Task name cannot be empty.")
            is_valid = False
        if len(name) > 30:
            print("Task name cannot exceed 30 characters.")
            is_valid = False
        if not instructions:
            print("Task instructions cannot be empty.")
            is_valid = False
        if len(instructions) > 150:
            print("Task instructions cannot exceed 150 characters.")
            is_valid = False
        return is_valid
    
    # Method to validate user input for optional pet profile attributes
    def validate_optional_attributes(self, photo, breed, bio, medications, allergies):
        if photo:
            if len(photo) > 100:
                print("Photo file path cannot exceed 100 characters.")
        if breed:
            if len(breed) > 30:
                print("Breed cannot exceed 30 characters.")
        if bio:
            if len(bio) > 150:
                print("Bio cannot exceed 150 characters.")
        if medications:
            if len(medications) > 150:
                print("Medications information cannot exceed 150 characters.")
        if allergies:
            if len(allergies) > 150:
                print("Allergies information cannot exceed 150 characters.")

    # Method to validate user input for optional task attributes
    def validate_optional_task_attributes(self, scheduled_time, scheduled_date, scheduled_frequency):
        if scheduled_time:
            if len(scheduled_time) > 5:
                print("Scheduled time cannot exceed 5 characters (HH:MM).")
            if scheduled_time.isalpha():
                print("Scheduled time cannot contain letters. Please enter a valid time in HH:MM format.")
            if not ":" in scheduled_time:
                print("Scheduled time must be in HH:MM format. Please include ':' as a separator.")
        if scheduled_date:
            if len(scheduled_date) > 10:
                print("Scheduled date cannot exceed 10 characters (MM/DD/YYYY).")
            if scheduled_date.isalpha():
                print("Scheduled date cannot contain letters. Please enter a valid date in MM/DD/YYYY format.")
            if not "/" in scheduled_date:
                print("Scheduled date must be in MM/DD/YYYY format. Please include '/' as a separator.")
        if scheduled_frequency:
            if len(scheduled_frequency) > 20:
                print("Scheduled frequency cannot exceed 20 characters.")
            if scheduled_frequency.isalpha() == False or scheduled_frequency.isdigit():
                print("Scheduled frequency cannot contain special characters. Please enter a valid frequency (e.g., 'Daily', 'Weekly', 'Monthly').")
