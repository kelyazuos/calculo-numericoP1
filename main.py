import os

while True:

    print("=" * 50)
    print("        CÁLCULO NUMÉRICO P1")
    print("=" * 50)

    print("1 - Interpolação de Lagrange")
    print("2 - Gregory-Newton")
    print("3 - Spline Linear")
    print("4 - Spline Cúbica Natural")
    print("5 - Método dos Mínimos Quadrados")
    print("6 - Regra dos Trapézios")
    print("7 - Regra 1/3 de Simpson")
    print("8 - Regra 3/8 de Simpson")
    print("9 - Quadratura de Gauss")
    print("0 - Sair")

    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        os.system("python interpolacao/lagrange.py")

    elif opcao == "2":
        os.system("python interpolacao/gregory_newton.py")

    elif opcao == "3":
        os.system("python interpolacao/spline_linear.py")

    elif opcao == "4":
        os.system("python interpolacao/spline_cubica.py")

    elif opcao == "5":
        os.system("python mmq/mmq.py")

    elif opcao == "6":
        os.system("python integracao/trapezios.py")

    elif opcao == "7":
        os.system("python integracao/simpson.py")

    elif opcao == "8":
        os.system("python integracao/newton_cotes.py")

    elif opcao == "9":
        os.system("python integracao/quadratura_gauss.py")

    elif opcao == "0":
        print("\nEncerrando programa...")
        break

    else:
        print("\nOpção inválida!")

    input("\nPressione Enter para continuar...")