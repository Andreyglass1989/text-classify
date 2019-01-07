from preprocessing import make_bag, to_one_hot, oha_to_text

bag = []

"""
Positive = label 1
Negative = label 0

"""

def file_to_bow(filepath='data/pos.txt'):
	global bag
	with open(filepath, 'r') as f:
		lines = f.readlines()
		for line in lines:
			escaped_line = line.replace('\n', '')
			bag = make_bag(escaped_line)

file_to_bow(filepath='data/pos.txt')
file_to_bow(filepath='data/neg.txt')

def file_to_oha(filepath='data/pos.txt', label=1):
	my_oha = []
	labels = []
	if filepath.endswith("neg.txt"):
		label = 0
	with open(filepath, 'r') as f:
		lines = f.readlines()
		for line in lines:
			escaped_line = line.replace('\n', '')
			oha = to_one_hot(escaped_line)
			labels.append(label)
			my_oha.append(oha)
	return my_oha, labels


pos_ohas, pos_labels = file_to_oha(filepath='data/pos.txt')
neg_ohas, neg_labels = file_to_oha(filepath='data/neg.txt')

# print(pos_ohas)
# print("-----")
# print(pos_labels)

import numpy as np
X_pos=np.array(pos_ohas)
X_neg=np.array(neg_ohas)

y_pos=np.array(pos_labels)
y_neg=np.array(neg_labels)

X = np.concatenate((X_pos, X_neg), axis=0)
y = np.concatenate((y_pos, y_neg), axis=0)

# X = Training data
# y = labels = target = this actual value of that Training data
print(X)
print(y)
print(len(X) ==14 )
print(len(y) == len(X))