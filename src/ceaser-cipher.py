from asciiart import CEASERCIPHER

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k","l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
print(CEASERCIPHER)

def caesar(original_text,shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
             shift_amount = shift_amount * -1

    for letter in original_text:
        if letter not in alphabet:
              output_text += letter
        else:
            shift_position = alphabet.index(letter) + shift_amount
            shift_position %= len(alphabet)
            output_text += alphabet[shift_position]

    print(f"{direction}d message: {output_text}\n")
        


should_continue = True


while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower().strip()
    shift = int(input("Type the shift number:\n"))

    caesar(text, shift,direction)

    restart = input("Type 'yes' if you want to continue. Otherwise, type 'no' to continue: \n")

    if restart == 'no':
         should_continue = False
         print("Goodbye")


