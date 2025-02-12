import random

#lista de palavras para jogo
palavras = ['maçã', 'banana,' 'laranja,' 'uva' 'morango']

def jogo_da_forca():
    # Escolhe uma palavra aleatória da lista 
    palavra = random.choice(palavras)
    # Cria uma lista para armazenar as letras corretas 
    letras_corretas = ['_'] * len(palavra)
    # Cria uma lista para armazenar as letras erradas 
    letras_erradas = []
    # Define o número de tentativas 
    tentativas = 6

    print("Bem-vindo ao jogo da forca!")
    print("Vocẽ tem 6 tentativas para adivinhar a palavra")

    while tentativas > 0 and '_' in letras_corretas:
        # Mostra a palavras com letras corretas 
        print(' '.join(letras_corretas))
        # Pede ao usuário para digitar uma letra
        letra = input("Digite uma letra: "). lower()
        # Verifica se a letra é correta 
        if letra in palavra:
            # Substitui as letras corretas na lista 
            for i, l in enumerate(palavras):
                if l == letra:
                    letras_corretas[i] = letra
                else:
                    # Adiciona a letra errada á lista
                    letras_erradas.append(letra)
                    # Diminui o número de tentativas
                    tentativas -= 1
                    print(f"Tentativas restantes: {tentativas}")
                    print(f"Letras erradas: {', '.join(letras_erradas)}")

                # Verifica se o usuário ganhou ou perdeu
                if '_' not in letras_corretas:
                    print("Parabéns! Vocẽ ganhou!")
                else:
                    print(f"Vocẽ perdeu! A palavra era {palavras}.")

# Inicia o jogo
jogo_da_forca()


