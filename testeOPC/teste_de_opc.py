#PROGRAMA ULTILIZANDO OPÇÃO ... BY : UZUMAKI DEVELOP

print("""
\033[1;32m
by = uzumaki dev
date : 06/08/2021
hora : 22:45 AM(maranhão)
""")
print("-=-"*15)
print(" BEM VINDOS AO MEU TESTE DE OPÇÕS ")
print("-=-"*15)

from time import sleep
sleep(2)
print(">>>CARREGANDO MENU... ")
sleep(2)

#menu principal

opc = 0
while opc != 4 :
    print("""\033[1;32mMENU DE OPÇÕES
    [ 1 ] >TABUADA
    [ 2 ] >CAUCULADORA
    [ 3 ] >CAUCULAR MEDIAS
    [ 4 ] >SAIR DO PROGRAMA \033[m""")

    opc = int(input(">>> \033[1;31mDIGITE SUA OPÇÃO \033[m: "))
#tabuada

    if opc == 1 :
        p = 0
        while p != 5 :
            print("""
\033[1;32m>TABUADA<
( 1 ) .ADIÇAÕ
( 2 ) .SUBTRAÇÃO
( 3 ) .MULTIPLICAÇÃO
( 4 ) .DIVISÃO
( 5 ) .VOLTAR AO MENU PRINCIPAL\033[m""")
            p = int(input(">>> \033[31mDIGITE SUA OPÇÃO\033[m : "))
            if p == 1 :
                numb = int(input("\033[11;31mdigite o numero que deseja ver a tabuada \033[m: "))
                for n in range(1,11):
                    soma = numb + n
                    print("\033[1;34m{} + {} = {}\033[m".format(numb, n, soma))
            elif p == 2 :
                numb = int(input("\033[11;31mdigite o numero que deseja ver a tabuada\033[m : "))
                for n in range (1, 11):
                    subtração = numb - n
                    print("\033[1;34m{} - {} = {}\033[m".format(numb, n, subtração))
            elif p == 3 :
                numb = int(input("\033[11;31mdigite o numero que deseja ver a tabuada\033[m : "))
                for n in range (1, 11):
                    multiplicação = numb * n
                    print("\033[1;34m{} x {} = {}\033[m".format(numb, n, multiplicação))
            elif p == 4 :
                numb = int(input("\033[11;31mdigite o numero que deseja ver a tabuada \033[m: "))
                for n in range (1, 11):
                    divisão = numb / n
                    print("\033[1;34m{} / {} = {}\033[m".format(numb, n, divisão))
            elif p == 5 :
                print(" \033[11;33mFINALIZANDO\033[m...")
                sleep(2)
            else :
                print("\033[11;31mOPÇÃO INVALIDA TENTE NOVAMENTE\033[m...")
    #calculadora

    elif opc == 2 :
        n1 = int(input("\033[1;31mPrimeiro número\033[m : "))
        n2 = int(input("\033[1;31mSegundo número\033[m : "))
        p = 0
        while p != 6 :
            print("""
            \033[1;32m>Opção<
    > 1 < .SOMAR
    > 2 < .SUBTRAIR
    > 3 < .MULTIPLICAR 
    > 4 < .DIVIDIR 
    > 5 < .EDITAR NUMEROS
    > 6 < .VOLTAR PRO MENU PRINCIPAL\033[m""")
            p = int(input("\033[1;31m>>>DIGITE SUA OPÇÃO \033[m: "))
            if p == 1 :
                soma = n1 + n2
                print("\033[1;34mA soma entre {} e {} será igual á {}\033[m".format(n1, n2, soma ))
            elif p == 2 :
                sub = n1 - n2
                print("\033[1;34mA subtração entre o {} e {} será igual á {}\033[m".format(n1, n2, sub))
            elif p == 3 :
                mul = n1 * n2
                print("\033[1;34mMultiplicação entre o {} e o {} vai ser igual á {}\033[m".format(n1, n2, mul))
            elif p == 4 :
                div = n1 / n2
                print("\033[1;34mA divisão entre {} e {} será de {}\033[m".format(n1, n2, div))
            elif p == 5 :
                print("\033[1;33mINFORME NOVOS NÚMEROS\033[m...")
                n3 = int(input("\033[1;31mPrimeiro número\033[m : "))
                n4 = int(input("\033[1;31mSegundo número \033[m: "))
            elif p == 6 :
                print("\033[1;31mCARREGANDO\033[m...")
                sleep(2)
            else :
                print("\033[11;31mOPÇÃO INVALIDA TENTE NOVAMENTE\033[m...")

#cauculo de medias ...

    elif opc == 3  :
        p = 0
        while p != 2 :
            print("""\033[1;32m
   >> MEDIA << 
> 1 < .MEDIA 
> 2 < .VOLTAR AO MENU PRINCIPAL\033[m""")
            p = int(input(" >>>\033[1;31mDIGITE SUA OPÇÃO\033[m : "))
            if p == 1 :
                n1 = float(input("\033[1;31mDIGITE SUA PRIMEIRA NOTA\033[m : "))
                n2 = float(input("\033[1;31mDIGITE SUA SEGUNDA NOTA \033[m: "))
                n3 = float(input("\033[1;31mDIGITE SUA TERCEIRA NOTA \033[m: "))
                n4 = float(input("\033[1;31mDIGITE SUA QUARTA E ULTIMA NOTA\033[m : "))

                resul = (n1 + n2 + n3 + n4)/4
                print("\033[1;34mDe acordo com suas notas sua media foi de {} ".format(resul))
                if resul >= 7 :
                    print("Você está na media, parabens Aprovado")
                elif resul <= 5 :
                    print("Você está abaixo da media , Reprovado...boa sorte na proxima")
                else :
                    print("Você está de recuperação se esfor-se mais , boa sorte\033[m!")
            elif p == 2 :
                print("carregando menu...")
                sleep(2)
            else :
                print("OPÇÃO INVALIDA TENTE NOVAMENTE...")

#finalizar programa

    elif opc == 4 :
        print(" FINALIZANDO PROGRAMA...")
        sleep(1)
    else :
        print("OPÇÃO INVALIDA TENTE NOVAMENTE...")
sleep(2)
print("-=-"*15)
print(" FIM DO PROGRAMA VOLTE SEMPRE ")
print("-=-"*15)

print("""
\033[1;4;31mBY : UZUMAKI > PRIMEIRO PROGRAMA < """)

# P ausar o cod no cmd 
import os
os.system("pause")

#PROGRAMA FINALIZADO COM SUCESSO
