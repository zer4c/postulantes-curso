cont = 0
product = []


class ProductService:
    @staticmethod
    def create_product():
        producto = {
            "id": cont,
            "name": f"coca-cola-{cont}",
            "empresa": "cocacola"
        }
        product.append(producto)
        return producto
    
    @staticmethod
    def get_by_id(id : int):
        try: 
            return product[id]
        except:
            return None
    
    @staticmethod
    def get_all_products():
        return product
    
