import tensorflow as tf
from tensorflow import keras
from config import config
from notifierbot.telegram.tf_callback import TelegramCallback

# Define the Keras model to add callbacks to
def get_model():
    model = keras.Sequential()
    model.add(keras.layers.Dense(1, input_dim=784))
    model.compile(
        optimizer=keras.optimizers.RMSprop(learning_rate=0.1),
        loss="mean_squared_error",
        metrics=["mean_absolute_error"],
    )
    return model

def load_data():
    # Load example MNIST data and pre-process it
    (x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
    x_train = x_train.reshape(-1, 784).astype("float32") / 255.0
    x_test = x_test.reshape(-1, 784).astype("float32") / 255.0

    # Limit the data to 1000 samples
    x_train = x_train[:1000]
    y_train = y_train[:1000]
    x_test = x_test[:1000]
    y_test = y_test[:1000]

    return (x_train, y_train), (x_test, y_test)

if __name__ == "__main__":
    # Get Data
    (x_train, y_train), (x_test, y_test) = load_data()

    # Initialize Callback
    callback = TelegramCallback(config, train = True, predict = True,
                                test = True, epochs = False)

    # Initialize Model
    model = get_model()

    # Train the model
    model.fit(
        x_train,
        y_train,
        batch_size=128,
        epochs=1,
        verbose=0,
        validation_split=0.5,
        callbacks=[callback],
    )

    # Model Testing
    res = model.evaluate(
        x_test, y_test, batch_size=128, verbose=0, callbacks=[callback]
    )

    # Model Predicting
    res = model.predict(x_test, batch_size=128, callbacks=[callback])