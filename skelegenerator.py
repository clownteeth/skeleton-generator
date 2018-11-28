#Special imports to make things work.
import random
import os

#Find where the files are
file1 = "Casket.txt"
file2 = "Tomb.txt"

#Create empty lists.
skelepowers = []
skeleparts = []

#Fill lists with file content.
with open(file1) as target_graves:
    for skeleton in target_graves:
    	skeleparts.append(skeleton)

with open(file2) as target_graves:
	for skeleton in target_graves:
		skelepowers.append(skeleton)

#test time
newskeleton = str.strip(skelepowers[random.randint(0, (len(skelepowers)-1))])
newbones = skeleparts[random.randint(0, (len(skeleparts)-1))]

print(newskeleton.rstrip() + newbones.rstrip() + " the skeleton")