import string
import logging
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
#stopwords array
stopwords = ['la','de','el','podrias','por','favor']

if _name_ == '_main_':
	sentence= 'Podiras reproducirla cancion de el noa noa , por favor !'

	#tokenizar
	tokens = sentence.split(' ')

	#sentence cleaning

	clean_token=[]

	for token in tokens:

		#remove punctuation
		if all(char in set(string.punctuation) for char in token):
			continue

		#remove numbers
		if token.isdigit():
			continue

		#transform the token to lowcase and remove sentences
		token= token.lower()
		token = token.strip()

		#remove stopworld
		if token in stopwords:
			continue

		

		clean_token.append(token)

	print(tokens)
	print(clean_token)

	count_vect = CountVectorizer()
	bag_of_words_array = count_vect.fit_transform(temp)