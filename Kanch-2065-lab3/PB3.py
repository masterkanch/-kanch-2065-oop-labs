VOWELS = ['A','E','I','O','U']

def return_vowel(list):
    vowel_checked = []
    for char in list:
        if char.upper() in VOWELS:
            vowel_checked.append(char.upper())
    return vowel_checked
                

if __name__ == "__main__":
    string = input("Enter a string:")
    chars = []
    for index, values in enumerate(string):
        chars.append(values)
    print(f"chars are {chars}")
    print(f"The enterd string is {string} and the result of convert a vowel to uppercase is")
    check_vowel = list(return_vowel(chars))
    print(check_vowel)
