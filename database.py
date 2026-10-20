import os
import oracledb


def conectar_banco():
    return oracledb.connect(#informações do banco de dados (sigilosas)
        user=os.getenv("ORACLE_USER", "RM571324"),
        password=os.getenv("ORACLE_PASSWORD", "250208"),
        dsn=os.getenv("ORACLE_DSN", "oracle.ficap.com.br")
    )