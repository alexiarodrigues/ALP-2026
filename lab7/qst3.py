chances = 5
palavra_secreta = 'batata'
while chances > 0:
    palavra = input(f"Qual a palavra secreta? Você tem {chances} chances")
    chances -= 1
    if palavra == 'batata':
        print("VocÃª acertou a palavra, toma aqui uma batata ðŸ¥”")
        break
#O while estava determinando a pergunta as chances da pessoa acertar,se acertar e mesmo assim ainda
#houver chances, o break vai parar a repeticoes. Se errar , o if vai ser ignorado enquanto as chances > 0