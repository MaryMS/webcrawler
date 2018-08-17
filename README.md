# Web Crawler
Web Crawler em Python que utiliza a lib Scrapy.



Como usar:

- Clonar o projeto
- Instalar o Scrapy
- Criar um novo projeto spider
- Rodar o webcrawler

#### Clonar o projeto
git clone https://github.com/MaryMS/webcrawler.git

#### Instalar o Scrapy
É recomendável usar virtualenv e instalar o Scrapy com o comando:
pip install scrapy

OU
##### Com Anaconda:
Criar um ambiente específico para o Scrapy:
conda create -n <myenv> scrapy
Substitua <myenv> pelo nome do ambiente.

. Para ativar o novo ambiente:
  Windows: activate myenv
  macOS/Linux: source activate myenv

. Para desativar um ambiente:
  Windows: prompt do Anaconda: deactivate
  macOS/Linux: no terminal: source deactivate

Em caso de problemas na instalação do Scrapy, consulte as instruções de cada plataforma:
https://doc.scrapy.org/en/latest/intro/install.html#intro-install-platform-notes

#### Criar um novo projeto spider

Executar o comando: 
```sh
scrapy startproject urls
```
O comando irá criar o projeto "urls" com arquivos úteis para a geração do crawler. 
Verifique a estrutura das pastas criadas.

Na nova pasta, executar o comando: 
```sh
scrapy genspider getlink example.com
```
Esse código cria o crawler e gera o código para o spider "getlink".

Copie o arquivo getlink clonado desse repositório para a pasta spiders

Copie os demais arquivos.py clonados desse repositório para a pasta urls

Edite o arquivo getlink.py na linha  start_urls, com o site que irá iniciar o crawling.

#### Rodar o webcrawler

Executar o comando: 
```sh
scrapy crawl getlink
```
Para extrair as urls para um arquivo JSON: 
```sh
scrapy crawl getlink -o urls.csv -t csv
```
Para extrair as urls para um arquivo CSV: 
```sh
scrapy crawl getlink -o urls.csv -t csv
```
Para extrair as urls para um arquivo XML:
```sh
scrapy crawl getlink -o urls.xml -t xml
```
