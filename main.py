# -*- coding: UTF-8 -*-

'''
This is a public domain - probably non-bug-free - "guess the number" game, dedicated to Edoardo, Benedetta, Viola, Annalice and all the little ones
who will smile playing it.

This software runs on python 2 (and probably 3) and requires emoji support:

$ pip install emoji --upgrade

run the game by typing:

$ python main.py

#TODO:

- Sanitize user input so that the program does not break when the user inputs a string instead of an int
- Not sure why the program breaks when accent letters (è à ù) are used, despite the shebang (probably that's an issue in Python 2 only)

by Johnny Costantini, Pesaro, Italy. April 2019

'''


import random
import emoji

nome_giocatore = raw_input("Come ti chiami? ")
print(emoji.emojize("Ciao " + nome_giocatore + "!! :smile: . Io sono un :computer: ed il mio nome e' HAL!", use_aliases=True))

numero_da_indovinare = random.randrange(1,10)

numero_tentativi=3

# DEBUG ONLY print(numero_da_indovinare)

while True:

	numero_indovinato = int(raw_input(nome_giocatore + " dimmi che numero ho pensato tra 1 e 9! : "))
	

	if numero_indovinato == numero_da_indovinare:
		print(emoji.emojize("Fantastico " + nome_giocatore + ", hai indovinato!  :heart_eyes: :candy: :thumbs_up: :heart_eyes: :thumbs_up:", use_aliases=True))
		giochi_ancora = raw_input("### Vuoi giocare ancora ? si o no ? ")
		if giochi_ancora == "si":
			numero_da_indovinare = random.randrange(1,9)
			numero_tentativi = 3
		else:
			print(emoji.emojize(":wave: :wave: :wave:  :kissing_heart:", use_aliases=True))
			break

	elif numero_indovinato < numero_da_indovinare and numero_tentativi > 1:
		numero_tentativi -= 1
		print(emoji.emojize(" :grimacing: Peccato, "  + nome_giocatore + " non e' giusto, il numero da indovinare e' piu' grande, riprova! Ti rimangono " + str(numero_tentativi) + " tentativi! :stuck_out_tongue_winking_eye: ", use_aliases=True))
		
		

	elif numero_indovinato > numero_da_indovinare and numero_tentativi > 1:
		numero_tentativi -= 1
		print(emoji.emojize("  :stuck_out_tongue_winking_eye: Peccato, "  + nome_giocatore + " non e' giusto, il numero da indovinare e' piu' piccolo, riprova! Ti rimangono " + str(numero_tentativi) + " tentativi! :grimacing: ", use_aliases=True))

	else:
		print(emoji.emojize(" :relieved: " + nome_giocatore + ", il numero da indovinare era " + str(numero_da_indovinare) + " !" + " Non hai piu' tentativi, ciao ciao! :kissing_heart:", use_aliases=True)) 
		giochi_ancora = raw_input("# # # Vuoi giocare ancora? si o no ? ")
		if giochi_ancora == "si":
			numero_da_indovinare = random.randrange(1,9)
			numero_tentativi = 3
		else:
			print(emoji.emojize(":wave: :wave: :wave:  :kissing_heart:", use_aliases=True))
			break




