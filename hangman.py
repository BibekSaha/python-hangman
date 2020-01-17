from random_word import RandomWords
import os


def clear_screen():
	'''
	clears out the console
	'''
	os.system("cls") if os.name == "nt" else os.system("clear")


def decode_word(string, word, letter):
	'''
	converts or decodes the encoded word as the user is able to guess correctly
	'''
	if letter in word:
		i = word.find(letter)
		string = string[:i] + word[i] + string[i+1:]
		return string
	return False


def show_word(txt):
	'''
	prints the word with the stars and the decoded characters
	'''
	clear_screen()
	print("Can you guess the word?\n")
	print(txt)
	print()


# driver code
if __name__ == "__main__":
	r = RandomWords()
	word = r.get_random_word(hasDictionaryDef=True, minLength=5)
	word_enc = "*" * len(word)		# encodes the random word with the stars

	show_word(word_enc)				# first call to start the game

	chances = 5
	while True:
		letter = input(f"Enter a character: ({chances} chances left) ")

		# if the user inputs more than one character or blank then tell the user		
		if len(letter) > 1 or letter == "":
			print("\nPlease check again!\n")
			continue

		if letter not in word:
			chances -= 1
		else:
			# change the encoded word to a less encoded one as the user correctly guesses
			word_enc = decode_word(word_enc, word, letter)
			
		show_word(word_enc)

		# if the word is already decode or the chances is over then stop the game
		if word == word_enc or chances == 0:
			print("\nGame Over!!!\n")
			print(f"The word was {word}")
			print("Better luck next time...")
			break
