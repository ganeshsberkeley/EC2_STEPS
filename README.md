# Git hub
In order to clone the repo do the following
In the user account (or create a directory which you created for the project), type the command

git clone https://github.com/ganeshsberkeley/EC2_STEPS

git pull

Also edit the .git/config to change the following line to

url = ssh://git@github.com/ganeshsberkeley/EC2_STEPS

Generate ssh keys
-------------------
ssh-keygen -t rsa -C ganeshsberkeley@github.com

ssh-copy-id ganeshsberkeley@github.com

Copy the keys to the github (logon on to git hub, select the repo, click on settings, click on deploy keys, and add the keys there)


cat ~/.ssh/id_rsa.pub


Process to check in files
-------------------------

Do the following

git status 

	to see what are the files that need to be pushed

git add <file> 

	for all the files that needs to be checked in

git commit -m "Message"

git push -u origin master 

# EC2_STEPS
===============

Steps to Create a new EC2 for labs

fdisk -l

chmod a+rwx /data

wget https://s3.amazonaws.com/ucbdatasciencew205/setup_ucb_complete_plus_postgres.sh

chmod 777 setup_ucb_complete_plus_postgres.sh

./setup_ucb_complete_plus_postgres.sh /dev/xvdf

/root/start-hadoop.sh

/data/start_postgres.sh

su - w205

cd /data

wget https://s3.amazonaws.com/ucbdatasciencew205/setup_spark.sh

bash ./setup_spark.sh

/data/start_metastore.sh

# To start spark-sql
/data/spark15/bin/spark-sql

# To start hive
hive

# Postgress
psql -U postgres

# Strom installation (need to be a root)
storm version

python --version

sudo yum install python27-devel -y

python --version

mv /usr/bin/python /usr/bin/python266

ln -s /usr/bin/python2.7 /usr/bin/python

/usr/bin/python --version

python --version

sudo curl -o ez_setup.py https://bootstrap.pypa.io/ez_setup.py

sudo python ez_setup.py

sudo /usr/bin/easy_install-2.7 pip

sudo pip install virtualenv

wget --directory-prefix=/usr/bin/ https://raw.githubusercontent.com/technomancy/leiningen/stable/bin/lein

ls -l /usr/bin/lein

chmod a+x /usr/bin/lein

ls -l /usr/bin/lein

sudo /usr/bin/lein

lein version

pip install streamparse

sparse quickstart wordcount


Exercice-2
----------
pip install psycopg2
pip install tweepy

sparse quickstart tweetwordcount

git clone https://github.com/UC-Berkeley-I-School/w205-summer-16-labs-exercises
