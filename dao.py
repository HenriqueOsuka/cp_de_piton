from database import conectar_banco
from models import Evento
import oracledb

class EventoDAO:
    @staticmethod
    def inserir(evento):
        conn = conectar_banco()
        cursor = conn.cursor()
        try:
            sql = """
                INSERT INTO EVENTOS (ID_EVENTO, NOME_EVENTO, CATEGORIA, DATA_EVENTO, 
                                     LOCAL_EVENTO, CAPACIDADE, VALOR_INGRESSO, 
                                     RESPONSAVEL, STATUS)
                VALUES (:1, :2, :3, TO_DATE(:4, 'YYYY-MM-DD'), :5, :6, :7, :8, :9)
            """
            cursor.execute(sql, (
                evento.id_evento, evento.nome_evento, evento.categoria, 
                evento.data_evento, evento.local_evento, evento.capacidade, 
                evento.valor_ingresso, evento.responsavel, evento.status
            ))
            conn.commit()
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def listar_todos():
        conn = conectar_banco()
        cursor = conn.cursor()
        eventos = []
        try:
            cursor.execute("SELECT ID_EVENTO, NOME_EVENTO, CATEGORIA, TO_CHAR(DATA_EVENTO, 'YYYY-MM-DD'), LOCAL_EVENTO, CAPACIDADE, VALOR_INGRESSO, RESPONSAVEL, STATUS FROM EVENTOS")
            for row in cursor:
                ev = Evento(
                    id_evento=row[0], nome_evento=row[1], categoria=row[2],
                    data_evento=row[3], local_evento=row[4], capacidade=row[5],
                    valor_ingresso=row[6], responsavel=row[7], status=row[8]
                )
                eventos.append(ev)
        finally:
            cursor.close()
            conn.close()
        return eventos

    @staticmethod
    def buscar_por_id(id_evento):
        conn = conectar_banco()
        cursor = conn.cursor()
        try:
            sql = "SELECT ID_EVENTO, NOME_EVENTO, CATEGORIA, TO_CHAR(DATA_EVENTO, 'YYYY-MM-DD'), LOCAL_EVENTO, CAPACIDADE, VALOR_INGRESSO, RESPONSAVEL, STATUS FROM EVENTOS WHERE ID_EVENTO = :1"
            cursor.execute(sql, (id_evento,))
            row = cursor.fetchone()
            if row:
                return Evento(
                    id_evento=row[0], nome_evento=row[1], categoria=row[2],
                    data_evento=row[3], local_evento=row[4], capacidade=row[5],
                    valor_ingresso=row[6], responsavel=row[7], status=row[8]
                )
            return None
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def atualizar(evento):
        conn = conectar_banco()
        cursor = conn.cursor()
        try:
            sql = """
                UPDATE EVENTOS 
                SET NOME_EVENTO = :1, CATEGORIA = :2, DATA_EVENTO = TO_DATE(:3, 'YYYY-MM-DD'), 
                    LOCAL_EVENTO = :4, CAPACIDADE = :5, VALOR_INGRESSO = :6, 
                    RESPONSAVEL = :7, STATUS = :8
                WHERE ID_EVENTO = :9
            """
            cursor.execute(sql, (
                evento.nome_evento, evento.categoria, evento.data_evento, 
                evento.local_evento, evento.capacidade, evento.valor_ingresso, 
                evento.responsavel, evento.status, evento.id_evento
            ))
            conn.commit()
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def excluir(id_evento):
        conn = conectar_banco()
        cursor = conn.cursor()
        try:
            cursor.execute("DELETE FROM EVENTOS WHERE ID_EVENTO = :1", (id_evento,))
            conn.commit()
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            cursor.close()
            conn.close()
            