## improved solution



X = [x.strip() for x in open('input.txt')]
Q = []
for elf in ('\n'.join(X).split('\n\n')):
    q = 0
    for x in elf.split('\n'):
        q += int(x)
    Q.append(q)

Q.sort()
print(Q[-1])
print(Q[-1]+Q[-2]+Q[-3])





# max = 0
# count = 0
# max_list = []


# with open('input.txt', 'a') as f:
#         f.write('\n')
# for x in open('input.txt'):
#     if x != '\n':
#         x = int(x)
#         # breakpoint()
#         count = count + x
#     else:
#         if len(max_list)<3:
#             max_list.append(count)
#             max_list.sort()
#             # print(max_list)
#         else:
#             if any(count> i for i in max_list):
#                 # if count == 10000:
#                 for i,it in enumerate(max_list):
#                     if it<count:
#                         max_list[i] = count
#                         max_list.sort()
#                         break

#         if count>max:
#             max = count
#         count = 0
# print(max)
# print(max_list)
# print(sum(max_list))

