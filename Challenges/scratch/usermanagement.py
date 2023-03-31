from scratch import User

def print_user_details(users):
    with open('Scratch/usermanagement.txt', 'w') as file:
        for user in users:
            file.write(f"{user.first_name} {user.last_name}\n")
            
def remove_user(userid):
    with open('Scratch/users.txt', 'r') as file:
        lines = file.readlines()
    with open('Scratch/users.txt', 'w') as file:
        for line in lines:
            if line.split(',')[2] != userid:
                file.write(line)
                
def add_user(first_name, last_name, userid, email):
    with open('Scratch/users.txt', 'a') as file:
        file.write(f"{first_name},{last_name},{userid},{email}\n")