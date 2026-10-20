class Evento:
    def __init__(self, id_evento, nome_evento, categoria, data_evento, #todo evento novo recomeça as informações
                 local_evento, capacidade, valor_ingresso, 
                 responsavel, status="ATIVO"):
        self.id_evento = id_evento
        self.nome_evento = nome_evento
        self.categoria = categoria
        self.data_evento = data_evento
        self.local_evento = local_evento#aonde se guarda as informações 
        self.capacidade = capacidade
        self.valor_ingresso = valor_ingresso
        self.responsavel = responsavel
        self.status = status