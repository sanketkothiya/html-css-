class person:
countinsatnce=0
    def __init__(self,fname,lname,age):
        person.countinsatnce +=1
        self.fname=fname
        self.lname=lname
        self.age=age

        @classmethod
        def countinsatnce(cls):
        print(f"heloo you call this function in {cls.countinsatnce} and name is{cls.__name__}")

p1=person("sanket","kothiya",20)
print(person.countinsatnce())

