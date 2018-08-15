class ListFile:
    def __init__(self,file_json):
        self.file_json = file_json[3]
        self.stack = []
        self.Dict = {}

    def printfile(self,file_json):
        self.stack.append(file_json[0]["name"])
        for i in range(1,len(file_json)):
            if isinstance(file_json[i], list):
                 self.printfile(file_json[i])
            else:
                self.stack.append(file_json[i]["name"])
                if "asize" in file_json[i]:
                    self.Dict["/".join(self.stack)]=file_json[i]["asize"]
                else:
                    self.Dict["/".join(self.stack)]=0
                print(self.Dict)
                self.stack.pop()
        self.stack.pop()

    def getlargefile(self,num):
        self.stack = []
        self.Dict={}
        self.printfile(self.file_json)
        tum = sorted(self.Dict.items(),key = lambda item:item[1], reverse=True)
        num = num if num<=len(tum) else len(tum) 
        for i in range(0,num):
            print(tum[i][0] + "  " + str(tum[i][1]) ) 
        


if __name__ == "__main__":
    dir_a = ListFile(a) 
    dir_a.getlargefile(4)  
