string ='ierdna si eman ym ih'


# def reverse(str):
#     ans = []
#     for s in range(len(string)-1, 0, -1):
#         ans.append(string[s])
        

#     sentence = ' '.join(ans)
#     return sentence

# result = reverse(string)
# print(result) 
#O(n)

def swap(string, a, b):
    string = list(string)
    temp = string[a]
    string[a] = string[b]
    string[b] = temp
    return ''.join(string)

def smarter_method(string):
    for i in range(len(string)//2):
        string = swap(string, i, len(string)-i-1)
    return string

print(smarter_method(string))



#Build in Method
# list1 = list(string)
# list1.reverse()
# print(''.join(list1))

string2 = reversed(string)
print(''.join(string2))
#O(n)