

l1 = [1, 3, 5, 2, 8]
l2 = [4, 2, 5, 6, 7, 8, 0]
l3 = [5, 2, 7]
# p = couple_list(l1,l2)


def decorate_list(function_to_decorate):
    def wrapper(*args):
        print(len(args))
        result = function_to_decorate(*args)
        print(result)
        l = []
        for i in result:
            if i not in l:
                l.append(i)
        print(l)
    return wrapper

@decorate_list
def couple_list(*args):
    sum = []
    for i in args:
        sum += i 
    return sum

couple_list(l1, l2, l3)



