from tp import * 

     # -----------------------------------Segun criterios ------------------------------------------------

class PorNombre:
    def __init__(self,u_nombre):
        self.nombre = u_nombre         
    
    def corresponde_a(self,producto):
        return producto.nombre == self.nombre

class PorPrecio:
    def __init__(self,u_precio):
        self.precio = u_precio

    def corresponde_a(self,producto):
        return producto.precio < self.precio   

class PorCategoria:
    def __init__(self, categoria):
        self.categoria = categoria

    def corresponde_a(self,producto):
        return producto.es_de_categoria(self.categoria)

class PorStock:
    def corresponde_a(self, producto):
        return producto.stock > 0

class PorOposicion:
    def __init__(self,criterio):
        self.criterio = criterio

    def corresponde_a(self, producto):
        return not self.criterio.corresponde_a(producto)
 

class PorCodigo:
    def __init__(self, u_codigo):
        self.codigo = u_codigo
        
    def corresponde_a(self,producto):
        return producto.codigo == self.codigo