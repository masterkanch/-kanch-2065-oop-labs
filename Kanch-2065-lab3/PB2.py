fruit = ['Grapefruit', 'Longan', 'Orange', 'Apple', 'Cherry']

def convert_to_uppercase():
    for index, values in enumerate(fruit):
        fruit[index] = values.upper()
        print(f" {index+1}. {values.upper()}")

if __name__ == '__main__':
    print("After converting fruits to uppercase letters, fruits are")
    convert_to_uppercase()
    print("After sorting fruits, fruits are")
    fruit.sort()
    print(fruit)
