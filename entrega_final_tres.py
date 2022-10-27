
from math import prod
import time
from collections import Counter

buzo_talle_s = {"codigo":100,"nombre":"buzo talle s","categoria":"buzo","precio": 3000,"stock":0}
jean_talle_38 = {"codigo":200,"nombre":"jean talle 38","categoria":"jean","precio":8000,"stock":0}

class Sucursal:
    
    def __init__(self):
        self.productos = []
        self.ventas = []
     
    def registrar_producto(self, nuevo_producto):
        self.productos.append(nuevo_producto)
        
    def recargar_stock(self,codigo_producto,cantidad_a_agregar):
        codigo_valido = False
        for producto in self.productos:
            if producto.codigo_valido(codigo_producto):
               codigo_valido = True
               producto.stock += cantidad_a_agregar
        if not codigo_valido:
            raise ValueError ("El codigo no corresponde a un producto registrado")
            
    """def ver_producto(self):
        for producto in range (len(self.productos)):
            return self.productos"""
     
    def hay_stock(self, codigo_producto):
        for producto in self.productos:
            if codigo_producto == producto.codigo:
                return producto.stock > 0
        return False
    
    
    def calcular_precio_final(self, producto, es_extranjero):
        precio_final = 0 
        for producto in self.productos:
            if es_extranjero and producto.precio > 70:
                precio_final = producto.precio
                return precio_final
            else:
                precio_final = producto.precio + 1.21
            return precio_final
        
    def contar_categorias(self):
        lista_total_categorias = set()
        for producto in self.productos:
            for categoria in producto.categoria:
                lista_total_categorias.add(categoria)
        return len(lista_total_categorias)

    def realizar_compra(self,codigo_producto,cantidad_a_comprar,es_extranjero):
        codigo_valido = False
        for producto in self.productos:
            if producto.codigo_valido(codigo_producto):
               codigo_valido = True
               if producto.hay_stock_para_venta(cantidad_a_comprar):
                  producto.stock -= cantidad_a_comprar
                  monto_total = self.calcular_precio_final(codigo_producto,es_extranjero)*cantidad_a_comprar
                  self.ventas.append({"producto":producto.nombre,"cantidad_vendida":cantidad_a_comprar,"monto":monto_total,"fecha":time.strftime("%d/%m"),"anio":time.strftime("%Y")})
               else:
                  raise ValueError ("No hay suficiente stock para realizar la venta")      
        if not codigo_valido:
           raise ValueError ("El codigo no corresponde a un producto registrado")       

    def descontinuar_productos(self):
        self.productos = {producto for producto in self.productos if producto.stock > 0}

    def valor_ventas_del_dia(self):
        venta_dia = 0
        if self.hay_ventas():
           for venta in self.ventas:
            if time.strftime("%d/%m") == venta["fecha"]:
               venta_dia += venta["monto"]
        else:
            raise ValueError ("No hay ventas registradas") 
        return venta_dia
    
    def ventas_del_anio(self):
        venta_anio = 0
        if self.hay_ventas(): 
           for venta in self.ventas:
               if time.strftime("%Y") == venta["anio"]:
                  venta_anio += venta["monto"]
        else:
            raise ValueError ("No hay ventas registradas")
        return venta_anio              

    def productos_mas_vendidos(self,cantidad_de_productos):
        productos_vendidos = []
        mas_vendidos = []
        for venta in self.ventas:
            productos_vendidos.append(venta["producto"])
        
        mas_vendidos = Counter(productos_vendidos)
        mas_vendidos = mas_vendidos.most_common(cantidad_de_productos)
        return mas_vendidos

    def actualizar_precios_por_categoria(self,categoria,porcentaje):
        for producto in self.productos:
            for categoria in producto.categoria:
                if categoria.lower() == categoria:
                   producto.precio += (producto.precio*porcentaje)/100

    def ganancia_diaria(self):
        if self.hay_ventas():
           return self.valor_ventas_del_dia() - self.gastos_del_dia()
        else:
            return self.gastos_del_dia()
    
    def hay_ventas(self):
        return len(self.ventas) > 0


    
    
