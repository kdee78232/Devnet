# Calculation for bi-weekly pay



hourly_rate=input('Please enter your pay rate' ':' '\n' '>')
paycheck= float(hourly_rate)*40
after_tax= paycheck * 0.25
print("this is your take home earnings",":" "\n" "$" ,float(after_tax))

def paycheck(money):
    paycheck=(money*80)*0.08
    return (round(paycheck,-4))

paycheck(46.89)