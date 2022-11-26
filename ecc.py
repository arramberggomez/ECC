# -*- coding: utf-8 -*-
"""
Helper functions for encoding messages to elliptic curve
"""

# import necessary packages
import math
import os
import itertools
import random

def rand_bin(n):
  """
  function to create n-bit long random binary string
  """
  key1 = ""
 
  for i in range(n):
      temp = str(random.randint(0, 1))
      key1 += temp
         
  return(key1)


# define bit-wise XOR
_xormap = {('0','0'): '0', ('0', '1'): '1', ('1', '0'): '1', ('1', '1'): '0'}
def xor(x,y):
  return ''.join(_xormap[a,b] for a, b in zip(x,y))


def XOR_block(block, b):
  """
  function to XOR two string bit-wise
  automatically pads each string according to whichever is longer
  """
  result = []

  if len(block) <= len(b):
    block = block.zfill(len(b))
  elif len(block) >= len(b):
    b = b.zfill(len(block))

  for i in range(len(b)):
    result.append(xor(block[i], b[i]))
  
  result = ''.join(result)
  return result



def encode_message(message, IV):
  """
  encodes message according to Algorithm 2
  once encoded, gets mapped to elliptic curve
  """
  N = 23    # default for now
  B = math.ceil(len(message)/N)

  # divide message into B blocks with leq N characters each
  message = [message[i:i+N] for i in range(0, len(message), N)]

  # convert each block to binary 
  for i in range(len(message)): 
    message[i] = ''.join(format(ord(x), 'b') for x in message[i])

  # xor blocks according to scheme in paper
  message[0] = XOR_block(IV, message[0])
  for i in range(len(message)-1):
    message[i+1] = XOR_block(message[i], message[i+1])
    
  # right pad with 3 zeros ie 192+3
  message = [message[i].ljust(195, '0') for i in range(len(message))]

  return message



def to_dec(message):
  """
  convert each block to decimal
  """
  new = []
  for i in range(len(message)):
    new.append(int(message[i], 2))
  return new


