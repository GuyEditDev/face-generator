import requests, time, platform, os
from colorama import Fore
def clear():
    if platform.system() == "Windows":
        os.system("cls")
    elif platform.system == "Linux":
        os.system("clear")
def logogr():
    asciiart = Fore.RED+ """
 (                                      )     (                      )  (     
 )\ )   (       (         (          ( /(     )\ )   (      *   ) ( /(  )\ )  
(()/(   )\      )\  (     )\ )   (   )\())(  (()/(   )\   ` )  /( )\())(()/(  
 /(_)|(((_)(  (((_) )\   (()/(   )\ ((_)\ )\  /(_)|(((_)(  ( )(_)|(_)\  /(_)) 
(_))_|)\ _ )\ )\___((_)   /(_))_((_) _((_|(_)(_))  )\ _ )\(_(_())  ((_)(_))   
| |_  (_)_\(_|(/ __| __| (_)) __| __| \| | __| _ \ (_)_\(_)_   _| / _ \| _ \  
| __|  / _ \  | (__| _|    | (_ | _|| .` | _||   /  / _ \   | |  | (_) |   /  
|_|   /_/ \_\  \___|___|    \___|___|_|\_|___|_|_\ /_/ \_\  |_|   \___/|_|_\  
                                                                              
""" + Fore.RESET
    logon = Fore.CYAN + 30*"-" + " by GuyEdit#6899 " + 30*"-"
    coldface = asciiart + "\n" + logon
    return coldface
def create_visage(name):
    url = "https://thispersondoesnotexist.com/image"
    r = requests.get(url, allow_redirects=True)
    open(name, 'wb').write(r.content)
def main():
    logo = logogr()
    clear()
    print(logo)
    much = int(input(Fore.MAGENTA+"[~]  How much for create a randomly visage: "+ Fore.RESET))
    name = input(Fore.MAGENTA+"[~]  Name of file: "+ Fore.RESET)
    i= 0
    clear()
    print(logo)
    for i in range(much):
        i = i + 1
        time.sleep(1)
        nof = str(i) + name + ".png"
        print(Fore.YELLOW+  f"{i}/{much}\n{nof}\n"+ Fore.RESET)
        create_visage(nof)
    print(Fore.GREEN + f"[+] Create of Successfull {much} random face! "+ Fore.RESET)
if __name__ == "__main__":
    main()