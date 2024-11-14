Prerequisites pentru functionarea proiectului:
   1. Python - in general este preinstalat in distributiile noi de Linux
   2. Docker - pentru instalarea Docker trebuie rulata comanda sudo apt install docker
   3. Docker-Compose - pentru instalarea Docker-Compose puteti utiliza comanda sudo apt install docker-compose
   4. Ansible - pentru instalarea Ansible se poate utiliza comanda sudo apt install ansible
   5. Git (optional) daca se doreste clonarea repositorului utilizand comanda git clone https://github.com/Gridean2605/Curs_DevOps/edit/main/DevOps_Project - sudo apt install git

Pentru rularea scripturilor, dupa clonarea repositorului, sa va asigurati ca acesta este executabil utilizand comanda ls -l.
Daca acesta nu este executabil, trebuie rulata comanda chmod +x <nume_script> .

Dupa rularea scripturilor, ar trebui sa rezulte un ouput similar celui de mai jos:
![image](https://github.com/user-attachments/assets/75d5739c-db48-4923-b417-ef7ce150083d)

Pentru rularea celor 2 dockerfile-uri, din directorul fiecarui script, trebuie sa rulam comanda docker build -t dockerfile . (cu tot cu punctul de la final), pentru a crea container-ul de docker si trebuie sa obtinem un output similar celui de mai jos: 
![image](https://github.com/user-attachments/assets/62f829bc-164a-4a44-b324-e6ef090c1fc7)

Pentru a porni containerele, trebuie sa utilizam comanda docker run dockerfile (aceasta comanda va deschide automat container-ul). Daca se doreste ca aceste containere sa ruleze in fundal, fara a deschide containerul la momentul rularii comenzii, putem utiliza comanda docker run -d --name <nume_container> dockerfile din fiecare director. 
Pentru a vizualiza daca acestea ruleaza, folosim comanda docker ps:
![image](https://github.com/user-attachments/assets/a024e659-c99f-4143-95db-778dd588fb9e)

Daca se doreste oprirea celor doua containere, se va utiliza comanda docker stop <id_docker_ps>

Pentru pornirea deployment-ului de docker-compose, mai intai utilizam comanda docker-compose build pentru a construi cele 2 containere:
![image](https://github.com/user-attachments/assets/d7547f0d-be61-4f85-bad4-33951b383a3c)

Daca se doreste oprirea deploymentului, vom utiliza comanda docker-compose down

Iar ulterior rezultatului, rulam comanda docker-compose up (sau docker-compose up -d , in caz ca dorim ca cele 2 containere sa ruleze in background) pentru a porni deploymentul care o sa porneasca cele 2 containere:
![image](https://github.com/user-attachments/assets/11a01a0b-3152-42d8-8753-5dd54ed7c896)

Pentru rularea playbook-ului de Ansible,mai intai trebuie sa modificam informatiile din fisierul hosts, cu informatiile specificate aferente masinii virtuale(IP si username) de pe care se ruleaza. Ulterior trebuie rulata comanda trebuie rulata comanda ansible-playbook -i deploy-playbook.yaml, urmand ca output-ul sa fie similar celui atasat:
![image](https://github.com/user-attachments/assets/fde940bd-0e66-499f-bd3c-28522ad7496b)






