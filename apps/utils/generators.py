import random
import string

class Generator:

    def generate_username(self, *args):
        """Generate a unique username based on the first name, last name, and a unique number."""
        if len(args) < 3:
            raise ValueError("Not enough arguments provided. Expected: firstname, lastname, existing_usernames")
        
        firstname, lastname, existing_usernames = args
        
        base_username = f"{firstname.lower()}.{lastname.lower()}"
        username = base_username
        counter = 1
        
        # Ensure uniqueness
        while username in existing_usernames:
            username = f"{base_username}{counter}"
            counter += 1
        
        return username

    def create_user(self, **kwargs):
        """Create a user with a unique username and a password based on DOB."""
        if not all(k in kwargs for k in ("first_name", "last_name", "dob", "existing_usernames")):
            raise ValueError("Not enough arguments provided. Expected: firstname, lastname, dob, existing_usernames")
        
        first_name = kwargs["first_name"]
        last_name = kwargs["last_name"]
        dob = kwargs["dob"]
        existing_usernames = kwargs["existing_usernames"]
        
        # Generate username and set password
        username = self.generate_username(first_name, last_name, existing_usernames)
        password = dob  # Assuming dob is in the format 'DD-MM-YYYY'
        
        return {
            'username': username,
            'password': password
        }
