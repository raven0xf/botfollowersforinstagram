import os
import shutil
import itertools
import argparse
from instabot import Bot

print("""
  _____       ______    _ _               
 |  __ \     |  ____|  | | |              
 | |__) |   _| |__ ___ | | | _____      __
 |  ___/ | | |  __/ _ \| | |/ _ \ \ /\ / /
 | |   | |_| | | | (_) | | | (_) \ V  V / 
 |_|    \__, |_|  \___/|_|_|\___/ \_/\_/  
         __/ |                            
        |___/                             
""")
path = "config"
isdir = os.path.isdir(path)

if isdir == True: 
    try:
        shutil.rmtree(path)
    except OSError as e:
        print("Error: %s - %s." % (e.filename, e.strerror))
else:
    print("Directory %s is non-existent or deleted." % path)


bot = Bot()

def Main():
    global parser 
    global args

    parser = argparse.ArgumentParser(description='Collect username and amount of followers')
    parser.add_argument('-u', '--user', type=str, required=True, help="Target username")
    parser.add_argument('-f', '--followers', type=int, required=True, help='Amount of wanted followers')
    parser.add_argument('-l', '--list', type=str, required=True, help="List of bots")   
    args = parser.parse_args()

def follow(user, followers):
    global read_botlist
    read_botlist = open(args.list, 'r')
    try:
        for line in itertools.islice(read_botlist, 0, followers):
            creds = line.strip().split(",")
            bot.login(username=creds[0], password=creds[1])
            bot.follow(user)
            print("Bot %s successfully followed %s" % (creds[0], user))
    except KeyboardInterrupt:
        print("Quitting; user interrupted with a keyboard shortcut.")
Main()
follow(args.user, args.followers)
