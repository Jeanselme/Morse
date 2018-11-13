"""
	Simple code for translating in morse
"""

morse_dict = {		'A':'.-',		'B':'-...',	
	'C':'-.-.',		'D':'-..',		'E':'.',	
	'F':'..-.',		'G':'--.',		'H':'....',	
	'I':'..',		'J':'.---',		'K':'-.-',	
	'L':'.-..',		'M':'--',		'N':'-.',	
	'O':'---',		'P':'.--.',		'Q':'--.-',	
	'R':'.-.',		'S':'...',		'T':'-',	
	'U':'..-',		'V':'...-',		'W':'.--',	
	'X':'-..-',		'Y':'-.--',		'Z':'--..',	

	'0':'-----',	'1':'.----',	'2':'..---',	
	'3':'...--',	'4':'....-',	'5':'.....',	
	'6':'-....',	'7':'--...',	'8':'---..',	
	'9':'----.',	

	',':'--..--',	'.':'.-.-.-',	'?':'..--..',	
	'/':'-..-.',	'-':'-....-',	'(':'-.--.',	
	')':'-.--.-',	' ':' '} 

reverse_morse = {morse: letter for letter, morse in morse_dict.items()}

def encrypt(message):
	"""
		Translates message in morse
		
		Arguments:
			message {str} -- Message 

		Returns:
			str -- Morse message
	"""
	morse_message = []
	for letter in message.upper():
		try:
			morse_message.append(morse_dict[letter])
		except:
			print('Letter "{}" unknown in morse'.format(letter))
	return ' '.join(morse_message)

def decrypt(morse_message):	
	"""
		From morse to message
		
		Arguments:
			message {str} -- Message 

		Returns:
			str -- Latin message
	"""
	message = []
	words = morse_message.split('  ')
	for word in words:
		symbols = word.split(' ')
		translation = []
		for symbol in symbols:
			if symbol != '':
				try:
					translation.append(reverse_morse[symbol])
				except:
					print('Symbol "{}" unknown in morse'.format(symbol))
		message.append(''.join(translation))
	return ' '.join(message)