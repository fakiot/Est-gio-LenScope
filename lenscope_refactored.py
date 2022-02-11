def chamar_valores():
    esfericoD = float(input("Digite o grau esferico do olho direito: "))
    esfericoE = float(input("Digite o grau esferico do olho esquerdo: "))
    cilindricoD = float(input("Digite o grau cilindrico do olho direito: "))
    cilindricoE = float(input("Digite o grau cilindrico do olho esquerdo: "))
    return cilindricoD, cilindricoE, esfericoE, esfericoD

def validar_esferico(esfericoD, esfericoE, max_esferico, min_esferico):
    if max_esferico >= (esfericoD and esfericoE) >= min_esferico:
        return True

def validar_cilindrico(cilindricoD, cilindricoE, min_cilindrico):
    if (cilindricoD and cilindricoE) >= min_cilindrico:
        return True

def validar_iteracao(esfericoD, esfericoE, cilindricoD, cilindricoE, iteracao):
    if (esfericoD and esfericoE and cilindricoD and cilindricoE) % iteracao == 0:
        return True

max_esferico = 0
min_esferico = -15
min_cilindrico = -6
iteracao = 0.25
cilindricoD, cilindricoE, esfericoE, esfericoD = chamar_valores()
mensagem_escolha = "Olá usuário! Obrigada por comprar na LenScope.\nA lente que melhor atende sua necessidade é nossa lente"
mensagem_erro = f"Olá usuário, temos algum valor inválido! Para ser válido eles devem seguir as seguintes regras:\nEstar iterados de {iteracao} a {iteracao} \nEstar entre {max_esferico} a {min_esferico} para esferico\nIr ate {min_cilindrico} para cilindrico"

if (validar_esferico(esfericoD, esfericoE, max_esferico, min_esferico) and validar_cilindrico(cilindricoD, cilindricoE, min_cilindrico) and validar_iteracao(esfericoD, esfericoE, cilindricoD, cilindricoE, iteracao)) == True:  
     
    if (cilindricoD and cilindricoE) == 0 and -3 >= (esfericoD or esfericoE) >= -12:
        print(f"{mensagem_escolha} Prime.")
    elif (cilindricoD and cilindricoE) >= -2 and -3 >= (esfericoD or esfericoE) >= -10:
        print(f"{mensagem_escolha} Prime.")
    else:
        print(f"{mensagem_escolha} Vision.") 
else:
    print(mensagem_erro)
    chamar_valores()

if __name__ == "__main__":
    chamar_valores(), validar_esferico(esfericoD, esfericoE, max_esferico, min_esferico), validar_cilindrico(cilindricoD, cilindricoE, min_cilindrico), validar_iteracao(esfericoD, esfericoE, cilindricoD, cilindricoE, iteracao)
