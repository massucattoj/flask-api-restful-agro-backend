# Projeto Agro

Um simples CRUD para cadastro / comunicaçāo de perdas em lavouras.

### Tecnologias utilizadas

- Python
- Flask
- RESTful
- SQLAlchemy
- PostgreSQL
- Heroku
- Flasgger
- unittest

### Execução do projeto heroku

- Link backend: https://agro-flask.herokuapp.com/
- Link frontend: https://agrotop.netlify.app/
- Link swagger: https://agro-flask.herokuapp.com/apidocs

### Execução do projeto Local

- Clonar repositorio
- Utilizar pip para instalar os pacotes necessarios (pip install -r requirements.txt) preferencialmente
  dentro de um ambiente virtual

- Para acessar o swagger basta iniciar o projeto python e acessar o endereco http://127.0.0.1:5000/apidocs

#### Endpoints

Os endpoints listados abaixo representam os endpoints criados pelo heroku, para testar localmente
basta substituir a parte que referencia o heroku para http://127.0.0.1:5000

- Listar todas as comunicação de perda: GET = http://127.0.0.1:5000/loss_communication
- Cadastrar nova comunicação de perda: POST = http://127.0.0.1:5000/loss_communication
- Atualizar comunicação de perda: PUT = http://127.0.0.1:5000/loss_communication/:id
- Deletar comunicação de perda: DELETE = http://127.0.0.1:5000/loss_communication/:id

- Listar todas as comunicaçōes de perda (O filtro acontece lado front end): GET

### Run Test

Terminal: export ENV_FILE_LOCATION=./.env.test
Terminal: python -m unittest tests/test_loss_communication.py

Descomentar essa linha no arquivo app.py

- app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///teste.db"

Comentar essa linha no arquivo app.py

- app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URI", "sqlite:///data.db") # tell where is the database

TODO: Configurar dotenv de testes

### Melhorias

- Busca de localização por CEP
- Dashboard das causalidades, periodos
- Prever possiveis causalidades com base em eventos passados
- Adicionar imagens do estrago causado pelos eventos
- Buscar evento automaticamente em alguma base de dados meteorológica com base na data
