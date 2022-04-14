def main():
    email_to_name = {}
    email = input("Email: ")
    while email !="":
        name = get_name_from_email(email)
        confirm_name = input(f"Is you name {name}? (Y/N) ")
        if confirm_name.upper =="N" or confirm_name =="no" :
            name = input("Name:")
            email_to_name[email] = name
        else:
            email_to_name[email] = name
        email = input("Email: ")
    for email,name in email_to_name.items():
        print(f"{name} ({email})")

def get_name_from_email(email):
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    name = " ".join(parts).title()
    return name


if __name__ == '__main__':
    main()