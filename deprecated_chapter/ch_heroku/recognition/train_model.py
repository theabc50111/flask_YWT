# Import datasets, classifiers and performance metrics
from sklearn import svm, metrics
from sklearn.model_selection import train_test_split
import tensorflow as tf
import pickle

(ori_x_train, ori_y_train), (ori_x_test, ori_y_test) = tf.keras.datasets.mnist.load_data()

# flatten the images
n_samples = len(ori_x_train)
data = ori_x_train.reshape((n_samples, -1))
clf = svm.SVC(C=0.57,gamma=0.0000001, verbose=True, cache_size=50000)

# Split data into 50% train and 50% test subsets
X_train, X_valid, y_train, y_valid = train_test_split(
    data, ori_y_train, test_size=0.1, shuffle=True)

# Learn the digits on the train subset
clf.fit(X_train, y_train)
train_pred = clf.predict(X_train)
print("train_pred acc",metrics.accuracy_score(train_pred,y_train))

# Predict the value of the digit on the test subset
valid_pred = clf.predict(X_valid)
print("valid_pred acc",metrics.accuracy_score(valid_pred,y_valid))

# Saving model
with open("model.pickle","wb") as f:
    pickle.dump(clf, f, protocol=pickle.HIGHEST_PROTOCOL)