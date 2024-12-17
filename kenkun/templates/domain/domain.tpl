from dataclasses import dataclass, field
from datetime import datetime as dt
from mongodb.base import MongoEntity

@dataclass
class {{domain.title()}}(MongoEntity):

    date_created: dt = None
    last_updated: dt = None    

    # put domain properties here      
    
    

    # default constructor
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
                
    # domain string representation
    def to_string(self):
        return f"{self._id}"
        