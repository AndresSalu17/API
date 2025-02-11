# repoandres
 Repositorio do Andres


Python
1- Criar ambiente virtual
python -m venv .venv

2- Entrar no ambiente
.venv/Scripts/activate

CRIAR NOVO PROJETO
django-admin startproject setup .

django-admin startapp NOME DO APP


3- Instalar os requisitos do txt
pip install -r requirements.txt

4- Se precisar atualizar o PIP
python.exe -m pip install --upgrade pip

5-Criando os arquivos de migração(SOMENTE QUANDO O BANCO DE DADOS ESTIVER MONTADO)
python manage.py makemigrations

6-Realizar a migração
python manage.py migrate

7-Criar um super usuário
python manage.py createsuperuser

8- Quando precisar do env(BAIXAR BIBLIOTECA)
pip install python-decouple

9-Desinstalar uma lib
pip uninstall python-decouple

10- Quando for atualizar meus requirements
pip freeze > requirements.txt
