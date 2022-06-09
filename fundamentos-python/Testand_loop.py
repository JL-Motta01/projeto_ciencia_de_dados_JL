# This Python file uses the following encoding: utf-8
from random import *

def selecaoo_sorteio ():
    quant=int(input ("Informe a quantidade de nùmeros a serem sorteados: "))
    return quant

def loop (qtd):
    quant = qtd
    sorteio=[]
    for n in range(quant):
        num= randrange(1,20)
        sorteio.append(num)
    for n in sorteio:
        print(n)

def main():
   loop(selecaoo_sorteio())


if __name__ == "__main__":
    main()
