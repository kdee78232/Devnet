class Car:
    def __init__ (self,manufact,model,year):
        self.manufact=manufact
        self.model=model
        self.year=year
    
    def getdesc(self):
        desc=(f'Car Manufacuter          :{self.manufact}\n'  
              f'Model                    :{self.model}\n'
              f'Year                     :{self.year}')
        return desc 
    
class Truck(Car):
    def getdesc(self):
        desc=(f'Car Manufacuter          :{self.manufact}\n'  
              f'Model                    :{self.model}\n'
              f'Year                     :{self.year}') 
        return desc 


taurus=Car('Ford','GT','2022')
Ram=Truck('Dodge','Lariat','2022')
Ram2=Truck('Dodge','Texas','2022')

print('Taurus\n', taurus.getdesc(), '\n',sep="")
print('Ram\n', Ram.getdesc(), '\n',sep="")
Ram2,Truck(Dodge,Texas,2023

