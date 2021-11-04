import re
if __name__ == '__main__':
    text = input("Enter text: ")
    pattern = input("Enter pattern: ")
    if re.search(pattern, text):
        print(f"Found {pattern} in {text} at {text.index(pattern)}")
    else:
        print(f"Cannot find {pattern} in {text}")
