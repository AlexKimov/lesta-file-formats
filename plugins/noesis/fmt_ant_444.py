from inc_noesis import *


def registerNoesisTypes():
    handle = noesis.register("Antanta (2003) 16 bit images", ".444")
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
        self.width = self.filereader.readUShort()
        self.height = self.filereader.readUShort()
   
        return 0

    def readtImage(self):
        data = self.filereader.readBytes(self.width * self.height)                                            
        self.data = rapi.imageDecodeRaw(data, self.width, self.height, "b4g4r4a4")       
         
    def read(self):
        self.parseHeader()
        self.readtImage()
    
    
def antCheckType(data):
    img = AntObjectGraphics(NoeBitStream(data))
    if img.parseHeader() != 0:
        return 0
        
    return 1  


def antLoadRGBA(data, texList):
    #noesis.logPopup() 
    image = AntObjectGraphics(NoeBitStream(data))       
    image.read() 
     
    texList.append(NoeTexture("anttex", image.width, image.height, image.data, noesis.NOESISTEX_RGBA32))
            
    return 1
