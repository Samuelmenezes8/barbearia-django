# 💈 Barbearia do Dev - Sistema de Agendamento

![Status do Projeto: Concluído](https://img.shields.io/badge/status-concluído-brightgreen)

<p align="center">
  </p>

## 📄 Descrição

Este é um projeto de uma aplicação web completa para o agendamento de horários em uma barbearia. Desenvolvido como parte dos meus estudos em desenvolvimento full-stack, o sistema permite que clientes visualizem os serviços, escolham um profissional e agendem um horário de forma intuitiva, enquanto oferece aos administradores da barbearia um painel para gerenciar todos os aspectos do negócio.

O foco foi criar um sistema robusto, com lógica de negócios para evitar conflitos de horários e uma base de código limpa e organizada, seguindo as melhores práticas do framework Django.

---

## ✨ Funcionalidades Principais

- **Para Clientes:**
  - [x] Visualização da lista de serviços com preços e durações.
  - [x] Página de detalhes para cada serviço.
  - [x] Formulário de agendamento com seleção de barbeiro.
  - [x] Calendário interativo para seleção de data e hora (usando Flatpickr.js).
  - [x] Validação em tempo real que impede agendamentos em horários já ocupados.
  - [x] Página de confirmação de sucesso após o agendamento.

- **Para Administradores (via Painel Admin do Django):**
  - [x] Gerenciamento completo (Criar, Ler, Atualizar, Deletar) de Barbeiros.
  - [x] Gerenciamento completo de Serviços.
  - [x] Visualização e gerenciamento de todos os Agendamentos.

---

## 🚀 Tecnologias Utilizadas

Este projeto foi construído utilizando as seguintes tecnologias:

- **Back-end:**
  - ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
  - ![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)

- **Front-end:**
  - ![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
  - ![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
  - ![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)

- **Banco de Dados:**
  - ![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)

- **Ferramentas e Bibliotecas:**
  - Git & GitHub
  - Flatpickr.js (para o seletor de data/hora)
  - python-dotenv (para gerenciamento de variáveis de ambiente)

---

## ⚙️ Como Rodar o Projeto Localmente

Siga os passos abaixo para executar o projeto em sua máquina.

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/Samuelmenezes8/barbearia-django.git](https://github.com/Samuelmenezes8/barbearia-django.git)
    cd barbearia-django
    ```

2.  **Crie e ative um ambiente virtual:**
    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # Linux / Mac
    source venv/bin/activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure as variáveis de ambiente:**
    - Crie um arquivo `.env` na raiz do projeto.
    - Adicione a seguinte linha, substituindo pela sua chave:
      ```
      SECRET_KEY='sua_secret_key_aqui'
      ```

5.  **Aplique as migrações do banco de dados:**
    ```bash
    python manage.py migrate
    ```

6.  **Crie um superusuário para acessar o Admin:**
    ```bash
    python manage.py createsuperuser
    ```

7.  **Inicie o servidor:**
    ```bash
    python manage.py runserver
    ```

8.  Acesse a aplicação em `http://127.0.0.1:8000/` no seu navegador.

---

## 📸 Screenshots

**Página Inicial**
![Página Inicial com a lista de serviços](screenshots/pagina%20inicial.png)

**Formulário de Agendamento**
![Formulário de agendamento com o seletor de data](screenshots/pagina%20de%20agendamento.png/)

**Formulário do Adm**
![Pagina de administração do barbeiro](screenshots/pagina%20dos%20agendamentos.png)

**Pagina Final do Agendamento**
![Pagina final do agendamento](screenshots/pagina%20final%20do%20agendamento.png)


---

---
### Passo 2: Criar o Arquivo `requirements.txt`

Na seção "Como Rodar", mencionamos um arquivo `requirements.txt`. Este arquivo lista todas as dependências do Python que seu projeto precisa. É uma prática essencial.

* Para criá-lo, vá ao seu terminal (com o `venv` ativo) e rode o seguinte comando:

```bash
pip freeze > requirements.txt