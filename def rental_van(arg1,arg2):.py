

def van(arg1,arg2):
    total_vans= arg2/arg1
    return total_vans



van_capacity= input(f"Please enter the van capacity=> ")
total_passengers= input(f"Please enter your total passengers=> ")
arg1= int(van_capacity)
arg2=int(total_passengers)

print(van(arg1,arg2))




