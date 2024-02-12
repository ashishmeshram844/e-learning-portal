# def handle_model_validation():
#     def decorator(fun):
#         def wrapper(*args, **kwargs):  
#             try:         
#                 return fun(*args, **kwargs)
#             except Exception as e:
#                 raise ValueError(f"Server connection error")
#         return wrapper
#     return decorator




def handle_model_validation(fun):
    def wrapper(*args, **kwargs):  
        try:         
            return fun(*args, **kwargs)
        except Exception as e:
            raise ValueError(f"Server connection error")
    return wrapper


