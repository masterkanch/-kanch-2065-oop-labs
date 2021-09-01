"""
Kanch Ruansiripiyakul 633040206-5
"""
if __name__ == "__main__":
    with open("words.txt", "r") as text_file:
        data = text_file.read().split()
        print(data)
        print(f"There are {len(data)} words in file words.txt")
