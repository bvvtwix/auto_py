from pydantic import BaseModel, field_validator, ValidationError, Field

class Post(BaseModel):
    id: int
    title: str
    content: str
    user_id: int
    # test: Field(gt=2) 

    @field_validator("id")
    def check_that_id_is_less_than_two(cls, v):
        if v < 0:
            raise ValueError('Id is not less than two')
        else:
            return v



# [{'id': 1, 
# 'title': 'My first post', 
# 'content': 'The content for first post', 
# 'user_id': 1}