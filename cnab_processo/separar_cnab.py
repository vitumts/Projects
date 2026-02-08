# ==========================================================
# 📄 SCRIPT: separar_cnab.py
#
# 🎯 OBJETIVO:
#   Separar um CNAB em vários arquivos,
#   permitindo escolher quantos títulos
#   cada CNAB gerado terá.
#
# 📌 TRAILER (LAYOUT CONFIRMADO):
#   🔹 018–025 → quantidade de títulos (8)
#   🔹 026–039 → valor total em cobrança (14 / centavos)
#   🔹 Últimos 6 → total de linhas
#
# 📌 DETALHE:
#   🔹 153–165 → valor do título (13 / centavos)
#
# 📁 Pastas mantidas:
#   - cnab_origem
#   - cnab_saida
# ==========================================================

import os
import sys

# ==========================================================
# 💰 FORMATAÇÃO DE VALOR (APENAS PARA EXIBIÇÃO)
# ==========================================================

def formatar_brl(valor_centavos: int) -> str:
    valor = valor_centavos / 100
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

# ==========================================================
# ⚙️ CONFIGURAÇÕES FIXAS
# ==========================================================

PASTA_ORIGEM = "cnab_origem"
PASTA_SAIDA = "cnab_saida"

os.makedirs(PASTA_SAIDA, exist_ok=True)

# ==========================================================
# 📂 LOCALIZA O CNAB
# ==========================================================

arquivos = [
    f for f in os.listdir(PASTA_ORIGEM)
    if os.path.isfile(os.path.join(PASTA_ORIGEM, f))
]

if len(arquivos) == 0:
    print("❌ Nenhum arquivo encontrado em 'cnab_origem'")
    sys.exit(1)

if len(arquivos) > 1:
    print("❌ Mais de um arquivo encontrado em 'cnab_origem'")
    sys.exit(1)

arquivo_cnab = arquivos[0]
caminho_cnab = os.path.join(PASTA_ORIGEM, arquivo_cnab)

# ==========================================================
# 📄 LEITURA DO CNAB
# ==========================================================

with open(caminho_cnab, "r", encoding="utf-8") as f:
    linhas = f.readlines()

header = linhas[0]
trailer_original = linhas[-1]
detalhes = linhas[1:-1]

print("==========================================")
print("📄 CNAB carregado com sucesso")
print(f"📄 Arquivo : {arquivo_cnab}")
print(f"🔢 Títulos : {len(detalhes)}")
print("==========================================\n")

# ==========================================================
# 🎯 INPUT DO USUÁRIO
# ==========================================================

while True:
    try:
        titulos_por_cnab = int(
            input("👉 Quantos títulos por CNAB deseja gerar? ")
        )
        if titulos_por_cnab <= 0:
            raise ValueError
        break
    except ValueError:
        print("❌ Digite um número inteiro maior que zero.\n")

# ==========================================================
# 🔢 ACUMULADORES GERAIS
# ==========================================================

valor_total_geral = 0
total_titulos_geral = 0

# ==========================================================
# ✂️ PROCESSAMENTO
# ==========================================================

contador = 1

for i in range(0, len(detalhes), titulos_por_cnab):
    bloco_detalhes = detalhes[i:i + titulos_por_cnab]
    qtd_titulos = len(bloco_detalhes)

    # ======================================================
    # 🧮 CÁLCULO DO VALOR DO CNAB
    # ======================================================

    valor_cnab = 0

    for detalhe in bloco_detalhes:
        valor_str = detalhe[152:165]

        if not valor_str.strip().isdigit():
            print("❌ Valor inválido encontrado em um detalhe")
            sys.exit(1)

        valor_cnab += int(valor_str)

    valor_total_geral += valor_cnab
    total_titulos_geral += qtd_titulos

    # ======================================================
    # 🧮 RECÁLCULO DO TRAILER
    # ======================================================

    qtd_titulos_fmt = str(qtd_titulos).zfill(8)
    valor_cnab_fmt = str(valor_cnab).zfill(14)

    total_linhas = 1 + qtd_titulos + 1
    total_linhas_fmt = str(total_linhas).zfill(6)

    trailer = trailer_original.rstrip("\r\n")

    trailer = trailer[:17] + qtd_titulos_fmt + trailer[25:]
    trailer = trailer[:25] + valor_cnab_fmt + trailer[39:]
    trailer = trailer[:-6] + total_linhas_fmt

    trailer_novo = trailer + "\r\n"

    # ======================================================
    # 💾 GRAVAÇÃO
    # ======================================================

    nome_saida = f"{arquivo_cnab.replace('.txt','')}_{contador:03}.txt"
    caminho_saida = os.path.join(PASTA_SAIDA, nome_saida)

    with open(caminho_saida, "w", encoding="utf-8") as f:
        f.write(header)
        f.writelines(bloco_detalhes)
        f.write(trailer_novo)

    print(
        f"✅ Gerado: {nome_saida} | "
        f"🔢 Títulos: {qtd_titulos} | "
        f"💰 Valor CNAB: {formatar_brl(valor_cnab)} | "
        f"📏 Linhas: {total_linhas}"
    )

    contador += 1

# ==========================================================
# 🧾 RESUMO FINAL
# ==========================================================

print("\n==========================================")
print("📊 RESUMO GERAL")
print(f"🔢 Total de títulos              : {total_titulos_geral}")
print(f"💰 Valor total em cobrança       : {formatar_brl(valor_total_geral)}")
print("==========================================")

print("\n🎉 Processamento concluído com sucesso!")
print(f"📁 Arquivos gerados em: {PASTA_SAIDA}")
print("==========================================")