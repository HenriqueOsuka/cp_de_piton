from datetime import datetime


def _texto(form, campo, rotulo):
    valor = form.get(campo, '').strip()
    if not valor:#nenhum campo fica vazio
        raise ValueError(f"{rotulo} não pode ficar vazio.")
    return valor


def validar_evento(form, com_id=True):
    dados = {}

    if com_id:
        try:
            dados['id_evento'] = int(form.get('id_evento', ''))
        except ValueError:
            raise ValueError("O ID deve ser um número inteiro.")
        if dados['id_evento'] <= 0:
            raise ValueError("O ID deve ser maior que zero.")

    dados['nome_evento'] = _texto(form, 'nome_evento', 'O nome')#esses campos nao podem ficar vazios
    dados['categoria'] = _texto(form, 'categoria', 'A categoria')

    data = form.get('data_evento', '').strip()#exigi uma data válida
    try:
        datetime.strptime(data, '%Y-%m-%d')
    except ValueError:#leitura do arquivo de data
        raise ValueError("Data inválida.")
    dados['data_evento'] = data

    dados['local_evento'] = _texto(form, 'local_evento', 'O local')#guarda o local

    try:
        dados['capacidade'] = int(form.get('capacidade', ''))
    except ValueError:#valida apenas capacidades maiores que 0 
        raise ValueError("A capacidade deve ser um número inteiro.")
    if dados['capacidade'] <= 0:
        raise ValueError("A capacidade deve ser maior que zero.")

    try:
        dados['valor_ingresso'] = float(form.get('valor_ingresso') or 0)
    except ValueError:#valida o valor do ingresso impedindo que seja negativo
        raise ValueError("Valor do ingresso inválido.")
    if dados['valor_ingresso'] < 0:
        raise ValueError("O valor do ingresso não pode ser negativo.")

    dados['responsavel'] = _texto(form, 'responsavel', 'O responsável')#quem é o manda chuva

    dados['status'] = form.get('status', 'ATIVO')
    if dados['status'] not in ('ATIVO', 'CANCELADO'):
        raise ValueError("Status inválido.")#ativo ou inavito no caso cancelado

    return dados