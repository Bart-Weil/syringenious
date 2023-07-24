import random
import string
import english_words

alph = list(string.ascii_lowercase)

k = 4

n_data = []

for i in english_words.english_words_lower_alpha_set:

	if len(i) >= max(8,k):

		n_data.append(i)

secs = []

for i in n_data:

	for j in range(len(i)-k):

		secs.append(i[j:(j+k+1)])

secs = list(set(secs))

ends = list(set([i[-k:] for i in n_data]))

def generate(n):

	word = random.choice(n_data)[:k]

	while True:

		compat = []

		for i in secs:

			if i[0:k-1] == word[-k+1:]:

				compat.append(i)

		if len(compat) == 0:

			print("fail")
			return word

		word += random.choice(compat)[k-1]

		if word[-k:] in ends and len(word)>=n:

			return word

for i in range(100):
	print(generate(5))

