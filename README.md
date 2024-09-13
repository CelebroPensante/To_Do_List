# Aplicativo To-Do List em Django

##  Explicação:

Este é um aplicativo de lista de tarefas desenvolvido com Django, para o nosso trabalho de python. Ele permite que os usuários criem, editem e excluam tarefas, além de gerenciar prioridades e status. O sistema de autenticação garante que cada usuário visualize apenas suas tarefas, com permissões adicionais para administradores, feito usando
um css e html próprio.

Funcionalidades: 

 - Autenticação de usuários (registro/login/logout)
 - Gerenciamento de tarefas (criar, editar, excluir)
 - Filtragem por status e prioridade
 - Controle administrativo para visualização de todas as tarefas

Instalação:
1. Clone a repo:

    ```bash
    git clone git clone https://github.com/CelebroPensante/To_Do_List.git
    ```
Crie um ambiente virtual e ative:

2. Crie um ambiente virtual e ative:

    ```bash
    python3 -m venv env
    source env/bin/activate
    ```
3. Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

4. Aplique as migrações e crie um superusuário:

   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```
3. Inicie o servidor:

   ```bash
    python manage.py runserver
   ```

### Uso: 

- Gerencie tarefas criando, editando e excluindo conforme necessário.
- Admins podem visualizar todas as tarefas e filtrar por usuário.

### ALUNOS
- VITOR
- LUCAS
- PEDRO 
