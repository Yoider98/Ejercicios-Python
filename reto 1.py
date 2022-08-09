def CDT(usuario:str,capital:int,tiempo:int):
    Valor_int=(capital*0.03*tiempo)/12
    
    if tiempo <=2:
        ValorPerdida = capital*0.02
        ValorTotal=capital-ValorPerdida	
    else:
        ValorTotal=Valor_int+capital
    return f"Para el usuario{usuario} La cantidad de dinero a recibir, según el monto inicial{capital}para un tiempo de{tiempo} meses es:{ValorTotal}"
    