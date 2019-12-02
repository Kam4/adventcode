
def main():
    input_file = open(r'C:\Users\kmudy\Documents\Python Scripts\data\input2.txt')

    string_list = input_file.read()
    string_array = string_list.split(",")

    int_array = list(map(int, string_array))

    calc(int_array)
    print (int_array)




def calc(list):
    for i in range(0,len(list),4):
            if list[i] == 1:
                pos_1 = list[i+1]
                pos_2 = list[i+2]
                pos_3 = list[i+3]

                list[pos_3] = list[pos_1] + list[pos_2]
                
            if list[i] == 2:
                pos_1 = list[i+1]
                pos_2 = list[i+2]
                pos_3 = list[i+3]

                list[pos_3] = list[pos_1] * list[pos_2]
               
            if list[i] == 99:
                break
    return list

if __name__ == "__main__":
    main()
        


