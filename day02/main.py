###############################
##       100DaysOfCode       ##
##       Day02               ##
###############################

# Aventuras Lendárias I: Ilha do castelo fantasma
# For accessibility reasons, this game will be written in my native language.

def win():
	print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
	print("\n\nVocê pegou o tesouro da Rainha Lilith, fonte da riquesa, vida e felicidade eterna!!!\n")

def die():
	print('''
                       ______
                    .-"      "-.            you
                   /            \           die.
       _          |              |          _
      ( \         |,  .-.  .-.  ,|         / )
       > "=._     | )(__/  \__)( |     _.=" <
      (_/"=._"=._ |/     /\     \| _.="_.="\_)
             "=._ (_     ^^     _)"_.="
                 "=\__|IIIIII|__/="
                _.="| \IIIIII/ |"=._
      _     _.="_.="\          /"=._"=._     _
     ( \_.="_.="     `--------`     "=._"=._/ )
      > _.="                            "=._ <
     (_/                                    \_)
''')

print('''
                                   ]=I==II==I=[
                                    \\__||__//                 ]=I==II==I=[
               ]=I==II==I=[          |.. ` *|                   \\__||__//
                \\__||__//           |. /\ #|                    |-_ []#|
                 | []   |            |  ## *|                    |      |
                 |    ..|            | . , #|                  ]=I==II==I=[
 ___   ____  ___ |   .. |         __ |..__.*| __                \\__||__//
 ] I---I  I--I [ |..    |        |  ||_|  |_|| |                 |    _*|
 ]_____________[ | .. []|         \--\-|-|--/-//                 |   _ #|
  \_\| |_| |/_/  |_   _ | _   _   _|      ' *|                   |`    *|
   |  .     |'-'-` '-` '-` '-` '-` | []     #|-|--|-_-_-_-_ _ _ _|_'   #|
   |     '  |=-=-=-=-=-=-=-=-=-=-=-|      []*|-----________` ` `   ]   *|
   |  ` ` []|      _-_-_-_-_  '    |-       #|      ,    ' ```````['  _#|
   | '  `  '|   [] | | | | |  []`  |  []    *|   `          . `   |'  I*|
   |      - |    ` | | | | | `     | ;  '   #|     .  |        '  |    #|
''')

def embora():
	print("+" * 55)
	print("\nO castelo some como poeira no vento...\nVocê nunca saberá quais fortunas lhe aguardavam!")
	print("\n\nFim do jogo.")

print("\nVocê é uma pessoa aventureira que ouviu rumores sobre tesouros em um castelo fantasma\nPor obra de forças sobrenaturais, ou pelo acaso, seu barco encalhou em uma ilha, um castelo misterioso surge à sua frente!")

def subsolo():
	print("\nO subsolo é escuro e úmido, você vê uma tocha")
	tocha = input("\nO que você faz? <pegar> / <deixar>\n").lower()
	if tocha == "pegar":
		print("\n\nVocê anda pelo subsolo, vê muitas coisas velhas, esquelestos, armas... e vê um baú do tesouro no final do subsolo")
		bat = input("\nDois morcegos te atacam, você foge ou ataca? <atacar> / <fugir>\n").lower()
		if bat == "atacar":
			print("\n\nVocê ataca com a tocha, ela se apaga, mas consegue matar os morcegos!")
			tesouro = input("\nO tesouro esta bem a sua frente, você pega ou vai embora? <pegar> / <embora>\n").lower()
			if tesouro == "pegar":
				win()
			elif tesouro == "embora":
				embora()
		else:
			print("\n\nVocê tenta fugir, mas eles te alcançam, seus gritos de agonia chamam mais morcegos!")
			die()
	elif tocha == "deixar":
		print("\nVocê anda pelo subsolo, vê muitas coisas velhas, esquelestos, armas... e vê um baú do tesouro no final do subsolo")
		bat = input("\n\nDois morcegos te atacam, você foge ou ataca? <atacar> / <fugir>\n").lower()
		if bat == "atacar":
			print("\n\nVocê ataca, mas os morcegos te mordem, seus gritos de agonia chamam mais morcegos!\nse ao menos você tivesse uma tocha...")
			die()
		else:
			print("\n\nVocê tenta fugir, mas eles te alcançam, seus gritos de agonia chamam mais morcegos!")
			die()


def game():
	enter = input("\nVocê entra no castelo ou vai embora? <entrar> / <embora>\n").lower()
	if enter == "entrar":
		print("\n\nVecê vê um corredor a sua frente, uma sala escura à esquerda, uma sala iluminada a direita")
		decision1 = input("\nVocê entra na sala a esquerda, direita, ou segue no corredor? <esquerda> / <direita> / <corredor>\n").lower()
		if decision1 == "esquerda":
			print("\n\nVocê encontra uma escada para subsolo.")
			sub = input("\nDescer a escada ou ir embora? <descer> / <embora>\n").lower()
			if sub == "descer":
				subsolo()
			elif sub == "embora":
				embora()
		elif decision1 == "direita":
			print("\nVocê encontra os guardas do castelo, fortemente armados, te matam!")
			die()
		elif decision1 == "corredor":
			print("\nVocê chega ao final do corregor, encontra-se com o rei do castelo, ele te oferece vinho.")
			decision2 = input("\nVocê aceita o vinho? <sim> / <não>\n").lower()
			if decision2 == "sim":
				print("Você acorda no seu barco no meio do mar, com muita dor de cabeça.\nMas ainda com vida...")
				print("\n\nFim de jogo.")
			else:
				print("O rei se ofende com sua recusa, esmaga seu crânio com uma só mão...")
				die()
	elif enter == "embora":
		embora()
	else:
		print("resposta inválida")
		game()

game()
