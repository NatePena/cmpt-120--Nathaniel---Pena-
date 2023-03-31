from scratch import User

users = []

with open('Scratch/users.txt', 'r') as file:
    for line in file:
        user_data = line.strip().split(',')
        user = User(first_name=user_data[0], last_name=user_data[1], userid=user_data[2], email=user_data[3])
        users.append(user)
        
        

