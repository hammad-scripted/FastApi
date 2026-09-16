from pydantic import BaseModel

class MenuItem(BaseModel):
    name: str
    price: float
    id:int
    category: str
    description: str
    available: bool
    

class MenuResponse(BaseModel):
    status: str="success"
    count:int
    menu_items: list[MenuItem]
    