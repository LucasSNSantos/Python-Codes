from unittest import result


def sum(a,b):
    result = a + b
    return result

def minus(a,b):
    result = a - b
    return result

def plus(a,b):
    result = a * b
    return result

def division(a,b):
    if(a == 0):
        return "Impossible"
    else:
        return a/b    

def absolute(num):
    if(num >= 0):
        return num
    else:
        return -num

