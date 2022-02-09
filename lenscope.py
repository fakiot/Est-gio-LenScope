def chamar_valores():
    esfericoD = float(input("Digite o grau esferico do olho direito: "))
    esfericoE = float(input("Digite o grau esferico do olho esquerdo: "))
    cilindricoD = float(input("Digite o grau cilindrico do olho direito: "))
    cilindricoE = float(input("Digite o grau cilindrico do olho esquerdo: "))
    return cilindricoD, cilindricoE, esfericoE, esfericoD

cilindricoD, cilindricoE, esfericoE, esfericoD = chamar_valores()

if 0 >= esfericoD >= -15 and 0 >= esfericoE >= -15 and cilindricoD >= -6 and cilindricoE >= -6:
    if (esfericoD and esfericoE and cilindricoD and cilindricoE) % 0.25 == 0:
        if (cilindricoD and cilindricoE) == 0 and -3 >= (esfericoD or esfericoE) >= -12:
            print("Olá usuário! Obrigada por comprar na LenScope. \nA lente que melhor atende sua necessidade é nossa lente Prime.")
        elif (cilindricoD and cilindricoE) >= -2 and -3 >= (esfericoD or esfericoE) >= -10:
            print("Olá usuário! Obrigada por comprar na LenScope. \nA lente que melhor atende sua necessidade é nossa lente Prime.")
        else:
            print("Olá usuário! Obrigada por comprar na LenScope. \nA lente que melhor atende sua necessidade é nossa lente Vision.") 
else:
    print("Olá usuário, temos algum valor inválido! Para ser válido eles devem seguir as seguintes regras:\nEstar iterados de 0,25 a 0,25 \nEstar entre 0 a -15 para esferico \nIr ate -6 para cilindrico")
    chamar_valores()
