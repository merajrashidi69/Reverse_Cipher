
def rev(message): #reverses messages
	message = message[::-1]
	return message

while True:
	user = input('Enter your message: ')
	message = rev(user)
	print(message)
