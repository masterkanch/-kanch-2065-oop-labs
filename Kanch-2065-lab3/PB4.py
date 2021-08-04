VOWELS = ['A','E','I','O','U']

def return_char(string):
    char = [char for char in string]
    return char

def check_vowel(char):
    if char.upper() in VOWELS:
        return char.upper()

if __name__ == "__main__":
    string = input("Enter a string: ")
    chars = return_char(string)
    print(f"chars are {chars}")
    print(f"The enterd string is {string} and the result of convert a vowel to uppercase is")
    result = [ vowel for vowel in list(map(check_vowel,chars)) if vowel]
    print(result)

   
