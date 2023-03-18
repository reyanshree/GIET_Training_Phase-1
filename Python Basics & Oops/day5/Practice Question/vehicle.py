class vehicle:
    
    def __init__(self,id,type1,cost):
        self.__id=id
        self.__type1=type1
        self.__cost=cost

        if(self.__type1=="Two Wheeler"):
            self.__premium=0.02*self.__cost
        elif(self.__type1=="Four Wheeler"):
            self.__premium=0.06*self.__cost
    def get_id(self):
        return self.__id
    def set_id(self,id):
        self.__id=id
    def get_type(self):
        return self.__type1
    def set_type(self,type1):
        self.__type1=type1
    def get_cost(self):
        return self.__cost
    def set_cost(self,cost):
        self.__cost=cost
    def get_premium(self):
        return self.__premium
    def display(self):
        print("id of vehicle is ",self.__id)
        print("cost of vehicle is ",self.__cost)
        print("premium of vehicle is ",self.__premium)
        print("type of vehicle is ",self.__type1)
bike=vehicle(101,"Two Wheeler",10000)
bike.set_cost(60000)
bike.set_type("Two Wheeler")
bike.set_id(102)
bike.display()
print(bike.get_cost())
print(bike.get_premium())

