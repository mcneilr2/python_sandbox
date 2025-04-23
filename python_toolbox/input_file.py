
# Reading from an Input File in Python
def read_file(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    return [line.strip() for line in lines]

# Example
# contents = read_file("example.txt")
