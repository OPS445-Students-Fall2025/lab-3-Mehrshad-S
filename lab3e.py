#!/usr/bin/env python3

# Global list (declared before functions)
my_list = [100, 200, 300, 'six hundred']

def give_list():
    # Return the whole list unchanged
    return my_list

def give_first_item():
    # Return the first item as a string
    return str(my_list[0])

def give_first_and_last_item():
    # Return [first, last]
    return [my_list[0], my_list[-1]]

def give_second_and_third_item():
    # Return [second, third]
    return [my_list[1], my_list[2]]

if __name__ == '__main__':
    print(give_list())
    print(give_first_item())
    print(give_first_and_last_item())
    print(give_second_and_third_item())

