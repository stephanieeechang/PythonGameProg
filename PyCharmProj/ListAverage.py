#calculates and prints the average of a list
def list_average(listNum = [1, 2, 3, 3, 4]):
    sum = 0
    x = 0
    length = 0
    for i in listNum:
        try:
            sum += i*1.0
            length += 1
        except TypeError:
            print('Skipped list: ' + str(i))

    average = sum/length
    print(average)

list_num = [1, 2, '4', '5']
list_average(list_num)
