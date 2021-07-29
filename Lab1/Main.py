#Kanch Ruansiripiyakul 633040206-5 

def compute_avg_list(number):
    inputnumber = list(map(int,input(f"Enter {number} positive number:").split())) 
    print(f"Numbers are {inputnumber}")
    avg = sum(inputnumber) / number
    print(f"The average number of the list is {avg}")

def compute_avg():
    listnum = []
    while True:
        number = int(input("Enter positive number:"))
        if number == 0:
            print(f"Numbers are {listnum}")
            avg = sum(listnum) / len(listnum)
            print(f"The average number of list is {avg}")
            break
        elif number < 0:
            pass
        elif number != 0:
            listnum.append(number)

if __name__ == "__main__":
    compute_avg()
    
