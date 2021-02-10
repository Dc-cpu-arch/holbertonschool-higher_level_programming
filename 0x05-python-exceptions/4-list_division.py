#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    r_list = []
    for i in range(list_length):
        result = 0
        try:
            result = my_list_1[1] / my_list_2[i]
        except ZeroDivisionError:
            print('division by 0')
            result = 0
        except TypeError:
            print('wrong type')
            result = 0
        except IndexError:
            print('out of range')
            result = 0
        finally:
            r_list.append(result)
    return r_list
