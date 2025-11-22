#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    res_list = []
    res = ""
    for i in range(list_length):
        try:
            div_res = my_list_1[i] / my_list_2[i]
            res_list.append(div_res)
        except ZeroDivisionError:
            res += "division by 0\n"
            res_list.append(0)
        except TypeError:
            res += "wrong type\n"
            res_list.append(0)
        except IndexError:
            res += "out of range"
            res_list.append(0)
        finally:
            pass
    return res + "\n" + str(res_list)
