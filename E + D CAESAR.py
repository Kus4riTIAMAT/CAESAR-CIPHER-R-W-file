import string

def enkripsi():
    
    print('RUNNING ENCRYPT PROGRAM...')
    print('1. Encrypt from ASCII')
    print('2. Encrypt from plaintext')
    choise = input('CHOOSE YOUR METHOD : ')
    
    
    if choise == '1':
        Message = input('Input your ASCII: ')
        decodedmessage = ""
        for item in Message.split():
            decodedmessage += chr(int(item))
        plaintext = decodedmessage  
        
        
               
        def encrypt(text,key):
            result = ''
            for i in range(len(text)):
                char = text[i] 
                if (char.isupper()):
                    result += chr((ord(char) + key - 65) % 26 + 65)
                elif(char.isnumeric()):
                    result += chr((ord(char) + key - 48) % 10 + 48)
                elif (char.islower()):
                    result += chr((ord(char) + key - 97) % 26 + 97)
                elif (ord(char)) >= 32 and ord(char) <= 47:
                    result += chr((ord(char) + key - 32) % 15 + 32) #contoh menggunakan lebih dan kurang
                else:
                    result += chr((ord(char) + key - 48) % 10 + 48)
            return result
        
        
        
        text = plaintext
        s = int(input('ENTER YOUR SHIFT PATTERN : '))
        print ('Your ASCII CODE IS : ' + decodedmessage)
        print ("Shift pattern : " + str(s))
        print ("Cipher: " + encrypt(text,s))
        for key in range(26):
                hasil = ('using key: ' + str(key) , str(encrypt(plaintext, key)))
                print(hasil)
        convert = input('conver to ASCII? (y/n) ')
        if convert == 'y':
            value = encrypt(text,s)
            list=[ord(ch) for ch in value]
            ascii= ''.join(str(list).split(','))
            print(ascii)
        else:
            print('thanks!')
            
            
            
        lanjut = input('Repeat the program?(y/n)... : ')        
        if lanjut == 'y':
                welcome()
        else:
            print('Terimakasih!')
    elif choise == '2' :
        plaintext = input("INPUT YOUR MESSAGE : ")
        
        
        
        def encrypt(text,key):
            result = ''
            for i in range(len(text)):
                char = text[i] 
                if (char.isupper()):
                    result += chr((ord(char) + key - 65) % 26 + 65)
                elif(char.isnumeric()):
                    result += chr((ord(char) + key - 48) % 10 + 48)
                elif (char.islower()):
                    result += chr((ord(char) + key - 97) % 26 + 97)
                elif (ord(char)) >= 32 and ord(char) <= 47:
                    result += chr((ord(char) + key - 32) % 15 + 32) #contoh menggunakan lebih dan kurang
                else:
                    result += chr((ord(char) + key - 32) % 1 + 32)
            return result
        
        
        text = plaintext
        s = int(input("ENTER YOUR SHIFT PATTERN : "))
        print ("Shift pattern : " + str(s))
        print ("Cipher: " + encrypt(text,s))
        for key in range(26):
                hasil = ('using key: ' + str(key) , str(encrypt(plaintext, key)))
                print(hasil)
        convert = input('conver to ASCII? (y/n) ')
        if convert == 'y':
            value = encrypt(text,s)
            list=[ord(ch) for ch in value]
            ascii= ''.join(str(list).split(','))
            print(ascii)
        else:
            print('thanks!')    
            
            
            
        lanjut = input('Repeat the program?(y/n)... : ')                
        if lanjut == 'y':
                welcome()
        else:
            print('Terimakasih!')
def dekripsi():
    print('1. Decrypt positif')
    print('2. Decrypt negatif')
    choose = input('silahkan pilih (1/2) : ')
    if choose == '1':
        print("Choose your method: ")
        print("1. ASCII")
        print("2. Cipher")
        choise = input('enter your method: ')
        if choise == '1':
            Message = input('Input your ASCII: ')
            decodedmessage = ""
            for item in Message.split():
                decodedmessage += chr(int(item))
            plaintext = decodedmessage
            
            
            
            def caesar(char, key):
                output_text = ""
                for i in range(len(plaintext)):
                    char = plaintext[i]
                    if (char.isupper()):
                        output_text += chr((ord(char) - key - 65) % 26 + 65)      
                    elif (char.isnumeric()):
                        output_text += chr((ord(char) - key - 48) % 10 + 48)
                    elif (char.islower()):
                        output_text += chr((ord(char) - key - 97) % 26 + 97)    
                    else:
                        output_text += chr((ord(char) - key - 32) % 15 + 32)
                return output_text
            print ('Your ASCII CODE IS : ' + decodedmessage)
            for key in range(26):
                hasil = ('using key: ' + str(key) , str(caesar(plaintext, key)))
                print(hasil)
                
                
                
            lanjut = input('Repeat the program?(y/n)... : ')                
            if lanjut == 'y':
                    welcome()
            else:
                print('Terimakasih!')
        if choise == '2':
            plaintext = input("Input your Cipher : ")
            
            
            
            def caesar(char, key):
                output_text = ""
                for i in range(len(plaintext)):
                    char = plaintext[i]
                    if (char.isupper()):
                        output_text += chr((ord(char) - key - 65) % 26 + 65)      
                    elif (char.isnumeric()):
                        output_text += chr((ord(char) - key - 48) % 10 + 48)
                    elif (char.islower()):
                        output_text += chr((ord(char) - key - 97) % 26 + 97) 
                    elif (ord(char)) >= 33 and ord(char) <= 47:
                        output_text += chr((ord(char) - key - 33) % 15 + 33)
                    elif (char.isspace()):
                        output_text += chr((ord(char) - key - 32) % 1 + 32)
                    else:
                        output_text += chr((ord(char) + key - 32) % 1 + 32)
                return output_text
            for key in range(26):
                    hasil = ('using key: ' + str(key) , str(caesar(plaintext, key)))
                    print(hasil)
                    
                    
                    
            lanjut = input('Repeat the program?(y/n)... : ')             
            if lanjut == 'y':
                    welcome()
            else:
                print('Terimakasih!')
                
                
    elif choose == '2':
        
        
        print("Choose your method: ")
        print("1. ASCII")
        print("2. Cipher")
        pilih = input('enter your method: ')
        if pilih == '1':
            pesan = input("Input your ASCII: ")
            decodedmessage = ""
            for item in pesan.split():
                decodedmessage += chr(int(item))
            encrypted = decodedmessage
            
            
            
            def decrypt(char, key):
                output_text = ""
                for i in range(len(encrypted)):
                    char = encrypted[i]
                    if (char.isupper()):
                        output_text += chr((ord(char) + key - 65) % 26 + 65)
                        if (char.isupper()) > 90:
                            char = char -26        
                    elif (char.isnumeric()):
                        output_text += chr((ord(char) + key - 48) % 10 + 48)
                        if (char.isnumeric()) > 57:
                            char = char - 10
                    elif (char.islower()):
                        output_text += chr((ord(char) + key - 97) % 26 + 97)
                        if (char.islower()) > 122:
                            char = char - 26
                    else:
                        output_text += chr((ord(char) + key - 32) % 15 + 32)
                return output_text
            
            
            
            for key in range(26):
                    result = ("using key: -" + str(key) , decrypt(encrypted, key))
                    print(result)
            lanjut = input('Repeat the program?(y/n)... : ')             
            if lanjut == 'y':
                    welcome()
            else:
                print('Terimakasih!')
                
                
                
        elif pilih == '2':
            cipher = input("Input your Ciphertext : ")
            def decrypt(char, key):
                output_text = ""
                for i in range(len(cipher)):
                    char = cipher[i]
                    if (char.isupper()):
                        output_text += chr((ord(char) + key - 65) % 26 + 65)
                        if (char.isupper()) > 90:
                            char = char -26        
                    elif (char.isnumeric()):
                        output_text += chr((ord(char) + key - 48) % 10 + 48)
                        if (char.isnumeric()) > 57:
                            char = char - 10
                    elif (char.islower()):
                        output_text += chr((ord(char) + key - 97) % 26 + 97)
                        if (char.islower()) > 122:
                            char = char - 26
                    elif (ord(char)) >= 32 and ord(char) <= 47:
                        output_text += chr((ord(char) + key - 32) % 15 + 32)
                            
                    else:
                        output_text += chr((ord(char) + key - 32) % 15 + 32)
                return output_text
            for key in range(26):
                    result = ("using key: -" + str(key) , decrypt(cipher, key))
                    print(result)
                    
                    
                    
            lanjut = input('Repeat the program?(y/n)... : ')               
            if lanjut == 'y':
                    welcome()
            else:
                print('Terimakasih!')
                print('Thankyou! ~Dymi XII TKJ 2~')
    else:
        print('Invalid Input')
        
def welcome():
    print("WELCOME TO THE PROGRAM")
    pilihan = input('INPUT YOUR CHOICE \n 1. ENCRYPT \n 2. DECRYPT \n 1/2 : ')
    if pilihan == '1':
        enkripsi()
    elif pilihan == '2':
        dekripsi()
    else:
        print('Thanks!')


program = input('PRESS ENTER TO RUN THE PROGRAM...')
if program == '':
    welcome()
else:
    print('terimakasih!')
    print('Thankyou! ~Dymi XII TKJ 2~')






