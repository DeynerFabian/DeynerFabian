from tp import *
       # ----------------------------------Sucursales ---------------------------------------

class SucursalFisica(Sucursal):
    def __init__(self):
        self.productos = set()
        self.ventas = []
        self.registros = [] 
        self.gasto_por_dia = 15000
    
    def gastos_del_dia(self):
        return self.gasto_por_dia
    def cuentas_diarias(self):
        self.registros.append([date.strftime(date.today(),"%Y-%m-%d"), self.cantidad_de_ventas_diarias() ,self.valor_ventas_del_dia()])
        with open("reporte_fis.csv", "w", newline="")as file:
            writer = csv.writer(file,delimiter=",")
            writer.writerows(self.registros)
            
class SucursalVirtual(Sucursal):
    def __init__(self):
        self.productos = set()
        self.gasto_por_dia = 1000
        self.gasto_variable = 1
        self.ventas = []
        self.registros = []
        
    def cuentas_diarias(self):
        self.registros.append([date.strftime(date.today(),"%Y-%m-%d"), self.cantidad_de_ventas_diarias() ,self.valor_ventas_del_dia()])
        with open("reporte_vir.csv", "w", newline="")as file:
            writer = csv.writer(file,delimiter=",")
            writer.writerows(self.registros)
            
    def gastos_del_dia(self):
        if len(self.ventas) > 100:
            return len(self.ventas)*self.gasto_variable
        else:
            return self.gasto_por_dia

    def modificar_gasto_variable(self,nuevo_valor):
        self.gasto_variable = nuevo_valor

    def calcular_precio_final_mas_envio(self, producto):
        precio_final_mas_envio = 0
        if producto.precio > 3000:
            precio_final_mas_envio = producto.precio
            return precio_final_mas_envio
        else:
            precio_final_mas_envio = producto.precio + (10*producto.precio)/100
            return precio_final_mas_envio

