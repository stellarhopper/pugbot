How To Run

1.Install the necessary files:
postgresql
postgresql-server
psycopg2 (aptitude install python-psycopg2)

2.Create the database:
su postgres // This command need to be run as root.
psql -c "CREATE USER tf2ib WITH PASSWORD 'jw8s0F4'"
psql -c "CREATE DATABASE tf2ib"
psql tf2ib < database.sql
psql tf2ib < sample.sql // Run this command only if you want to populate your database with testing data.

3.Edit the config.py file and enter in the correct information

4. Run the bot and messengers:
./run.sh pug.py PUG-BOT
./run.sh send.py PUG-MESSENGER
./run.sh send.py PUG-MESSENGER2
(you probably need at least 3 messengers)

Files:
BeautifulSoup.py // Library used to parse HTLM, it's only used on the ESEA bot.
config.py // Configuration file used by some scripts, you will probably set the variable values to what you need.
data.sh // Script that is intended to run as a cron job on a TF2 server. It does copy the stats and STV files to the web server.
database.sql // File used to create the tables for the bot database.
irclib.py // Library used by the different bots to connect and communicate through the IRC protocol.
pug.py // Main bot, I is strongly recommended to analyze the code before doing any modifications.
run.sh // Wrapper script that automatically re-launch the bot when they crash (this will happen). You usually use the script as follow (arguments are optionnals): ./run.sh script.py argument1 argument2
sample.sql // Data for the database, this is mostly for if you need to fill the tables with some testing data.
send.py // Messenger bot, you need at least one running.
SRCDS.py // Library used to send rcon commands and control the TF2 servers.
