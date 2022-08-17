"""
  Given a number n, return True if n is in the range 1..10, inclusive. 
  Unless "outsideMode" is True, in which case return True if the number is 
  less or equal to 1, or greater or equal to 10.

  """
def in1to10(num,outsidemode):
    if not outsidemode:
        return num in range(1,11)
    else:
        return num<=1 or num>=10
print(in1to10(11,True))

