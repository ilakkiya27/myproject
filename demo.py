def palindrome():
    string = input("Enter the string:")
    if(string==string[::-1]):
        print("palindrome")
    else:
        print("not palindrome")
palindrome()
