def filtr_name(func_to_dec):
    def wrapper():
        res = func_to_dec()

        l = []
        for i in res:
            print(i[0])
            if i[0].lower() == "a":
                l.append(i)
        return l
    return wrapper
@filtr_name
def list_of_names():
    return ["Aman", "Askat", "Bolot", "Gulnaz", "Akjol"]

p = list_of_names()

print(p)