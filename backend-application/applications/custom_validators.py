

from datetime import datetime,timezone
from pydantic import BaseModel,validator
from typing import Annotated,Optional
from fastapi import Query
from pydantic import Field
from uuid import uuid4
from pydantic import EmailStr
from bson import ObjectId
from dbs.mongo.queries.user_query import DBQuery
from applications.user_management.tables import USER_TABLES
import uuid


def check_val_avail(
    collection = None,
    query : tuple = None,        
    ):
    """
    check given collection has entry of query value or not
    - Arguments : 
        - collection : string - collection name in which we want to find
        - query : tuple - example (key,value)
    """
    data = DBQuery().find(
        collection=collection,
        query={query[0] : query[1]},
        only_one=True
    )
    if data.get('body'):
        raise ValueError(f'{query[0]} already registered')
    return query[1]


def convert_miliseconds_to_time(
    date_obj  
    ):
    """
    Converts miliseconds to datetime object in utc
    - Arguments : 
        - date_obj : dict | str - object which contain $date key and value is miliseconds
    """
    try:
        created = datetime.fromtimestamp(
            date_obj.get('$date') / 1000.0, tz=timezone.utc
            )
    except:
        pass
    return created


def validate_string_length(
    string = None,
    max_len = 20
    ):
    """
    Converts miliseconds to datetime object in utc
    - Arguments :
        - date_obj : dict | str - object which contain $date key and value is miliseconds
    """
    try:
        if len(string) > max_len:
            raise ValueError(f"{string} has length exceeded (string must be {max_len} size)")
    except:
        pass
    return string


def override_uuid():
    return str(uuid.uuid4())


def check_id_in_collection(
    collection = None,
    query : tuple = None,        
    ):
    data = DBQuery().find(
        collection=collection,
        query={query[0] : query[1]},
        only_one=True
    )
    if data.get('body'):
        return query[1]
    raise ValueError(f"{query[1]} is invalida")

