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


print(bag)

