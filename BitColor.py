import numpy as np

class ShadePair():
    # a shade is a numpy array of r, g, b
    def __init__(self, original, newShade):
        self.original = original
        self.newShade = newShade

class BitColor():
    #  bitValue: Which value in the code does this color represent? (char)
    # numShades: how many different shades of this color
    #    shades: array of ShadePairs
    def __init__(self, bitValue, numShades, shades, defaultShade=[]):
        self._bitValue = bitValue
        self._numShades = numShades
        self._shades = shades
        self._defaultShade = defaultShade

    def getBitValue(self):
        return self._bitValue

    def shade(self, original):
        for pair in self._shades:
            if (pair.original == original).all():
                return pair.newShade

        if len(self._defaultShade) > 0:
            return self._defaultShade
        else:
            return original
