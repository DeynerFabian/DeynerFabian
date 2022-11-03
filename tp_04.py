class Sucursal:
    def __init__(self):
        self.productos = []

    def registrar_producto(self,producto):
        self.productos.append(producto)

    def recargar_stock(self,codigo_producto,cantidad_agregar):
        for producto in self.productos:
            if codigo_producto == producto.codigo:
               producto.stock += cantidad_agregar

    def actualizar_precio_segun(self,criterio,porcentaje):
        for producto in self.productos:
            if criterio.corresponde_a(producto):
                producto.precio += (producto.precio*porcentaje)/100

    def lista_de_producto_segun(self,criterio): # 2 
        productos_x = []
        for producto in self.productos:
            if criterio.corresponde_a(producto):
             productos_x.append(producto)
        return productos_x
      #  return [producto for producto in self.productos if criterio.corresponde_a(producto)]
        
class Producto:
    def __init__(self,u_codigo,u_nombre,u_precio,u_categoria):
        self.codigo = u_codigo
        self.nombre = u_nombre
        self.precio = u_precio
        self.categoria = u_categoria
        self.estado = Nuevo()
        self.stock = 0

class Nuevo:
    pass     

class PorPrecio:
    def __init__(self,u_precio):
        self.precio = u_precio

    def corresponde_a(self,producto):
        return producto.precio < self.precio   

class PorNombre:
    def __init__(self,u_nombre):
        self.nombre = u_nombre         
    
    def corresponde_a(self,producto):
        return producto.nombre == self.nombre

class PorStock:

    def corresponde_a(self,producto): # 1.3 
        return producto.stock == 0

class PorCategoria:
    def __init__(self,u_categoria):
        self.categoria = u_categoria

    def corresponde_a(self,producto):
        return producto.categoria == self.categoria
