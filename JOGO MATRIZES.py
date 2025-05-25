from random import randint, choice
from time import sleep

coresniveis = {"amarelo": "\033[33m",
        "roxo": "\033[35m",
        "azul": "\033[34m",
        "magenta": "\033[36m"}

coresrespostas = {"vermelho": "\033[31m",
                  "verde": "\033[32m"}
fim = "\033[0m"
print("=-" * 32)
print("Jogo do CAÇA LETRA".center(64))
print("=-" * 32)
print("Você precisa localizar qual a letra que mais aparece no tabuleiro. "
      "\nA cada nível, o jogo ficará mais difícil."
      "\nSe não houver uma letra única com o maior número de repetições, "
      "\na resposta correta é 0 (ZERO). FIQUE ATENTO!")

nivel = 1
jogardnv = 'S'
while jogardnv == 'S':
    tamanho = nivel + 2
    vidas = 3
    while vidas > 0 and nivel < 6:
        cor = choice(list(coresniveis.values()))
        sleep(1)
        print(f"\n{cor}NIVEL {nivel}\n")
        tela = [[" "] * tamanho for t in range(tamanho)]
        alfabeto = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
                    "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X",
                    "Y", "Z")
        contador = {letra: 0 for letra in alfabeto}
        for x in range(len(tela)):
            for y in range(len(tela[x])):
                letra = alfabeto[randint(0, 25)]
                tela[x][y] = letra
                contador[letra] += 1
                print(letra, end=" ")
            print()
        max_count = max(contador.values())
        maisrepetidas = [letra for letra, count in contador.items() if count == max_count]
        if len(maisrepetidas) > 1:
            respostacerta = "0"
        else:
            respostacerta = maisrepetidas[0]
        resposta = input("\nDigite qual a letra que mais se repetiu: ").upper()
        if resposta == respostacerta:
            print(f"{coresrespostas['verde']}Acertou!!{fim}")
            if nivel == 5:
                sleep(3)
                print(f"\n{coresrespostas['verde']}🎆 PARABÉNS!! Você venceu o jogo e se mostrou um excelente observador.{fim} 🎆")
            nivel += 1
            tamanho += 1
            break
        else:
            vidas -= 1
            if vidas > 0:
                print(f"{coresrespostas['vermelho']}ERROU. A resposta correta era {respostacerta}. Você tem mais {vidas} chance(s). Tente novamente!{fim}")
            else:
                print(f"{coresrespostas['vermelho']}ERROU. A resposta correta era {respostacerta}. Você perdeu!{fim}")
                jogardnv = input("Deseja jogar novamente? Responda S (sim) ou N (Não): ").upper()
                if jogardnv == 'S':
                    nivel = 1
                    print("Reiniciando o jogo...")
                elif jogardnv == 'N':
                    break
                while jogardnv != 'S' and jogardnv != 'N':
                    jogardnv = input("Responda S (sim) ou N (Não): ").upper()