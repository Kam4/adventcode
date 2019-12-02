
def main():
    input_file = open(r'path to file')

    string_list = input_file.read()
    string_array = string_list.split(",")

    int_array = list(map(int, string_array))

    iter_array = [None] * len(int_array)


    

    for k in range(0,100):
        for j in range(0,100):
            copy_array(int_array, iter_array) 
            iter_array[1] = k
            iter_array[2] = j 
            
            calc(iter_array)

            if iter_array[0] == 19690720:
                print (iter_array[1], iter_array[2])

   

def copy_array(list, list1):
    for i in range(0, len(list)):
        list1[i] = list[i]



def calc(list):
    for i in range(0,len(list),4):
        if list[i] == 1:
            pos_1 = list[i+1]
            pos_2 = list[i+2]
            pos_3 = list[i+3]

            list[pos_3] = list[pos_1] + list[pos_2]
            #print(list[1], list[2])
                
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
        


