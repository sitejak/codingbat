# def first_last6(nums):
#
#        if len(nums)>=1 and nums[0] == nums[-1]:
#          print("True")
#        else:
#            print("False")
#
#
# #
# first_last6([1, 2, 6])

# def sum3(nums):
#
#     print(nums[::-1])
#
# sum3([1,2,3])


# Given an array of ints, return the sum of the first 2 elements in the array.
# If the array length is less than 2, just sum up the elements that exist, returning 0 if the array is length 0.


def sum2(nums):

  if len(nums)<=2:
      print(sum(nums))
  elif len(nums) == 0:
      print(0)
      
sum2([1,2,3])
sum2([1, 1])
sum2([1, 1, 1, 1])