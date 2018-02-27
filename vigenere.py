
def decrypt():
    print("Please insert your encrypted message")
    crypt=input()

    print("Please insert your KEY")
    key=input()

    ans=""
    for i in range(len(crypt)):
        if crypt[i]==' ':
            ans=ans+" "
        else:
            if ord(crypt[i])>=ord('a'):
                shift=ord(key[i])-ord('a')
                if ord(crypt[i])<ord(key[i]):
                    ans=ans+chr(ord(crypt[i])+26-shift)
                else:
                    ans=ans+chr(ord('a')+ord(crypt[i])-ord(key[i]))
            else:
                shift=ord(key[i])-ord('A')
                if ord(crypt[i])<ord(key[i]):
                    ans=ans+chr(ord(crypt[i])-shift+26)
                else:
                    ans=ans+chr(ord('A')+ord(crypt[i])-ord(key[i]))
    print("Decrypted message:")
    print(ans)


def encrypt():
    print("Please insert the message you wish you encrypt")
    messg=input()

    print("Please insert your KEY")
    key=input()

    ans=""
    for i in range(len(messg)):
        if messg[i]==' ':
            ans=ans+" "
        else:
            if ord(messg[i])>=ord('a'):
                shift=ord(key[i])-ord('a')
                if ord('z')-ord(messg[i])>shift:
                    ans=ans+chr(ord(messg[i])+shift)
                else:
                    ans=ans+chr(ord(messg[i])+shift-26)
            else:
                shift=ord(key[i])-ord('A')
                if ord('Z')-ord(messg[i])>shift:
                    ans=ans+chr(ord(messg[i])+shift)
                else:
                    ans=ans+chr(ord(messg[i])+shift-26)


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
