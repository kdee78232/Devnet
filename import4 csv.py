class Car:
    def __int__(self,manufact,model,year):
        self.manufact=manufact
        self.model=model
        self.year=year
    
    def getdesc(self):
        desc=(f'Car Manufacuter      :{self.manufact}\n'  
              f'Model                 :{self.model}\n'
              f'Year                  :{self.year}')
        return desc  

taurus=Car('Ford','GT','2022')

print('Taurus\n', taurus.getdesc(), '\n',sep="")