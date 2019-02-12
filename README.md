# rest-cities

Aplicação REST básica para manutenção de uma lista de cidades

## Execução local

### Instalar pacotes

Criar um novo VirtualEnvironment com a runtime Python 3.6.7:

https://realpython.com/python-virtual-environments-a-primer/

Após ativar o VirtualEnvironment, instalar os pacotes utilizando o pip:

```
pip install -r requirements.txt
```

### Execução

No diretório do projeto, utilizar o script **manage.py** para migrar o banco de dados:

```
python manage.py migrate
```

Subir a aplicação utilizando o script **manage.py**:

```
python manage.py runserver
```

## Detalhes da API REST

### Operações GET:

Listar cidades
```
http://127.0.0.1:8000/cidades/
```
Retornar somente as cidades que são capitais ordenadas por nome
```
http://127.0.0.1:8000/capitais/
```
Retornar a quantidade de cidades por estado
```
http://127.0.0.1:8000/numero_cidades_por_estado/
```
Obter os dados da cidade informando o id do IBGE
```
http://127.0.0.1:8000/cidades/{id_ibge}/
```
Retornar o nome das cidades baseado em um estado selecionado
```
http://127.0.0.1:8000/cidades_por_estado/{uf}/
```
Retornar a quantidade de registros total
```
http://127.0.0.1:8000/quantidade_registros/
```

## Operações POST:

Ler o arquivo CSV das cidades para a base de dados
```
http://127.0.0.1:8000/popula-bd/
```
Adicionar uma nova cidade
```
http://127.0.0.1:8000/cidades/
```

## Operações DELETE:
Remover uma cidade
```
http://127.0.0.1:8000/cidades/{id_ibge}/
```
