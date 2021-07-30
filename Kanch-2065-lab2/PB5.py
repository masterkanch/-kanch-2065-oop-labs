"""
Kanch Ruansiripiyakul 633040206-5

Program that print from dictionary data
"""
taekwondo_olympics2020_w49k = {
    "Gold": {'Thailand'}
}

if __name__ == "__main__":
    taekwondo_olympics2020_w49k["Silver"] = {'Spain'}
    taekwondo_olympics2020_w49k["Bronze"] = {'Israel','Serbia'}
    print("The list of medals in Taekwondo Olypics 2020 women 49 kilograms:")
    for medals in taekwondo_olympics2020_w49k:
        for country in taekwondo_olympics2020_w49k[medals]:
            print(f"{country} received {medals} medal")
    print(f"The dictionary of medals is {taekwondo_olympics2020_w49k}")
