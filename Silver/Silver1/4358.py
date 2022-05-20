from collections import defaultdict
import sys

input = sys.stdin.readline

trees = defaultdict(int)
count = 0

while True:
    tree_name = input().strip()
    if not tree_name:
        break
    trees[tree_name] += 1
    count +=1
    
tree_list = list(trees.keys())
tree_list.sort()

for tree in tree_list:
    print("%s %.4f" %(tree, trees[tree]/count*100))
