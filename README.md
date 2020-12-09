# Projeto MIDSI

### Código fonte do motor de inferência Midsi com estudo de caso e benchmark

Nova solução para descoberta de dados em soluções baseadas em Web Semântica, possibilita o carregamento de ontologias e inferência de resultados utilizando WSML.

### Pré-requisitos:

- SwiProlog
- Python 3.\*
  - pyswip

### Instalando dependências do projeto

Sistemas baseados em debian:

    sudo ./install.sh

Outros sistemas instalar seguintes pacotes:

    default_jre
    python3
    swi-prolog #swi-prolog ou pl
    pip pyswip

### Benchmark

Para executar e visualizar os resultados `python3 benchmark.py`. Será criado uma pasta log contendo o resultado do benchmark.
