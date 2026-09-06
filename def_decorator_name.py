def decorator_name(func):
    def  wrapper(*arg, **kwargs):
        print("before Execution")
        result = func(*arg, **kwargs)
        print("After Execution")
        return result
    return wrapper
    
@decorator_name
def add(a,b):
    return a+b

print(add(5,3))
