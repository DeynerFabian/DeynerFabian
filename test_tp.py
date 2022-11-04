from posixpath import supports_unicode_filenames
from tp import *
import pytest

# utilidades
sucursal_retiro = SucursalFisica()
remera_talle_s = Prenda(100,"remera talle s",1500,"remera")
jean_talle_40 = Prenda(200, "jean_talle_40", 3000, "jean")
gorra_blanca = Prenda(300, "gorra_blanca", 4500, "gorra")

def reiniciar_listas(sucursal):
    sucursal.productos.clear()
    sucursal.ventas.clear()

def reiniciar_stock(prenda):
    prenda.stock = 0


def test_registrar_un_producto():
    reiniciar_listas(sucursal_retiro)
    sucursal_retiro.registrar_producto(remera_talle_s)
    assert len(sucursal_retiro.productos) == 1
    
    
def test_recargar_stock():
    reiniciar_listas(sucursal_retiro)
    sucursal_retiro.registrar_producto(remera_talle_s)
    sucursal_retiro.recargar_stock(100, 500)
    assert sucursal_retiro.hay_stock(100)

def test_recargar_10_de_stock_a_remera_talle_s():
    reiniciar_listas(sucursal_retiro)
    reiniciar_stock(remera_talle_s)
    sucursal_retiro.registrar_producto(remera_talle_s)
    sucursal_retiro.recargar_stock(100, 10)
    assert remera_talle_s.stock == 10

     
def test_hay_stock():
    reiniciar_listas(sucursal_retiro)
    sucursal_retiro.registrar_producto(remera_talle_s)
    sucursal_retiro.recargar_stock(100, 500)
    assert sucursal_retiro.hay_stock(100) == True
    
def test_calcular_precio_final_extranjero():
    reiniciar_listas(sucursal_retiro)
    sucursal_retiro.registrar_producto(remera_talle_s)
    sucursal_retiro.registrar_producto(jean_talle_40)
    sucursal_retiro.recargar_stock(100, 500)
    sucursal_retiro.recargar_stock(200, 500)
    assert sucursal_retiro.calcular_precio_final(remera_talle_s, True) == 1500

def test_realizar_compra():
    reiniciar_listas(sucursal_retiro)
    sucursal_retiro.registrar_producto(remera_talle_s)
    sucursal_retiro.registrar_producto(jean_talle_40)
    sucursal_retiro.recargar_stock(100, 500)
    sucursal_retiro.recargar_stock(200, 500)
    sucursal_retiro.realizar_compra(100,1, True)
    assert len(sucursal_retiro.ventas) == 1


def test_calcular_precio_final_extranjero():
    reiniciar_listas(sucursal_retiro)
    sucursal_retiro.registrar_producto(remera_talle_s)
    sucursal_retiro.registrar_producto(jean_talle_40)
    sucursal_retiro.recargar_stock(100, 500)
    sucursal_retiro.recargar_stock(200, 500)
    assert sucursal_retiro.calcular_precio_final(remera_talle_s, True) == 1500

def test_calcular_precio_final_local():
    reiniciar_listas(sucursal_retiro)
    sucursal_retiro.registrar_producto(remera_talle_s)
    sucursal_retiro.registrar_producto(jean_talle_40)
    sucursal_retiro.recargar_stock(100, 500)
    sucursal_retiro.recargar_stock(200, 500)
    assert sucursal_retiro.calcular_precio_final(jean_talle_40, False) == 3630

def test_contar_por_categorias_varias():
    reiniciar_listas(sucursal_retiro)
    sucursal_retiro.registrar_producto(remera_talle_s)
    sucursal_retiro.registrar_producto(jean_talle_40)
    sucursal_retiro.recargar_stock(100, 500)
    sucursal_retiro.recargar_stock(200, 500)
    assert sucursal_retiro.contar_categorias() == 2

def test_contar_por_categoria():
    reiniciar_listas(sucursal_retiro)
    sucursal_retiro.registrar_producto(remera_talle_s)
    sucursal_retiro.registrar_producto(jean_talle_40)
    sucursal_retiro.recargar_stock(100, 500)
    assert sucursal_retiro.contar_categorias() == 2

def test_se_puede_dar_al_producto_una_categoria_inicial():
    reiniciar_listas(sucursal_retiro)
    sucursal_retiro.registrar_producto(remera_talle_s)
    sucursal_retiro.recargar_stock(100, 500)
    assert remera_talle_s.categoria == {"remera"}
"""
def test_se_puede_buscar_remera_por_categoria():
    reiniciar_listas(sucursal_retiro)
    
    sucursal_retiro.registrar_producto(remera_talle_s)
    sucursal_retiro.registrar_producto(jean_talle_40)
    
    assert sucursal_retiro.lista_de_producto_segun(PorCategoria("remera")) == [
        "remera_talle_s"
    ]
"""
def test_se_puede_buscar_remera_por_precio():
    reiniciar_listas(sucursal_retiro)
    
    sucursal_retiro.registrar_producto(remera_talle_s)
    sucursal_retiro.registrar_producto(jean_talle_40)
    
    assert sucursal_retiro.lista_de_producto_segun(PorPrecio(2000)) == [
        remera_talle_s
    ]   
    
def test_descontinuar_jean_talle_40_sin_stock():
    reiniciar_listas(sucursal_retiro)
    sucursal_retiro.descontinuar_productos()
    assert len(sucursal_retiro.productos) == 0

def test_ventas_del_dia_con_productos_y_15_und_del_mismo():
    reiniciar_listas(sucursal_retiro)
    sucursal_retiro.registrar_producto(remera_talle_s)
    sucursal_retiro.registrar_producto(jean_talle_40)
    sucursal_retiro.recargar_stock(100, 500)
    sucursal_retiro.recargar_stock(200, 500)
    sucursal_retiro.realizar_compra(100, 35, True) == 52500

















#TODO testear todas las busquedas
#TODO testear el actualizar_segun
#TODO corregir los tests rotos de categoria (al terminar todo tiene que estar en verde)
#TODO hacer el criterio por oposicion
#TODO hacer el discontinuar productos 
#TODO hacer la tarea programada de discontinuar productos

# PROBANDO MI GIT