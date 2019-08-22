import os
os.system('cls') or None
w=int(1)
ans = 0
while (w==1):
    os.system('cls') or None
    print("")
    print(" escolha uma opção : ")
    print(" 1-multiplicação")
    print(" 2-soma")
    print(" 3-subtração")
    print(" 4-divisao")
    print(" 5-sair")
    print("")
    mano = float(input("opção: "))
    if mano==1:
        os.system('cls') or None
        print("multiplicação")
        print("")
        a=float(input("digite o primeiro numero da multiplicação: \n"))
        b=float(input("digite o segundo numero da multiplicação: \n"))
        ans=float(a*b)
        print("\n resultado : "+str(a*b))
        input("")
    elif mano==2:
        os.system('cls') or None
        print("soma")
        print("")
        a=float(input("digite o primeiro numero da soma: \n"))
        b=float(input("digite o segundo numero da soma: \n"))
        ans=float(a+b)
        print("\n resultado : "+str(a+b))
        input("")
    elif mano==3:
        os.system('cls') or None
        print("subtração")
        print("")
        a=float(input("digite o primeiro numero da subtração: \n"))
        b=float(input("digite o segundo numero da subtração: \n"))
        ans=float(a-b)
        print("\n resultado : "+str(a-b))
        input("")
    elif mano==4:
        os.system('cls') or None
        print("divisão")
        print("")
        a=float(input("digite o numero divisor: \n"))
        b=float(input("digite o numero dividendo: \n"))
        ans=float(b/a)
        print("\n resultado : "+str(b/a))
        input("")
    elif mano==5:
        os.system('cls') or None
        exit()  
    else:
       os.system('cls') or None
       print("essa opção nao existe insira uma das opções a baixo :")      