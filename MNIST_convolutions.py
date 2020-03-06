import tensorflow as tf
from os import path, getcwd, chdir

# If you are developing in a local
# environment, then grab mnist.npz from the Coursera Jupyter Notebook
# and place it inside a local folder and edit the path to that location

path = f"{getcwd()}/../tmp2/mnist.npz"
config = tf.ConfigProto()
config.gpu_options.allow_growth = True
sess = tf.Session(config=config)

class myCallback(tf.keras.callbacks.Callback):
    def on_epoch_end(self, epoch, logs={}):
        if (logs.get('acc')>=0.998):
            print ('\nReached 99.8% accuracy so cancelling training!')
            self.model.stop_training=True
            
# GRADED FUNCTION: train_mnist_conv
def train_mnist_conv():
    
    callbacks=myCallback()
    
    mnist = tf.keras.datasets.mnist
    (training_images, training_labels), (test_images, test_labels) = mnist.load_data(path=path)
    
    training_images=training_images.reshape(60000, 28, 28, 1)
    training_images=training_images/255.0
    test_images=test_images.reshape(10000, 28, 28, 1)
    test_images=test_images/255.0

    model = tf.keras.models.Sequential([
        tf.keras.layers.Conv2D(64, (3,3), activation='relu', input_shape=(28, 28, 1)),
        tf.keras.layers.MaxPooling2D(2,2),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(256, activation='relu'),
        tf.keras.layers.Dense(10, activation='softmax')])

    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    # model fitting
    history = model.fit(training_images, training_labels, epochs=20, callbacks=[callbacks])
    # model fitting
    return history.epoch, history.history['acc'][-1]

_, _ = train_mnist_conv()
