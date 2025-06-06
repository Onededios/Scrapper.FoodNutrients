
from dataclasses import dataclass    
from typing import List

@dataclass
class Atribute:
    name: str

@dataclass
class TypeElement:
    level: str

@dataclass
class Selection:
    atribute: List[Atribute]

@dataclass
class Order:
    ordtype: str
    atribute3: Atribute

@dataclass
class FoodQuery:
    type: TypeElement
    selection: Selection
    order: Order

@dataclass
class RequestCategories:
    foodQuery: FoodQuery