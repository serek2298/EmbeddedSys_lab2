print('zadanie 1')
X = input('Enter something')
dict1 = {"a": 1}
for i in X:
    if (i != ' ') & (i != '.'):
        dict1[i] = i
print('Number of diffrent signs exluding space and dot: ', len(dict1.keys()))
print('zadanie 2')
f = open("text.txt", "r")
with open("text.txt", "r") as f:
    string = f.read()
    dict2={"a":1}
    for i in string:
        if (i != ' ') & (i != '.'):
            dict2[i] = i
    print('Number of diffrent signs exluding space and dot: ', len(dict2.keys()))
print('zadanie 3')
nums = [10, 25, 3, 4, 5, 6, 7, 43, 1, 321, 21]
min = 0
for count, it in enumerate(nums):
    if(it < nums[min]):
        min = count
print('Lowest num is: ', nums[min])
