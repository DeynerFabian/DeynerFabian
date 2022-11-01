from posixpath import supports_unicode_filenames
from tp_3 import *
import pytest

# utilidades
sucursal_retiro = SucursalFisica()
remera_talle_s= Prenda(100,"remera talle s",1500,"remera")
def reiniciar_listas(sucursal):
    sucursal.productos.clear()
    sucursal.ventas.clear()


def test_registrar_un_producto():
    reiniciar_listas(sucursal_retiro)
    sucursal_retiro.registrar_producto(remera_talle_s)
    assert len(sucursal_retiro.productos) == 1
    
    
def test_recargar_stock():
    reiniciar_listas(sucursal_retiro)
    sucursal_retiro.registrar_producto(remera_talle_s)
    sucursal_retiro.recargar_stock(100, 500)
    assert sucursal_retiro.hay_stock(100)
    
     
def test_hay_stock():
    reiniciar_listas(sucursal_retiro)
    sucursal_retiro.registrar_producto(remera_talle_s)
    sucursal_retiro.recargar_stock(100, 500)
    assert sucursal_retiro.hay_stock(100) == True
    
