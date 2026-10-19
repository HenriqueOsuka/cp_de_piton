from flask import Flask, render_template, request, redirect, url_for, jsonify
from dao import EventoDAO
from models import Evento
from api_service import consultar_feriados

app = Flask(__name__)

@app.route('/')
def index():
    feriados = consultar_feriados(2026)[:5] # Pega alguns feriados para exibir na home
    return render_template('index.html', feriados=feriados)

@app.route('/eventos')
def listar_eventos():
    try:
        eventos = EventoDAO.listar_todos()
        return render_template('eventos.html', eventos=eventos)
    except Exception:
        return render_template('eventos.html', eventos=[], erro="Erro ao carregar banco de dados.")

@app.route('/eventos/cadastrar', methods=['GET', 'POST'])
def cadastrar_evento():
    if request.method == 'POST':
        try:
            id_evento = int(request.form['id_evento'])
            nome_evento = request.form['nome_evento'].strip()
            categoria = request.form['categoria'].strip()
            data_evento = request.form['data_evento']
            local_evento = request.form['local_evento'].strip()
            capacidade = int(request.form['capacidade'])
            valor_ingresso = float(request.form['valor_ingresso'] or 0)
            responsavel = request.form['responsavel'].strip()
            status = request.form.get('status', 'ATIVO')

            # Validações básicas
            if not nome_evento or not categoria or not responsavel:
                raise ValueError("Preencha todos os campos obrigatórios.")
            if capacidade <= 0:
                raise ValueError("Capacidade deve ser maior que zero.")
            if valor_ingresso < 0:
                raise ValueError("O valor do ingresso não pode ser negativo.")

            novo_evento = Evento(id_evento, nome_evento, categoria, data_evento, 
                                 local_evento, capacidade, valor_ingresso, responsavel, status)
            EventoDAO.inserir(novo_evento)
            return redirect(url_for('listar_eventos'))
        except Exception as e:
            return render_template('cadastrar.html', erro=str(e))

    return render_template('cadastrar.html')

@app.route('/eventos/editar/<int:id>', methods=['GET', 'POST'])
def editar_evento(id):
    evento = EventoDAO.buscar_por_id(id)
    if not evento:
        return redirect(url_for('listar_eventos'))

    if request.method == 'POST':
        try:
            evento.nome_evento = request.form['nome_evento'].strip()
            evento.categoria = request.form['categoria'].strip()
            evento.data_evento = request.form['data_evento']
            evento.local_evento = request.form['local_evento'].strip()
            evento.capacidade = int(request.form['capacidade'])
            evento.valor_ingresso = float(request.form['valor_ingresso'] or 0)
            evento.responsavel = request.form['responsavel'].strip()
            evento.status = request.form['status']

            EventoDAO.atualizar(evento)
            return redirect(url_for('listar_eventos'))
        except Exception as e:
            return render_template('editar.html', evento=evento, erro=str(e))

    return render_template('editar.html', evento=evento)

@app.route('/eventos/excluir/<int:id>', methods=['POST'])
def excluir_evento(id):
    try:
        EventoDAO.excluir(id)
    except Exception:
        pass
    return redirect(url_for('listar_eventos'))

# Rota para exportar dados em JSON (Exigência do projeto)
@app.route('/api/eventos', methods=['GET'])
def api_eventos():
    try:
        eventos = EventoDAO.listar_todos()
        lista_json = [{
            'id': e.id_evento,
            'nome': e.nome_evento,
            'categoria': e.categoria,
            'data': e.data_evento,
            'local': e.local_evento,
            'capacidade': e.capacidade,
            'valor': e.valor_ingresso,
            'responsavel': e.responsavel,
            'status': e.status
        } for e in eventos]
        return jsonify(lista_json)
    except Exception as e:
        return jsonify({'erro': 'Não foi possível carregar os dados'}), 500

if __name__ == '__main__':
    app.run(debug=True) 