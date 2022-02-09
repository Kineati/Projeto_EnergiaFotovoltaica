from array import *

def MediaDomiciliar_e_Fotovoltaica():
    EnergiaDomiciliarUsadaMes = []
    EnergiaDomiciliarPreçoMes = []
    aux5 = []
    UnidadeFederativa = ''
    Cidade = ''
    País = ''
    ValorMedia_UsoDomiciliarMes = 0.0
    ValorMedia_PreçoDomiciliarMes = 0.0
    PreçoTotal_Ano = 0.0
    SomaTotal1 = 0.0
    TotalPessoas = 0
    MediaPorPessoa = 0.0

    TotalPessoas = int(input("Digite a Quantidade de Pessoas que Convivem na Mesma Casa:  "))
    print("  ")

    País = input("Digite o Pais que Voce reside:  ")
    print("  ")

    UnidadeFederativa = input("Digite a UF(Unidade Federativa) que voce reside:  ")
    print("  ")

    Cidade = input("Digite a Cidade que voce reside:  ")
    print("  ")

    for i in range(1,13):
        aux1 = float(input("Digite a Quantidade de Energia Domiciliar (Killowatts) que voce usa no mes %i:  " % i))
        print("  ")
        SomaTotal1 += aux1
        EnergiaDomiciliarUsadaMes.insert(i,aux1)
        EnergiaDomiciliarPreçoMes.insert(i,(aux1*0.6))

    ValorMedia_UsoDomiciliarMes = SomaTotal1/len(EnergiaDomiciliarUsadaMes)
    ValorMedia_PreçoDomiciliarMes = ValorMedia_UsoDomiciliarMes*0.6
    MediaPorPessoa = SomaTotal1/TotalPessoas
    aux5.extend(EnergiaDomiciliarUsadaMes)
    aux5.insert(14,0)
    PreçoTotal_Ano = SomaTotal1*0.6
    
    print("Preço em Reais do mes 0 a 12:  ")
    print(EnergiaDomiciliarPreçoMes)
    print("  ")

    print("Preço total no ano:  %f" % PreçoTotal_Ano, "R$")
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
            aux6 = float(input("Digite a Carga Maxima que a Bateria %i possui:  " %i2))
            Carga_Maxima_Bat["Max_Bateria%s" %i2] = aux6
            Max_Bat["Carga_Max_Baterias"] = Carga_Maxima_Bat
            for i in range(1,13):
                aux4 = float(input("Digite a Quantidade de energia Fotovoltaica (Killowatts) armazenada no mes %i (caso nao armazene,digite 0 em todos os meses), na bateria %i:   " %(i,i2)))
                print("  ")
                SomaTotal4 += aux4
                EnergiaFotovoltaicaArmazena["Bateria%s_Mes%s" %(i2,i)] = aux4
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
