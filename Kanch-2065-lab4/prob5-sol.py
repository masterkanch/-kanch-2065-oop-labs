import logging
logging.basicConfig(level=logging.DEBUG)
n1 = int(input("Enter n1:"))
n2 = int(input("Enter n2:"))
logging.debug('hello')
result = n1 / n2
print(f"The result is {result}")
logging.debug(f'n1 = {n1}')
logging.debug(f'n2 = {n2}')
