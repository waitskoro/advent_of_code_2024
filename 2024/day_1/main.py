PATH = "./2024/day_1/text.txt"

def get_lists_from_string(stroke):
    number_of_characters = len(data)

    left_list = [];
    right_list = [];

    for i in range(number_of_characters):
        if i % 2 == 0:
            left_list.append(data[i])
        else: 
            right_list.append(data[i])

    return left_list, right_list

if __name__ == '__main__':
    file = open(PATH, "r")
    data = file.read().split()
    
    lists = get_lists_from_string(data)
    print(lists)