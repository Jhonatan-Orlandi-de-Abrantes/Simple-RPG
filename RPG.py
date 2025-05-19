import os, time as t, random as r

arquivo = 'Info.txt'

def ler_numeros(arquivo):
    with open(arquivo, 'r') as f:
        linhas = [int(linha.strip()) for linha in f.readlines()]
    return linhas[0], linhas[1], linhas[2], linhas[3]

derrotas, slimes, duendes, gigantes = ler_numeros(arquivo)

def atualizar_valores(arquivo, variavel):
    with open(arquivo, 'r') as f:
        linhas = [int(linha.strip()) for linha in f.readlines()]
    if variavel == 'derrotas':
        linhas[0] += 1
    elif variavel == 'slimes':
        linhas[1] += 1
    elif variavel == 'duendes':
        linhas[2] += 1
    elif variavel == 'gigantes':
        linhas[3] += 1
    
    with open(arquivo, 'w') as f:
        f.writelines('\n'.join(map(str, linhas)))
    
    derrotas, slimes, duendes, gigantes = ler_numeros(arquivo)

class Enemy:
    def __init__(self, nome, vida, ataque): 
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
    
    def atacar(self, jogador):
        os.system('cls')
        t.sleep(1.5)
        print('O inimigo escolheu: Atacar!')
        t.sleep(1.5)
        print(f'{jogador.nome} recebe {self.ataque} de dano!')
        jogador.vida -= self.ataque
        if jogador.vida <= 0:
            os.system('cls')
            t.sleep(0.8)
            print('Você foi derrotado!')
            atualizar_valores(arquivo, 'derrotas')
            derrotas, slimes, duendes, gigantes = ler_numeros(arquivo)
            match jogador.habilidade:
                case 'Cavalheiro':
                    jogador.vida = 100
                case 'Mago':
                    jogador.vida = 80
                case 'Titã':
                    jogador.vida = 175
            press_continue()
            menu()
        t.sleep(0.5)
        print(f'Vida restante: {jogador.vida}')

    
    def curar(self):
        os.system('cls')
        t.sleep(0.8)
        print('O inimigo escolheu: Curar!')
        t.sleep(1.5)
        match self.nome:
            case 'Slime':
                self.vida += 10
            case 'Duende':
                self.vida += 25
            case 'Gigante':
                self.vida += 50
        print(f'Vida restante do inimigo: {self.vida}')
        press_continue()

class Player:
    def __init__(self, nome, vida, habilidade):
        self.nome = nome
        self.vida = vida 
        self.habilidade = habilidade
    
    def curar(self):
        os.system('cls')
        t.sleep(0.8)
        print(f'{self.nome} escolheu: Curar.')
        t.sleep(1.5)
        self.vida += 25
        print(f'Vida: {self.vida}')
        press_continue()

    def atacar(self, inimigo):
        os.system('cls')
        t.sleep(0.8)
        print(f'{self.nome} escolheu: Atacar!')
        t.sleep(1.5)
        match self.habilidade:
            case 'Cavalheiro':
                inimigo.vida -= 75
            case 'Mago':
                inimigo.vida -= 25
            case 'Titã':
                inimigo.vida -= 100
        print(f'Vida restante do inimigo: {inimigo.vida}')
        press_continue()

def press_continue():
    t.sleep(0.8)
    print()
    input('Pressione [ENTER] para prosseguir')

def escolha_random(inimigo, jogador):
    chance = r.randint(1, 100)
    if chance > 0:
        inimigo.atacar(jogador)
    else:
        inimigo.curar()

def batalha(jogador, inimigo):
    os.system('cls')
    t.sleep(0.5)
    print('Início da batalha!')
    t.sleep(2)

    while jogador.vida > 0 and inimigo.vida > 0:
        if inimigo.vida <= 0:
            os.system('cls')
            t.sleep(0.8)
            print(f'{jogador.nome} Venceu!')
            match inimigo.nome:
                case 'Slime':
                    atualizar_valores(arquivo, 'slimes')
                case 'Duende':
                    atualizar_valores(arquivo, 'duendes')
                case 'Gigante':
                    atualizar_valores(arquivo, 'gigantes')
            press_continue()
            menu()

        if jogador.vida <= 0:
            os.system('cls')
            t.sleep(0.8)
            print('Você foi derrotado!')
            atualizar_valores(arquivo, 'derrotas')
            derrotas, slimes, duendes, gigantes = ler_numeros(arquivo)
            match jogador.habilidade:
                case 'Cavalheiro':
                    jogador.vida = 100
                case 'Mago':
                    jogador.vida = 80
                case 'Titã':
                    jogador.vida = 175
            press_continue()
            menu()

        print('Sua vez de jogar!')
        t.sleep(1.5)
        escolha = input('''Selecione uma das opções para seguir com a batalha:
[1] Atacar inimigo!
[2] Usar cura (+25)
Escolha: ''')
        match escolha:
            case '1':
                jogador.atacar(inimigo)
            case '2':
                jogador.curar()
            case _:
                print('Digite uma opção válida!')
                press_continue()

        os.system('cls')
        t.sleep(0.8)
        print(f'Vez do {inimigo.nome}!')
        t.sleep(1.5)
        print(f'{inimigo.nome} escolhendo...')
        t.sleep(2)
        escolha_random(inimigo, jogador)

def selecionar_inimigo():
    global inimigo

    os.system('cls')
    t.sleep(0.5)

    inimigo_n = input('''Escolha o inimigo desejado digitando o número relacionado a ele:
[1] Slime
[2] Duende
[3] Gigante
Escolha: ''')
    match inimigo_n:
        case '1':
            inimigo = Enemy('Slime', 50, 10)
        case '2':
            inimigo = Enemy('Duende', 80, 30)
        case '3':
            inimigo = Enemy('Gigante', 150, 65)
        case _:
            print('Digite uma opção válida!')
            press_continue()
            selecionar_inimigo()
    batalha(jogador, inimigo)

def status_jogador():
    os.system('cls')
    t.sleep(0.5)
    derrotas, slimes, duendes, gigantes = ler_numeros(arquivo)
    print(f'Status de [{jogador.nome}]:')
    print(f'Nome: {jogador.nome}')
    print(f'Vida: {jogador.vida}')
    print(f'Habilidade: {jogador.habilidade}')
    print(f'Derrotas: {derrotas}')
    print()
    print('Status de Inimigos:')
    print(f'Slimes Derrotados: {slimes}')
    print(f'Duendes Derrotados: {duendes}')
    print(f'Gigantes Derrotados: {(gigantes)}')
    t.sleep(0.5)
    press_continue()
    menu()

def criar_player():
    global jogador

    hab = 0
    v = 0
    os.system('cls')
    print('Criação do personagem!')
    t.sleep(2)
    n = input('Defina o nome do seu personagem: ')
    h = input('''
Escolha uma das seguintes habilidades digitando o número relacionado a elas:
[1] Cavalheiro
[2] Mago
[3] Titã
Escolha: ''')    
    match h:
        case '1':
            hab = 'Cavalheiro'
        case '2':
            hab = 'Mago'
        case '3':
            hab = 'Titã'
        case _:
            print('Digite uma opção válida!')
            press_continue()
            criar_player()
    match hab:
        case 'Cavalheiro':
            v = 100
        case 'Mago':
            v = 80
        case 'Titã':
            v = 175
    jogador = Player(nome=n, vida=v, habilidade=hab)
    status_jogador()

def menu():
    os.system('cls')
    t.sleep(0.5)

    print('                 [MENU]                  ')
    menu_opt = input('''Escreva os números correspondentes com a opção desejada:
[1] Lutar!
[2] Status do jogo
Escolha: ''')
    
    match menu_opt:
        case '1':
            selecionar_inimigo()
        case '2':
            status_jogador()
        case _:
            print('Digite uma opção válida!')
            press_continue()
            menu()

print('''ATENÇÃO!!! Para que este jogo funcione corretamente é necessário que o arquivo "Info.txt" esteja instalado e no mesmo local que este jogo. Se você não possui o arquivo instale-o no seguinte link:
https://github.com/Jhonatan-Orlandi-de-Abrantes/Simple-RPG''')
press_continue()

criar_player()
