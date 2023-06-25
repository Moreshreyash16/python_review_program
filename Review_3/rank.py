'''
@Author: Shreyash More

@Date: 2023-06-24 11:35:30

@Last Modified by: Shreyash More

@Last Modified time: 2023-06-25 12:35:30

@Title : Count the rank of number and append it in list
'''
def count_rank(user_list):
    """
    Description:
        It calculates the rank of numbers inside list
    Parameter:
        user_list:Takes list as input
    Return:
        Returns the new list
    """
    new_list=[]
    for i in user_list:
        count=1
        for j in user_list:
            if i>j:
                count+=1
        new_list.append(count)
    return new_list

def main():
    user_input=list(map(int,input("enter space seperated values ").split()))
    print(f"The original list is {user_input} and the rank list is :{count_rank(user_input)}")

if __name__=="__main__":
    main()