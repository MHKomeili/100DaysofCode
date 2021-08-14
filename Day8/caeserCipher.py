from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caeser(start_text, shift_amount, cipher_direction):
    
    if cipher_direction == 'decode':
        shift_amount *= -1
    
    new_positions = [(alphabet.index(l)+shift_amount)%26 if (l in alphabet) else l
                    for l in start_text]   

    end_text = ''.join(alphabet[pos] if type(pos) == int else pos for pos in new_positions)

    print(f"Here is the {cipher_direction}d result: {end_text}")
    
    
print(logo)

should_continue = True
while should_continue:
    
    direction = input("Type 'encode' to encrypt or 'decode' to decrypt:\n")
    text = input('Type your message:\n').lower()
    shift = int(input('Type the shift number:\n'))

    caeser(start_text=text, shift_amount=shift, cipher_direction=direction)
    
    keep_on = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n")
    if keep_on == 'no':
        should_continue = False

print("Goodbye.")