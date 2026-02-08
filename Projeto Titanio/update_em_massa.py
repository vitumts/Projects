import csv

# ==============================
# CONFIGURAÇÕES
# ==============================

arquivo_csv = "dados.csv"
arquivo_saida = "update_em_massa.sql"

nome_tabela = "SIGFLU"
coluna_sql_documento = "DCTO"
coluna_sql_bancario = "numero_port"

# ==============================
# LEITURA DO CSV
# ==============================

registros = []

with open(arquivo_csv, newline='', encoding='utf-8') as csvfile:
    leitor = csv.reader(csvfile, delimiter=';')
    next(leitor)  # pula cabeçalho

    for linha in leitor:
        doc = linha[0].strip()
        banco = linha[3].strip()

        if doc and banco:
            registros.append(f"('{doc}', '{banco}')")

# ==============================
# GERAÇÃO DO SQL
# ==============================

with open(arquivo_saida, "w", encoding="utf-8") as f:

    f.write("-- Script gerado automaticamente\n")
    f.write(f"-- Total de registros: {len(registros)}\n\n")

    f.write("BEGIN TRANSACTION;\n\n")

    f.write(f"""
UPDATE t
SET t.{coluna_sql_bancario} = v.{coluna_sql_bancario}
FROM {nome_tabela} t
JOIN (
    VALUES
""")

    f.write(",\n".join(registros))

    f.write(f"""
) AS v({coluna_sql_documento}, {coluna_sql_bancario})
ON t.{coluna_sql_documento} = v.{coluna_sql_documento};

COMMIT;
""")

print(f"✅ Script otimizado gerado com {len(registros)} registros!")
