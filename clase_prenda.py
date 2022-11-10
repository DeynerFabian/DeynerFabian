from tp import * 

#--------------------------------Prenda-----------------------------------------------------------------

class Prenda:
    def __init__(self,un_codigo,un_nombre,un_precio,categoria):
        self.codigo = un_codigo
        self.nombre = un_nombre
        self.precio = un_precio
        self.estado = Nueva()
        self.stock = 0
        self.categoria = set()
        self.categoria.add(categoria)
        
        
    def hay_stock(self):
       return self.stock > 0

    def hay_stock_para_venta(self,cantidad_a_vender):
        if self.stock >= cantidad_a_vender:
            return True
        else:
            return False
        

    def codigo_valido(self,codigo):
       return codigo == self.codigo

    def ver_categorias(self):
        categorias = ",".join(self.categoria)
        return categorias
           
    def agregar_categoria(self,nueva_categoria):
       self.categoria.add(nueva_categoria)
    
    def cambiar_estado(self,nuevo_estado):
        self.estado = nuevo_estado

    def precio_final(self,precio):
        preci0_final = self.estado.precio_final(precio)
        return preci0_final

    def es_de_categoria(self, categoria):
        return categoria in self.categoria 
        

    def es_de_nombre(self, un_nombre): 
        return un_nombre == self.nombre 

    def actualizar_precio_segun_porcentaje(self, porcentaje):
        self.precio = self.precio + (self.precio * porcentaje)/100
        
class Nueva:
    def precio_final(self,precio):
        return precio
    
class Promocion:
    def __init__(self, valor_descuento):
        self.valor = valor_descuento
        
    def precio_final(self, precio):
      return precio - self.valor
    
class Liquidacion:
    def precio_final(self, precio):
        return precio / 2  
    
