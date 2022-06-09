# This Python file uses the following encoding: utf-8
from random import *

def selecaoo_sorteio ():
    quant=int(input ("Informe a quantidade de nùmeros a serem sorteados: "))
    return quant

def loop_sorteio (qtd):
    quant = qtd
    sorteio=[]
    for n in range(quant):
        num= randrange(1,20)
        sorteio.append(num)
    for n in sorteio:
        print(n)
        checagem(n)

def checagem (numero):
    if numero > 10:
        print("O numero é maior do que 10")
    elif numero == 20:
        print("O numero é a maior opção a ser sorteada")
    else:
        print("O numero é menor do que 10")
 

def main():
   loop_sorteio(selecaoo_sorteio)


if __name__ == "__main__":
    main()
