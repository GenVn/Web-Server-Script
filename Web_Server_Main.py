
import os
from web_server import *
def main():
    print('''
 __          __  _        _____                                          _           _____           _       _   
 \ \        / / | |      / ____|                              /\        | |         / ____|         (_)     | |  
  \ \  /\  / /__| |__   | (___   ___ _ ____   _____ _ __     /  \  _   _| |_ ___   | (___   ___ _ __ _ _ __ | |_ 
   \ \/  \/ / _ \ '_ \   \___ \ / _ \ '__\ \ / / _ \ '__|   / /\ \| | | | __/ _ \   \___ \ / __| '__| | '_ \| __|
    \  /\  /  __/ |_) |  ____) |  __/ |   \ V /  __/ |     / ____ \ |_| | || (_) |  ____) | (__| |  | | |_) | |_ 
     \/  \/ \___|_.__/  |_____/ \___|_|    \_/ \___|_|    /_/    \_\__,_|\__\___/  |_____/ \___|_|  |_| .__/ \__|
                                                                                                      | |        
                                                                                                      |_|        
    ''')
    while True:
        optionDomain = int(input("################# Web Server AutoScript #################\n1: Domain Configuration\n2: Choose your domain \n3: Select your web folder \n4: Exit\nEnter option: "))
        if optionDomain == 1:
            os.system("python2 Domain_Main.py")
        elif optionDomain == 2:
            domain = input("Enter domain to config: ")
            mainProcess(domain)
            tempDomain = domain
        elif optionDomain == 3:
            domain = input("Select your web folder directory: ")
            tempDomain = input("Enter your domain: ")
            copyFolder(domain,tempDomain)
        elif optionDomain == 4:
            exit()
main()
