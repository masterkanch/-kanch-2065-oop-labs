"""
Kanch Ruansiripiyakul 633040206-5
"""
read_file = input("Enter filename to read:")
append_text = input("Enter text to append:")
write_file = input("Enter file name to write:")

with open(f"{read_file}", "r") as input_file:
    with open(f"{write_file}", "w") as new_file:
        new_file.write(input_file.read())
        new_file.write(append_text)

with open(f"{write_file}", "r") as new_file:
    print(new_file.read())
