#!/usr/bin/python

import config
import irclib
import psycopg2
import sys
import time

#irclib.DEBUG = 1

def checkConnection():
    global connectTimer
    if not server.is_connected():
        connect()
    server.join(config.channel)

def connect():
    print [config.network, config.port, nick, name]
    server.connect(config.network, config.port, nick, ircname = name)

def welcome(connection, event):
    print nick + ' welcome seen, will auth!'
    server.send_raw("AUTH " + nick + " " + passwd)
    server.send_raw("MODE " + nick + " +x")
    server.join(config.channel)

nick = 'Pug-Messenger'
if len(sys.argv) == 2:
    nick = sys.argv[1]

passwd = config.irc_auths[nick]
print [nick, passwd]

# Create an IRC object
name = 'BOT'
irc = irclib.IRC()

# Create a server object, connect and join the channel
server = irc.server()
connect()
irc.add_global_handler('welcome', welcome)

database = psycopg2.connect('dbname=tf2ib host=localhost user=tf2ib password=' + config.databasePassword)
cursor = database.cursor()
minuteTimer = time.time()

while 1:
    cursor.execute('BEGIN;')
    cursor.execute('LOCK TABLE messages;')
    cursor.execute('SELECT * FROM messages LIMIT 1;')
    for row in cursor.fetchall():
        print row
        print time.time()
        cursor.execute('DELETE FROM messages WHERE id = %s', (row[0],))
        server.send_raw(row[1])
    cursor.execute('COMMIT;')
    irc.process_once(0.2)
    if time.time() - minuteTimer > 60:
        minuteTimer = time.time()
        checkConnection()
