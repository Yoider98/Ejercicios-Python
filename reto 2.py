def cliente(informacion):
  resp={}
  resp["nombre"] = informacion["nombre"]
  resp["edad"] = informacion["edad"]
  if informacion["edad"]>18:
    resp["atraccion"] = "X-treme"
    resp["apto"]=True
    if informacion["primer_ingreso"]==True:
          resp["primer_ingreso"]=True
          resp["total_boleta"]=20000-(20000*0.05)
    else:
          resp["primer_ingreso"]=False
          resp["total_boleta"]=20000
  elif informacion["edad"]>=15 and informacion["edad"]<=18:
       resp["atraccion"] = "Carros chocones"
       resp["apto"]=True
       if informacion["primer_ingreso"]==True:
            resp["primer_ingreso"]=True
            resp["total_boleta"]=5000-(5000*0.07)  
       else:
          resp["primer_ingreso"]=False
          resp["total_boleta"]=5000
  elif informacion["edad"]>=7 and informacion["edad"]<15:
      resp["atraccion"] = "Sillas voladoras"
      resp["apto"]=True
      if informacion["primer_ingreso"]==True:
            resp["primer_ingreso"]=True
            resp["total_boleta"]=10000-(10000*0.05)  
      else:
          resp["primer_ingreso"]=False
          resp["total_boleta"]=10000
  else:
    resp["atraccion"]= "N/A"
    resp["apto"]=False
    resp["total_boleta"]= "N/A"
  return resp