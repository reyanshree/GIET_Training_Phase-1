class student:
    def __init__(self):
        self.__id=None
        self.__age=None
        self.__name=None
        self.__marks=None
        
    def set_id(self,id):
        self.__id=id  
    def get_id(self):
        return self.__id
    
    def set_age(self,age):
        self.__age=age
    def get_age(self):
        return self.__age
    
    def set_marks(self,marks):
        self.__marks=marks
    def get_marks(self):
        return self.__marks
    
    def set_name(self,name):
        self.__name=name
    def get_name(self):
        return self.__name
    
    def validate_age(self):
        if(self.__age>20):
            return True
        else:
            return False
    def validate_marks(self):
        if(self.__marks >=0 and self.__marks <=100):
            return True
        else:
            return False
    def course(self,mar):
        d={"CSE":2554,"ECE":3000}
        if(mar>85):
            for i in d:
                d[i]=d[i]-d[i]*0.25
            print("The course offered to you after discount of 25%: ", d)
        else:
            print("The course offered to you",d)
        
        
    def validate_qualification(self):
        if(self.__marks>65 and  self.validate_marks() and self.validate_age()):
            self.course(self.__marks)
            return True
        else:
            return False
sri=student()
sri.set_id(9)
sri.set_name("srinath")
sri.set_age(22)
sri.set_marks(60)

if(sri.validate_qualification()):
    print("Addmission can be done")
else:
    print("Addmission cant be done")
