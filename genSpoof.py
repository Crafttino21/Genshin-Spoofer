import os
import time
from loguru import logger
from colorama import Fore, init
import ctypes
import configparser
import subprocess

init(autoreset=True)

banner = '''
 ██████╗ ███████╗███╗   ██╗███████╗██╗  ██╗██╗███╗   ██╗    ███████╗██████╗  ██████╗  ██████╗ ███████╗
██╔════╝ ██╔════╝████╗  ██║██╔════╝██║  ██║██║████╗  ██║    ██╔════╝██╔══██╗██╔═══██╗██╔═══██╗██╔════╝
██║  ███╗█████╗  ██╔██╗ ██║███████╗███████║██║██╔██╗ ██║    ███████╗██████╔╝██║   ██║██║   ██║█████╗  
██║   ██║██╔══╝  ██║╚██╗██║╚════██║██╔══██║██║██║╚██╗██║    ╚════██║██╔═══╝ ██║   ██║██║   ██║██╔══╝  
╚██████╔╝███████╗██║ ╚████║███████║██║  ██║██║██║ ╚████║    ███████║██║     ╚██████╔╝╚██████╔╝██║     
 ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝    ╚══════╝╚═╝      ╚═════╝  ╚═════╝ ╚═╝     
        Genshin Version Spoofer by WeepingAngel | GitHub: https://github.com/Crafttino21                                                                                      
                    Version: 1.1  | Build: 1 (GitHub) | Windows Only
'''

warning_text = '''
██╗    ██╗ █████╗ ██████╗ ███╗   ██╗██╗███╗   ██╗ ██████╗ ██╗
██║    ██║██╔══██╗██╔══██╗████╗  ██║██║████╗  ██║██╔════╝ ██║
██║ █╗ ██║███████║██████╔╝██╔██╗ ██║██║██╔██╗ ██║██║  ███╗██║
██║███╗██║██╔══██║██╔══██╗██║╚██╗██║██║██║╚██╗██║██║   ██║╚═╝
╚███╔███╔╝██║  ██║██║  ██║██║ ╚████║██║██║ ╚████║╚██████╔╝██╗
 ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝
                * WARNING! READ CAREFULL!! *

  I dont take any part if you damage your game or system!
            Use at your own Risk!  

TYPE "I AGREE" in caps to Continue !!
'''
succ = '''
███████╗██╗   ██╗ ██████╗ ██████╗███████╗███████╗███████╗███████╗██╗   ██╗██╗     ██╗  ██╗   ██╗
██╔════╝██║   ██║██╔════╝██╔════╝██╔════╝██╔════╝██╔════╝██╔════╝██║   ██║██║     ██║  ╚██╗ ██╔╝
███████╗██║   ██║██║     ██║     █████╗  ███████╗███████╗█████╗  ██║   ██║██║     ██║   ╚████╔╝ 
╚════██║██║   ██║██║     ██║     ██╔══╝  ╚════██║╚════██║██╔══╝  ██║   ██║██║     ██║    ╚██╔╝  
███████║╚██████╔╝╚██████╗╚██████╗███████╗███████║███████║██║     ╚██████╔╝███████╗███████╗██║   
╚══════╝ ╚═════╝  ╚═════╝ ╚═════╝╚══════╝╚══════╝╚══════╝╚═╝      ╚═════╝ ╚══════╝╚══════╝╚═╝   
                Spoofing Successfully! Thnaks For Using!
                If you wanna Support me, buy me a Coffe :)
                ko-fi | https://ko-fi.com/crafttino21
'''


menu = '''
Choose your version you want to spoof!
[1] Newest (5.6.0)
[2] Fake Dev Build (7.0.0)
[3] Version 4.6.0
[4] Version 4.5.0
[5] Custom Version
=======================================
[6] Supress/Disable Autoupdates (BETA)
'''


class colors:
    red = Fore.LIGHTRED_EX
    magenta = Fore.LIGHTMAGENTA_EX
    green = Fore.LIGHTGREEN_EX


class syscalls:
    @staticmethod
    def Mbox(title, text, style):
        return ctypes.windll.user32.MessageBoxW(0, text, title, style)

    @staticmethod
    def clearConsole():
        os.system("cls")

    @staticmethod
    def changeTitle(title):
        os.system(f"title {title}")


class modules:
    @staticmethod
    def update_game_version(file_path, new_version):
        config = configparser.ConfigParser()
        if not os.path.exists(file_path):
            logger.critical(f"File {file_path} not found!")
            return

        config.read(file_path)

        if 'General' in config and 'game_version' in config['General']:
            config['General']['game_version'] = new_version

            with open(file_path, 'w') as configfile:
                config.write(configfile)
            logger.info("Patching game...")
            time.sleep(3)
            logger.info(f"Game Version Spoofed Succsessfully to {new_version}.")
        else:
            logger.error("Section 'General' or key 'game_version' not found. Try to Update offsets")

    @staticmethod
    def supress_update_patch(file_path):
        config = configparser.ConfigParser()
        if not os.path.exists(file_path):
            logger.error(f"File {file_path} not found!")
            return

        config.read(file_path)

        if 'General' in config and 'channel' in config['General']:
            config['General']['channel'] = '0'  # Wert als String setzen

            with open(file_path, 'w') as configfile:
                config.write(configfile)
            logger.info("Patching Game...")
            time.sleep(3)
            logger.info("Update Supression succsessflly Patched!")
        else:
            logger.critical("Section 'General' or 'channel' not found. Try to update your offsets!")


class version_build:
    @staticmethod
    def spoof_version(version):
        main_installation_directory = input(
            f"{colors.magenta}Please enter the main installation directory (the 'Genshin Impact' folder): ")
        time.sleep(3)
        config_file_path = os.path.join(main_installation_directory, 'Genshin Impact game', 'config.ini')
        modules.update_game_version(config_file_path, version)
        print(colors.green + succ)
        syscalls.Mbox('Genshin Spoofer by WeepingAngel', f'Spoofed successfully to {version}', 64)
        exit()

    @staticmethod
    def supress_update():
        syscalls.Mbox('Genshin Spoofer by WeepingAngel', 'ATTENTION! This is a testing Feature that might be not work!', 48)
        main_installation_directory = input(
            "Please enter the main installation directory (the 'Genshin Impact' folder): ")
        time.sleep(3)
        config_file_path = os.path.join(main_installation_directory, 'Genshin Impact game', 'config.ini')
        modules.supress_update_patch(config_file_path)
        print(colors.green + succ)
        syscalls.Mbox('Genshin Spoofer by WeepingAngel', f'Patched Update Supression Succsessfully!', 64)
        exit()



class warning:
    @staticmethod
    def warning_msg():
        print(colors.red + warning_text)
        xsf = input(" > ")
        if xsf == "I AGREE":
            return True
        else:
            logger.critical("ERROR You didn't accept the Terms of Service!")
            syscalls.Mbox('Genshin Spoofer by WeepingAngel', 'You Dont accept the Terms of Service!', 16)
            exit()


print(colors.magenta + banner)
syscalls.changeTitle('Genshin Spoofer by WeepingAngel')
syscalls.Mbox('Genshin Spoofer by WeepingAngel', 'Thanks for Download! | Version: 1.1', 64)
if not warning.warning_msg():
    exit()
syscalls.Mbox('Genshin Spoofer by WeepingAngel', 'Thanks for Accepting the Terms of Service!', 64)
print(colors.magenta + menu)

version_mapping = {
    "1": "5.6.0",
    "2": "7.0.0",
    "3": "4.6.0",
    "4": "4.5.0",
}

ver = input(" > ")

if ver in version_mapping:
    version_build.spoof_version(version_mapping[ver])
elif ver == "5":
    syscalls.clearConsole()
    custom_version = input("Enter value (only numbers, format: x.x.x) > ")
    syscalls.changeTitle(f'Spoofing to {custom_version} Version')
    version_build.spoof_version(custom_version)
elif ver == "6":
    syscalls.clearConsole()
    syscalls.changeTitle("Disable Updates Genshin Spoofer by WeepingAngel")
    version_build.supress_update()
else:
    logger.error("Invalid selection. Please try again.")
