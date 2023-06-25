'''
@Author: Shreyash More

@Date: 2023-06-24 11:35:30

@Last Modified by: Shreyash More

@Last Modified time: 2023-06-25 12:35:30

@Title : 
Create a function that takes a string and returns a new string with its first and last characters swapped, except under two conditions:If the length of the string is less than two, return "Incompatible.".
If the first and last characters are the same, return "Two's a pair.".
ExamplesflipEndChars("Cat, dog, and mouse.") ➞ ".at, dog, and mouseC"

flipEndChars("ada") ➞ "Two's a pair."

flipEndChars("Ada") ➞ "adA"

flipEndChars("z") ➞ "Incompatible."

'''
def flipEndChars(letters):
    """
    Description:
        It swaps the first and last letter of string
    Parameter:
        letters:Takes string  as input
    Return:
        Returns the new string
    """
    length=len(letters)
    new_string=""
    if length<=2:
        return "Incompatible."
    elif letters[0]==letters[length-1]:
        return "Two's a pair."
    else:
        new_string+=letters[length-1]+letters[1:length-1]+letters[0]
        return new_string

def main():
    sent=input("Enter a sentence or word: ")
    print(flipEndChars(sent))

if __name__=="__main__":
    main()