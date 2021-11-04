import csv
if __name__ == '__main__':
    write_numbers_file = open("./Kanch-2065-lab11/numbers.csv", "w")
    write_numbers_file.write("2,4,6\n")
    write_numbers_file.write("3,7,5\n")
    write_numbers_file.write("8,9,7\n")
    write_numbers_file.close()

    read_numbers_file = open("./Kanch-2065-lab11/numbers.csv", "r")
    line = read_numbers_file.read()
    txt_array = []
    for i in line:
        if i != ',' and i != '\n':
            txt_array.append(i)
    read_numbers_file.close()

    first_row = [txt_array[2], txt_array[1], txt_array[0], float(txt_array[1])]
    second_row = [txt_array[5], txt_array[4],
                  txt_array[3], float(txt_array[5])]
    third_row = [txt_array[8], txt_array[7], txt_array[6], float(txt_array[6])]

    write_numbers2_file = open("./Kanch-2065-lab11/numbers2.csv", "w")
    write_outfile = csv.writer(write_numbers2_file)
    write_outfile.writerow(first_row)
    print(first_row)
    write_outfile.writerow(second_row)
    print(second_row)
    write_outfile.writerow(third_row)
    print(third_row)
