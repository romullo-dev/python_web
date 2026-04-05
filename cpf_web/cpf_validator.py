def limpar_cpf (cpf):
    return cpf.replace(".", "").replace("-", "").strip()

def cpf_valido(cpf):
    cpf = limpar_cpf(cpf)

    if len(cpf) != 11 or not cpf.isdigit():
        return False
    
    if cpf == cpf[0] * 11:
        return False
    
    soma = 0

    for i in range(9):
        soma += int(cpf[i]) * (10 - i)

    resto = soma % 11
    if resto < 2:
        digito1 = 0
    else:
        digito1 = 11 - resto

    soma = 0 
    for i in range(10):
        soma += int(cpf[i]) *  (11 - i)

    resto = soma % 11
    if resto < 2:
        digito2 = 0
    else:
        digito2 = 11 - resto

    if int(cpf[9]) == digito1 and int(cpf[10]) == digito2:
        return True

    return False
