def time(func):
    import time
    def wrap_func(*args, **kwargs): 
        start_time = time.time() 
        result = func(*args, **kwargs) 
        end_time = time.time() 
        print(f'{func.__doc__} answer is {result}. Done in {(end_time-start_time):.1f}s') 
        return result 
    return wrap_func 