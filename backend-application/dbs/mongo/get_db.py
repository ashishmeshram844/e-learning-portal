from .mongo import PymongoDB

def get_db():
    try:
        db = PymongoDB().get_pymongo_client()['db_name']
        dbs = PymongoDB().get_pymongo_client().list_database_names()
        if 'db_name' in dbs:
            return db
        else:
            return None
    except Exception as e:
        return None
    

