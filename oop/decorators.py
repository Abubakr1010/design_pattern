from functools import wraps

class User:

    """ 
    class base decorators 
    """
    def __init__(self, func):
        self.func = func

    def __call__(self, name):
        self.func(name)
    


@User
def user_1(name):
    print (f"{name}")


user_1("Tim")



def log_execution(func):
    @wraps(func)

    
    def wrapper(*args, **kwargs):

        
        result = func(*args)
        
        """
            function base decorators 
        """
        
        print(result)
        return result

    return wrapper


@log_execution
def user_2(name:str):

    return(f"{name}")

user_2("Jack")