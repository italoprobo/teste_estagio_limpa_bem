# teste_estagio_limpa_bem

LIMPA-BEM
O LIMPA-BEM é um aplicativo web para gerenciamento de serviços de limpeza.

Instalação
Clone o repositório do projeto do GitHub em seu computador. Para isso, abra o terminal (ou prompt de comando) e digite o seguinte comando:
git clone https://github.com/seu-nome-de-usuario/nome-do-repositorio.git
Substitua <seu-nome-de-usuario> pelo seu nome de usuário no GitHub e <nome-do-repositorio> pelo nome do repositório que você clonou.

Instale as dependências do projeto. Para isso, navegue até a pasta do projeto clonado e digite o seguinte comando:
pip install -r requirements.txt
Esse comando irá instalar todas as dependências necessárias para o projeto.

Crie o banco de dados. Para criar as tabelas do banco de dados, execute o seguinte comando:
python manage.py migrate
Esse comando irá criar todas as tabelas no banco de dados.

Crie um superusuário. Para criar um superusuário, digite o seguinte comando:
python manage.py createsuperuser
Esse comando irá pedir que você crie um nome de usuário, endereço de e-mail e senha para o superusuário. O superusuário terá acesso a todas as funcionalidades do sistema.

Execute o servidor local. Para executar o servidor local, digite o seguinte comando:
python manage.py runserver
Copie e cole o endereço no seu navegador, estará mais ou menos dessa forma:
Starting development server at http://xxx.x.x.x:8000/
