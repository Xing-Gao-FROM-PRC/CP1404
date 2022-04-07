FILENAME = "subject_data.txt"

def main():
    data = get_data()
    show_subjects(data)
    
def get_data():
    data = []
    input_file = open(FILENAME)
    for line in input_file:
        print(line)
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(parts)
        data.append(parts)    
    input_file.close()
    return data
        
def show_subjects(data):
    for subject_data in data:
        print("{} is taught by {:12} and has {:3} students".format(*subject_data))
        
main()