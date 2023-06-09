def print_even_odd(choice,n):
    count=1
    even_list=[]
    odd_list=[]
    if(choice==1):
        while(len(even_list)<n):
            if count%2==0:
                even_list.append(count)
            count+=1
        return even_list
    elif(choice==2):
        while(len(odd_list)<n):
            if count%2!=0:
                odd_list.append(count)
            count+=1
        return odd_list
    else:
        print(" Please select a valid choice")
        return 0  


def main():
    
    while(True):
        print(" Enter 1 to continue \n Enter 2 to exit  ")
        user_input=int(input("Enter a choice : "))
        if user_input==1:
            user_choice=int(input(("Enter a choice 1 for even numbers and 2 for odd numbers : ")))
            user_count=int(input("How many number you want? : "))
            print(f"The list of your choice : {print_even_odd(user_choice,user_count)}")
            print("")
        elif user_input==2:
            print("Exit succesfull")
            break
        else:
            print("Enter a valid choice")

if __name__ == "__main__":
    main()

