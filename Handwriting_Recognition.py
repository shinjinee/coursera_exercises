import tensorflow as tf
from os import path, getcwd, chdir

#If you are developing in a local
# environment, then grab mnist.npz from the Coursera Jupyter Notebook
# and place it inside a local folder and edit the path to that location
path = f"{getcwd()}/../tmp2/mnist.npz"

class myCallbacks(tf.keras.callbacks.Callback):
    def on_epoch_end(self, epoch, logs={}):
        if logs.get('acc')>=0.99:
            print('\nReached 99% accuracy so cancelling training!')
            self.model.stop_training=True
            
# GRADED FUNCTION: train_mnist
def train_mnist():
   
    callbacks=myCallbacks()
   
   mnist = tf.keras.datasets.mnist

    (x_train, y_train),(x_test, y_test) = mnist.load_data(path=path)
    x_train, x_test=x_train/255.0, x_test/255.0
  
    model = tf.keras.models.Sequential([
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(1024, activation=tf.nn.relu),
        tf.keras.layers.Dense(10, activation=tf.nn.softmax)])

    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    
    # model fitting
    history = model.fit(x_train, y_train, epochs=10, callbacks=[callbacks])
    # model fitting
    return history.epoch, history.history['acc'][-1]
    
train_mnist()
