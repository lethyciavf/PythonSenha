#Projeto Final - Coding Tank 812
import random
lista_cores = ['amarelo', 'verde', 'azul', 'roxo', 'vermelho', 'laranja']
lista_apresentavel = (str(lista_cores)).replace('[','').replace(']','').replace("'","")
x = 0 #controle das tentativas

print('Escolha o nível de dificuldade')
print('F para Fácil com 20 tentativas \nM para Médio com 10 tentativas \nD para Difícil com 5 tentativas')

dificuldade = input('Digite a letra correspondente: ').upper()

while dificuldade not in {'F', 'M', 'D'}: #Tratar para caso não digitem o esperado
    dificuldade = input('Tente novamente com um valor valido: ').upper()

if dificuldade == 'F':
    dificuldade = 20
elif dificuldade == 'M':
    dificuldade = 10
else:
    dificuldade = 5

pinos = {'amarelo':dificuldade,
         'verde':dificuldade,
         'azul':dificuldade,
         'roxo':dificuldade,
         'vermelho':dificuldade,
         'laranja':dificuldade}


print('\nVocê deseja jogar sozinho ou com mais alguém?\nSingleplayer: 1 \nMultiplayer: 2')
jogador = input('Digite a opção desejada:  ')
while jogador not in {'1','2'}:
    jogador = input('Você precisa escolher entre 1 ou 2, tente novamente: ')
    
if jogador == '1':
    senha = random.sample(lista_cores,4) #senha recebe random para gerar a senha caso jogue sozinho

else:
    print('\nVocê deve escolher entre: ', lista_apresentavel)
    print('Lembre-se que a senha será exatamente nessa ordem e não pode ser repetida')

    senha = (input('Entre com a senha, separe as cores usando vírgulas: ').lower().replace(' ','')).split(',')
    print(senha)

    while len(senha) != 4:
        print('Você deve entrar com 4 valores.')
        senha = (input('Tente novamente, separe as cores usando vírgulas: ').lower().replace(' ','')).split(',')

    for i in range(4):
        while senha[i] not in lista_cores or senha.count(senha[i]) > 1:
            print('Use cores válidas e não as repita')
            senha = (input('Tente novamente: ').lower().replace(' ','')).split(',')
        
    
flag = False
print('\n\n################# S E N H A ####################\n')
print('As cores são', lista_apresentavel, '\ne agora você pode começar tentar descobrir a senha: ')
while flag == False: #Roda até que acabe os pinos ou adivinhem a senha
    pino = ['Vazio','Vazio','Vazio','Vazio'] #zera todas as vezes que as tentativas recomeçam
    #chute = []

    chute = (input('\nEntre com o chute, separe as cores usando vírgulas: ').lower().replace(' ','')).split(',')
    while len(chute) != 4:
        print('Você deve entrar com 4 valores.')
        chute = (input('Tente novamente, separe as cores usando vírgulas: ').lower().replace(' ','')).split(',')


    
    for i in range(4):
        while chute[i] not in lista_cores:
            print(chute[i], 'não é um pino disponível')
            chute = (input('Entre com cores válidas, separe as cores usando vírgulas: ').lower().replace(' ','')).split(',')

        if chute[i] in pinos:
            pinos[chute[i]] -= 1

        if pinos[chute[i]] < 0:
            print('Tente novamente', chute[i], 'não é mais um pino disponível.')
            chute = (input('Entre com cores válidas, separe as cores usando vírgulas: ').lower().replace(' ','')).split(',')
        if pinos[chute[i]] <= 0:
            lista_cores.remove(chute[i])
        
        if senha[i]==chute[i]: #cor exata na posição exata
            pino[i]='Branco'
        elif chute[i] in senha:
            pino[i]='Preto' #a cor existe na lista mas não nessa posição
        else:
            pino[i]='Vazio' #Talvez não precise desse else

    print('\n',pino)
    print('Você ainda tem ', dificuldade-x-1, 'jogadas. E os seguintes pinos ainda estão disponíveis:')
    print(pinos)
    x += 1

    if senha == chute:
        flag = True
        print('\nVOCÊ DESCOBRIU A SENHA!!')
    elif x == dificuldade:
        flag = True
        print('\nAcabaram as tentativas')
        print('A senha era: ')
        print(senha)
