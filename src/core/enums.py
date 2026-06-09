from enum import Enum 

class TypeProduct(Enum):
    ELECTRONICO = "electronico"
    DOMESTICO = "domestico"
    CONSUMO = "consumo"

class TypeRoles(Enum):
    ADMIN = "admin"
    USER = "user"