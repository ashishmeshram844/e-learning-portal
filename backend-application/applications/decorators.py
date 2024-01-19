



def get_all_data(collection = None):
    def decorator(func):
        print("DDD")
        def wrapper(*args, **kwargs):
            print("ONNN")
            print(*args)
            
            print(f"Decorator parameter: {collection}")
            result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator