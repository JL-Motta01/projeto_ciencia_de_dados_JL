def soma(a,b):
    soma=a+b
    print(soma)
    print(soma,type(soma))   
#a=int(input ("digite um número para a soma : ")) 
#b=int(input ("digite outro numero para a soma: "))
#soma(a,b)

def subtração(a, b):
    subtração=a-b 
    print(subtração)
    print(subtração,type(subtração))
#a=int(input ("digite um número para a subtração: ")) 
#b=int(input ("digite outro numero para a subtração: "))
#subtração(a,b)

def dividir(a, b):
    dividir=a/b
    print(dividir)
    print(dividir,type(dividir))
#a=int(input ("digite um número para a divisão: ")) 
#b=int(input ("digite outro numero para a divisão: "))
#dividir(a,b)

def multiplicar(a, b):
    multiplicar=a*b
    print(multiplicar)
    print(multiplicar, type(multiplicar))
#a=int(input ("digite um número para a multiplicação: ")) 
#b=int(input ("digite outro numero para a multiplicação: "))
#multiplicar(a,b)

def main ():
    a=int(input ("digite um número: ")) 
    b=int(input ("digite outro numero: "))
    dividir(a,b)
    
if __name__ == "__main__":
    main()
