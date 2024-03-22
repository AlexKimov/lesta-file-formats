from inc_noesis import *

def registerNoesisTypes():
    handle = noesis.register("Antanta (2003) images", ".img")
    noesis.setHandlerTypeCheck(handle, antCheckType)
    noesis.setHandlerLoadRGBA(handle, antLoadRGBA)

    return 1
      

class PackedPixelOffset:
    def __init__(self, start, end, offset):
         self.start = start   
         self.end = end   
         self.offset = offset 
         
  
class AntImage:
    def __init__(self, reader):
        self.filereader = reader
        self.width = 0
        self.height = 0
        self.size = 0
 
    def parseHeader(self):
        self.filereader.seek(5, NOESEEK_ABS)
       
        self.width = self.filereader.readUShort()
        self.height = self.filereader.readUShort()
        self.size = self.filereader.readUInt()
   
        return 0

    def unpackImage(self, offsets, data):
        pixelSize = 24 >> 3
        image = bytearray(self.width * self.height * pixelSize)
        
        row = 0
        
        for index, colOffsets in enumerate(offsets):
                for colOffs in colOffsets:
                    dataBegin = colOffs.offset
                    dataEnd = colOffs.offset + (colOffs.end - colOffs.start + 1) * pixelSize
                    pixelStart = (row + colOffs.start) * pixelSize
                    pixelEnd = (row + colOffs.end + 1) * pixelSize
                    image[pixelStart: pixelEnd] = data[dataBegin:dataEnd]
                
                row = index*self.width                   
        return image    

    def getImagetData(self):
        row = 0         
        imageRowDataOffsets = []  
        while row < self.height:      
            num = self.filereader.readUShort()
            offsets = []
            for i in range(num):
                start = self.filereader.readUShort()
                end = self.filereader.readUShort()
                offset = self.filereader.readUInt()

                offsets.append(PackedPixelOffset(start, end, offset))
            imageRowDataOffsets.append(offsets)    
            row += 1
        data = self.filereader.readBytes(self.size)                                            
        self.data = rapi.imageDecodeRaw(self.unpackImage(imageRowDataOffsets, data), self.width, self.height, "r8g8b8")       
                             
    def read(self):
        self.parseHeader() 
        self.getImagetData()
        
    
def antCheckType(data):
    img = AntImage(NoeBitStream(data))
    if img.parseHeader() != 0:
        return 0
        
    return 1  


def antLoadRGBA(data, texList):
    #noesis.logPopup() 
    image = AntImage(NoeBitStream(data))       
    image.read() 
     
    texList.append(NoeTexture("anttex", image.width, image.height, image.data,
                              noesis.NOESISTEX_RGBA32))
            
    return 1
