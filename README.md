# Instruções para execução:

```
git clone https://github.com/gllherme/desafio-insightlab.git
cd desafio-insightlab
sudo docker compose up --build
```

Obs: Não é possivel executar sem o docker já que a aplicação precisa do container do mongodb para funcionar.

# Funcionalidades
A aplicação utiliza a [API de países do IBGE](https://servicodados.ibge.gov.br/api/docs/paises) para coletar os dados, extrai as informações relevantes e adiciona a funcionalidade de filtro por data.

- **Consultar perfil do país**: Exibe um perfil do país consultado. O perfil inclui nome, código, área territorial, linguas, moedas e um texto sobre o país.
- **Consultar dados**: A consulta de dados permite selecionar um país, consultar e filtrar por ano dados sobre a população, redes, saúde, economia, indicadores sociais e meio ambiente.
