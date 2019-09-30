from keras.layers import Input, Embedding, Flatten, Dot, Dense
from keras.models import Model
from keras.models import model_from_json
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

class Recommender_Model():
	def __init__(self):
		self.dataset = pd.read_csv('../scripts/goodbooks-10k-master/ratings.csv')
		self.book_data = np.array(list(set(self.dataset.book_id)))
		self.books = pd.read_csv('../scripts/goodbooks-10k-master/books.csv')
		
	def create_net(self):

		train, test = train_test_split(self.dataset, test_size=0.2, random_state=42)
		n_users = len(self.dataset.user_id.unique())
		n_books = len(self.dataset.book_id.unique())

		book_input = Input(shape=[1], name="Book-Input")
		book_embedding = Embedding(n_books+1, 5, name="Book-Embedding")(book_input)
		book_vec = Flatten(name="Flatten-Books")(book_embedding)

		user_input = Input(shape=[1], name="User-Input")
		user_embedding = Embedding(n_users+1, 5, name="User-Embedding")(user_input)
		user_vec = Flatten(name="Flatten-Users")(user_embedding)

		prod = Dot(name="Dot-Product", axes=1)([book_vec, user_vec])
		
		self.model = Model([user_input, book_input], prod)
		self.model.compile('adam', 'mean_squared_error')

		history = self.model.fit([train.user_id, train.book_id], train.rating, epochs=10, verbose=1)
	def train(self):
		# serialize model to JSON
		model_json = self.model.to_json()
		with open("model.json", "w") as json_file:
		    json_file.write(model_json)
		# serialize weights to HDF5
		self.model.save_weights("model.h5")
		print("Saved model to disk")

	def predict(self,user_data):

		json_file = open('model.json', 'r')
		loaded_model_json = json_file.read()
		json_file.close()
		loaded_model = model_from_json(loaded_model_json)
		# load weights into new model
		loaded_model.load_weights("model.h5")
		print("Loaded model from disk")

		loaded_model.compile('adam', 'mean_squared_error')

		# Creating dataset for making recommendations for the first user
		if len(user_data) != len(self.book_data):
			return
		user = np.array([1 for i in range(len(self.book_data))])
		#user = np.array(user_data) #[1,1,0,1,0,0,0......0,1,1]
		predictions = loaded_model.predict([user, self.book_data])
		predictions = np.array([a[0] for a in predictions])
		recommended_book_ids = (-predictions).argsort()[:5]

		return self.books[self.books['id'].isin(recommended_book_ids)]
mod = Recommender_Model()
mod.create_net()
mod.train()

