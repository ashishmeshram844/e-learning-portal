

from datetime import datetime,timezone
from pydantic import BaseModel,validator
from typing import Annotated,Optional
from fastapi import Query
from pydantic import Field
from uuid import uuid4
from pydantic import EmailStr
from bson import ObjectId
from .tables import USER_TABLES
from dbs.mongo.queries.user_query import DBQuery




def check_val_avail(
    collection = None,
    query : tuple = None,        
    ):
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
    try:
        created = datetime.fromtimestamp(
            date_obj.get('$date') / 1000.0, tz=timezone.utc
            )
    except:
        pass
    return created
