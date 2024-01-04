from sys import argv
import cv2
import numpy as np
#import pdb

import getPreviewImage as preview
import BitColor as bc
from Bitstream import *
from colors import *
import getArgs


def pacmanTest():
    BITS_PER_STITCH = 1
    NUM_SHADES = 4
    STS_PER_PIXEL = 1
    RESULT_ZOOM = 4

    ORIG_WHITE = np.array([0xf9, 0xdd, 0xdf])
    NEW_WHITE = np.array([255, 255, 255])
    PELLET_COLOR = np.array([0xaf, 0xbf, 0xfc])
    WALL_COLOR = np.array([0xde, 0x21, 0x21])
    NEW_BLACK = np.array([0x3f, 0x3f, 0x41])

    grayscale = [bc.ShadePair(ORIG_WHITE, NEW_WHITE),
             bc.ShadePair(PELLET_COLOR, NEW_WHITE),
             bc.ShadePair(WALL_COLOR, DARK_GRAY),
             bc.ShadePair(BLACK, NEW_BLACK)]
 
    colors = [bc.BitColor(0, NUM_SHADES, grayscale, LIGHT_GRAY)]
    testImage = cv2.imread(argv[1])
    if STS_PER_PIXEL > 1:
        testImageHeight = len(testImage)
        testImageWidth = len(testImage[0])
        testImage = cv2.resize(testImage, (testImageWidth * STS_PER_PIXEL, 
            testImageHeight * STS_PER_PIXEL), fx=STS_PER_PIXEL, 
            fy=STS_PER_PIXEL, interpolation=cv2.INTER_NEAREST)


    previewImage = preview.previewImageSomeUnchanged(colors, BITS_PER_STITCH, testImage, "pokered.gbc")
    if RESULT_ZOOM > 1:
        testImageHeight = len(testImage)
        testImageWidth = len(testImage[0])
        previewImage = cv2.resize(previewImage, (testImageWidth * RESULT_ZOOM, 
            testImageHeight * RESULT_ZOOM), fx=RESULT_ZOOM, 
            fy=RESULT_ZOOM, interpolation=cv2.INTER_NEAREST)
    cv2.imshow("Test", previewImage)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    if len(argv) == 3:
        cv2.imwrite(argv[2], previewImage)

def palletArgsTest():
    args = getArgs.Args()
    args.getArgs()
    #pdb.set_trace()


    testImage = cv2.imread(args.imageIn)
    if args.stsPerPixel > 1:
        testImageHeight = len(testImage)
        testImageWidth = len(testImage[0])
        testImage = cv2.resize(testImage, (testImageWidth * args.stsPerPixel, 
            testImageHeight * args.stsPerPixel), fx=args.stsPerPixel, 
            fy=args.stsPerPixel, interpolation=cv2.INTER_NEAREST)


    previewImage = preview.getPreviewImage(args.colors, args.bitsPerStitch, 
        testImage, args.codefile)
    if args.resultZoom > 1:
        testImageHeight = len(testImage)
        testImageWidth = len(testImage[0])
        previewImage = cv2.resize(previewImage, (testImageWidth * args.resultZoom, 
            testImageHeight * args.resultZoom), fx=args.resultZoom, 
            fy=args.resultZoom, interpolation=cv2.INTER_NEAREST)

    if args.showImage:
        cv2.imshow("Test", previewImage)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    
    if len(args.imageOut) > 0:
        cv2.imwrite(args.imageOut, previewImage)

def grayscaleRedTest():
    BITS_PER_STITCH = 2
    NUM_SHADES = 4
    STS_PER_PIXEL = 6

    colors = [bc.BitColor(0, NUM_SHADES, grayscale)]
    colors.append(bc.BitColor(1, NUM_SHADES, reds));
    #colors = [bc.BitColor(0, NUM_SHADES, reds)]
    colors.append(bc.BitColor(2, NUM_SHADES, blues));
    colors.append(bc.BitColor(3, NUM_SHADES, yellows));
    #colors.append(bc.BitColor(3, NUM_SHADES, greens));

    testImage = cv2.imread(argv[1])
    if STS_PER_PIXEL > 1:
        testImageHeight = len(testImage)
        testImageWidth = len(testImage[0])
        testImage = cv2.resize(testImage, (testImageWidth * STS_PER_PIXEL, 
            testImageHeight * STS_PER_PIXEL), fx=STS_PER_PIXEL, 
            fy=STS_PER_PIXEL, interpolation=cv2.INTER_NEAREST)


    previewImage = preview.getPreviewImage(colors, BITS_PER_STITCH, testImage, "pokered.gbc")
    #previewImage = cv2.resize(previewImage, (testImageWidth * 2, testImageHeight * 2),
     #   fx=2, fy=2, interpolation=cv2.INTER_NEAREST)
    cv2.imshow("Test", previewImage)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    if len(argv) == 3:
        cv2.imwrite(argv[2], previewImage)

def usage():
    print("Usage: python3 main.py [img_filename] [save_filename]")

if __name__ == "__main__":
    #pdb.set_trace()
    if len(argv) > 0:
        #grayscaleRedTest()
        #pacmanTest()
        palletArgsTest()
    else:
        usage()
