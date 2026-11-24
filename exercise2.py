def display_main_menu():
    print("enter some numbers seperated by commas (e.g 5,67,32)")

def calc_average():
    print("calc_average")

def get_user_input():

    user_input = input("enter your numbers: ")
    print("user input " + user_input)
    str_list = user_input.split ("," )
    float_list = [float(x) for x in str_list]
    print(float_list)
    return float_list

def find_min_max():
    print("find_min_max")

def sort_temperature():
    print("sort_temperature")

def calc_median_temperature():
    print("calc_median_temperature")

print(get_user_input())