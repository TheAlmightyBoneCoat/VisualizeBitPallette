import cv2
#import numpy as np
import pdb
import random

from Bitstream import *
import BitColor as bc

# Reads next bits from BitStream,
# or zeroes if there are none
# Returns integer
#def getNextBits(stream, numBits):
 #   result = 0
#
 #   if len(stream) == 0:
  #      return 0
#
 #   if (numBits > len(stream)):
  #      streamLength = len(stream)
   #     result = getNextBits(stream, streamLength)
    #    result *= 2 ** (numBits - streamLength)

    # Otherwise, we have plenty of bits to read
#    else:
 #       for i in range(numBits):
  #          result *= 2
   #         if stream.read(bool, 1):
    #            result += 1

  #  return result

def sortColorArray(colors):
    result = colors
    for i in range(len(colors)):
        result[colors[i].getBitValue()] = colors[i]
    return result

#        colors: array of BitColors
#      bitDepth: how many bits each stitch represents
# originalImage: cv2::mat that we are basing this on
#         fname: name of the file to read bytes from
def getPreviewImage(colors, bitDepth, originalImage, fname=""):
    # For debugging purposes
    USE_RANDRANGE = False
   # FIND_LAST_NONZERO = True

   # lastNonzero = 0

#    colors = sortColorArray(colors)

    stream = ""
    if not USE_RANDRANGE:
        if (len(fname) == 0):
            # Use uninitialized data
            stream = Bitstream_char(originalImage.shape[0] * originalImage.shape[1])
        else:
            stream = Bitstream_char(fname)

    newImage = originalImage;

    for i in range(originalImage.shape[0]):
        for j in range(originalImage.shape[1]):
            bitValue = 0


            if USE_RANDRANGE:
                bitValue = random.randrange(2 ** bitDepth - 1)
                newImage[i][j] = colors[bitValue].shade(originalImage[i][j])
            
            else:
                if not stream.eof():
                    bitValue = stream.getNextVal(bitDepth)
                    newImage[i][j] = colors[ord(bitValue)].shade(originalImage[i][j])
               # if (bitValue != 1):
                #    pdb.set_trace()
    #        if FIND_LAST_NONZERO and ord(bitValue) != 0:
     #           lastNonzero = (i * originalImage.shape[1]) + j

   # if FIND_LAST_NONZERO:
    #    print(lastNonzero)
    return newImage

def previewImageSomeUnchanged(colors, bitDepth, originalImage, fname=""):
    if (len(fname) == 0):
        # Use uninitialized data
        stream = Bitstream_char(originalImage.shape[0] * originalImage.shape[1])
    else:
        stream = Bitstream_char(fname)

    newImage = originalImage

    
    for i in range(originalImage.shape[0]):
        for j in range(originalImage.shape[1]):
            bitValue = 0

            if not stream.eof():
                bitValue = ord(stream.getNextVal(bitDepth))
                if bitValue < len(colors) and colors[bitValue] != None:
                    newImage[i][j] = colors[bitValue].shade(originalImage[i][j])

    return newImage
