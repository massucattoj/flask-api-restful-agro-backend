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

### Execução do projeto Local

- Clonar repositorio
- Utilizar pip para instalar os pacotes necessarios (pip install -r requirements.txt) preferencialmente
  dentro de um ambiente virtual

- Para acessar o swagger basta iniciar o projeto python e acessar o endereco http://127.0.0.1:5000/apidocs

#### Endpoints

Os endpoints listados abaixo representam os endpoints criados pelo heroku, para testar localmente
basta substituir a parte que referencia o heroku para http://127.0.0.1:5000

- Cadastrar nova comunicação de perda: POST
- Atualizar comunicação de perda: PUT
- Deletar comunicação de perda: DELETE

- Listar todas as comunicaçōes de perda (O filtro acontece lado front end): GET
