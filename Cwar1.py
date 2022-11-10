
def longest_consec(s, k):
    return max(["".join(s[i:i+k]) for i in range(len(s)-k+1)], key=len) if s and 0 < k <= len(s) else ""

# def longest_consec(strarr, k):
#     contr = []
#     if len(strarr) == 0 or k > len(strarr) or k <= 0:
#         contr = ""
#     else:
#         for i in range(0, len(strarr)):
#             l = ''
#             for j in range(0, k):
#                 if i + k <= len(strarr):
#                     l += strarr[i + j]
#                 else:
#                     break
#             if l != "":
#                 contr.append(l)
#         print(contr)
#         max = 0
#         for i in contr:
#             if len(i) > max:
#                 max = len(i)
#         print(max)
#         hold = ''
#         for i in contr:
#             print(len(i))
#             if len(i) == max:
#                 hold = i
#                 print('yes')
#                 break
#         contr = hold
#         print(hold)
#     return contr

f = longest_consec(["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"], 1)
print(f)