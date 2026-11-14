class Managedfile:
    def __init__(self,filename):
        print("init")
        self.filename=filename

    def __enter__(self):
        print("Opening file")
        self.filename=open(self.filename,'w')
        return self.filename
    def __exit__(self,exc_type,exc_val,exc_tb):
        if self.filename:
            self.filename.close()
        print("Closing file")

with Managedfile('test.txt') as f:  
    f.write("Hello, World!")
    print("File is being written...")