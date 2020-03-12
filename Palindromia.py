# Определить является ли слово палиндромом
# Determine if a word is a palindrome
a=list(input().split())
k=0
for i in a:
    if a[0]==a[-1]:
        k+=1
print (k)

a=input()
b=len (a)
for i in range (b//2):
    if a[i]!=a[-1-i]:
        print ("НЕ Палиндром")
        quit()
print ("Палиндром")
