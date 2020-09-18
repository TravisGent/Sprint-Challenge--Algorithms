'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    count = 0
    if len(word) >= 2:
        if word[0] + word[1] == "th":
            count += 1
        count += count_th(word[1:])
    return count

# count = # 1 # thth
# if len(word) >= 2:
#     if word[0] + word[1] == "th":
#         count += 1
#     count += #count_th(word[1:])
# 
#         count = # 0 # hth
#         if len(word) >= 2:
#             if word[0] + word[1] == "th":
#                 count += 1
#             count += #count_th(word[1:])
# 
#                 count = # 1 # th
#                 if len(word) >= 2:
#                     if word[0] + word[1] == "th":
#                         count += #count_th(word[1:])
#                     count += 0
#                 return count
# 
#                     count = # 0 # h 
#                     if len(word) >= 2:
#                         if word[0] + word[1] == "th":
#                             count += 0
#                         count += 0
#                     return count
#         return count
# return count