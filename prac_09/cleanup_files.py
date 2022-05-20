import os


def main():
    """Process all subdirectories using os.walk()."""
    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        '''
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))
        '''

        for filename in filenames:
            new_name = get_fixed_filename(get_filename(filename))
            print("Renaming {} to {}".format(filename, new_name))
            full_name = os.path.join(directory_name, filename)
            new_name = os.path.join(directory_name, get_fixed_filename(filename))
            os.rename(full_name, new_name)

def get_fixed_filename (filename) :
    """Return a 'fixed' version of filename."""
    new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
    return new_name

def get_filename(filename):
    if ' ' in filename or "_" in filename:
        return filename

    else:
        for z in range(len(filename) - 1):
            if filename[z].islower() and filename[z + 1].isupper():
                filename = filename[:z + 1] + ' ' + filename[z + 1:]
        return filename
main()
