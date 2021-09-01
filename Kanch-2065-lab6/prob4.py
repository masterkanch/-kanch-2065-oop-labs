"""
Kanch Ruansiripiyakul 633040206-5
"""
import json

if __name__ == "__main__":
    with open("hobbies.json", "r") as json_file:
        data = json.load(json_file)
        print(
            f'{data["firstName"]} has hobbies as {(", ").join(data["hobbies"])}')
