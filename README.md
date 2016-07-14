# Git hub
In order to clone the repo do the following
1.  In the user account (or create a directory which you created for the project), type the command
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

# EC2_STEPS

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

# TO start spark-sql
/data/spark15/bin/spark-sql

# To start hive
hive
