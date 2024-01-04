from sys import argv, exit
import colors
import BitColor as bc
import pdb

# Need:
# image file to read
# save file name
# FOR EACH COLOR: bitval and color
# TODO: binary file to get code from
class Args():
    def __init__(self):
        self.imageIn = "pallet_town.png"
        self.imageOut = "pallet_town_out.png"
        self.codefile = "lorem_ipsum.txt"
        self.colors = []
        self.bitsPerStitch = 2
        self.numShades = 4
        self.stsPerPixel = 1
        self.resultZoom = 1
        self.showImage = False

    def defaultColors(self):
        self.colors = [bc.BitColor(0, self.numShades, colors.grayscale)]
        self.colors.append(bc.BitColor(1, self.numShades, colors.reds));
        self.colors.append(bc.BitColor(2, self.numShades, colors.yellows));
        self.colors.append(bc.BitColor(3, self.numShades, colors.blues));

    def sortColors(self):
        result = []
        for i in range(2 ** self.bitsPerStitch):
            for j in range(len(self.colors)):
                if self.colors[j].getBitValue() == i:
                    result.append(self.colors[j])
                    break

            # If we didn't end up finding it
            if len(result) == i:
                result.append(None)

        self.colors = result
    
    # Example color string:
    # 1=gray - value 1 represented by (gray, gray) pairs
    # 2=red  - bit value 2 represented by (gray, red) pairs
    def extractColor(self, colorStr):
        equalIndex = colorStr.find("=")
        bitValue = int(colorStr[:equalIndex])
        colorName = colorStr[equalIndex + 1:]
        self.colors.append(bc.BitColor(bitValue, self.numShades,
            colors.allShades[colorName]))

    def usage(self):
        print("python3 main.py --[option1] --[option2]=[optarg] ...")
        print("")
        print("       code: The file to read in bit values from.")
        print("-c or color:")
        print(" -h or help: Displays this message.")
        print("   image-in: Image file to read in.")
        print("  image-out: Filename to save the preview image under.")
        print(" num-shades: How many shades of each color.")
        print("  per-pixel: How many stitches to a size for each pixel.")
        print(" per-stitch: How many bits per stitch.")
        print("       show: If set, shows the preview image in a new window.")
        print("       zoom: How much to zoom in the resulting image.")

    def getArgs(self):
        for i in range(len(argv)):
            if argv[i] == "--help" or argv[i] == "-h":
                self.usage()
                exit()
            elif argv[i][:len("--per-pixel=")] == "--per-pixel=":
                self.stsPerPixel = int(argv[i][len("--per-pixel="):])
            elif argv[i][:len("--per-stitch=")] == "--per-stitch=":
                self.bitsPerStitch = int(argv[i][len("--per-stitch="):])
            elif argv[i][:len("--zoom=")] == "--zoom=":
                self.resultZoom = int(argv[i][len("--zoom="):])
            elif argv[i] == "--show":
                self.showImage = True
            elif argv[i][:len("--num-shades=")] == "--num-shades=":
                self.numShades = int(argv[i][len("--num-shades="):])
            elif argv[i][:len("--image-in=")] == "--image-in=":
                self.imageIn = argv[i][len("--image-in="):]
            elif argv[i][:len("--image-out=")] == "--image-out=":
                self.imageOut = argv[i][len("--image-out="):]
            elif argv[i][:len("--code=")] == "--code=":
                self.codefile = argv[i][len("--code="):]
            elif argv[i][:len("--color")] == "--color":
                self.extractColor(argv[i][len("--color"):])
            elif argv[i][:2] == "-c":
                self.extractColor(argv[i][2:])

        if len(self.colors) == 0:
            self.defaultColors()
        else:
            self.sortColors()
 #       pdb.set_trace()
