## Iniciando aplicação

Para instalar todas as dependências, rode:
```sh
pip install -r requirements.txt
```

## Banco de dados
Instale o docker e docker-compose, e depois rode:
```sh
docker-compose up
```
Isso deve fazer com que um banco de dados MySQL seja 
rodado no endereço `172.16.1.3` com senha `root` sem senha.

O arquivo de setup do banco é o [portaria_cadastro.sql](./database/portaria_cadastro.sql)
e criará o banco de dados `controle_condominio`