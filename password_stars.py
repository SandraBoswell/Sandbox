minimum_length = 10
password = input(f"Password (must be {minimum_length} long): ")
while len(password) < minimum_length:
    print("invalid password")
    password = input(f"Password (must be {minimum_length} long): ")
print("*" * len(password))
