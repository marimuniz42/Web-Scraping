# Web Scraping com Python - Extração de Tabelas do Wikipedia

Este é um projeto simples de web scraping em Python que utiliza a biblioteca **BeautifulSoup** para extrair dados de uma tabela do Wikipedia que lista as maiores empresas dos Estados Unidos por receita. O objetivo é explorar técnicas de raspagem de dados e criar um **DataFrame** usando **Pandas** para estruturar as informações.

## Objetivo

Extrair dados da página do Wikipedia com a lista das maiores empresas dos Estados Unidos por receita:  
[https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue](https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue)

## Tecnologias Utilizadas

- Python 3.x
- Bibliotecas:
  - `BeautifulSoup` (para parseamento HTML)
  - `requests` (para requisições HTTP)
  - `pandas` (para manipulação de dados)

## Como Funciona

1. O script faz uma requisição à URL da página do Wikipedia.
2. Utiliza o **BeautifulSoup** para parsear o HTML e localizar a tabela de interesse.
3. Extrai os dados da tabela, organiza as colunas e armazena os dados como um **DataFrame** do pandas.


## Como Executar

1. Clone este repositório:
   ```bash
   git clone https://github.com/marimuniz42/Web-Scraping.git
   cd Web-Scraping
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Execute o programa:
   ```bash
   python3 scrappingTeste.py
   ```

## Dependências

As bibliotecas necessárias estão listadas no arquivo `requirements.txt`.

## Recursos

Este projeto foi inspirado no vídeo do YouTube:  
[Como fazer web scraping com Python | BeautifulSoup + Pandas](https://www.youtube.com/watch?v=8dTpNajxaH0)

## Status do Projeto

✅ Este projeto está **finalizado**.