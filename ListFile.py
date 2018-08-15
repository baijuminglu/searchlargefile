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
    a = [
        1, 
        1, 
        {
            "progname": "ncdu", 
            "progver": "1.13", 
            "timestamp": 1534244357
        }, 
        [
            {
                "name": "/usr/local/src/test", 
                "asize": 4096, 
                "dsize": 4096, 
                "dev": 64769, 
                "ino": 1328152
            }, 
            [
                {
                    "name": "t1", 
                    "asize": 4096, 
                    "dsize": 4096, 
                    "ino": 1448563
                }, 
                [
                    {
                        "name": "s1", 
                        "asize": 4096, 
                        "dsize": 4096, 
                        "ino": 1448567
                    }, 
                    [
                        {
                            "name": "n1", 
                            "asize": 4096, 
                            "dsize": 4096, 
                            "ino": 1448569
                        }, 
                        {
                            "name": "2.tt", 
                            "ino": 1448570
                        }, 
                        {
                            "name": "3.tt", 
                            "ino": 1448571
                        }
                    ], 
                    {
                        "name": "1.txt", 
                        "ino": 1448568
                    }
                ]
            ], 
            [
                {
                    "name": "t3", 
                    "asize": 4096, 
                    "dsize": 4096, 
                    "ino": 1448565
                }
            ], 
            [
                {
                    "name": "t2", 
                    "asize": 4096, 
                    "dsize": 4096, 
                    "ino": 1448564
                }
            ], 
            [
                {
                    "name": "t4", 
                    "asize": 4096, 
                    "dsize": 4096, 
                    "ino": 1448566
                }
            ], 
            {
                "name": "1.txt", 
                "asize": 10485760, 
                "dsize": 10485760, 
                "ino": 1328153
            }
        ]
    ]
    dir_a = ListFile(a) 
    dir_a.getlargefile(4)  
