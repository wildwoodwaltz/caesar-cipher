import re
from .corpus_loader import word_list, name_list

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
  key = 0
  percentage = 0
  for a in alpha:
    verified_words=0
    key += 1
    cracked_msg = decrypt(message, key)
    cracked_msg_verify = cracked_msg.split(' ')

    for word in cracked_msg_verify:
      word = re.sub(r'[^A-Za-z]+','', word)
      if word.lower() in word_list or word in name_list:
        verified_words += 1
      else:
        pass
    percentage = int(verified_words // len(cracked_msg_verify) * 100)
    if percentage >= 50:
      return cracked_msg
  if percentage < 50: 
    return ""
  