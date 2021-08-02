if __name__ == "__main__":
    string = input("Enter a string:")
    chars = []
    for index, values in enumerate(string):
        chars.append(values)
    print(f"chars are {chars}")
    print(f"The enterd string is {string} and the result of convert a vowel to uppercase is")
    check_vowel = [char.upper() for char in chars if char == 'a' or char == 'e' or char == 'i' or char ==
                   'o' or char == 'u' or char == 'A' or char == 'E' or char == 'I' or char == 'O' or char == 'U']
    print(check_vowel)
