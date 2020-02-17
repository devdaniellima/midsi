# Projeto wsml-engine
## TCC - Sistemas de Informação - Universidade Federal de Sergipe - Itabaiana - SE

### Pré-requisitos:
* SwiProlog
* Python 3.*
    * pyswip

### Instalando em distribuições baseadas em Debian:
    Para instalar basta executar o arquivo install.sh como sudo ou executar os seguintes comandos:

    # Instalando o SwiProlog
    sudo apt-get install software-properties-common
    sudo apt-add-repository ppa:swi-prolog/stable
    sudo apt-get update
    sudo apt-get install swi-prolog

    # Instalando o Python 3.* e o PIP
    sudo apt-get install python3.6
    sudo apt-get install python3-pip

    #Instalando a biblioteca pyswip
    pip3 install pyswip

    # Para executar o Íris benchmark
    sudo apt-get install default-jre

    # Para executar o wsml engine e íris como serviço
    pip3 install flask