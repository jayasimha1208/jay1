class employee:
    def __init__(self,id=0,name=None,sal=0.0):
        self.id=id
        self.na=name
        self.sal=sal
    def display(self):
        print(self.id)
        print(self.na)
        print(self.sal)
e1=employee(name="jai",id=101)
e1.display()
