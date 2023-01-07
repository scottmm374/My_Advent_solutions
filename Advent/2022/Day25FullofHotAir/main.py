import math


# nums = {
#     0:1,
#     1: 5,
#     2: 25, 
#     3: 125, 
#     4: 625, 
#     5: 3125, 
#     6: 15625, 
#     7: 78125, 
#     8: 390625, 
#     9: 1953125, 
#     10: 9765625, 
#     11: 48828125, 
#     12: 244140625, 
#     13: 1220703125, 
#     14: 6103515625, 
#     15: 30517578125, 
#     16: 152587890625, 
#     17: 762939453125, 
#     18: 3814697265625, 
#     19: 19073486328125, 
#     20: 95367431640625, 
#     21: 476837158203125
#     }
# total = 0


# # for x in range(1, 22):
# #     nums[x] = round(math.pow(5, x))



# def calc_val(data):
#     subtotal = 0
#     reverse = data[::-1]
    
#     for x in range(len(reverse)):
#         if reverse[x] == "1":
#             y = nums[x]
#             subtotal += y
#             # print("1: ", y)
#         elif reverse[x] == "2":
#             w = (nums[x]) * 2
#             subtotal += w
#             # print("2", w)
#         elif reverse[x] == '-':
#              z = nums[x]
#              subtotal -= z
#             #  print("-", z)
#         elif reverse[x] == "=":
#             q = (nums[x]) * 2
#             subtotal -= q
#             # print("=" ,q)
#         else:
#             continue
#         # print(subtotal)
#     return subtotal
        

# with open('input.txt', 'r') as file:
#     lines = file.readlines()
#     total = 0
#     for x in lines:
#         z = calc_val(x.strip())
#         total += z
#     print(total)

# calc_val(data_string)

x =  32005641587247

a = 19073486328125 * 2
b = 3814697265625 * 2

print ((b + a) - x)