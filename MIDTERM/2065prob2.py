# 633040206-5 Kanch Ruansiripiyakul
def get_trips_info(hometown="Nakhonpanom"):
    trip_data = {}
    while True:
        try:
            trip = input("Enter a trip year (e.g. 2021):")
            if trip == 'q' or trip == 'Q':
                return trip_data
            trip = int(trip)
            if trip <= 2000 or trip >= 2021:
                print(
                    "A valid trip year is an integer in the range [2000,2021]")
                continue
            place = input("Enter a places you visit: ")
            trip_data[trip] = place.split(',')
            trip_data[trip].append(hometown)
        except ValueError:
            print("Please enter a valid year.")


def print_welcome_msg(NAME, ID, HOMETOWN):
    print(
        f"Welcome to the program prob2.py by {NAME}, {ID} who has hometown as {HOMETOWN}")


def display_trips_info(trips):
    if trips is not None:
        print(trips)


def search_trip_year(trips, place):
    for key, values in trips.items():
        for value in values:
            if place == value:
                return key


if __name__ == "__main__":
    print_welcome_msg("Kanch", "633040206-5", "Nakhon panom")
    trips = get_trips_info()
    display_trips_info(trips)
    place = input("Enter place for which you want to search: ")
    year = search_trip_year(trips, place)
    if year:
        print(f"Trip {place} happened in {year}")
    else:
        print(f"cannot find the year for the trip to {place}")
