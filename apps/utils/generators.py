from django.contrib.auth import get_user_model
import random
import string 


User = get_user_model()

class Generator:

    def generate_username(self, *args):
        """Generate a unique username based on the first name, last name, and a unique number."""
        if len(args) < 3:
            raise ValueError("Not enough arguments provided. Expected: firstname, lastname, existing_usernames")
        
        firstname, lastname, existing_usernames = args
        
        base_username = f"{firstname.lower()}.{lastname.lower()}"
        username = base_username
        counter = 1
        
        while username in existing_usernames:
            username = f"{firstname.lower()}{counter}.{lastname.lower()}"
            counter += 1
            
        return username

    def generate_random_phone_no(self):
        """Generate a random phone number with 10 digits."""
        return ''.join(random.choices(string.digits, k=10))
    
    def create_user(self, **kwargs):

        """Create a user with a unique username and a password based on DOB."""
        if not all(k in kwargs for k in ("first_name", "last_name", "dob" )):
            raise ValueError("Not enough arguments provided. Expected: first_name, last_name, dob.")
        
        existing_usernames = list(User.objects.values_list('username', flat=True))
        dob = kwargs["dob"].strftime('%d-%m-%Y')
               
        first_name = kwargs.get("first_name")
        last_name = kwargs["last_name"]
        email = kwargs.get("email")  
        phone_no = kwargs.get("phone_no") or self.generate_random_phone_no()
        
        # Generate username and set password
        username = self.generate_username(first_name, last_name, existing_usernames)
        
        if not email:
            email = f"{username}@attendo.com"
            
        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            dob=dob,
            email=email,
            phone_no=phone_no,
            username=username,
            password=dob
        )
        user.role = "employee"
        user.save()
        return user 