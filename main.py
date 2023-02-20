roman = '''
        ___       
              \\||      
             ,'_,-\     
             ;'____\    
             || =\=|    
             ||  - |                               
         ,---'._--''-,,---------.--.----_,         
        / `-._- _--/,,|  ___,,--'--'._<            
       /-._,  `-.__;,,|'                           
      /   ;\      / , ;                            
     /  ,' | _ - ',/, ;
    (  (   |     /, ,,;
     \  \  |     ',,/,;
      \  \ |    /, / ,;
     (| ,^.|   / ,, ,/;
      `-'./ `-._,, ,/,;
           �-._ `-._,,;
           |/,,`-._ `-.
           |, ,;, ,`-._

'''
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(roman)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

if direction == "encode":
  cipher_text = ""
  for letter in text:
    position = alphabet.index(letter)
    new_position = position + shift
    cipher_text += alphabet[new_position]
  print(f"The encoded text is {cipher_text}")  
elif "decode":
  cipher_text = ""
  for letter in text:
    position = alphabet.index(letter)
    new_position = position - shift
    cipher_text += alphabet[new_position]
  print(f"The decoded text is {cipher_text}") 


