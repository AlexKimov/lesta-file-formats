from inc_noesis import *


ORIENTATIONS_NUM = 5


def registerNoesisTypes():
    handle = noesis.register("Antanta (2003) unit graphics", ".ugr")
    noesis.setHandlerTypeCheck(handle, antCheckType)
    noesis.setHandlerLoadRGBA(handle, antLoadRGBA)

    return 1
      

class FileRec:
    def __init__(self, reader):
         self.filereader = reader
         self.offsetY = 0  
         self.offsetX = 0  
         self.colNum = 0
         self.rowNum = 0
         self.width = 0
         self.height = 0
         self.size = 0
         self.offset = 0
         
    def read(self):     
         self.offsetX = self.filereader.readUShort() 
         self.offsetY = self.filereader.readUShort()
         self.colNum = self.filereader.readUShort()
         self.rowNum = self.filereader.readUShort()
         self.width = self.filereader.readUShort()
         self.smallWidth = self.filereader.readUShort()
         self.size = self.filereader.readUInt()
         self.offset = self.filereader.readUInt()  


class AnimationsFileSet:
    def __init__(self, orients, pos):
        self.fileSetOffset = pos
        self.orientations = orients
    
  
class AntUnitGraphics:
    def __init__(self, reader):
        self.filereader = reader
        self.width = 0
        self.height = 0
        self.size = 0
        self.animationsSet = []
        
    def parseHeader(self):     
        self.fileNum = self.filereader.readUByte()
        self.setNum = self.filereader.readUByte()
   
        return 0

    def unpackImage(self, data, fileRec):
        pixelSize = 16 >> 3
        
        image = bytes()        
        image += bytes(fileRec.offsetY * fileRec.width * pixelSize) # 
        
        row = 0
        start = 0
        size = fileRec.size
        length = fileRec.colNum * pixelSize
        transpPixelsRight = bytes((fileRec.width - (fileRec.colNum + fileRec.offsetX)) * pixelSize)
        transpPixelsLeft = bytes(fileRec.offsetX * pixelSize)        
        while size:   
            start = row * length        
            image += transpPixelsLeft + data[start:start + length] + transpPixelsRight
            size -= length
            row += 1
                
        image += bytes((fileRec.width - fileRec.offsetY - fileRec.rowNum) * fileRec.width * pixelSize)
        
        return image    

    def getImages(self):  
        fileSet = self.animationsSet[0]
        self.filereader.seek(fileSet.fileSetOffset, NOESEEK_ABS) 
        for orientation in fileSet.orientations:
            for i in range(self.fileNum):
                data = self.filereader.readBytes(orientation[i].size)           
                image = rapi.imageDecodeRaw(self.unpackImage(data, orientation[i]), orientation[i].width, orientation[i].width, "b4g4r4a4")       
                yield [image, orientation[i]]
            
    def readFileRecords(self):       
        for k in range(self.setNum):
            size = 0 
            self.orients = []
            
            for i in range(ORIENTATIONS_NUM):                 
                fileRecords = []
                for k in range(self.fileNum):
                    rec = FileRec(self.filereader)
                    rec.read()
                    size += rec.size
                    fileRecords.append(rec)
                self.orients.append(fileRecords)           
            self.animationsSet.append(AnimationsFileSet(self.orients, self.filereader.tell())) 
          
            self.filereader.seek(size, NOESEEK_REL)            
        
    def read(self):
        self.parseHeader() 
        self.readFileRecords()
        
    
def antCheckType(data):
    img = AntUnitGraphics(NoeBitStream(data))
    if img.parseHeader() != 0:
        return 0
        
    return 1  


def antLoadRGBA(data, texList):
    #noesis.logPopup() 
    image = AntUnitGraphics(NoeBitStream(data))       
    image.read() 
     
    for data, image in image.getImages(): 
        texList.append(NoeTexture("anttex", image.width, image.width, data,
                              noesis.NOESISTEX_RGBA32))
            
    return 1
