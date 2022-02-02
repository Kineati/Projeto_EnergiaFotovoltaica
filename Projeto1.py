from array import *

def MediaDomiciliar_e_Fotovoltaica():
    EnergiaDomiciliarUsadaMes = []
    EnergiaDomiciliarPreçoMes = []
    aux5 = []
    ValorMedia_UsoDomiciliarMes = 0.0
    ValorMedia_PreçoDomiciliarMes = 0.0
    PreçoTotal_Ano = 0.0
    SomaTotal1 = 0.0
    TotalPessoas = 0
    MediaPorPessoa = 0.0

    TotalPessoas = int(input("Digite a Quantidade de Pessoas que Convivem na Mesma Casa:  "))
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
        EnergiaFotovoltaicaConsume = []
        EnergiaFotovoltaicaArmazena = []
        EnergiaDomiciliareFotovoltaicaDif = []
        Cont_Painel = {}
        Cont_Baterias = {}
        ValorMedia2 = 0.0
        ValorMedia3 = 0.0
        ValorMedia4 = 0.0
        SomaTotal2 = 0.0
        SomaTotal3 = 0.0
        SomaTotal4 = 0.0
        TotalPaineisSolar = 0
        TotalBaterias = 0

        TotalPaineisSolar = int(input("Digite a Quantidade de Paines Solares que Voce Possui:  "))
        print("  ")

        TotalBaterias = int(input("Digite a Quantidade de Baterias que Voce Possui:  "))
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
        print(Cont_Painel)
        print("  ")
        
        for i2 in range(1,TotalBaterias + 1):
            aux4 = 0
            for i in range(1,13):
                aux4 = float(input("Digite a Quantidade de energia Fotovoltaica (Killowatts) armazenada no mes %i (caso nao armazene,digite 0 em todos os meses), na bateria %i:   " %(i,i2)))
                print("  ")
                SomaTotal4 += aux4
                EnergiaFotovoltaicaArmazena.insert(i,aux4)
            Cont_Baterias["Armazem_Bateria%s" %i2] = EnergiaFotovoltaicaArmazena
            EnergiaFotovoltaicaArmazena.clear()
        print(Cont_Baterias)

        for i in range(1,13):
            aux3 = float(input("Digite a Quantidade de energia Fotovoltaica (Killowatts) usada no mes %i (caso nao use,digite 0 em todos os meses): " % i))
            print("  ")
            SomaTotal3 += aux3
            EnergiaFotovoltaicaConsume.insert(i,aux3)
        ValorMedia3 = SomaTotal3/len(EnergiaFotovoltaicaConsume)

        aux5.extend(EnergiaFotovoltaicaConsume)

    MediaFotovoltaica(ValorMedia_UsoDomiciliarMes,TotalPessoas,aux5)
    
    return aux5

if __name__ == '__main__':
    aux1 = []
    aux1 = MediaDomiciliar_e_Fotovoltaica()
    print(aux1)
