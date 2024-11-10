#!/bin/bash

#Stabilim numarul de secunde pentru o noua rulare a script-ului
freq=5

#Bucla infinita
while true; do
	#Info OS
	cat /etc/os-release
	echo -e "\n"

	#Ora si data rularii script-ului
	echo -e "Ora si data sistemului: $(date '+%d-%m-%Y %H:%M:%S')\n"
	
	#Info RAM
	echo "RAM:"
       	free -h
	echo -e "\n"

	#Info spatiu disk
	echo "Info disk:"
	df -h
	
	#Fauza de 'freq' secunde
	sleep $freq
done

exit 0;

