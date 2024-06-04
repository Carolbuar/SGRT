# SGRT
Django Project

# Documentação do Projeto

## 1. Introdução
Este projeto é uma API RESTful para gerenciar clientes, empregos e candidatos. Ele foi desenvolvido utilizando Django e Django REST Framework.
Primeiramente desenvolveu-se a aplicação SGRT com templates html para visualização das informações. Foram aplicados alguns métodos e validações, assim como configurado o Django admin para receber as informações dos models e para permitir alguns filtros.
Logo foi desenvolvida uma API para ações CRUD, a qual foi desenvolvida de duas formas para fins de aprendizagem: utilizando o ModelViewSet e utilizando funções de view compatíveis com a API.
Por fim desenvolvou-se alguns testes para testes dos modelos e da API.

## 2. Estrutura do Projeto
A estrutura do projeto segue a convenção padrão do Django:

├── manage.py
├── SGRT
│ ├── settings.py
│ ├── urls.py
| ├── asgi.py
│ ├── wsgi.py
│ └── init.py

├── app_sgrt
│ ├── migrations
│ ├── templates
│ ├── tests
│ ├── admin.py
│ ├── apps.py
│ ├── models.py
│ ├── views.py
│ ├── urls.py
│ └── init.py

├── API
│ ├── serializers.py
│ ├── filters.py
│ ├── views.py
│ ├── urls.py
│ └── init.py
└── requirements.txt

Optou-se incluir a API em uma raiz diferente da aplicação somente para fins de organização.

## 3. Principais Decisões
- **Framework**: Django e Django REST Framework foram escolhidos pela sua robustez e facilidade de uso para criar APIs RESTful.
- **Modelo de Dados**: Foram definidos três modelos principais - `Customer`, `Job`, `Candidate`.
- **Serializers**: Utilizamos serializers para transformar os dados dos modelos em formatos JSON.
- **Views**: Implementamos views baseadas em função utilizando `@api_view` do Django REST Framework para simplicidade.

## 4. APIs e Endpoints
### Customer (ModelViewSet)
- **GET /api/customers/**: Lista todos os clientes
- **GET /api/customers/{id}/**: Detalha um cliente específico
- **POST /api/customers/**: Cria um novo cliente
- **PUT /api/customers/{id}/**: Atualiza um cliente existente
- **DELETE /api/customers/{id}/**: Deleta um cliente

### Job (ModelViewSet)
- **GET /api/jobs/**: Lista todas as vagas de emprego
- **GET /api/jobs/{id}/**: Detalha uma vaga de emprego específica
- **POST /api/jobs/**: Cria uma nova vaga de emprego
- **PUT /api/jobs/{id}/**: Atualiza uma vaga de emprego existente
- **DELETE /api/jobs/{id}/**: Deleta uma vaga de emprego

### Candidate (ModelViewSet)
- **GET /api/candidates/**: Lista todos os candidatos
- **GET /api/candidates/{id}/**: Detalha um candidato específico
- **POST /api/candidates/**: Cria um novo candidato
- **PUT /api/candidates/{id}/**: Atualiza um candidato existente
- **DELETE /api/candidates/{id}/**: Deleta um candidato

### Associações
- **POST /api/add-candidate-to-job/{candidate_id}/{job_id}/**: Adiciona um candidato a um emprego
- **GET /api/candidates-applied-to-job/{job_id}/**: Lista candidatos associados a um emprego

### Filters
- **GET /api/filtered-job-list-location/**: Filtra as vagas de emprego por localização
- **GET /api/filtered-job-list-status/**: Filtra as vagas de emprego pelo status
- **GET /api/filtered-job-list-customer/**: Filtra as vagas de emprego por localização

### @api_view - Customer
- **GET /api/customer-list/**:Lista todos os clientes
- **GET /api/customer-detail/{id}/**: Detalha um cliente específico
- **POST /api/customer-create/**: Cria um novo cliente
- **PUT /api/customer-update/{id}**: Atualiza um cliente existente
- **DELETE /api/customer-delete/{id}/**: Deleta um cliente

### @api_view - Job
- **GET /api/job-list/**:Lista todas os vagas de emprego
- **GET /api/job-detail/{id}/**: Detalha uma vaga de emprego específica
- **POST /api/job-create/**: Cria uma nova vaga de emprego
- **PUT /api/job-update/{id}/**: Atualiza uma vaga de emprego existente
- **DELETE /api/job-delete/{id}/**: Deleta uma vaga de emprego

### @api_view - Candidate
- **GET /api/candidate-list/**:Lista todos os candidatos
- **GET /api/candidate-detail/{id}/**: Detalha um candidato específico
- **POST /api/candidate-create/**: Cria um novo candidato
- **PUT /api/candidate-update/{id}/**: Atualiza um candidato existente
- **DELETE /api/candidate-delete/{id}/**: Deleta um candidato

## 5. Testes
Testes unitários foram implementados para garantir o funcionamento correto das operações CRUD para `Customer`, `Job` e `Candidate`.

## 6. Configuração e Execução
### Requisitos

- Python 3.11.5*


### Instalação
1. Clone o repositório:
   
    git clone https://github.com/Carolbuar/SGRT.git
   
2. Navegue até o diretório do projeto:
    
    cd ../SGRT

3. Use o pyenv para instalar a versão específica do Python (Opcional):
   
    pyenv install 3.11.5
    pyenv local 3.11.5

3. Crie um ambiente virtual:
   
    python -m venv venv
    
4. Ative o ambiente virtual:

    venv\Scripts\activate
  
5. Instale as dependências:
   
    pip install -r requirements.txt
  
6. Execute as migrações do banco de dados:
    
    python manage.py migrate
    
7. Inicie o servidor:
    
    python manage.py runserver

8. Para rodar os testes:
    
    python manage.py test
    

## 7. Tecnologias Utilizadas
- **Django**: Framework principal para o desenvolvimento da aplicação.
- **Django REST Framework**: Biblioteca utilizada para criar a API RESTful.
- **SQLite**: Banco de dados utilizado para desenvolvimento e testes.

## 8. Notas Finais
Qualquer dúvida ou problema encontrado durante o uso ou avaliação do projeto pode ser encaminhado para o email do desenvolvedor em [carolba@hotmail.com].