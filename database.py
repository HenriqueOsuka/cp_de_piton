import oracledb

def conectar_banco():
    try:
        # Substitua pelas suas credenciais reais do Oracle
        connection = oracledb.connect(
            user="seu_usuario",
            password="sua_senha",
            dsn="localhost:1521/XE"
        )
        return connection
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados Oracle: {e}")
        raise e