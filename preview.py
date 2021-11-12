from PIL import Image
import os
import time

class PreviewClass(object):
    """Allows to create a new image using textures instead of pixels"""
    
    def __isDir(self, file):
        pointCounter = 0;
        for i in file:
            if i == ".":
                pointCounter += 1;
            if i == "\\" or i == "/":
                return True;
        if pointCounter == 0:
            return True;
        return False

    __texturesSize = ();
    def _checkTexturesInDir(self, path):
        files = os.listdir(path);
        size = 0;
        for file in files:
            if self.__isDir(file):
                return False;
            else:
                (name, ext) = file.split('.');
                if ext != "png" and ext != "jpg" and ext != "jpeg":
                    return False;
                image = Image.open(path + "\\" + name + '.' + ext).convert("RGBA");
                (x, y) = image.size;
                if x != y:
                    return False;
                else:
                    self.__texturesSize = (x, y);
        return True;

    def matchPixelWithTextures(self, pixel, texturesDir, texturesColorsArray):
        dr = abs(pixel[0] - int(texturesColorsArray[0][1]));
        dg = abs(pixel[1] - int(texturesColorsArray[0][2]));
        db = abs(pixel[2] - int(texturesColorsArray[0][3]));
        da = abs(pixel[3] - int(texturesColorsArray[0][4]));
        minDif = dr + dg + db + da;
        minName = texturesColorsArray[0][0];
        for i in range(0, len(texturesColorsArray)):
            texture = texturesColorsArray[i];
            dr = abs(pixel[0] - int(texture[1]));
            dg = abs(pixel[1] - int(texture[2]));
            db = abs(pixel[2] - int(texture[3]));
            da = abs(pixel[3] - int(texture[4]));
            delta = dr + dg + db + da;
            if delta < minDif:
                minDif = delta;
                minName = texture[0];
        return minName;

    def showArt(self, texturesColorsArray, image, texturesDir):
        start = time.time();
        matchTime = 0;
        openTime = 0;
        pasteTime = 0;
        if self._checkTexturesInDir(texturesDir):
            openTimeStart = time.time();
            textures = [];
            files = os.listdir(texturesDir);
            for file in files:
                textures.append(Image.open(texturesDir + "\\" + file));
            openTime += time.time() - openTimeStart;

            previewImgSize = (image.size[0] * self.__texturesSize[0], image.size[1] * self.__texturesSize[1]);
            previewImg = Image.new("RGBA", previewImgSize);
            pxls = image.convert("RGBA").load();
            for x in range(image.size[0]):
                for y in range(image.size[1]):
                    pixel = pxls[x, y];

                    matchTimeStart = time.time();
                    textureName = self.matchPixelWithTextures(pixel, texturesDir, texturesColorsArray);
                    matchTime += time.time() - matchTimeStart;

                    openTimeStart = time.time();
                    #texture = Image.open(texturesDir + "\\" + textureName);
                    index = files.index(textureName);
                    texture = textures[index];
                    openTime += time.time() - openTimeStart;

                    posX = x * self.__texturesSize[0];
                    posY = y * self.__texturesSize[1];

                    pasteTimeStart = time.time();
                    previewImg.paste(texture, (posX, posY));
                    pasteTime += time.time() - pasteTimeStart;
            #previewImg.show();
            previewImg.save("preview.png");
        else:
            print("Something went wrong! Check your textures folder. It mustn't contain any folders in it");
        end = time.time()
        workingTime = (end - start);
        print("Working time: {0} seconds".format(workingTime));
        print("MatchTime: {0}\nPasteTime: {1}\nOpenTime: {2}\n".format(matchTime, pasteTime, openTime));
        print();


