# 🎟️ cp_de_piton

### Plataforma de eventos com Python + Oracle

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Oracle](https://img.shields.io/badge/Oracle-F80000?style=for-the-badge&logo=oracle&logoColor=white)

</div>

---

## 📌 Sobre o projeto

Site de eventos que permite **criar** e **consultar** eventos, com integração a um banco de dados **Oracle**.

---

## 👥 Equipe

| 👤 Integrante | 🎓 RM |
|:--------------|:------:|
| Tiago Borges dos Santos | `569926` |
| Flavio Luiz Kuratomi Junior | `571211` |
| João Victor de Jesus Bernardo | `568729` |
| Pedro Andreotti Pugliesi | `569357` |
| Henrique Osuka | `571324` |

---

## 🛠️ Tecnologias

| Tecnologia | Uso |
|------------|-----|
| 🐍 Python | Linguagem principal |
| 🌶️ Flask | Servidor web |
| 🗄️ Oracle | Banco de dados |

---

## ▶️ Como executar

**1.** Abra o terminal (cmd) na pasta do projeto.

**2.** Instale as dependências:

```bash
pip install -r requirements.txt
```

**3.** Inicie a aplicação:

```bash
python app.py
```

**4.** Abra no navegador o endereço `http://...` exibido no terminal.

---

## 🗃️ Banco de dados

O script SQL utilizado é o disponibilizado no enunciado do projeto.

---

## 🔌 API: tratamento de erros

| Exceção | Descrição |
|---------|-----------|
| ⏱️ `requests.exceptions.Timeout` | Tempo limite da requisição excedido |
| ❌ `requests.exceptions.HTTPError` | A API retornou erro HTTP (4xx ou 5xx) |
| ⚠️ `requests.exceptions.RequestException` | Erro genérico na requisição |
| 🧩 `ValueError` | Dados ou resposta em formato inválido |

---

## 🤖 Uso de IA

> A inteligência artificial foi utilizada principalmente para **tirar dúvidas** durante o desenvolvimento.

---

