# guessinggame

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
