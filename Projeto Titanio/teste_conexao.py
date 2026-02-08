import pyodbc

def testar_conexao(driver, servidor):
    """
    Testa a conexão com o SQL Server e lista bancos disponíveis.
    """
    try:
        print(f"🔹 Tentando conectar ao SQL Server usando o driver '{driver}' no servidor '{servidor}'...")
        conn = pyodbc.connect(f'DRIVER={{{driver}}};SERVER={servidor};Trusted_Connection=yes;')
        cursor = conn.cursor()
        print("✅ Conexão estabelecida com sucesso!\n")

        # Lista os bancos de dados (excluindo os do sistema)
        cursor.execute("SELECT name FROM sys.databases WHERE database_id > 4")
        bancos = [row[0] for row in cursor.fetchall()]
        print("📚 Bancos disponíveis no servidor:")
        for b in bancos:
            print(f"  - {b}")

        conn.close()
        print("\n🎯 Teste concluído com sucesso!")

    except pyodbc.Error as e:
        print("❌ Erro ao conectar:")
        print(e)

if __name__ == "__main__":
    # Ajuste aqui se mudar de servidor
    DRIVER = "ODBC Driver 17 for SQL Server"
    SERVIDOR = "."  # Servidor local

    testar_conexao(DRIVER, SERVIDOR)