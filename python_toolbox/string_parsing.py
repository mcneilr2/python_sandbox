
# String Parsing in Python
def parse_string(s):
    tokens = s.split(',')
    cleaned = [t.strip() for t in tokens]
    return cleaned

# Example
data = "apple, banana, cherry"
print(parse_string(data))
