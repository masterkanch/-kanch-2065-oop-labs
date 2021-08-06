fruit = ['Grapefruit', 'Longan', 'Orange', 'Apple', 'Cherry']

if __name__ == '__main__':
    print("After converting fruits to uppercase letters, fruits are")
    for index, values in enumerate(fruit):
        fruit[index] = values.upper()
        print(f" {index+1}. {values.upper()}")
    print("After sorting fruits, fruits are")
    fruit.sort()
    print(fruit)
