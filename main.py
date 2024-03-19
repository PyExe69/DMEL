import pyperclip
import time
import os
from urllib.parse import urlparse
import ctypes

ctypes.windll.kernel32.SetConsoleTitleW("DMEL v1.0")

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

clear()

while True:

    time.sleep(2)

    print("""                                        $$$$$$$\  $$\      $$\ $$$$$$$$\ $$\       
                                        $$  __$$\ $$$\    $$$ |$$  _____|$$ |      
                                        $$ |  $$ |$$$$\  $$$$ |$$ |      $$ |      
                                        $$ |  $$ |$$\$$\$$ $$ |$$$$$\    $$ |      
                                        $$ |  $$ |$$ \$$$  $$ |$$  __|   $$ |      
                                        $$ |  $$ |$$ |\$  /$$ |$$ |      $$ |      
                                        $$$$$$$  |$$ | \_/ $$ |$$$$$$$$\ $$$$$$$$\ 
                                        \_______/ \__|     \__|\________|\________|\n""")

    print("Select metod:\n1 - Server Vanity URL (Without 3 lvl)\n2 - Soon\n3 - Exit\n")
    time.sleep(1)
    select = int(input("Metod: "))

    try:
        if select >= 3 and select <= 0:
            print("Uknown method try again\n")
            time.sleep(2)
            select = int(input("Metod: "))
    except:
        None

    if select == 1:
        print("Example: discord.gg/hTKzmak")
        servlink_full  = input("Enter server link: ")
        servlink = servlink_full.split('discord.gg/')[-1]
    
        time.sleep(1)
    
        print("Example: discord.gg/Roblox")
        newlink_full = input("Enter new link: ")
        newlink = newlink_full.split('discord.gg/')[-1]

        time.sleep(1)

        vanity_new = f"[dіsсоrd.gg/{newlink}](https://discord.gg/{servlink}) ||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​|| discord.gg/{servlink}"
        try:
            pyperclip.copy(vanity_new)
            time.sleep(2)
            print("Successfully copied to clipboard\nCheck clipboard and paste it to discord message")
        except:
            print("Error while copying to clipboard")
        time.sleep(4)
        clear()

    if select == 2:
        print("Comming soon")
        time.sleep(3)
        clear()

    if select == 3:
        exit()
