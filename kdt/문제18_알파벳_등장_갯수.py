word = input()

# my_dict = {}

# for i in range(len(word)):
#   if word[i] in my_dict:
#     my_dict[word[i]] += 1
#   else:
#     my_dict[word[i]] = 1

# for c, i in my_dict.items():
#   print(c,i)


# get()으로 풀어보셔
my_dict = {}

for i in range(len(word)):
   my_dict[word[i]] =  my_dict.get(word[i],0) + 1

for c, i in my_dict.items():
  print(c,i)