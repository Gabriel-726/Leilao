def limpar_terminal():
    print("\033[H\033[J", end="")
#\033[H: Move o cursor para o canto superior esquerdo do terminal.
#\033[J: Limpa a tela a partir da posição atual do cursor.
#end="": Evita uma nova linha extra ao final.

p = "s"
leilao = {}

while p == "s":
    nome = str(input("Escreva seu nome: "))
    val = float(input("Qual a sua aposta? "))    
    
    leilao[nome] = val
    #nome = key  val = value
    
    p = input("Mais alguém irá fazer uma oferta? S/N").lower()
    limpar_terminal()

maior_val = 0

for nome in leilao:
    if leilao[nome] > maior_val: #leilão[acessa a chave nome, que contém o valor da aposta]
        maior_val = leilao[nome]
        vencedor = nome
print(f"{vencedor} é o vencedor do leilão com uma oferta de RS: {maior_val}")