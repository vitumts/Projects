def calcular_dac(numero):
    """Calcula a DAC/DV do BMP"""
    mult = 2
    soma = 0
    for d in reversed(numero):
        soma += int(d) * mult
        mult = 2 if mult == 7 else mult + 1
    resto = soma % 11
    dac = 11 - resto
    if dac > 9:
        return "P"
    return dac

def validar_numero():
    """Função para validar/calcular um número"""
    # Carteira
    while True:
        carteira = input("📄 Digite a carteira (2 dígitos): ").strip()
        if not carteira.isdigit() or len(carteira) != 2:
            print("❌ Carteira inválida! Deve ter exatamente 2 dígitos.")
            continue
        break

    # Nosso número
    while True:
        nn = input("📄 Digite o Nosso Número (11 dígitos sem DV ou 12 dígitos com DV): ").strip()
        if not nn.isdigit():
            print("❌ Nosso Número inválido! Apenas números são permitidos.")
            continue
        if len(nn) not in (11, 12):
            print("❌ Nosso Número inválido! Deve ter 11 dígitos (sem DV) ou 12 dígitos (com DV).")
            continue
        break

    # Validação ou cálculo do DV
    if len(nn) == 12:
        numero_base = nn[:-1]
        dv_digitado = nn[-1]
        dv_calculado = calcular_dac(carteira + numero_base)
        dv_status = "correto" if str(dv_calculado) == dv_digitado else f"incorreto (correto: {dv_calculado})"
        dv_final = dv_calculado
    else:  # 11 dígitos
        numero_base = nn
        dv_calculado = calcular_dac(carteira + numero_base)
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