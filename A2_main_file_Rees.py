def rot3Encrypt(inputText):
    charSet="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz`~!@#$%^&*()_-=|\}]{[\"':;?/>.<, "
    enText = "".join([charSet[(charSet.find(c)+3)%95] for c in inputText])
    return enText

def rot3Decrypt(inputText):
      charSet="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz`~!@#$%^&*()_-=|\}]{[\"':;?/>.<, "
      deText = "".join([charSet[(charSet.find(c)-3)%95] for c in inputText])
      return deText


#Initial message
print("Welcome to our password manager!")

#Initiate the whileloop by making the initial option value 0
choice= ""

#Whileloop begins and only exits once user chooses Q option to break the loop. 
while choice != 'q':
    print("\n[1] Enter 1 to Create an encryption key.")
    print("[2] Enter 2 to Add stored credentials")
    print("[3] Enter 3 to View stored credentials")
    print("[q] Enter q to Quit.")

    #User is prompted to choose an option
    choice = input("\nChoose one of the following.")

    #They have made a choice and these are the following responses back on which choice was made
    if choice == '1':
            print("\nEnter a name for the encryption key\n")
            #below is me trying to figure out where encryption enters the sequence
            name = input ("\nWhat's your name? ")
            encryptName = rot3Encrypt(name) 
            print("\nyour encrypted name is", encryptName, "\n") 


    elif choice == '2':
            print("\nEnter Username, password and url\n")
            #the following is me adding the create/open file sequences in order to store the users given details.
            username = input("\nEnter your username ")
            password = input("\nEnter your password ")
            url = input("\nEnter your url ")

            #establishing the function of encryptText to perform the encryption sequence on the inputs of the 3 questions asked when starting this choice
            encryptText = rot3Encrypt(username + " " + password + " " + url + " ") 
            print(encryptText)
            f = open("A2_text_file.", "a")

            #instead of writing the initial plan inputs, the f is writing in the encrypted versions
            f.write(encryptText) 
            print("\nYour new details have now been stored\n")
            
        
    elif choice == '3':
            #below is me trying to figure out where checking file occurs in sequence
            try:
                #text file ive made is "A2_text_file"
                f = open('A2_text_file', "r") 
                print("file exists")

                #instead of the name data "encryptedText" was used instead
                encryptedText = f.read()   
                print(encryptedText)

                #since the text file was read with the previous function, the decrypt function now runs off what has been previously read
                decryptText = rot3Decrypt(encryptedText) 

                #The decypted text (data) has now been stripped of any leading or trailing white spaces
                strippedText = decryptText.strip() 
                print(strippedText)

                #split string into a list with 2 spaces as the default delimiter
                dataList = strippedText.split(" ")  
                print(dataList)
                print(dataList[1])
                i = 0
                border = "|"
                print(f"{border}{'Username' : ^20}{border}{'Password' : ^20}{border}{'Url' : ^20}{border}")
                print("----------------------------------------------------------------")

                #repeat until 'i' is larger than the list length
                while i < len(dataList): 
                    print(f"{border}{dataList[i] : ^20}{border}{dataList[i+1] : ^20}{border}{dataList[i+2] : ^20}{border}")   
                    i += 3
                else:
                    print("\nAll data has now been displayed\n")
                f. close
            except FileNotFoundError: 
                print('No password file created, create and add data to a new file first')


    elif choice == 'q':
            print("\nExiting the menu\n")
    else:
            print("\nInvalid option, please try again.\n")


       
       
       