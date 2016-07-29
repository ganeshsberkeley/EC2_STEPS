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

Directory Structure
-------------------

Once the git hub is cloned you will see the following directories

1.  tweetwordcount -> Directory in which the application is run

2.  SCREENSHOTS -> PNG files of screenshots of the application run

3.  docs -> EX2 documents that explains setup to done for creatng twitter account and application as well as architecture



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

# Storm installation (need to be a root)
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


Steps for Exercice-2
---------------------
pip install psycopg2

pip install tweepy

sudo pip install redis


# This needs to be done only if you want to clone the entire instructor git (otherwise just skip it)
git clone https://github.com/UC-Berkeley-I-School/w205-summer-16-labs-exercises


Steps for running exercise-2
----------------------------
After performing all the SW installation steps, please do the following

cd tweetwordcount

The tweetwordcount has all the source files required for running exercise-2.

Before exectuing the exercise-2, please look at the course PDF for ex2 to setup twitter account and twitter application creation.  A copy of the PDF is available in the doc folder

After setting up the accounts, please so the following in the tweetwordcount folder

1.   Login to postgres first using the following command

psql --username=postgres

2.   Now within postgres do the following to create the tcount database

CREATE USER w205 WITH PASSWORD 'postgres';

DROP DATABASE Tcount;

CREATE DATABASE Tcount;

ALTER DATABASE Tcount OWNER TO w205;

GRANT ALL ON DATABASE Tcount TO w205;

Quit out of posgres using 

\q

3.   Log back in using the following command to create the tweetwordcount table

psql --host=localhost --username=postgres --dbname=tcount


Type the following command to create the table

DROP TABLE IF EXISTS Tweetwordcount ;

CREATE TABLE Tweetwordcount (word TEXT PRIMARY KEY NOT NULL, count INT NOT NULL);


Quit out of postgres by typing

\q


Now that data base and table has been created execute the following command to start capturing streaming data

sparse run 

Wait for a few minutes for the data to captured and written to posgres data base

Press CTRL-C to quit

How to run post-processing Scripts?
-----------------------------------

There are two scripts that can be run to gather some statistics

1.   finalresults.py -> It takes no or 1 input parameter. The process to run it is python finalresults.py or python finalresults.py <variable>

When no parameter is entered, the script will return all the words with there occurances sorted in alphabetical order

If a parameter is entered, the script will return the number of occurances of that particular variable

2.   histogram.py -> It takes no or 1 or 2 input parameters. The process to run it is python histogram.py or python histogram.py k1 or python histogram.py k1 k2

When no parameter is entered, the script will return all the words with there occurances

When k1 is alone entered, the script will return all the words that have a minimum of k1 ocurances

When k1 and k2 are entered, the script will return all the words that have a minimum of k1 ocurances and a maximum of k2 occurances
