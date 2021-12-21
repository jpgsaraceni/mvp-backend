from pydantic import BaseModel

class ResponseSchema (BaseModel):
    ''' Response schema '''
    message: str
    data: dict
