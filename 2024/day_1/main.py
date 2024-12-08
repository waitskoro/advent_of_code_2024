import copy

PATH = "./2024/day_1/text.txt"

def get_lists_from_string(data):
    number_of_characters = len(data)

    left_list = [];
    right_list = [];

    for i in range(number_of_characters):
        if i % 2 == 0:
            left_list.append(data[i])
        else: 
            right_list.append(data[i])

    return left_list, right_list


def getDifferenceAddition(left_list, right_list):
    sum = 0
    
    while(len(left_list) > 0 and len(right_list) > 0):
        min_left = min(left_list)
        min_right = min(right_list)

        if min_left > min_right:
            sum = sum + (int(min_left) - int(min_right))
        if min_right > min_left:
            sum = sum + (int(min_right) - int(min_left))

        left_list.remove(min_left)
        right_list.remove(min_right)

    print("Сумма для первого решения:", sum)


def getDifferenceMultiplication(left_list, right_list):
    sum = 0

    for i in range(len(left_list)):
        count = 0

        for j in range(len(right_list)):
            if left_list[i] == right_list[j]:
                count = count + 1
        
        sum = sum + (int(left_list[i]) * count)
        count = 0

    print("Сумма для второго решения:", sum)

if __name__ == '__main__':
    file = open(PATH, "r")
    data = file.read().split()
    
    lists = get_lists_from_string(data)

    getDifferenceAddition(copy.copy(lists[0]), copy.copy(lists[1]))
    getDifferenceMultiplication(lists[0], lists[1])