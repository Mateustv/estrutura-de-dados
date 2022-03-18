def isPalindrome(x:int):
    numberTest = str(x)
    return numberTest == numberTest[::-1]
teste = isPalindrome(151)
print(teste)