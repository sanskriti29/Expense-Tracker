from pydantic import BaseModel,HttpUrl
from typing import List,Set,Optional
from enum import Enum

class Categories(str,Enum):
    laptop = "Laptop"
    phone = "Mobile Phones"
    watch = "Watches"
    speaker = "Speakers"

class Images(BaseModel):
    url : HttpUrl
    name : str

class Items(BaseModel):
    name:str
    price:float
    category:Categories
    tags : Set
    image : Optional[Images] = None
