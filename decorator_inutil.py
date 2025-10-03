from functools import wraps

def hello(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print("Isso é um decorador") # ELE SOMENTE DA UM PRINT NO MEIO DA EXECUÇAO
        return result
    return wrapper
