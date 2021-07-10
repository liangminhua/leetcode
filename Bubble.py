def bubble_sort(input_list):
    for i in range(len(input_list)):
        for j in range(i):
            if int(input_list[j]) > int(input_list[j+1]):
                input_list[j], input_list[j+1] = input_list[j+1], input_list[j]
    return input_list


if __name__ == "__main__":
    input_list = [10, 1, 2, 11]
    print(bubble_sort(input_list))
