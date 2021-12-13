from pydantic import BaseModel

class ResponseSchema (BaseModel):
    ''' Response schema '''
    message: str
    product_id: int
