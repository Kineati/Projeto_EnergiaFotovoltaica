from array import *
from tkinter import *
from math import radians
import numpy as np
import matplotlib.pyplot as plt

def main():
  x = [1, 2, 3]
  y = [2, 4, 1]
  plt.plot(x,y)
  plt.show()

main()

def MediaDomiciliar_e_Fotovoltaica():
    EnergiaDomiciliarUsadaMes = []
    EnergiaDomiciliarPreçoMes = []
    aux5 = []
    EnergiaDomiciliarUsadaTotal = {}
    EnergiaDomiciliarAno_Mes = {}
    EnergiaDomiciliarUsadaTotalPreco = {}
    EnergiaDomiciliarAno_MesPreco = {}
    UnidadeFederativa = ''
    Cidade = ''
    País = ''
    ValorMedia_UsoDomiciliarMes = 0.0
    ValorMedia_PreçoDomiciliarMes = 0.0
    PreçoTotal_Ano = 0.0
    SomaTotal1 = 0.0
    SomaTotal5 = 0.0
    TotalPessoas = 0
    TotalAnos = 0
    MediaPorPessoa = 0.0
    MediaPorAnos = 0.0

    TotalPessoas = int(input("Digite a Quantidade de Pessoas que Convivem na Mesma Casa:  "))
    print("  ")

    País = input("Digite o Pais que Voce reside:  ")
    print("  ")

    UnidadeFederativa = input("Digite a UF(Unidade Federativa) que voce reside:  ")
    print("  ")

    Cidade = input("Digite a Cidade que voce reside:  ")
    print("  ")


    TotalAnos = int(input("Digite a Quantidade de Anos para Calcular a Media de Energia (Killowatts) Domiciliar Usada:  "))
    print("  ")

    for i4 in range(1,TotalAnos + 1):
        aux6 = 0
        SomaTotal1 = 0
        x = [1,2,3,4,5,6,7,8,9,10,11,12]
        for i in range(1,13):
            aux6 = float(input("Digite a Quantidade de Energia Domiciliar (Killowatts) que voce usou no ano %i no mes %i:  " % (i4,i)))
            print("  ")
            SomaTotal1 += aux6
            SomaTotal5 += aux6
            EnergiaDomiciliarAno_Mes["Ano%s_Mes%s" %(i4,i)] = aux6
        EnergiaDomiciliarUsadaTotal["EnergiaDomiciliarTotal"] = EnergiaDomiciliarAno_Mes
        EnergiaDomiciliarAno_MesPreco["Ano%s" % i4] = SomaTotal1*0.6
        EnergiaDomiciliarUsadaTotalPreco["EnergiaDomiciliarTotalUsada"] = EnergiaDomiciliarAno_MesPreco
        y = [EnergiaDomiciliarAno_Mes['Ano1_Mes1'],EnergiaDomiciliarAno_Mes['Ano1_Mes2'],EnergiaDomiciliarAno_Mes['Ano1_Mes3'],EnergiaDomiciliarAno_Mes['Ano1_Mes4'],EnergiaDomiciliarAno_Mes['Ano1_Mes5'],EnergiaDomiciliarAno_Mes['Ano1_Mes6'],EnergiaDomiciliarAno_Mes['Ano1_Mes7'],EnergiaDomiciliarAno_Mes['Ano1_Mes8'],EnergiaDomiciliarAno_Mes['Ano1_Mes9'],EnergiaDomiciliarAno_Mes['Ano1_Mes10'],EnergiaDomiciliarAno_Mes['Ano1_Mes11'],EnergiaDomiciliarAno_Mes['Ano1_Mes12']]
        plt.plot(x,y,color='green', linestyle='dashed', linewidth = 3,
         marker='o', markerfacecolor='blue', markersize=12)
        plt.show()

    MediaPorAnos = SomaTotal5*0.6

    print(EnergiaDomiciliarUsadaTotal)
    print("  ")

    print(EnergiaDomiciliarUsadaTotalPreco)
    print("  ")

    print(MediaPorAnos,"R$")
    print("  ")

    MediaPorPessoa = MediaPorAnos/TotalPessoas

    print(MediaPorPessoa)
    print("  ")

    def MediaFotovoltaica(ValorMedia_UsoDomiciliarMes,TotalPessoas,aux5):
        EnergiaFotovoltaicaProduz = {}
        EnergiaFotovoltaicaConsume = {}
        EnergiaFotovoltaicaArmazena = {}
        Tamanho_Paineis = {}
        Cont_Painel = {}
        Cont_Painel2 = {}
        Cont_Baterias = {}
        Cont_Anos = {}
        Carga_Maxima_Bat = {}
        Max_Bat = {}
        ValorMedia2 = 0.0
        ValorMedia3 = 0.0
        ValorMedia4 = 0.0
        SomaTotal2 = 0.0
        SomaTotal3 = 0.0
        SomaTotal4 = 0.0
        SomaTotal6 = 0.0
        Largura = 0.0
        Comprimento = 0.0
        Area = 0.0
        TotalPaineisSolar = 0
        TotalBaterias = 0
        TotalAnos = 0
        Inversor = 0
        CC_CA = ''

        TotalPaineisSolar = int(input("Digite a Quantidade de Paines Solares que Voce Possui:  "))
        print("  ")

        TotalBaterias = int(input("Digite a Quantidade de Baterias que Voce Possui:  "))
        print("  ")

        TotalAnos = int(input("Digite a Quantidade de Anos Consumindo a Energia Fotovoltaica:  "))
        print("  ")

        Inversor = int(input("Digite 1 se voce possui um Inversor, ou 0 se voce não possui:  "))

        if(Inversor == 1):
            print("Voce póde transformar a Corrente Continua em Corrente Alternada !!!")
            print("  ")
            CC_CA = "Corrente Alternada"
        else:
            print("Voce póde apenas utilizar Corrente Continua !!!")
            print("  ")
            CC_CA = "Corrente Continua"

        for i4 in range(1,TotalPaineisSolar + 1):
            Largura = float(input("Digite a Largura do Painel Solar %i:  " % i4))
            Comprimento = float(input("Digite o Comprimento do Painel Solar %i:  " % i4))
            Area = Largura*Comprimento
            Tamanho_Paineis["Tamanho_Painel%s" % i4] = Area
            Cont_Painel2["Area_Dos_Paineis_MetroQuadrado"] = Tamanho_Paineis

        print(Cont_Painel2)
        print("  ")



        for i1 in range(1,TotalPaineisSolar + 1):
            aux2 = 0
            for i in range(1,13):
                aux2 = float(input("Digite a Quantidade de Energia Fotovoltaica (Killowatts) que voce produz no mes %i (caso nao produza,digite 0 em todos os meses), na placa solar %i:  " %(i,i1)))
                print("  ")
                SomaTotal2 += aux2
                EnergiaFotovoltaicaProduz["Painel%s_Mes%s" %(i1,i)] = aux2
            Cont_Painel["Producao_Paineis"] = EnergiaFotovoltaicaProduz
        
        ValorMedia2 = SomaTotal2/(TotalPaineisSolar*12)

        print("Media entre os paineis solares:  %f" % ValorMedia2)
        print("  ")

        print(Cont_Painel["Producao_Paineis"]["Painel1_Mes12"])
        print("  ")
        
        for i2 in range(1,TotalBaterias + 1):
            aux4 = 0
            SomaTotal6 = 0
            aux6 = float(input("Digite a Carga Maxima que a Bateria %i possui:  " %i2))
            Carga_Maxima_Bat["Max_Bateria%s" %i2] = aux6
            Max_Bat["Carga_Max_Baterias"] = Carga_Maxima_Bat
            for i in range(1,13):
                aux4 = float(input("Digite a Quantidade de energia Fotovoltaica (Killowatts) armazenada no mes %i (caso nao armazene,digite 0 em todos os meses), na bateria %i:   " %(i,i2)))
                print("  ")
                SomaTotal4 += aux4
                SomaTotal6 += aux4
                EnergiaFotovoltaicaArmazena["Bateria%s_Mes%s" %(i2,i)] = aux4
            if(SomaTotal6 >= aux6):
                print("Quantidade Maxima de Carga Excedida, da Bateria %i !!!" % i2)
                print("  ")
                TotalBaterias = i2

            Cont_Baterias["Armazem_Bateria"] = EnergiaFotovoltaicaArmazena
            ValorMedia4 = SomaTotal4/(TotalBaterias*12)
        
        print("Media entre as baterias:  %f" % ValorMedia4)
        print("  ")

        print(Cont_Baterias)
        print("  ")

        print(Carga_Maxima_Bat)
        print("  ")


        for i3 in range(1,TotalAnos+1):
            for i in range(1,13):
                aux3 = float(input("Digite a Quantidade de energia Fotovoltaica (Killowatts) usada no mes %i (caso nao use,digite 0 em todos os meses) no ano %i: " % (i,i3)))
                print("  ")
                SomaTotal3 += aux3
                EnergiaFotovoltaicaConsume["Ano%s_Mes%s" % (i3,i)] = aux3
            Cont_Anos["Consumo_EnergiaFotovoltaica%s" %i3] = EnergiaFotovoltaicaConsume
            ValorMedia3 = SomaTotal3/(TotalAnos*12)

        print("Media entre os anos  %f" % ValorMedia3)
        print("  ")

        print(Cont_Anos)
        print("  ")

    MediaFotovoltaica(ValorMedia_UsoDomiciliarMes,TotalPessoas,aux5)
    
    return aux5

if __name__ == '__main__':
    aux1 = []
    aux1 = MediaDomiciliar_e_Fotovoltaica()
    print(aux1)
