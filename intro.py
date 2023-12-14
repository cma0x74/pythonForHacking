import os
import msvcrt
#from colorama import init, Fore, Back, Style

print('\npra que servem tantos códigos \nse a vida nao eh programada \ne as melhores coisas nao tem logica')

#pause + cls
def limpar():
    os.system('cls')

def main():
    input('press any key to continue... ')
    limpar()

    #init(autoreset = True)

if __name__ == "__main__":
    main()

print('Thanks for using my program! \n')
pet = input('whats your pet name? ')
bcity = input('where do you born? ')
print(f'Your new instagram handle and bio is @cyber{pet} from {bcity}')
