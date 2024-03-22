from inc_noesis import *

IMAGE_WIDTH = 256
IMAGE_HEIGHT = 256
IMAGE_DATA_SIZE = 131072


def registerNoesisTypes():
    handle = noesis.register("Antanta (2003) object graphics", ".ogr")
    noesis.setHandlerTypeCheck(handle, antCheckType)
    noesis.setHandlerLoadRGBA(handle, antLoadRGBA)

    return 1
         
  
class AntObjectGraphics:
    def __init__(self, reader):
        self.filereader = reader
        self.width = 0
        self.height = 0
        self.size = 0
 
    def parseHeader(self):     
        num = self.filereader.readUShort()
        self.filereader.seek(num*56, NOESEEK_REL)
   
        return 0

    def getImages(self):
        num = self.filereader.readUByte()
        for i in range(num):
            data = self.filereader.readBytes(IMAGE_DATA_SIZE)                                            
            image = rapi.imageDecodeRaw(data, IMAGE_WIDTH, IMAGE_HEIGHT, "b4g4r4a4")       
            yield image
         
    def read(self):
        self.parseHeader()
        
    
def antCheckType(data):
    img = AntObjectGraphics(NoeBitStream(data))
    if img.parseHeader() != 0:
        return 0
        
    return 1  


def antLoadRGBA(data, texList):
    #noesis.logPopup() 
    image = AntObjectGraphics(NoeBitStream(data))       
    image.read() 
     
    for img in image.getImages():
        texList.append(NoeTexture("anttex", IMAGE_WIDTH, IMAGE_HEIGHT, img, noesis.NOESISTEX_RGBA32))
            
    return 1
