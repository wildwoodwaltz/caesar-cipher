
import keyword


alpha = "abcdefghijklmnopqrstuvwxyz"



def encrypt(message, key):
  final_message = ''
  if key < 0:
    key = key % 26
    print(key)
  for character in message:
    if not character.isalpha():
      final_message += character
    else:
      alpha_index=alpha.find(character.lower())
      alpha_index += key
      if alpha_index >= len(alpha):
        alpha_index -= len(alpha)
      elif alpha_index < 0:
        alpha_index += len(alpha)
      if character.isupper():
        letter = alpha[alpha_index]
        final_message += letter.upper()
      if character.islower():
        final_message += alpha[alpha_index]
  return final_message

def decrypt(message, key):
  return encrypt(message, -key)


def crack(message):
  pass