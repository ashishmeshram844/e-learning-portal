from pymongo import MongoClient
from config.logger.all_loggers import create_db_log_message
import inspect

connection_string = 'mongodb://root:Ashish123@localhost:27017/'

CONNECTION_DB = connection_string

class Database():
    """
    Base database class for the engine drivers
    All confidential variables are private so they are not accessible to the child class
    """
    def __init__(
        self, 
        username: str = None , 
        passwd: str = None, 
        connection: str = CONNECTION_DB
        ):
        self.__username = username
        self.__passwd = passwd
        self.__connection = connection
        self.__client = None

    def __enter__(self):
        return self.get_pymongo_client()

    def __exit__(self):
        self.close()

    def get_pymongo_client(
        self
        ):
        try:
            self.__client = MongoClient(self.__connection)
            return self.__client
        except Exception as e:
            create_db_log_message(
                message=f"Failed to connect mongodb  because : {e}",
                state=('warning'),
                module=f"{__name__}.{inspect.stack()[0][3]}"
            )

    def close(self):
        self.__client.close()

class PymongoDB(Database):
    """
    Protects confidential information.
    Only this class is to be used, so the confidential variables will not be exposed in the coded
    """
    def __init__(self):
        super().__init__()
     
