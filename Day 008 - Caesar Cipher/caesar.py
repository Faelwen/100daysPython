from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start, shift, direction):
    final_text = ""
    if direction == "decode":
        shift *= -1
    for char in start:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift
            final_text += alphabet[new_position]
        else:
            final_text += char
    print(f"Here's the {direction}d result: {final_text}")

print(logo)

ongoing = True
while ongoing:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    caesar(start=text, shift=shift, direction=direction)
    restart = input("Type 'yes' to try again. Otherwise type 'no'.\n")
    if restart == "no":
        ongoing = False
        print("Goodbye")
