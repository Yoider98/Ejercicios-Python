from typing import List


def AutoPartes(ventas: List):
    Venta={}
    for IdProducto, dProducto, pnProducto, cvProducto, sProducto, nComprador, cComprador, fVenta in ventas:
        if Venta.get(IdProducto) == None:
            Venta[IdProducto] =[]
        Venta[IdProducto].append((dProducto, pnProducto, cvProducto, sProducto, nComprador, cComprador, fVenta))
               
    return Venta

def consultaRegistros(ventas, idProducto):
    if idProducto in ventas:
        for  dProducto, pnProducto, cvProducto, sProducto, nComprador, cComprador, fVenta in ventas[idProducto]:
            print ("  Producto consultado :", idProducto, "Descripción", dProducto, "#Parte", pnProducto, "Cantidad vendida", cvProducto, "Stock",  sProducto, "Comprador", nComprador, "Documento", cComprador, "Fecha Venta", fVenta)
    else:
        print("No hay registro de venta de ese producto")
        
        
consultaRegistros(AutoPartes([(2001,'rosca', 'PT29872',2,45,'Luis Molero',3456,'12/06/2020'),
 (2010,'bujía', 'MS9512',4,15,'Carlos Rondon',1256,'12/06/2020'),
 (2010,'bujía', 'ER6523',9,36,'Pedro Montes',1243,'12/06/2020'),
 (3578,'tijera', 'QW8523',1,128,'Pedro Faria',1456,'12/06/2020'),
 (9251,'piñón', 'EN5698',2,8,'Juan Peña',565,'12/06/2020')]),2010)