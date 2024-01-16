


def handle_custom_exception(func):
    def wrapper_func(*args, **kwargs):
        try:
            print("BEFORE")
            res = func(*args, **kwargs)
            print(res)
            print("LST")
        except Exception as e:
            return e
    return wrapper_func