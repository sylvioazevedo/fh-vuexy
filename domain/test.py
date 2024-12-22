from dataclasses import dataclass, field
from datetime import datetime as dt, date
from mongodb.base import MongoEntity

@dataclass
class Test(MongoEntity):

    date_created: dt = None
    last_updated: dt = None    

    # put domain properties here
    name: str = None
    description: str = field(default=None, metadata='textarea')	
    birthday: date = None

    # default constructor
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
                
    # domain string representation
    def to_string(self):
        return f"{self._id}"
        