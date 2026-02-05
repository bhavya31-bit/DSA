#creating array
arr = [1,2,3]
print(arr)

#using list()
arr = list((1,2,3))
print(arr)

#single line input
arr = list(map(int, input().split()))
print(arr)

#multi line input
n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

#Operations
arr.append(19)
arr.pop() #last element
arr.pop(2) #element at index 2
arr.insert(1, 15) #insert 15 at index 1
arr.remove(2) #remove first occurrence of 2