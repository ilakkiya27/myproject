def checkpalindrome():
    string = input("Enter the string:")
    if(string==string[::-1]):
        print("palindrome")
    else:
        print("not palindrome")
checkpalindrome()
