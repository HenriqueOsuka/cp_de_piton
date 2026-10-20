from database import conectar_banco
from models import Evento
#importação de outros arquivos
class EventoDAO:
    @staticmethod
    def inserir(evento):#conexão com banco de dados
        conn = conectar_banco()
        cursor = conn.cursor()
        try:
            sql = """
                INSERT INTO EVENTOS (ID_EVENTO, NOME_EVENTO, CATEGORIA, DATA_EVENTO, 
                                     LOCAL_EVENTO, CAPACIDADE, VALOR_INGRESSO, 
                                     RESPONSAVEL, STATUS)
                VALUES (:1, :2, :3, TO_DATE(:4, 'YYYY-MM-DD'), :5, :6, :7, :8, :9)
            """#ordem da tupla 
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
            cursor.close()#se deu certo ou nao fecha-se
            conn.close()

    @staticmethod
    def listar_todos():
        conn = conectar_banco()
        cursor = conn.cursor()
        eventos = []#aonde será guardado os eventos
        try:
            cursor.execute("SELECT ID_EVENTO, NOME_EVENTO, CATEGORIA, TO_CHAR(DATA_EVENTO, 'YYYY-MM-DD'), LOCAL_EVENTO, CAPACIDADE, VALOR_INGRESSO, RESPONSAVEL, STATUS FROM EVENTOS")
            for row in cursor: # Percorre o resultado linha por linha. Cada "row" é uma
            # tupla; row[0] é a 1ª coluna do SELECT, row[1] a 2ª, etc.
                ev = Evento(
                    id_evento=row[0], nome_evento=row[1], categoria=row[2],
                    data_evento=row[3], local_evento=row[4], capacidade=row[5],
                    valor_ingresso=row[6], responsavel=row[7], status=row[8]
                )
                eventos.append(ev)#adiciona o evento à lista
        finally:
            cursor.close()
            conn.close()
        return eventos

    @staticmethod
    def buscar_por_id(id_evento):
        conn = conectar_banco()
        cursor = conn.cursor()#filtra o evendo desejado
        try:
            sql = "SELECT ID_EVENTO, NOME_EVENTO, CATEGORIA, TO_CHAR(DATA_EVENTO, 'YYYY-MM-DD'), LOCAL_EVENTO, CAPACIDADE, VALOR_INGRESSO, RESPONSAVEL, STATUS FROM EVENTOS WHERE ID_EVENTO = :1"
            cursor.execute(sql, (id_evento,))
            row = cursor.fetchone()
            if row:#se sucesso
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
            if cursor.rowcount == 0:#atualiza o evento com as informações dadas
                conn.rollback()
                raise LookupError("Evento não encontrado.")
            conn.commit()
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            cursor.close()
            conn.close()

    @staticmethod#exclui o evento se existir
    def excluir(id_evento):
        conn = conectar_banco()
        cursor = conn.cursor()
        try:
            cursor.execute("DELETE FROM EVENTOS WHERE ID_EVENTO = :1", (id_evento,))
            if cursor.rowcount == 0:
                conn.rollback()
                raise LookupError("Evento não encontrado.")
            conn.commit()
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            cursor.close()
            conn.close()
            