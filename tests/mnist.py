import glob
import os
import gzip
import pickle
import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt
from helpers import pickle_model, normalize
from src.model import model


# load data
with gzip.open('../datasets/mnist/mnist.pkl.gz', 'rb') as f:
    train_set, valid_set, test_set = pickle.load(f, encoding='latin1')

train_x, train_y = train_set
valid_x, valid_y = valid_set
test_x, test_y = test_set

m = train_x.shape[0]

# show image
# img_idx = 23
# plt.imshow(train_x[img_idx].reshape((28, 28)), cmap=cm.Greys_r)
# plt.show()

# map train_y to output vector
y = np.zeros((10, m))
y[train_y.reshape(1, m) - 1, np.arange(m)] = 1

hyp_params = {
    'epochs': 500,
    'learning_rate': 0.1,
    'layers_dims': [28 * 28, 10, 10],
    'print_cost': True
}

X = normalize(train_x)
model = model(X.T, y, **hyp_params)

pickle_name = '../datasets/mnist/model-alpha-{0}-iterations-{1}.pickle'\
    .format(hyp_params['learning_rate'], hyp_params['epochs'])

pickle_model(pickle_name, model)
