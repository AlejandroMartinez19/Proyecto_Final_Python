def funcion1():
    value = 1
    while value <= 3:
        print(value)
        value += 1
        cantidad = float(input(" Escriba el valor:"))
        
        if cantidad > 0 :
            print(" la cantidad es positiva")
        
        elif cantidad < 0:
            print(" la cantidad es negativa")
        
        else:
            print(" la cantidad es cero")
        
funcion1()
