"""
Kanch Ruansiripiyakul 633040206-5

Program that print from dictionary data
"""
taekwondo_olympics2020_w49k = {
    "Gold": {'Thailand'},
    "Silver": {'Spain'},
    "Bronze": {'Israel', 'Serbia'}
}

if __name__ == "__main__":
    print("The list of medals in Taekwondo Olypics 2020 women 49 kilograms:")
    for medals in taekwondo_olympics2020_w49k:
        for country in taekwondo_olympics2020_w49k[medals]:
            print(f"{country} received {medals} medal")
    print(f"The dictionary of medals is {taekwondo_olympics2020_w49k}")
