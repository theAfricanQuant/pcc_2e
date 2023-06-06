filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''.join(line.strip() for line in lines)
print(f"{pi_string[:52]}...")
print(len(pi_string))
