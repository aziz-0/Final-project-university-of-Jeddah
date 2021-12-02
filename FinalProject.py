def creditCard(cardNumber):
    strCardNumber = str(cardNumber) # we need to convert the integer numbers to string
    hideCardNum = '' # this variable will contain the hidden card numbers except the last 4 numbers will not be hidden

    # get insdie for loop to hide every number with ("*") except the last 4 numbers we want them to be not hidden
    for i in strCardNumber[:-4]: # here i wrote [:-4] to make sure that the last 4 numbers will not be hidden
        hideCardNum = hideCardNum + '*'
    # now get out from the for loop

    # now we are out from the for loop and we want in this code below to print the last 4 numbers without hiding them
    # to be just like this for example ***********8375.
    # strCardNumber[-4:] contains the indexes of the last 4 numbers.
    hideCardNum = hideCardNum + strCardNumber[-4:]
    # now the (hideCardNum) contain the hidden numbers except the last 4 numbers they are not hidden.

    return hideCardNum
 # now we need to run the function by calling it with a few steps, i wrote them below

result = creditCard(4284884791351130) # here we call the function and it has a credit card number as a parameter
print(result)
