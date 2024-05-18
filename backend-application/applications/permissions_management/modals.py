"""
Contain all modal which are used in groups  management application
"""

from pydantic import BaseModel, validator
from datetime import datetime
import uuid
from applications.custom_validators import override_uuid



from applications.apis_management.modals import ApiAvailDataModal

class AddPermissionsModal(BaseModel):
    """
    Sample request modal while adding permission in group
    - request should contains this modal fields while adding permission
    in a specific group
    """
    id : str
    api_permissions : list[str]

    @validator('id')
    def override_id_value(cls,id):
        """
        Override uuid of the client request data
        """
        return override_uuid()

