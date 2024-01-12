from .mongo import PymongoDB
from fastapi import HTTPException
from fastapi import status

def get_db(db_name: str = None) -> any : 
    """
    This function help to connect database which provided in parameter
    - Parameters : 
        - db_name : select this database while querying in mongodb
    """
    try:
        db = PymongoDB().get_pymongo_client()[db_name]
        dbs = PymongoDB().get_pymongo_client().list_database_names()
        if db_name in dbs:
            return db
    except Exception as e:
        pass
    raise HTTPException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail="Database Connection Error"
        )
