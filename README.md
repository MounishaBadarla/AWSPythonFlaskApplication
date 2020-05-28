# Deployment of a Simple Python flask application into Amazon EC2 instance.
This project has 6 basic processes needed to be followed
1. Creating a python flask web application in local
2. Creating an Amazon EC2 instance
3. Generation of a private key using Putty Gen
4. Transfering files from local to linux ubuntu web server
5. Configuring the python flask web application into EC2 instance
6. Code in putty terminal for configuration


## Creating a python flask web application in local

### Steps to install python and sublime
Install python from: https://www.python.org/downloads/release/python-383/
Install sublime or any IDE to run python: http://www.sublimetext.com/

#### Step to check if python is installed in the system:
1. Open command prompt and enter 'python --version'
2. If u get the version name then it means python is installed.

#### Writing python code:
1. Open sublimetext and enter the code in the editor and save it in a file in a specific location.
2. Open command prompt and enter 'pip install flask' to instal flask.
3. Run the saved python code by entering 'python filename.py' in command prompt.
4. A URL is generated which gives the web application in browser.

#### file structure
A python flask application is created and it is arranged in such a way that in the main folder there are two folders and a python file. 
Such that a templates folder is created for html or database files. A static folder is created for css, javascript and other design files. Python file is kept as it is without creating a folder.


## Creating an Amazon EC2 instance

Steps:
1. Open aws management console and if new user its needed to signin to create an account by paying $1.
2. After signin click on launch instance in EC2(it is present in services).
3. Under free tier select "Ubuntu Server 18.04 LTS..... - 64bit" if you are planning to deploy python code using ubuntu linux server.
4. Choose instance type"General purpose - t2.micro(free tier eligible)" and click on configure instance details.
5. Click on Next: Add Storage and Next: Add Tags and Next Configure Security group
6. Click on create a new security group and give the specifications for inbound rules of security group as 
    Inbound rules:
    HTTP (80) - anywhere
    HTTPS (443) - anywhere
    SSH (22) - anywhere
    All traffic anywhere
    Outbound rules: Same as inbound rules 
7. Review and launch security groups then click on launch.
8. For security purpose we need a public key(For storing in aws) and private key(for our storage purpose)
click on create a new key pair and give a name for key pair. Download key pair. A .pem file gets downloaded.
if u already have a key pair then click on choose an existing key pair.
9. Then click on launch.

## Generation of a private key using Putty Gen

1. download puttygen online
2. Open putty gen and under the type of key to generate, choose RSA. If your using an older version choose SSH-2 RSA
3. Choose load and select all files in dropdown. choose the pem file from downloads
4. Click on save private key. .ppk file will be saved in the specified location.

## Transfering files from local to linux ubuntu web server

1. Open putty and under host name give "ubuntu@Public DNS IPV4(we get this from amazon ec2 running instance)" 
2. after giving hostname. Expand SSH in connections given. 
3. Click on Auth in SSH. Browse for private key and upload it.
4. putty terminal gets opened. 

## Configuring the python flask web application into EC2 instance

1. Open putty and under host name give "ubuntu@Public DNS IPV4(we get this from amazon ec2 running instance)" 
2. after giving hostname. Expand SSH in connections given. 
3. Click on Auth in SSH. Browse for private key and upload it.
4. putty terminal gets opened. 

## Code in putty terminal

##### downloads the packages from the repositories and "updates" them to get information on the newest versions of packages and their dependencies.
sudo apt-get update 
#### checking the python version
python3 -V 
#### installing the package manager for python.
sudo apt install python3-pip 
#### package manager is used to install flask
pip3 install flask
#### web server is installed.
sudo apt-get install nginx 
#### python web server gateway interface is getting installed. As we want it for python3.x we are installing gunicorn3
sudo apt-get install gunicorn3 
#### sqlite3 is installed for database
sudo apt-get install sqlite3 
#### flaskApp is the folder name we have dropped in the filezilla ubuntu server. It has all the local code. We are now going into flaskApp folder
cd flaskApp
#### checking the list of fiels in flaskApp folder
ls
#### returning back to the terminal
cd 
#### we are moving into the nginix configuration folder.
cd /etc/nginx/sites-enabled/
#### checking the list of configuration files in nginx
ls
#### By default one file will be there and a new file needs to be created as given below.
#### a new file with the name flaskApp gets opened.
sudo vim flaskApp 
#### code in flaskApp configuration file
    server{
    			listen 80;//port is always 80
    			server_name 3.23.126.52; //this server name is the IPV4 Public IP address for our running EC2 instance 

    			location / {
        			proxy_pass http://127.0.0.1:8000;
    			}
		}
#### inorder to save the file press esc and type :wq and press enter.
#### sudo service nginx restart #start the nginx web server with the configuration file.
#### gives the list with added flaskApp configuration file.
ls 
#### return back to the terminal
cd 
#### move into the flaskApp folder
cd flaskApp/ 
#### command used to run the application. gunicorn is also followed by many commands like bind and etc.
gunicorn3 app:app 
#### Go to browser and enter the IPV4 public IP Address and the application will start running.



