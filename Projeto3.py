import random
import time

print('\nBem Vindo ao jogo da forca!\n')
nome = input('Digite seu nome: ')
print(f'Ola {nome}, boa sorte! ')
time.sleep(2)
print('O jogo esta prestes a comecar!\nVamos jogar!')
time.sleep(3)

def main():
    global count
    global display
    global palavra
    global adivinhado
    global comprimento
    global jogar_jogo
    palavras_para_adivinhar = ['boneca', 'piso', 'castelo', 'filme', 'plano', 'azul', 'outra', 'tampo', 'perda', 'vazo']
    palavra = random.choice(palavras_para_adivinhar)
    comprimento = len(palavra)
    count = 0
    display = '_' * comprimento
    adivinhado = []
    jogar_jogo = ""

def loop_jogar():
    global jogar_jogo
    jogar_jogo = input('Voce gostaria de jogar novamente?: S = sim , N = nao \n')
    while jogar_jogo not in ['s', 'S', 'n', 'N']:
        jogar_jogo = input('Voce gostaria de jogar novamente?: S = sim, N = nao \n')
    if jogar_jogo == 's' or 'S':  
        main()
        jogo_forca()
    elif jogar_jogo == 'N' or 'n':
        print('Obrigado por jogar! Nos vemos em breve!')
        exit()         

def jogo_forca():
    global count
    global display
    global palavra
    global adivinhado
    global jogar_jogo
    limite = 5
    guess = input('Esta e a palavra da forca: ' + display + ' Digite seu chute: \n')
    guess = guess.strip().lower()
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= '9':
        print('Digito invalido, tente uma letra!\n')
        jogo_forca()

    elif guess in palavra:
        adivinhado.extend([guess]) 
        index = palavra.find(guess)
        palavra = palavra[:index] + "_" + palavra[index + 1:] 
        display = display[:index] + guess + display[index + 1: ]
        print(display + "\n")

    elif guess in adivinhado:
        print('Tente outra letra.\n')

    else:
        count += 1

        if count == 1:
            time.sleep(1)
            print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")           
            print('Chute errado ' + str(limite - count) + ' chutes restantes\n')

        elif count == 2:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print('Chute errado ' + str(limite - count) + ' chutes restantes\n')

        elif count == 3:
            time.sleep(1)
            print("   _____ \n"
                 "  |     | \n"
                 "  |     |\n"
                 "  |     | \n"
                 "  |      \n"
                 "  |      \n"
                 "  |      \n"
                 "__|__\n")
            print('Chute errado ' + str(limite - count) + ' chutes restantes\n')

        elif count == 4:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print('Chute errado ' + str(limite - count) + ' ultima tentativa\n')

        elif count == 5:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")
            print("Chute errado. FORCA!!!\n")
            print("A palavra era:",adivinhado,palavra) 
            loop_jogar() 

    if palavra == '_' * comprimento:
        print('Parabens! Voce adivinhou a palavra corretamente!') 
        loop_jogar()

    elif count != limite:
        jogo_forca()

main()

jogo_forca()