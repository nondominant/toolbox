ubuntu vCPU
create new user
create ssh key and connect

#install docker 
 sudo apt-get update

 sudo apt-get install \
    ca-certificates \
    curl \
    gnupg \
    lsb-release

 curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

 echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt-get update

sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin

#check docker is installed correctly 
 sudo docker run hello-world

#install docker-compose
 sudo apt-get install docker-compose-plugin

 #write a docker-compose.yaml file
 version: '3.3'
services:
  mssql:
    image: mcr.microsoft.com/mssql/server:2019-latest
    user: root
    ports:
      - 1433:1433
    environment:
      - ACCEPT_EULA=Y
      - SA_PASSWORD=Laundrytechsolutions12#
    volumes:
      - ./data:/var/opt/mssql/data

#install mysql default docker image
sudo docker pull mcr.microsoft.com/mssql/server:2019-latest

sudo docker run -e "ACCEPT_EULA=Y" -e "SA_PASSWORD=<YourStrong@Passw0rd>" \
   -p 1433:1433 --name admin_mssql_1 --hostname sql1 \
   -d mcr.microsoft.com/mssql/server:2019-latest

sudo docker ps -a #view containers, omit -a to check it's running

#connect to sql server
sudo docker exec -it admin_mssql_1 "bash"

/opt/mssql-tools/bin/sqlcmd -S localhost -U SA -P "Laundrytechsolutions12#"

#restore from backup
# prompt should look like: ' 1> '
sudo docker exec -it admin_mssql_1 mkdir /var/backups #mkdir if not there

#assume .bak file is on the machine, we need to copy to inside container
sudo docker cp file.bak admin_mssql_1:/var/backups

#list files
sudo docker exec -it admin_mssql_1 /opt/mssql-tools/bin/sqlcmd -S localhost -U SA -P 'Laundrytechsolutions12#' -Q 'RESTORE FILELISTONLY FROM DISK = "/var/backups/backup.bak"' | tr -s ' ' | cut -d ' ' -f 1-2

#specify new paths for all the files in the previous step
sudo docker exec -it admin_mssql_1 /opt/mssql-tools/bin/sqlcmd -S localhost -U SA -P 'Laundrytechsolutions12#' -Q 'RESTORE DATABASE MEXDB FROM DISK = "/var/backups/backup.bak" WITH REPLACE, MOVE "MEXDB" TO "/var/opt/mssql/data/MEXDB.mdf", MOVE "MEXDB_log" TO "/var/opt/mssql/data/MEXDB_log.ldf"'

#verify
sudo docker exec -it admin_mssql_1 /opt/mssql-tools/bin/sqlcmd \
   -S localhost -U SA -P 'Laundrytechsolutions12#' \
   -Q 'SELECT Name FROM sys.Databases'
