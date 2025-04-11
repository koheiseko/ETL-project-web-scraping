# Projeto ETL com Web Scraping — Notebooks do Mercado Livre
Este projeto realiza um processo ETL (Extração, Transformação e Carga) utilizando web scraping com Scrapy para coletar dados de notebooks anunciados no site Mercado Livre, Pandas para transformar os dados e SQLite para armazená-los em um banco de dados local.

# Objetivo
Coletar informações atualizadas sobre notebooks vendidos no Mercado Livre, como:

- Marca do produto
- Nome do produto
- Preço
- Número de avaliações
- Loja em que o produto está sendo anunciado

Esses dados são então limpos, transformados e armazenados em uma base de dados para análises futuras.

# Tecnologias Utilizadas

- Scrapy — Para extração dos dados (web scraping)
- Pandas — Para limpeza e transformação dos dados
- SQLite3 — Como banco de dados local
- Python 3.9+ — Linguagem principal do projeto

# Observações

- Pode ser necessário ajustar o User-Agent para evitar bloqueios.
- Os dados extraídos são públicos e utilizados apenas para fins educacionais.
