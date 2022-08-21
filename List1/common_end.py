'''

Given 2 arrays of ints, a and b, return True if they have the same first element or they have the same last element.
Both arrays will be length 1 or more.


common_end([1, 2, 3], [7, 3]) → True
common_end([1, 2, 3], [7, 3, 2]) → False
common_end([1, 2, 3], [1, 3]) → True

'''
def common_end(a, b):
  la = len(a)
  lb = len(b)
  return la>0 and lb>0 and (a[0]==b[0] or a[-1]==b[-1])

print(common_end([1, 2, 3], [7, 3])) #→ True
print(common_end([1, 2, 3], [7, 3, 2])) #→ False
print(common_end([1, 2, 3], [1, 3])) #→ True
