![image](https://github.com/user-attachments/assets/a69ecfcc-8c2c-4d98-b39b-8191e3ab43f2)1. **Bash script output**

   ionut@ionut-VirtualBox:~/GIT_Repo/Curs_DevOps/DevOps_Project/bash_script$ ./bash_script.sh
PRETTY_NAME="Ubuntu 24.04 LTS"
NAME="Ubuntu"
VERSION_ID="24.04"
VERSION="24.04 LTS (Noble Numbat)"
VERSION_CODENAME=noble
ID=ubuntu
ID_LIKE=debian
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
UBUNTU_CODENAME=noble
LOGO=ubuntu-logo


Ora si data sistemului: 10-11-2024 23:21:54

RAM:
               total        used        free      shared  buff/cache   available
Mem:           7.8Gi       871Mi       5.7Gi        13Mi       1.5Gi       6.9Gi
Swap:          4.0Gi          0B       4.0Gi


Info disk:
Filesystem      Size  Used Avail Use% Mounted on
tmpfs           795M  1.8M  793M   1% /run
/dev/sda2       100G   21G   74G  22% /
tmpfs           3.9G     0  3.9G   0% /dev/shm
tmpfs           5.0M  8.0K  5.0M   1% /run/lock
tmpfs           795M   92K  795M   1% /run/user/120
tmpfs           795M   80K  795M   1% /run/user/1000
PRETTY_NAME="Ubuntu 24.04 LTS"
NAME="Ubuntu"
VERSION_ID="24.04"
VERSION="24.04 LTS (Noble Numbat)"
VERSION_CODENAME=noble
ID=ubuntu
ID_LIKE=debian
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
UBUNTU_CODENAME=noble
LOGO=ubuntu-logo


Ora si data sistemului: 10-11-2024 23:21:59

RAM:
               total        used        free      shared  buff/cache   available
Mem:           7.8Gi       870Mi       5.7Gi        13Mi       1.5Gi       6.9Gi
Swap:          4.0Gi          0B       4.0Gi


Info disk:
Filesystem      Size  Used Avail Use% Mounted on
tmpfs           795M  1.8M  793M   1% /run
/dev/sda2       100G   21G   74G  22% /
tmpfs           3.9G     0  3.9G   0% /dev/shm
tmpfs           5.0M  8.0K  5.0M   1% /run/lock
tmpfs           795M   92K  795M   1% /run/user/120
tmpfs           795M   80K  795M   1% /run/user/1000


2. **Python script output:**
   ionut@ionut-VirtualBox:~/GIT_Repo/Curs_DevOps/DevOps_Project$ cd python_script/
ionut@ionut-VirtualBox:~/GIT_Repo/Curs_DevOps/DevOps_Project/python_script$ ./python_script.py
Timestamp: 10-11-2024 23:23:53
Operating System: Linux
Distribution: Ubuntu 24.04 LTS
CPU: x86_64
Memory (RAM): Total: 7.76 GB, Used: 0.61 GB, Free: 6.90 GB
Disk Usage: Total: 99.13 GB, Used: 20.09 GB, Available: 73.96 GB


Timestamp: 10-11-2024 23:23:58
Operating System: Linux
Distribution: Ubuntu 24.04 LTS
CPU: x86_64
Memory (RAM): Total: 7.76 GB, Used: 0.61 GB, Free: 6.90 GB
Disk Usage: Total: 99.13 GB, Used: 20.09 GB, Available: 73.96 GB


3. **Rezultat build dockerfile bash script:**
   ionut@ionut-VirtualBox:~/GIT_Repo/Curs_DevOps/DevOps_Project/bash_script$ docker build -t dockerfile .
[+] Building 1.6s (10/10) FINISHED                                                                                                                                            docker:default
 => [internal] load build definition from dockerfile                                                                                                                                    0.1s
 => => transferring dockerfile: 408B                                                                                                                                                    0.0s
 => [internal] load metadata for docker.io/library/ubuntu:latest                                                                                                                        1.2s
 => [auth] library/ubuntu:pull token for registry-1.docker.io                                                                                                                           0.0s
 => [internal] load .dockerignore                                                                                                                                                       0.0s
 => => transferring context: 2B                                                                                                                                                         0.0s
 => [1/4] FROM docker.io/library/ubuntu:latest@sha256:99c35190e22d294cdace2783ac55effc69d32896daaa265f0bbedbcde4fbe3e5                                                                  0.0s
 => [internal] load build context                                                                                                                                                       0.0s
 => => transferring context: 36B                                                                                                                                                        0.0s
 => CACHED [2/4] RUN apt-get update &&     apt-get install -y     bash     procps     coreutils                                                                                         0.0s
 => CACHED [3/4] COPY bash_script.sh /usr/local/bin/bash_script.sh                                                                                                                      0.0s
 => CACHED [4/4] RUN chmod +x /usr/local/bin/bash_script.sh                                                                                                                             0.0s
 => exporting to image                                                                                                                                                                  0.0s
 => => exporting layers                                                                                                                                                                 0.0s
 => => writing image sha256:0d704b4674e05f1d9df198b56ab4921386c55ee86cacf6738002dcf878836354                                                                                            0.0s
 => => naming to docker.io/library/dockerfile

4. **Rezultat build dockerfile python script:**
   ionut@ionut-VirtualBox:~/GIT_Repo/Curs_DevOps/DevOps_Project/python_script$ docker build -t dockerfile .
[+] Building 0.4s (9/9) FINISHED                                                                                                                                              docker:default
 => [internal] load build definition from dockerfile                                                                                                                                    0.0s
 => => transferring dockerfile: 566B                                                                                                                                                    0.0s
 => [internal] load metadata for docker.io/library/python:3.10-slim                                                                                                                     0.0s
 => [internal] load .dockerignore                                                                                                                                                       0.0s
 => => transferring context: 2B                                                                                                                                                         0.0s
 => [1/4] FROM docker.io/library/python:3.10-slim                                                                                                                                       0.0s
 => [internal] load build context                                                                                                                                                       0.0s
 => => transferring context: 38B                                                                                                                                                        0.0s
 => CACHED [2/4] RUN pip install --upgrade pip &&     pip install psutil                                                                                                                0.0s
 => CACHED [3/4] COPY python_script.py /usr/local/bin/python_script.py                                                                                                                  0.0s
 => CACHED [4/4] RUN chmod +x /usr/local/bin/python_script.py                                                                                                                           0.0s
 => exporting to image                                                                                                                                                                  0.0s
 => => exporting layers                                                                                                                                                                 0.0s
 => => writing image sha256:ea73c9538efb420e8eaa37832734f2dbec7b7dba3c53cac5ef199a7704c5ca44                                                                                            0.0s
 => => naming to docker.io/library/dockerfile

5. **Output docker logs container python:**
   ionut@ionut-VirtualBox:~/GIT_Repo/Curs_DevOps/DevOps_Project/bash_script$ docker ps
CONTAINER ID   IMAGE                              COMMAND                  CREATED          STATUS          PORTS     NAMES
dcea9c26b57d   ansible-deployment_bash-script     "/usr/local/bin/bash…"   28 minutes ago   Up 14 minutes             dcea9c26b57d_bash_script_container
c9ed1f75cdc5   ansible-deployment_python-script   "python3 /usr/local/…"   28 minutes ago   Up 14 minutes             c9ed1f75cdc5_python-script-container


ionut@ionut-VirtualBox:~/GIT_Repo/Curs_DevOps/DevOps_Project/bash_script$ docker logs --since 5m c9ed1f75cdc5
Distribution: Debian GNU/Linux 12 (bookworm)
CPU: N/A
Memory (RAM): Total: 7.76 GB, Used: 0.60 GB, Free: 6.90 GB
Disk Usage: Total: 99.13 GB, Used: 20.09 GB, Available: 73.96 GB


Timestamp: 10-11-2024 21:27:02
Operating System: Linux
Distribution: Debian GNU/Linux 12 (bookworm)
CPU: N/A
Memory (RAM): Total: 7.76 GB, Used: 0.60 GB, Free: 6.90 GB
Disk Usage: Total: 99.13 GB, Used: 20.09 GB, Available: 73.96 GB

6. **Output docker logs container bash:**
   ionut@ionut-VirtualBox:~/GIT_Repo/Curs_DevOps/DevOps_Project/bash_script$ docker ps
CONTAINER ID   IMAGE                              COMMAND                  CREATED          STATUS          PORTS     NAMES
dcea9c26b57d   ansible-deployment_bash-script     "/usr/local/bin/bash…"   30 minutes ago   Up 16 minutes             dcea9c26b57d_bash_script_container
c9ed1f75cdc5   ansible-deployment_python-script   "python3 /usr/local/…"   30 minutes ago   Up 16 minutes             c9ed1f75cdc5_python-script-container
ionut@ionut-VirtualBox:~/GIT_Repo/Curs_DevOps/DevOps_Project/bash_script$ docker logs --since 3m dcea9c26b57d
PRETTY_NAME="Ubuntu 24.04.1 LTS"
NAME="Ubuntu"
VERSION_ID="24.04"
VERSION="24.04.1 LTS (Noble Numbat)"
VERSION_CODENAME=noble
ID=ubuntu
ID_LIKE=debian
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
UBUNTU_CODENAME=noble
LOGO=ubuntu-logo


Ora si data sistemului: 10-11-2024 21:32:10

RAM:
               total        used        free      shared  buff/cache   available
Mem:           7.8Gi       872Mi       5.7Gi        13Mi       1.5Gi       6.9Gi
Swap:          4.0Gi          0B       4.0Gi


Info disk:
Filesystem      Size  Used Avail Use% Mounted on
overlay         100G   21G   74G  22% /
tmpfs            64M     0   64M   0% /dev
shm              64M     0   64M   0% /dev/shm
/dev/sda2       100G   21G   74G  22% /bash_script
tmpfs           3.9G     0  3.9G   0% /proc/asound
tmpfs           3.9G     0  3.9G   0% /proc/acpi
tmpfs           3.9G     0  3.9G   0% /proc/scsi
tmpfs           3.9G     0  3.9G   0% /sys/firmware
tmpfs           3.9G     0  3.9G   0% /sys/devices/virtual/powercap
PRETTY_NAME="Ubuntu 24.04.1 LTS"
NAME="Ubuntu"
VERSION_ID="24.04"
VERSION="24.04.1 LTS (Noble Numbat)"
VERSION_CODENAME=noble
ID=ubuntu
ID_LIKE=debian
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
UBUNTU_CODENAME=noble
LOGO=ubuntu-logo


Ora si data sistemului: 10-11-2024 21:32:15

RAM:
               total        used        free      shared  buff/cache   available
Mem:           7.8Gi       872Mi       5.7Gi        13Mi       1.5Gi       6.9Gi
Swap:          4.0Gi          0B       4.0Gi


Info disk:
Filesystem      Size  Used Avail Use% Mounted on
overlay         100G   21G   74G  22% /
tmpfs            64M     0   64M   0% /dev
shm              64M     0   64M   0% /dev/shm
/dev/sda2       100G   21G   74G  22% /bash_script
tmpfs           3.9G     0  3.9G   0% /proc/asound
tmpfs           3.9G     0  3.9G   0% /proc/acpi
tmpfs           3.9G     0  3.9G   0% /proc/scsi
tmpfs           3.9G     0  3.9G   0% /sys/firmware
tmpfs           3.9G     0  3.9G   0% /sys/devices/virtual/powercap

7. **Output docker-compose:**
ionut@ionut-VirtualBox:~/GIT_Repo/Curs_DevOps/DevOps_Project/python_script$ docker-compose build
Building bash-script
[+] Building 1.3s (10/10) FINISHED                                                                                                                                            docker:default
 => [internal] load build definition from dockerfile                                                                                                                                    0.1s
 => => transferring dockerfile: 408B                                                                                                                                                    0.0s
 => [internal] load metadata for docker.io/library/ubuntu:latest                                                                                                                        1.0s
 => [auth] library/ubuntu:pull token for registry-1.docker.io                                                                                                                           0.0s
 => [internal] load .dockerignore                                                                                                                                                       0.0s
 => => transferring context: 2B                                                                                                                                                         0.0s
 => [1/4] FROM docker.io/library/ubuntu:latest@sha256:99c35190e22d294cdace2783ac55effc69d32896daaa265f0bbedbcde4fbe3e5                                                                  0.0s
 => [internal] load build context                                                                                                                                                       0.0s
 => => transferring context: 36B                                                                                                                                                        0.0s
 => CACHED [2/4] RUN apt-get update &&     apt-get install -y     bash     procps     coreutils                                                                                         0.0s
 => CACHED [3/4] COPY bash_script.sh /usr/local/bin/bash_script.sh                                                                                                                      0.0s
 => CACHED [4/4] RUN chmod +x /usr/local/bin/bash_script.sh                                                                                                                             0.0s
 => exporting to image                                                                                                                                                                  0.0s
 => => exporting layers                                                                                                                                                                 0.0s
 => => writing image sha256:0d704b4674e05f1d9df198b56ab4921386c55ee86cacf6738002dcf878836354                                                                                            0.0s
 => => naming to docker.io/library/devops_project_bash-script                                                                                                                           0.0s
Building python-script
[+] Building 0.4s (9/9) FINISHED                                                                                                                                              docker:default
 => [internal] load build definition from dockerfile                                                                                                                                    0.1s
 => => transferring dockerfile: 566B                                                                                                                                                    0.0s
 => [internal] load metadata for docker.io/library/python:3.10-slim                                                                                                                     0.0s
 => [internal] load .dockerignore                                                                                                                                                       0.0s
 => => transferring context: 2B                                                                                                                                                         0.0s
 => [1/4] FROM docker.io/library/python:3.10-slim                                                                                                                                       0.0s
 => [internal] load build context                                                                                                                                                       0.0s
 => => transferring context: 38B                                                                                                                                                        0.0s
 => CACHED [2/4] RUN pip install --upgrade pip &&     pip install psutil                                                                                                                0.0s
 => CACHED [3/4] COPY python_script.py /usr/local/bin/python_script.py                                                                                                                  0.0s
 => CACHED [4/4] RUN chmod +x /usr/local/bin/python_script.py                                                                                                                           0.0s
 => exporting to image                                                                                                                                                                  0.0s
 => => exporting layers                                                                                                                                                                 0.0s
 => => writing image sha256:ea73c9538efb420e8eaa37832734f2dbec7b7dba3c53cac5ef199a7704c5ca44                                                                                            0.0s
 => => naming to docker.io/library/devops_project_python-script  
   
ionut@ionut-VirtualBox:~/GIT_Repo/Curs_DevOps/DevOps_Project$ docker-compose up
Creating network "devops_project_default" with the default driver
Creating python-script-container ... done
Creating bash_script_container   ... done
Attaching to bash_script_container, python-script-container

8. **Ansible playbook output:**
   ionut@ionut-VirtualBox:~/GIT_Repo/Curs_DevOps/DevOps_Project$ ansible-playbook deploy-playbook.yaml --ask-become-pass
BECOME password:
[WARNING]: No inventory was parsed, only implicit localhost is available
[WARNING]: provided hosts list is empty, only localhost is available. Note that the implicit localhost does not match 'all'

PLAY [Deploy Docker Compose services] *******************************************************************************************************************************************************

TASK [Gathering Facts] **********************************************************************************************************************************************************************
ok: [localhost]

TASK [Create deployment directory] **********************************************************************************************************************************************************
changed: [localhost]

TASK [Create deployment directory] **********************************************************************************************************************************************************
changed: [localhost]

TASK [Create bash directory] ****************************************************************************************************************************************************************
changed: [localhost]

TASK [Copy bash script and Dockerfile] ******************************************************************************************************************************************************
changed: [localhost] => (item=bash_script/bash_script.sh)
changed: [localhost] => (item=bash_script/dockerfile)

TASK [Copy python script and Dockerfile] ****************************************************************************************************************************************************
changed: [localhost] => (item=python_script/python_script.py)
changed: [localhost] => (item=python_script/dockerfile)

TASK [Copy docker-compose.yaml] *************************************************************************************************************************************************************
changed: [localhost]

TASK [Run docker-compose up to deploy services] *********************************************************************************************************************************************
changed: [localhost]

PLAY RECAP **********************************************************************************************************************************************************************************
localhost                  : ok=8    changed=7    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0


