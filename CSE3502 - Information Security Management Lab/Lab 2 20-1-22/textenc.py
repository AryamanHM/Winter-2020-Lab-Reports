
def encrypt(text,s):
	result = ""
	for i in range(len(text)):
		char = text[i]
		if (char.isupper()):
			result += chr((ord(char) + s-65) % 26 + 65)
		else:
			result += chr((ord(char) + s - 97) % 26 + 97)
	return result



text_file = open("C:/Users/aryam/Desktop/Winter Sem 2021-22/CSE3502 - Information Security Management Lab/Lab 2 20-1-21/EncryptText.txt", "r")
text = text_file.read()
text_file.close()
print("Enter value of shifting.")
s = int(input())
print("Text : " + text)
print("Shift : " + str(s))
print("Cipher: " + encrypt(text,s))
