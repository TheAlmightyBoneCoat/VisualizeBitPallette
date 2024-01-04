import numpy as np
import BitColor as bc

WHITE = np.array([0xf7, 0xf7, 0xf7])
LIGHT_GRAY = np.array([0xa5, 0xa5, 0xa5])
DARK_GRAY = np.array([0x63, 0x63, 0x63])
BLACK = np.array([0, 0, 0])

    
PALE_RED = np.array([0x5d, 0x68, 0xf7])
MEDIUM_RED = np.array([0x0a, 0x1a, 0xf4])
DEEP_RED = np.array([0x09, 0x15, 0xaf])
DARK_RED = np.array([0x05, 0x0b, 0x63])

PALE_BLUE = np.array([0xf7, 0x68, 0x5d])
MEDIUM_BLUE = np.array([0xf4, 0x1a, 0x0a])
DEEP_BLUE = np.array([0xaf, 0x15, 0x09])
DARK_BLUE = np.array([0x63, 0x0b, 0x05])

PALE_YELLOW = np.array([0x5d, 0xf7, 0xe9])
MEDIUM_YELLOW = np.array([0x0a, 0xdd, 0xf4])
DEEP_YELLOW = np.array([0x09, 0xab, 0xaf])
DARK_YELLOW = np.array([0x63, 0x60, 0x05])

PALE_GREEN = np.array([0x5d, 0xf7, 0x6c])
MEDIUM_GREEN = np.array([0x0a, 0xf4, 0x21])
DEEP_GREEN = np.array([0x09, 0xaf, 0x25])
DARK_GREEN = np.array([0x15, 0x63, 0x05])

grayscale = [bc.ShadePair(WHITE, WHITE),
             bc.ShadePair(LIGHT_GRAY, LIGHT_GRAY),
             bc.ShadePair(DARK_GRAY, DARK_GRAY),
             bc.ShadePair(BLACK, BLACK)]

reds = [bc.ShadePair(WHITE, PALE_RED),
        bc.ShadePair(LIGHT_GRAY, MEDIUM_RED),
        bc.ShadePair(DARK_GRAY, DEEP_RED),
        bc.ShadePair(BLACK, DARK_RED)]

blues = [bc.ShadePair(WHITE, PALE_BLUE),
        bc.ShadePair(LIGHT_GRAY, MEDIUM_BLUE),
        bc.ShadePair(DARK_GRAY, DEEP_BLUE),
        bc.ShadePair(BLACK, DARK_BLUE)]

yellows = [bc.ShadePair(WHITE, PALE_YELLOW),
        bc.ShadePair(LIGHT_GRAY, MEDIUM_YELLOW),
        bc.ShadePair(DARK_GRAY, DEEP_YELLOW),
        bc.ShadePair(BLACK, DARK_YELLOW)]

greens = [bc.ShadePair(WHITE, PALE_GREEN),
        bc.ShadePair(LIGHT_GRAY, MEDIUM_GREEN),
        bc.ShadePair(DARK_GRAY, DEEP_GREEN),
        bc.ShadePair(BLACK, DARK_GREEN)]

allShades = {"gray" : grayscale, "red" : reds, "blue" : blues, 
    "yellow" : yellows, "green" : greens}
