import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#Ceasar Function
def ceasar(text, shift, direction):
  end_text = ""
  for letter in text :
    if letter in alphabet :
      old_index = alphabet.index(letter)
      if direction.lower() == "encode" :
        new_index = (old_index + shift) % 26
      elif direction.lower() == "decode" :
        new_index = (old_index - shift + 26) % 26
      end_text += alphabet[new_index]
    else :
      end_text += letter
  print(f"The {direction}d text is: {end_text}")

#Print the logo and loop until user selects no
print(art.logo)
continue_executing = True
while(continue_executing == True) :
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n")) % 26

  ceasar(text = text, shift = shift, direction = direction)
  continue_again = input("Type 'yes' if you want to continue or 'no' if you want to end the program:\n")

  if continue_again.lower() == "yes" :
    continue_executing = True
  elif continue_again.lower() == "no" :
    continue_executing = False
    print("Goodbye")