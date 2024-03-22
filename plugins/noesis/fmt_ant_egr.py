from inc_noesis import *


def registerNoesisTypes():
    handle = noesis.register("Antanta (2003) effects graphics", ".egr")
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
         self.offsetX = self.filereader.readShort() 
         self.offsetY = self.filereader.readShort()
         self.colNum = self.filereader.readUShort()
         self.rowNum = self.filereader.readUShort()
         self.width = self.filereader.readUShort()
         self.smallWidth = self.filereader.readUShort()
         self.size = self.filereader.readUInt()
         self.offset = self.filereader.readUInt()  

  
class AntUnitGraphics:
    def __init__(self, reader):
        self.filereader = reader
        self.width = 0
        self.height = 0
        self.size = 0
        self.fileRecs = []
        
    def parseHeader(self):     
        self.fileNum = self.filereader.readUByte()
        self.width = self.filereader.readUInt()
        self.height = self.filereader.readUInt()
        self.width1 = self.filereader.readUShort()
        self.width1 = self.filereader.readUShort()
          
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
        for i in range(self.fileNum):
            if self.fileRecs[i].offsetX != -1 and self.fileRecs[i].width == self.width:
                data = self.filereader.readBytes(self.fileRecs[i].size)           
                image = rapi.imageDecodeRaw(self.unpackImage(data, self.fileRecs[i]), self.fileRecs[i].width, self.fileRecs[i].width, "b4g4r4a4")       
                yield [image, self.fileRecs[i]]
            
    def readFileRecords(self):                        
        for k in range(self.fileNum):
            rec = FileRec(self.filereader)
            rec.read()
            self.fileRecs.append(rec)                       
        
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
