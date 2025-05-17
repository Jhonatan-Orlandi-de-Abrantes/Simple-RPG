import os, time as t

class inimigo_c:
    def __init__(self, nome, vida, ataque): 
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
    
    def atacar(self):
        print(f'Vez do {inimigo.nome}!')
        t.sleep(0.5)
        print(f'{jogador.nome} recebe {inimigo.ataque} de dano!')
        jogador.vida -= inimigo.ataque
        t.sleep(0.5)
        print(f'Vida restante: {jogador.vida}')
    
    def curar(self):
        print('O inimigo escolheu: Curar!')
        match inimigo.nome:
            case 'slime':
                ()
            case ():
                ()

        inimigo.vida += ()
        print(f'Vida restante do inimigo: {inimigo.vida}')

def opt_bat():
    global escolha

    os.system('cls')
    t.sleep(0.5)

    escolha = int(input('''Selecione uma das opções para seguir com a batalha:
[1] Atacar inimigo!
[2] Usar cura (+25)

Escolha: '''))

def vez_do_player():
    os.system('cls')
    t.sleep(0.5)

    match escolha:
        case 1:
            player.atacar()
        case 2:
            player.curar()
        case _:
            print('Digite uma opção válida!')
            t.sleep(1)
            selecionar_inimigo()

def batalha():
    os.system('cls')
    t.sleep(0.5)
    
    print('Início da batalha!')
    t.sleep(1)
    
    vez = 'player'
    
    opt_bat()
    
    if vez == 'player':
        opt_bat()
        vez_do_player()

def selecionar_inimigo():
    global inimigo

    os.system('cls')
    t.sleep(0.5)

    inimigo = int(input('''Escolha o inimigo desejado digitando o número relacionado a ele:
[1] Slime
[2] Duende
[3] Gigante

Escolha: '''))

    match inimigo:
        case 1:
            inimigo_n = 'Slime'
            inimigo = inimigo_c(inimigo_n, vida=50, ataque=10)
        case 2:
            inimigo_n = 'Duende'
            inimigo = inimigo_c(inimigo_n, vida=80, ataque=60)
        case 3:
            inimigo_n = 'Gigante'
            inimigo = inimigo_c(inimigo_n, vida=150, ataque=75)
        case _:
            print('Digite uma opção válida!')
            t.sleep(1)
            selecionar_inimigo()
        
    batalha()

class player:
    def __init__(self, nome, vida, habilidade):
        self.nome = nome
        self.vida = vida 
        self.habilidade = habilidade
    
    def curar(self):
        self.vida += 25
        print(f'Vida: {self.vida}')

    def atacar(self):
        match jogador.habilidade:
            case 'Cavalheiro':
                inimigo.vida -= 75
            case 'Mago':
                inimigo.vida -= 25
            case 'Titã':
                inimigo.vida -= 100
        print(f'Vida restante do inimigo: {inimigo.vida}')

def menu():
    os.system('cls')
    t.sleep(0.5)

    print('                 [MENU]                  ')
    t.sleep(0.5)
    print()
    input('Pressione [ENTER] para prosseguir para uma luta!')
    
    selecionar_inimigo()

def status_jogador():
    os.system('cls')
    t.sleep(0.5)
    print(f'Status de [{jogador.nome}]:')
    print(f'Nome: {jogador.nome}')
    print(f'Vida: {jogador.vida}')
    print(f'Habilidade: {jogador.habilidade}')
    t.sleep(0.5)
    print()
    input('Pressione [ENTER] para voltar.')

    menu()

def criar_player():
    global jogador

    os.system('cls')
    t.sleep(0.5)

    print('Criação do personagem!')
    t.sleep(0.5)
    n = input('Defina o nome do seu personagem: ')
    
    h = int(input('''
Escolha uma das seguintes habilidades digitando o número relacionado a elas:
[1] Cavalheiro
[2] Mago
[3] Titã

Escolha: '''))
    if not isinstance(h, int):
        print('O valor precisa ser um número inteiro!')
        t.sleep(1)
        criar_player()
    
    match h:
        case 1:
            hab = 'Cavalheiro'
        case 2:
            hab = 'Mago'
        case 3:
            hab = 'Titã'
        case _:
            print('Digite uma opção válida!')
            t.sleep(1)
            criar_player()
    
    match hab:
        case 'Cavalheiro':
            v = 100
        case 'Mago':
            v = 80
        case 'Titã':
            v = 175

    jogador = player(nome=n, vida=v, habilidade=hab)
    
    status_jogador()

criar_player()
