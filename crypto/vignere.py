#!/bin/python3

# Accepted alphabet is [a-zA-Z] and [:space:]

# Hardcode for ASCII

b1 = 96 # 96 is int for b'1100000'
b2 = 31 # 31 is int for b'0011111'

def decrypt():
    print("Please insert your encrypted message")
    crypt = input()

    print("Please insert your KEY")
    key = input()

    ans = ""
    for i in range(len(crypt)):
        if crypt[i] == ' ':
            ans=ans+" "
        else:
            ans = chr()
    print("Decrypted message:")
    print(ans)


def encrypt():
    print("Please insert the message you wish you encrypt")
    messg = [ord(x) for x in input()]

    print("Please insert your KEY")
    key = [ord(x) for x in input()]

    ans = ""
    j = 0
    for i in range(len(messg)):
        if messg[i] == ord(' '):
            ans += " "
        else:
            off = ((messg[i]&b2)+(key[j%len(key)]&b2)-1)%26
            ans += chr(messg[i]&96|((messg[i]&b2)+(key[j%len(key)]&b2)-1)%26)
            j += 1

    print("Encrypted message:")
    print(ans)

def main():
	print ("** Vigenere Cipher **")
	print ("1 - Encrypt\n2 - Decrypt")
	option = int(input("Choose option: \n"))
	if (option==1):
		encrypt()
	elif(option == 2):
		decrypt()

main()
