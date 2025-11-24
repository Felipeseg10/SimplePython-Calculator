def pedir_operacion():
    while True:
        operacion = input("Elige una operación (+, -, *, /): ")
        if operacion in ['+', '-', '*', '/']:
            return operacion
        else:
            print('Operación no Valida')
            continue


def pedir_numero(mensaje):
    while True:
        try:
            numero=float(input(mensaje))
            return numero
        except ValueError:
            print('Escribe un Valor valido')


def Calculadora():
    while True:
        num1=pedir_numero('Escoge el primero Numero: ')
        operacion=pedir_operacion()
        num2=pedir_numero('Escoge el segundo Numero: ')

        try:
            if operacion == '+':
                resultado=num1+num2

            elif operacion == '-':
                resultado=num1-num2

            elif operacion == '*':
                resultado=num1*num2

            elif operacion == '/':
                resultado=num1/num2

            print('El resultado es ', resultado)
            break
        except ZeroDivisionError:
            print('Error: no se puede dividir entre 0')
            continue


Calculadora()


        
    
           
    

    
        