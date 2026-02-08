def dv_vortx(nosso_numero):
    """Calcula o DV do Nosso Número VORTX corretamente"""
    # Nosso número deve ter 11 dígitos
    if len(nosso_numero) != 11:
        raise ValueError("Nosso número deve ter 11 dígitos")

    pesos = [2,3,4,5,6,7,8,9]
    soma = 0
    # Aplica os pesos da direita para a esquerda
    for i in range(len(nosso_numero)-1, -1, -1):
        digito = int(nosso_numero[i])
        peso = pesos[(len(nosso_numero)-1 - i) % len(pesos)]
        soma += digito * peso

    resto = soma % 11
    dv = 11 - resto
    if dv == 10:
        dv = 1
    elif dv == 11:
        dv = 0
    return dv

def validar_numero():
    """Função para validar/calcular um número"""
    carteira = "21"

    while True:
        nn = input("📄 Digite o Nosso Número (11 dígitos sem DV ou 12 dígitos com DV): ").strip()
        if not nn.isdigit():
            print("❌ Nosso Número inválido! Apenas números são permitidos.")
            continue
        if len(nn) not in (11, 12):
            print("❌ Nosso Número inválido! Deve ter 11 dígitos (sem DV) ou 12 dígitos (com DV).")
            continue
        break

    if len(nn) == 12:
        numero_base = nn[:-1]
        dv_digitado = int(nn[-1])
        dv_calculado = dv_vortx(numero_base)
        dv_status = "correto" if dv_digitado == dv_calculado else f"incorreto (correto: {dv_calculado})"
        dv_final = dv_calculado
    else:  # 11 dígitos
        numero_base = nn
        dv_calculado = dv_vortx(numero_base)
        dv_digitado = dv_calculado
        dv_status = "calculado"
        dv_final = dv_calculado

    numero_completo = f"{carteira}{numero_base}{dv_final}"

    # Resultado final
    print("\n📄 RESULTADO FINAL")
    print("----------------------------")
    print(f"Carteira digitada: {carteira}")
    print(f"Nosso número digitado: {numero_base}")
    print(f"DV: {dv_digitado} ({dv_status})")
    print(f"Número completo com carteira + nosso número + DV: {numero_completo}")

def main():
    while True:
        validar_numero()
        print("\nEscolha uma opção:")
        print("1 - Voltar ao menu principal")
        print("2 - Validar/Calcular outro número")
        opcao = input("👉 Opção: ").strip()
        if opcao == "1":
            break
        elif opcao == "2":
            continue
        else:
            print("❌ Opção inválida, retornando ao menu principal.")
            break

if __name__ == "__main__":
    main()