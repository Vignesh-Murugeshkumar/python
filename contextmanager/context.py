class Managedfile:
    def __init__(self,filename):
        print("init")
        self.filename=filename
        self.file=None

    def __enter__(self):
        print("Opening file")
        self.file=open(self.filename,'w')
        return self.file
    def __exit__(self,exc_type,exc_val,exc_tb):
        if self.file:
            self.file.close()
        print("Closing file")

with Managedfile('test.txt') as f:  
    f.write("Hello, World!")
    print("File is being written...")