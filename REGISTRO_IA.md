Uso do claude para tentar entender o erro. 
Prompt:
import json
from datetime import date

import oracledb
from flask import (Flask, render_template, request, redirect,
                   url_for, jsonify, flash)
erro na linha 4 e 5 o que poderia ser?
Resposta:
Investigando erros de importação em um trecho de código.
Investigando erros de importação em um trecho de código.
As linhas 4 e 5 são import oracledb e from flask import (...). Como são justamente os dois pacotes de terceiros (o restante é biblioteca padrão), o mais provável é um ModuleNotFoundError: No module named 'oracledb' ou 'flask'.

Causas mais comuns

Pacotes não instalados. Instale com:
bash
   pip install flask oracledb
Interpretador ou ambiente virtual errado. Você instalou em um Python, mas o editor (VS Code, PyCharm) ou o terminal roda outro. Confira com:
bash
   python -m pip install flask oracledb
   python -c "import flask, oracledb; print('ok')"
Usar python -m pip garante que a instalação vai para o mesmo Python que executa o script. No VS Code, selecione o interpretador correto em Ctrl+Shift+P → Python: Select Interpreter.

Arquivo com o mesmo nome do pacote. Se você tem um arquivo flask.py ou oracledb.py (ou uma pasta com esse nome) no projeto, ele sobrescreve o pacote real e causa erros de importação.
Nome antigo do pacote. O driver da Oracle antes se chamava cx_Oracle. O oracledb é o nome atual, instalado com pip install oracledb.
Versão do Python muito antiga. O oracledb exige Python 3.8 ou superior (confira a versão atual com python --version).
Se não resolver, me envie a mensagem de erro completa (a última linha do traceback, tipo ModuleNotFoundError: ... ou ImportError: ...) e qual editor ou terminal você está usando, que eu aponto a causa exata.


prompt
nome: cp_de_piton
integrantes:
Tiago Borges Dos Santos RM 569926
Flavio Luiz Kuratomi Junior RM 571211
João Victor de Jesus Bernardo RM 568729
Pedro Andreotti Pugliesi RM 569357
Henrique Osuka RM 571324
objetivo:criar um site de eventos, podendo criar, verificar e ter uma ligação com banco de dados
tecnologias: oracle, python
como executar: deixar rodado estes comando no cmd
   pip install -r requirements.txt
   python app.py
desta forma aparecerá o http
o script sql usado foi o disponibilizado no enunciado
api:
requests.exceptions.Timeout:
requests.exceptions.HTTPError 
ValueError 
requests.exceptions.RequestException:

o uso de ia foi mais para tirar dúvidas

reescreva para deixar mais bonito visualmente

resposta
Deixando o README mais atraente visualmente.

Aqui está o README reescrito, pronto para copiar e colar no seu README.md:

markdown
# 🎟️ cp_de_piton

Site de eventos desenvolvido em **Python** com banco de dados **Oracle**.

---

## 👥 Integrantes

| Nome | RM |
|------|--------|
| Tiago Borges dos Santos | 569926 |
| Flavio Luiz Kuratomi Junior | 571211 |
| João Victor de Jesus Bernardo | 568729 |
| Pedro Andreotti Pugliesi | 569357 |
| Henrique Osuka | 571324 |

---

## 🎯 Objetivo

Criar um site de eventos que permita **criar** e **consultar** eventos, com integração a um banco de dados Oracle.

---

## 🛠️ Tecnologias

- 🐍 Python
- 🗄️ Oracle Database
- 🌐 Flask

---

## 🚀 Como executar

1. Abra o terminal (cmd) na pasta do projeto.
2. Instale as dependências:

```bash
   pip install -r requirements.txt
```

3. Execute a aplicação:

```bash
   python app.py
```

4. Acesse o endereço (`http://...`) que aparecerá no terminal.

---

## 🗃️ Banco de dados

O script SQL utilizado é o disponibilizado no enunciado do projeto.

---

## 🔌 API – Tratamento de erros

As exceções abaixo são tratadas nas requisições à API:

| Exceção | Quando ocorre |
|---------|---------------|
| `requests.exceptions.Timeout` | A requisição excedeu o tempo limite |
| `requests.exceptions.HTTPError` | A API retornou um status de erro (4xx ou 5xx) |
| `requests.exceptions.RequestException` | Erro genérico de requisição |
| `ValueError` | Resposta inválida ou dados em formato incorreto |

---

## 🤖 Uso de IA

A inteligência artificial foi utilizada principalmente para **tirar dúvidas** durante o desenvolvimento.

Mantive todas as informações originais, só reorganizei e formatei. Troquei “cp_de_piton” por um título com emoji e adicionei Flask nas tecnologias, já que ele aparece no seu código; remova se preferir. Se a API tiver um nome ou URL, vale incluir na seção de API.