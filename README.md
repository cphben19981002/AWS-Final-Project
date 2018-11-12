# labmonitor_collector

## IAM Setup ##

go to IAM > Users > awsstudent 

In the Permissions setting add new permissions policies call AdministratorAccess 

Then delete other permissions without AdministratorAccess


## Cloud 9 Setup ##

git clone https://github.com/HIN0815/AWS-Final-Project.git  
cd AWS-Final-Project/  
chmod +x *.sh  
./setup.sh  

after that you need to run  
source venv/bin/activate  

then use the  
. ./set_config.sh  
command to set the config, not forget the first "."

next edit the bucket name in deployment.sh line 3  
(sourcebucket=my$STACK_NAME) edit my to your name or id, such as Ben$STACK_NAME  
after that you can run  
./deployment.sh  
to deployment the final project
