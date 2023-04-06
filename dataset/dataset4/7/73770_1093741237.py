#If we define a list by:
nums = [[0]*3]*3
#nums = [[0,0,0],[0,0,0],[0,0,0]]
nums[0][1] = 1
print(mums)
# the result is
[[0,1,0],[0,1,0],[0,1,0]]
#I think it is because all the line use the same list variable, but it suppose #not.