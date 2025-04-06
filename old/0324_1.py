fruits = ["りんご", "ばなな", "みかん", "りんご", "りんご", "みかん"]

count_dict = dict()
for i in fruits:
    if i in count_dict:
        count_dict[i] += 1
    else:
        count_dict[i] = 1

print(count_dict)