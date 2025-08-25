import tensorflow as tf

from tensorflow.keras.models import Model
from tensorflow.keras.layers import (Input, BatchNormalization, Conv2D, MaxPool2D,
                                     Dropout, Flatten, Dense)
from tensorflow.keras.optimizers import Adam


def model_ana_class100_s1(input_shape=(32, 32, 3), learning_rate=1e-3):
    input = Input(shape=input_shape)
    
    x = BatchNormalization()(input)
    x = Conv2D(64, (5, 5), padding='same', activation='relu')(x)
    x = Conv2D(64, (1, 1), padding='same', activation='relu')(x)

    x = BatchNormalization()(x)
    x = MaxPool2D(pool_size=(4, 4))(x)
    x = Dropout(0.15)(x)

    x = Conv2D(64, (3, 3), padding='same', activation='relu')(x)
    x = BatchNormalization()(x)
    x = Dropout(0.15)(x)

    x = Conv2D(64, (3, 3), padding='same', activation='relu')(x)
    x = BatchNormalization()(x)
    x = MaxPool2D(pool_size=(4, 4))(x)
    x = Dropout(0.15)(x)

    x = Conv2D(32, (3, 3), padding='same', activation='relu')(x)
    x = BatchNormalization()(x)
    x = Dropout(0.15)(x)

    x = Conv2D(32, (3, 3), padding='same', activation='relu')(x)
    x = BatchNormalization()(x)
    x = MaxPool2D(pool_size=(2, 2))(x)

    x = Flatten()(x)
    x = Dropout(0.5)(x)

    # Output layer for classification
    output = Dense(100)(x)  # No activation, using from_logits=True

    model = Model(inputs=input, outputs=output)

    model.compile(
        loss=tf.keras.losses.CategoricalCrossentropy(from_logits=True),
        optimizer=Adam(learning_rate=learning_rate),
        metrics=["accuracy"]
    )

    model.summary()

    return model


def model_ana_class100_s2(input_shape=(32, 32, 3), learning_rate=1e-3):
    input = Input(shape=input_shape)

    x = BatchNormalization()(input)
    x = Conv2D(32, (5, 5), padding='same', activation="relu")(x)

    x = BatchNormalization()(x)
    x = MaxPool2D(pool_size=(4, 4))(x)
    x = Dropout(0.15)(x)

    x = Conv2D(32, (3, 3), padding='same', activation="relu")(x)
    x = BatchNormalization()(x)
    x = Dropout(0.15)(x)

    x = Conv2D(48, (3, 3), padding='same', activation="relu")(x)
    x = BatchNormalization()(x)
    x = MaxPool2D(pool_size=(4, 4))(x)
    x = Dropout(0.15)(x)

    x = Conv2D(48, (3, 3), padding='same', activation="relu")(x)
    x = BatchNormalization()(x)
    x = Dropout(0.15)(x)

    x = Conv2D(64, (3, 3), padding='same', activation="relu")(x)
    x = BatchNormalization()(x)
    x = MaxPool2D(pool_size=(2, 2))(x)
    x = Dropout(0.15)(x)

    x = Conv2D(64, (3, 3), padding='same', activation="relu")(x)
    x = BatchNormalization()(x)
    x = Flatten()(x)
    x = Dropout(0.3)(x)

    # Output layer for 100-class classification
    output = Dense(100)(x)

    model = tf.keras.Model(inputs=input, outputs=output)

    model.compile(
        loss=tf.keras.losses.CategoricalCrossentropy(from_logits=True),
        optimizer=tf.keras.optimizers.Adam(learning_rate=learning_rate),
        metrics=["accuracy"]
    )

    model.summary()

    return model