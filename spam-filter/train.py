from preprocessing import make_bag, to_one_hot, oha_to_text

bag = []

def file_to_bow(filepath='data/pos.txt'):
	global bag
	with open(filepath, 'r') as f:
		lines = f.readlines()
		for line in lines:
			escaped_line = line.replace('\n', '')
			bag = make_bag(escaped_line)

file_to_bow(filepath='data/pos.txt')
file_to_bow(filepath='data/neg.txt')

def file_to_oha(filepath='data/pos.txt'):
	my_oha = []
	with open(filepath, 'r') as f:
		lines = f.readlines()
		for line in lines:
			escaped_line = line.replace('\n', '')
			oha = to_one_hot(escaped_line)
			my_oha.append(oha)
	return my_oha


pos_ohas = file_to_oha(filepath='data/pos.txt')
neg_ohas = file_to_oha(filepath='data/neg.txt')

print(pos_ohas, neg_ohas)

