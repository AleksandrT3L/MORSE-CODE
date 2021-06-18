# Python Program for implementing Morse code
from encode_and_decode import encode, decode

on = True
while on:
    choice = input("What do you want to do? (encode/decode, end - exit the program)\n").lower()

    if choice == "encode":
        print(encode(input("Enter the text:\n")))
    elif choice == "decode":
        print(decode(input("Enter the text:\n").split("   ")))
    elif choice == "exit":
        on = False
    else:
        print("Incorrect input")
