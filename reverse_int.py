
def reverse_int(x):
    if x<0:
        str_x = str(abs(x))[::-1]
        if -int(str_x) < -2147483647:
            return 0
        return -int(str_x)
    else:
        str_x = str(x)[::-1]
        if int(str_x) > 2147483646:
            return 0
        return int(str_x)
