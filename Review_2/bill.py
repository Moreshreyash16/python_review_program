'''
@Author: Shreyash More

@Date: 2023-06-17 20:03:30

@Last Modified by: Shreyash More

@Last Modified time: 2023-06-19 20:03:30

@Title : Calculate bill for certain units

'''
def electric_bill_calculator(units):
    """
    Description:
        It counts the electricity bill for units 
    Parameter:
        units: It eletcric units as input
    Return:
        A bill
    """
    bill=0
    if units <=100:
        bill+=units*0
    elif units>100 and units<=200:
        bill+=((units-100)*10)
    elif units>200 and units<=350:
        bill+=1000+((units-200)*15)
    else:
        bill+=1000 + 2250 + ((units-350)*20)

    return bill


def main():
    unit=int(input("Enter units for calculation of bill: "))
    print(f"the bill for {unit} units is :Rs.{electric_bill_calculator(unit)}")

if __name__=="__main__":
    main()
