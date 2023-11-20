class Car:

    @property
    def model(self):
        return  self.__model
    
    @model.setter
    def model(self,model):
        if all([type(model)==str,1<len(model)<101,]):
            self.__model=model

car = Car()
car.model = "Toyota"
print(car.__dict__)


        