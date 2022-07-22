#imports

#caesers cipher function


#encryption
def encyption(message,shifter_key):
    encyption_results=""
    #go through every charcter
    for i in range(len(message)):
        letter=message[i]

        if(letter.isupper()):
            encyption_results+=chr((ord(letter)+shifter_key-65)%26+65)
        else:
            encyption_results+=chr((ord(letter)+shifter_key-97)%26+97)

        return encyption_results



        