from pydantic import BaseModel, validator

class CategoriesSchema(BaseModel):
    ''' Category schema '''
    name: str
    description: str

    @validator('name')
    def validate_name_lenght (cls, name): # pylint: disable=no-self-argument
        ''' Validate category name  lenght '''
        if not (len(name) > 2 and len(name) < 31):
            raise ValueError("Category name must be greater than 2 and smaller than 31 characters")

        return name.capitalize()

    @validator('description')
    def validate_description_lenght (cls, description): # pylint: disable=no-self-argument
        ''' Validate category description lenght '''
        if not (len(description) > 2 and len(description) < 141):
            raise ValueError("Description must be greater than 2 and smaller than 141 characters")

        return description.capitalize()

class CategoriesSchemaId(CategoriesSchema):
    ''' Category schema with id '''
    id: int
