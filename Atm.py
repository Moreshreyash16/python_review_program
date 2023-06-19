'''
@Author: Shreyash More

@Date: 2023-06-17 20:03:30

@Last Modified by: Shreyash More

@Last Modified time: 2023-06-19 20:03:30

@Title : Calculate minimum number of notes

'''
#logic 1
def note_count(goal):
    """
    Description:
        It counts the minimum number of notes 
    Parameter:
        goal: It takes goal amount as input
    Return:
        A dictionary
    """
    money_count={1000:0, 500:0, 200:0, 100:0, 50:0, 20:0, 10:0, 5:0, 2:0, 1:0}
    money=[1000,500,200,100,50,20,10,5,2,1]
    result=0
    for i in money:
        count=0
        if result!=goal:
            while(True):
                if result==goal:
                    money_count[i]=str(count)
                    break
                else:
                    result+=i
                    count+=1
                    if result>goal:
                        result-=i
                        count-=1
                        money_count[i]=str(count)
                        break
    return money_count

# Logic 2
def note_count_2(goal):
    """
    Description:
        It counts the minimum number of notes 
    Parameter:
        goal: It takes goal amount as input
    Return:
        A dictionary
    """
    money_count={1000:0, 500:0, 200:0, 100:0, 50:0, 20:0, 10:0, 5:0, 2:0, 1:0}
    new_dict={}
    money=[1000,500,200,100,50,20,10,5,2,1]
    while(True):
        try:
            if goal>0:
                for i in money:
                        money_count[i]=goal//i
                        goal=goal%i
                        
                for key,value in money_count.items():
                    if value!=0:
                        new_dict[key]=value
                
                return new_dict
                break
            else:
                print("\nEnter a amount greater than zero\n")
        except ValueError:
            print("Enter a Integer ")

def main():
    goal=int(input("\nEnter the amount you want to count the notes : "))
    print(note_count(goal))
    print(note_count_2(goal))

if __name__=="__main__":
    main()