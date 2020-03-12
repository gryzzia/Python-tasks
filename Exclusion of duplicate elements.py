# Условие: вводится текст, необходимо исключить из него повторяющиеся элементы
a=input()
b=' '
for i in range(len(a)):
    if b.find(a[i]) == -1 and a[i] != ' ':
        b+= a[i]
print(b)
