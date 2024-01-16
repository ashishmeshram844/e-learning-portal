

def get_status_message(status_code = 500):
    try:
        if status_code == 404:
            return 'not found'
        if status_code == 401:
            return 'Unauthorized'
        if status_code == 403:
            return 'Forbidden'
        if status_code == 429:
            return 'Too many requests'
        if status_code == 502:
            return 'bad gateway'
        if status_code == 503:
            return 'service unavailable'
        else:
            return 'server connection error'
    except Exception as e:
        return 'server connection error'        

class CustomException(Exception):
    
    def __init__(self, status_code = 500):
        self.status = status_code
        self.message = get_status_message(status_code=status_code)
        self.body = []
        super().__init__(self)
    

        
