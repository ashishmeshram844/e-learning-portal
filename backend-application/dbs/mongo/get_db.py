from .mongo import PymongoDB
from fastapi import HTTPException
from fastapi import status
from config.logger.all_loggers import create_db_log_message
import inspect
from routes.custom_exception import NotFoundException

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
        else:
            create_db_log_message(
                message=f"{db_name} database is not available",
                state=('info'),
                module=f"{__name__}.{inspect.stack()[0][3]}"
            )
    except Exception as e:
        create_db_log_message(
            message=f"failed to get database because : {e}",
            state=('warning'),
            module=f"{__name__}.{inspect.stack()[0][3]}"
        )
    raise HTTPException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail="Database Connection Error"
        )

