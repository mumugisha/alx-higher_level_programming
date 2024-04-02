#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    current_list = []
    for a in range(list_length):
        try:
            result = my_list_1[a] / my_list_2[a]
        except (TypeError, ZeroDivisionError, IndexError) as e:
            if isinstance(e, TypeError):
                print("wrong type")
            elif isinstance(e, ZeroDivisionError):
                print("division by 0")
            elif isinstance(e, IndexError):
                print("out of range")
            result = 0
        finally:
            current_list.append(result)
    return current_list
