#!/bin/bash

## Instalador testado em sistemas baseados em debian

if [ "$EUID" -ne 0 ]; then
    echo "Favor executar o script como sudo";
    exit;
fi

install () {
	#if [ -z "$(command -v $1)" ]; then
        if [ -x "$(command -v apt-get)" ]; then
            sudo apt-get -y install $2
        elif [ -x "$(command -v yum)" ]; then
            sudo yum install $3 -y
        elif [ -x "$(command -v dnf)" ]; then
            sudo dnf install $3 -y
        else
            echo "$2 não encontrado, favor instalar";
            exit;
        fi
    #else
    #	echo "$2 já instalado"
    #fi
}

echo 'Instalando...'

install java default-jre default-jre
install python3 python3 python3
install pip3 python3-pip pip3
install swipl swi-prolog pl
pip3 install pyswip
pip3 install flask

echo 'Finalizado...'