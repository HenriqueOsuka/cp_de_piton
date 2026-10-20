import json 
from datetime import date
#aqui estão os imports necessários
import oracledb
from flask import (Flask, render_template, request, redirect,
                   url_for, jsonify, flash)
#nossos arquivos 
from dao import EventoDAO
from models import Evento
from api_service import consultar_feriados, buscar_feriado
from validacoes import validar_evento

app = Flask(__name__)
app.secret_key = "eventtech-chave-secreta"  # necessária para flash()
#caso de erro no banco de dados
MSG_BANCO = "Banco de dados indisponível. Tente novamente mais tarde."

#converte objetos em dicionarios
def eventos_para_dicts(eventos):
    return [{
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

#liga o endereço à função
@app.route('/')
def index():
    hoje = date.today()
    feriados, erro_api = consultar_feriados(hoje.year)
    #filtra os próximos 5 feriados a partir de hoje
    proximos = [f for f in feriados if f.get('date', '') >= hoje.isoformat()][:5]
    return render_template('index.html', feriados=proximos, erro_api=erro_api)


@app.route('/eventos')
def listar_eventos():
    try:
        eventos = EventoDAO.listar_todos()
        return render_template('eventos.html', eventos=eventos)
    except Exception:#qualquer erro nao aparecerá o erro tecnico 
        return render_template('eventos.html', eventos=[], erro=MSG_BANCO)


@app.route('/eventos/<int:id>')
def detalhe_evento(id):#consula os eventos pelo is e aceita apenas numeros inteiros
    try:
        evento = EventoDAO.buscar_por_id(id)
    except Exception:
        return render_template('detalhe.html', evento=None, erro=MSG_BANCO)
    if not evento:
        return render_template('detalhe.html', evento=None, erro="Evento não encontrado.")
    return render_template('detalhe.html', evento=evento)


@app.route('/eventos/cadastrar', methods=['GET', 'POST'])
def cadastrar_evento():#mostra ao usuário o formulário
    if request.method == 'POST':
        try:#valida os dados
            dados = validar_evento(request.form)
            if EventoDAO.buscar_por_id(dados['id_evento']): #confere se o id já existe
                raise ValueError("Já existe um evento com esse ID.")
            EventoDAO.inserir(Evento(**dados))#SUCESSO POURRA, desculpa prof deu trabalho para fazer esta parte ass Henrique
            flash("Evento cadastrado com sucesso!", "sucesso")
            feriado = buscar_feriado(dados['data_evento'])
            if feriado:
                flash(f"Atenção: a data do evento coincide com o feriado nacional '{feriado}'.", "aviso")
            return redirect(url_for('listar_eventos'))
        except ValueError as e:
            erro = str(e)
        except oracledb.IntegrityError:#mennsagem de erro caso o id já exista
            erro = "Já existe um evento com esse ID."
        except Exception:
            erro = MSG_BANCO
        return render_template('cadastrar.html', erro=erro)

    return render_template('cadastrar.html')


@app.route('/eventos/editar/<int:id>', methods=['GET', 'POST'])
def editar_evento(id):
    try:
        evento = EventoDAO.buscar_por_id(id)
    except Exception:#verifica se o evento existe, caso não exista, retorna uma mensagem de erro
        flash(MSG_BANCO, "erro")
        return redirect(url_for('listar_eventos'))

    if not evento:
        flash("Evento não encontrado.", "erro")
        return redirect(url_for('listar_eventos'))

    if request.method == 'POST':
        try:
            dados = validar_evento(request.form, com_id=False)
            for campo, valor in dados.items():#atualiza as informações
                setattr(evento, campo, valor)
            EventoDAO.atualizar(evento)
            flash("Evento atualizado com sucesso!", "sucesso")
            return redirect(url_for('listar_eventos'))
        except (ValueError, LookupError) as e:
            erro = str(e)
        except Exception:
            erro = MSG_BANCO
        return render_template('editar.html', evento=evento, erro=erro)

    return render_template('editar.html', evento=evento)


@app.route('/eventos/excluir/<int:id>', methods=['POST'])
def excluir_evento(id):
    try:
        EventoDAO.excluir(id)#exclusão de eventos
        flash("Evento excluído com sucesso.", "sucesso")
    except LookupError as e:
        flash(str(e), "erro")
    except Exception:
        flash(MSG_BANCO, "erro")
    return redirect(url_for('listar_eventos'))


@app.route('/api/eventos', methods=['GET'])
def api_eventos():
    try:
        lista = eventos_para_dicts(EventoDAO.listar_todos())
    except Exception:#caso tenha o erro 500, novamente nao aparece o erro tecnico
        return jsonify({'erro': 'Não foi possível carregar os dados'}), 500

    # Também gera o arquivo eventtech.json (entregável)
    try:
        with open('eventtech.json', 'w', encoding='utf-8') as f:
            json.dump(lista, f, ensure_ascii=False, indent=2)
    except OSError:
        pass
    return jsonify(lista)


@app.errorhandler(404)
def pagina_nao_encontrada(e):#menseagem de carinho
    return render_template('erro.html', mensagem="Página não encontrada."), 404


@app.errorhandler(500)
def erro_interno(e):
    return render_template('erro.html', mensagem="Erro interno do servidor."), 500


if __name__ == '__main__':
    app.run(debug=False)