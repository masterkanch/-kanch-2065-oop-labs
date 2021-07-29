"""
Kanch Ruansiripiyakul 633040206-5

Program that return list of vowel from input words
"""

Input = input("Enter string input: ")
Input_list = list(Input)
Vowel = [char for char in Input_list if char == 'a' or char == 'e' or char == 'i' or char ==
         'o' or char == 'u' or char == 'A' or char == 'E' or char == 'I' or char == 'O' or char == 'U']
print(f"Vowels in {Input} are {Vowel}")
