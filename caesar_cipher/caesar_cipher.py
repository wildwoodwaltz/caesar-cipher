import re
from corpus_loader import word_list, name_list
alpha = "abcdefghijklmnopqrstuvwxyz"


def encrypt(message, key):
  final_message = ''
  if key < 26:
    key = int(key) % 26
  for symbol in message:
    alpha_index=alpha.find(symbol)
    if alpha_index == -1:
      final_message += symbol
    else:
      alpha_index += key
      final_message =+ alpha[alpha_index]

def decrypt(message, key):
  encrypt(message, -key)

def crack(message):
  pass