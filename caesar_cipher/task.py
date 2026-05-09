#Import the logo from the art file and print it to improve the user experience
from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#Create a function called ceaser which when called will encode or decode the text and provide the output in form of
#encryption or decryption
#We also need to make sure that if the shifted alphabets are over the range of alphabets then it needs to begin counting
#from the start of the alphabet list
def caesar(encode_or_decode, original_text, shift_amount):
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount = -shift_amount
    for letter in original_text:
        if letter not in alphabet:
            output_text += letter
        else:
            shifted_position = (alphabet.index(letter) + shift_amount) % len(alphabet)
            output_text += alphabet[shifted_position]
    print(f"Your text is {encode_or_decode}d and the result is: {output_text}")

#Now, for the final touch, we need to ask the user if they would like to keep encoding/decoding or would like to stop.
#This is done from the perspective of user experience as user might want to send encryption in batches
should_continue = True
while should_continue:
    # Let's get the input from the user about whether they would like to encode or decode, the text to encode/decode,
    # and by how many positions would the user like the text to be encoded/decoded
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    #Call the caesar function with keyword arguments to avoid confusion
    caesar(encode_or_decode=direction, original_text=text, shift_amount=shift)

    #Till now, we have worked on getting the inputs from user and based on those we are calling the defined function.
    #Now, we need to introduce a variable which will ask the user if they would like to keep going or stop!
    restart = input("Type 'yes' to continue encoding/decoding and 'no' to stop\n").lower()
    if restart == "no":
        should_continue = False
        print("Hope you enjoyed encryption and decryption! We'll see you again next time!")
