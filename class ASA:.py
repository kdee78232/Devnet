class ASA:
    def __init__ (self,model,location,ip_add):
        self.model=model
        self.location=location
        self.ip_add=ip_add

    def getdesc (self):
        desc= f'model       :{self.model}\n'\
              f'location    :{self.location}\n'\
              f'ip_add      :{self.ip_add}'
        return desc

class WLC(ASA):
    def getdesc (self):
        desc= f'model       :{self.model}\n'\
              f'location    :{self.location}\n'\
              f'ip_add      :{self.ip_add}'
        return desc
            
ASA1=ASA('2504','BLDG_1','10.1.1.1')
WLC1=WLC('2526','HQ','8.8.8.8')  
print("ASA1\n",ASA1.getdesc(), '\n',sep='')  
print("WLC1\n",WLC1.getdesc(),'\n', sep='')     
            