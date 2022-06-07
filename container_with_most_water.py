# def maxArea(height):
#     width = len(height) - 1
#     most_water = 0
#     for firt_pointer in range(width):
#         for second_pointer in range(firt_pointer, width + 1):
#             if height[firt_pointer] < height[second_pointer]:
#                 temp = height[firt_pointer] * (second_pointer - firt_pointer)
#                 if most_water < temp:
#                     most_water = temp
#             else:
#                 temp = height[second_pointer] * (second_pointer - firt_pointer)
#                 if most_water < temp:
#                     most_water = temp
#  #####################################################################################################################
#         width = len(height) - 1
#         most_water = 0
#         for firt_pointer in range(width):
#             for second_pointer in range(firt_pointer, width + 1):
#                 temp = min(height[firt_pointer], height[second_pointer]) * (second_pointer - firt_pointer)
#                 result = max(most_water, temp)
#                 most_water = result
#         return most_water
#     print(most_water)
def maxArea(height):
    n = len(height)
    right_pointer = n - 1
    left_pointer = 0
    most_water = 0

    while left_pointer < right_pointer:
        temp = min(height[left_pointer], height[right_pointer]) * (right_pointer - left_pointer)
        most_water = max(temp, most_water)

        if height[left_pointer] > height[right_pointer]:
            right_pointer -= 1
        else:
            left_pointer += 1

    print(most_water)

maxArea([4,4,2,11,0,11,5,11,13,8])