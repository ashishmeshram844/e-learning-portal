

class NotFoundException(Exception):
    def __str__(self) -> dict:
        return {
            'status' : 404,
            'body' : [],
            'message' : 'not found'
        }