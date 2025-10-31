# Write your solution here
layer = int(input('Layers: '))
length = 2*layer - 1
lines = [[chr(65+layer-1) for i in range(length)] for j in range(length)]

i, j = 0, length

while i<=j:
    if i!=j and i!=0:
        replaced_part = [chr(65+layer-1-i) for x in range(length-2*i)]

        for k in range(i, j):
            lines[k][i:j] = replaced_part
        
    i+=1
    j-=1

for line in lines:
    s = ''
    for letter in line:
        s+= letter
    print(s)
