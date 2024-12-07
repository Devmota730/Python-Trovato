def valida_cpf(cpf):
    # Remove caracteres não numéricos
    cpf = ''.join(filter(str.isdigit, cpf))
    print(f"CPF após remoção de caracteres não numéricos: {cpf}")

    # Verifica se o CPF tem 11 dígitos
    if len(cpf) != 11:
        print("CPF não tem 11 dígitos.")
        return False

    # Verifica se todos os dígitos são iguais (ex: 111.111.111-11)
    if cpf == cpf[0] * len(cpf):
        print("CPF tem todos os dígitos iguais.")
        return False

    # Função para calcular o dígito verificador
    def calcula_digito(cpf, peso):
        soma = 0
        for i in range(peso):
            soma += int(cpf[i]) * (peso + 1 - i)
        resto = soma % 11
        return 0 if resto < 2 else 11 - resto

    # Calcula o primeiro dígito verificador
    digito1 = calcula_digito(cpf, 9)
    print(f"Primeiro dígito verificador calculado: {digito1}")

    # Calcula o segundo dígito verificador
    digito2 = calcula_digito(cpf, 10)
    print(f"Segundo dígito verificador calculado: {digito2}")

    # Verifica se os dígitos calculados são iguais aos dígitos informados
    resultado = cpf[-2:] == f"{digito1}{digito2}"
    print(f"Dígitos verificadores informados: {cpf[-2:]}")
    print(f"Resultado da validação: {'válido' if resultado else 'inválido'}")
    return resultado

# Solicita o CPF do usuário
cpf = input("Informe o CPF (apenas números): ")

# Valida o CPF informado
if valida_cpf(cpf):
    print("CPF válido")
else:
    print("CPF inválido") 
