print("+-"*10," JOGUINHO DOS NÚMEROS ","+-"*10)
print('')
print("\033[1;36mTente adivinhar qual número eu joguei!\033[m \033[36mEntre 0 à 10.\033[m")
print('='*55)
from time import sleep
import random
n= random.randint(0,10)
tot = 0
n1 = 0
print('')
while n1 != n:
    n1=int(input("Digite um número entre 0 à 10: "))
    tot += 1
    print('')
    print("\033[33mVerificando...\033[m")
    sleep(1)
    print("-"*35)
    if n1 < n:
        print("\033[31mMais... Tente novamente!\033[m")
        sleep(0.7)
    elif n1 > n:
        print("\033[31mMenos... Tente novamente!\033[m")
        sleep(0.7)
print('-'*45)
print("\033[32mFinalmente! Você acertou!\033[m")
if tot == 1:
    print("Foi necessário apenas \033[34m1 palpite\033[m para acertar!")
else:
    print("Foram necessários \033[34m{} palpites\033[m para você acertar.".format(tot))