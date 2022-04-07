MIN_LENGTH = 4

def get_password(MIN_LENGTH):
    password = input(f"Enter your password with at least {MIN_LENGTH} characters:")
    while len(password) < MIN_LENGTH:
        print("Your password is less than the minimum number required")
        password = input(f"Enter your password with at least {MIN_LENGTH} characters:")
    return password

def main():
    password = get_password(MIN_LENGTH)
    print_star(password)
    
    
def print_star(password):
    print('*' * len(password))
    
main()