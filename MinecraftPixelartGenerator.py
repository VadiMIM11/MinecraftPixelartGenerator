from PIL import Image
import os, copy
from preview import PreviewClass

def avrgColorInDir(inputDir):
    files = os.listdir(inputDir);
    i = 1; # Counter for output
    output = "";
    for fileName in files:
        (name, ext) = fileName.split('.');
        print(str(i) + ": " + name);
        output += name + "." + ext + " ";
        i += 1;
        if ext == "png":
            image = Image.open(inputDir + "\\" + name + '.' + ext).convert("RGBA");
            pxs = image.load();
            r = pxs[0, 0][0];
            g = pxs[0, 0][1];
            b = pxs[0, 0][2];
            a = pxs[0, 0][3];
            for x in range(0, image.size[0]):
                for y in range(1, image.size[1]):
                    #print("x: " + str(x) + "; y: " + str(y) + " = " + str(pxs[x, y]));
                    r += pxs[x, y][0];
                    g += pxs[x, y][1];
                    b += pxs[x, y][2];
                    a += pxs[x, y][3];
            r = round(r / (image.size[0] * image.size[1]));
            g = round(g / (image.size[0] * image.size[1]));
            b = round(b / (image.size[0] * image.size[1]));
            a = round(a / (image.size[0] * image.size[1]));
            output += str(r) + " " + str(g) + " " + str(b) + " " + str(a);
            print("Average color: " + str((r, g, b, a)) + "\n");
            output += "\n";
    output = output[:-1];
    #output[len(output) - 1] = '';
    return output;
        
# Converts file data to array
def fileToArray(texturesFile):
    lineCount = 0;
    #print(blocksFile.read());

    text = texturesFile.read();
    lines = text.split("\n");
    i = 0;
    texturesColorsArray = [];
    while i < len(lines):
        texturesStr = lines[i];
        textureData = texturesStr.split();
        texturesColorsArray.append(textureData);
        i += 1;
    return texturesColorsArray

# Matches pixels with blocks
#def matchBlocks(image, blocksArray):



defaultFileName = "averageColorData.txt";
while(True):
    #
    print("C:\\Users\\Vadim\\Pictures\\x4D-qiVvuTA.jpg");
    #
    print("Commands:\n<exit>\n<new> - new textures database folder");
    print("<load> - load image for a pixelart");
    userInput = str(input());
    if userInput == "exit":
        exit();
    if userInput == "new":
        data = open(defaultFileName, 'w');
        print("Enter your textures folder path: ");
        data.write(avrgColorInDir(input()));
    elif userInput == "load":
        print("Enter your image path:");
        img = Image.open(input());
        print("Enter preferred size (press enter to keep source image size): <width> <height>");
        size = input();
        if size != "":
            w, h = map(int, size.split());
            img.thumbnail((w, h));
            #img.show();
        data = open(defaultFileName, 'r');
        texturesColorsArray = fileToArray(data);
        print("Type <preview> to create an image of a pixelart");
        userInput = input();
        #
        print("C:\\Users\\Vadim\\Desktop\\Delete\\blockForPreview");
        #
        if userInput == "preview":
            print("NOTE: All textures must the same square size.\nEnter path to your textures folder:");
            path = input();
            previewObj = PreviewClass();
            previewObj.showArt(texturesColorsArray, img, path);
        #matchBlocks();