class Loadjson():
    def __init__(self, file):
        self.file = file
    def __enter__(self):
        f = open(self.file, 'r')
        self.fd = f
        return(self)
    def __exit__(self, type, value, traceback):
        self.fd.close()
    def getdata(self):
        data = self.fd.read()
        return (data)

def print_formated(data):
    i = 1
    count = 0
    while i < len(data) - 1:
        if data[i] == '{':
            count += 1
            end = "\n"+("   " * count)
            print(data[i], end=end)
        elif data[i] == '}':
            count -= 1
            end = "\n"+("   " * count)
            print(end + data[i], end="")
        elif data[i] == '[':
            end = "\n"+("   " * count)
            print(data[i], end=end)
            i +=1
            while data[i] and data[i] != ']':
                if data[i] == ',':
                    print(data[i], end=end)
                else:
                    print(data[i], end="")
                i += 1
            if data[i] != ']':
                exit("ERROR")
            print(data[i], end=end)
        elif data[i] == ',':
            print(data[i], end=end)
        elif data[i] != '\n' and data[i] != '\t':
            print(data[i], end="")
        i += 1

with Loadjson('list.json') as js:
    data = js.getdata()
    print_formated(data)


