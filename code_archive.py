import sys
"""This is a module containing methods that perform varying functions"""
def is_isogram(word):
    '''To test if a word is an isogram'''
    if isinstance(word, str) and not word.isalpha():
        print (word, word.isalpha())
        return word, word.isalpha()
    elif isinstance(word, str) and word.isalpha():
        print (word, len(word) == len(set(word)))
        return word, len(word) == len(set(word))
    else:
        raise (TypeError("Argument should be a string"))

def longest(word):
    """To check for the longest word in a string"""
    c = word.split()
    y = [len(i) for i in c]
    for i in c:
        if len(i)==max(y):
            print (i)
            return i
 
def power(a,b):
    """To raise a power without using in-built pow function"""  
    count = 0
    result = 1
    while count != b:
        result *= a
        print (result)
        count += 1

def remove_duplicates(string):
    """to remove duplicate characters in a string"""
    if string.isalpha():
        a=list(set(string))
        a.sort()
        d=[]
        b=[]
        for i in string:
            if string.count(i)>1:
                b.append(i)
        for item in b:
            if not item  in d:
                d.append(item)
                del b[b.index(item)]
        c = "".join(a)
        print (c, len(b))
        return c, len(b)

def is_even(x):
    """to test if a number is even"""
    if x % 2 == 0:
        return True
    else:
        return False

def is_int(x):
    """code to test if a number is an integer(number without fraction)"""
    if (x - int(x)) > 0 or (x - int(x)) < 0:
        return False
    else:
        return True

def digit_sum(n):
    """code to calculate the sum of digits present in a number"""
    total = 0
    while n > 0:   
        total = total + (n%10)
        n=n // 10
        print (total)
    return total

def recur_digit_sum(n):
    '''codes to calculate sum of digits in a number using recursion'''
    a = n % 10
    b = n // 10
    if n < 10:
        return n
    else:
        return a + recur_digit_sum(b)

def recur_root(n):
    a = n % 10
    b = n // 10
    if n < 10:
        return n
    else:
        y = a + recur_root(b)
        if y < 10:
            return y
        else:
            return recur_root(y)

def factorial(x):
    """code to calculate the factorial of positive integers without using math.factorial"""
    fact = 1
    if x<0:
        x=raw_input("Please enter a positive integer:")
    elif x>=0 and (x - int(x)!=0):
         x=raw_input("Please enter a positive integer:")
    elif x==0:
        return fact 
    else:
        while x >= 1:
            fact *= x
            x-=1
        return fact

def is_prime(x):
    """code to test for prime numbers"""
    if x < 2:
        print ("no")
        return False
    else:
        for n in range(2, (x-1)):
            if (x % n) == 0:
                print ("no")
                return False
                break
        print ("yes")
        return True

def reverse(text):
    """code to reverse a string without using list(reversed(x)) function of backward iteration"""
    result = ""
    for i in range(0,len(text)):
        n = len(text)-1
        result += text[n-i]
    return result

def anti_vowel(text):
    """code to remove all vowels from a string"""
    for v in text:
        if v in "aeiouAEIOU":
            text = text.replace(v,"")
            print (text)
        else:
            text = text.replace(v,v)
            print (text)
    return text

def scrabble_score(word):
    """code to calculate word score in scrabble"""
    text = input("Spell out your word:")
    score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}
    total=0
    for i in word:
        i = i.lower()    
        total += score[i]
    print ("word score is: {}".format(total)) #prints a string
    return total

def censor(text, word):
    """code to censor a selected word or character from a group of strings"""
    if word in text:
        return text.replace(word, "*" * len(word))
    else:
        print ("Nothing Matched", text) #prints a tuple

def count(sequence, item):
    """code to count number of time a character occurs in a string"""
    return sequence.count(item)

def main(n):
    is_prime(n)


if __name__ == '__main__':
    main(int(sys.argv[1]))
    
    
