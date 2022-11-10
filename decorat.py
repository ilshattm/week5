def logger(func):
    def wrapper(*args, **kwargs):
        print(f'Function "{func.__name__}()" called with {args}, {kwargs} arguments')
        result = func(*args, **kwargs)
        print(f'Result after calling function: {result}')
        return result
    return wrapper

@logger
def say(name, text):
    """Citata cheloveka"""
    return f'{name}: "{text}"'

print(say(name="Asan", text="Decorators are great!!!"))