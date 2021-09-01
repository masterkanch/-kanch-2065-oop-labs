"""
Kanch Ruansiripiyakul 633040206-5
"""
filename = input("Enter a filename: ")
f = open(f'{filename}', 'r')
try:
    print(f.read())
finally:
    f.close()
