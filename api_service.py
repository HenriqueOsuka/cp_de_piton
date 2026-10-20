import requests


def consultar_feriados(ano):
    """Retorna (lista_de_feriados, mensagem_de_erro)."""
    url = f"https://brasilapi.com.br/api/feriados/v1/{ano}"
    try:#as api usadas
        resposta = requests.get(url, timeout=5)
        resposta.raise_for_status()
        return resposta.json(), None
    except requests.exceptions.Timeout:
        return [], "A API de feriados demorou demais para responder."
    except requests.exceptions.HTTPError:#essas api são necessárias para o funcionamento do site
        return [], "A API de feriados retornou uma resposta inesperada."
    except ValueError:
        return [], "A API de feriados retornou um JSON inválido."
    except requests.exceptions.RequestException:
        return [], "API de feriados indisponível."


def buscar_feriado(data_iso):
    """Recebe 'YYYY-MM-DD' e devolve o nome do feriado, ou None."""
    feriados, erro = consultar_feriados(int(data_iso[:4]))
    for f in feriados:
        if f.get('date') == data_iso:
            return f.get('name')
    return None