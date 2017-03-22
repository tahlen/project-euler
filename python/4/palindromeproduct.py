# Find largest palindrome product formed by two factors with ARG digits
# ex. arg = 2 find largest palindrome product formed by two 2-digit factors
def findLargestPalindrome(arg):
    list1 = range(10**(arg))
    
    # if True, attempt to speed up search by reducing list by 90%
    # does not guarantee correct answer
    cut = True
    if arg > 2 and cut:
        for x in range(9 * 10**(arg-1)):
            list1.remove(x)

    list2 = list1
    largestPalindrome = 0

    for x in list1:
        for y in list2:
            print(str(x) + ' * ' + str(y))
            if isPalindrome(x * y) and x * y > largestPalindrome:
                largestPalindrome = x * y
                print('largest: ' + str (largestPalindrome))

    return largestPalindrome

# Takes int as arg, returns true if arg is palindrome
def isPalindrome(arg):
    
    # Split arg into list
    # Convert to string first because easier
    lst = list(str(arg))
    
    # Compare first elem to last, second elem to second-to-last, etc.
    # Return false if any don't match, else true
    n = 0
    while n <= len(lst)/2:
        if not lst[n] == lst[-(n+1)]:
            return False
        n += 1
    return True

while True:
    print(findLargestPalindrome(input()))
