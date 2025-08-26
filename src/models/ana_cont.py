import tensorflow as tf

from tensorflow.keras.models import Model
from tensorflow.keras.layers import (Input, BatchNormalization, Conv2D, MaxPool2D,
                                     Dropout, Flatten, Dense)
from tensorflow.keras.regularizers import l2
from tensorflow.keras.optimizers import Adam


def model_ana_cont_s0(input_shape=(32, 32, 3), learning_rate=1e-3):
    input = Input(shape=input_shape)

    x = BatchNormalization()(input)
    x = Conv2D(16, (3, 3), padding='same', activation="relu")(x)
    x = MaxPool2D(pool_size=(2, 2))(x)

    x = BatchNormalization()(x)
    x = Conv2D(32, (3, 3), padding='same', activation="relu")(x)
    x = MaxPool2D(pool_size=(2, 2))(x)

    x = BatchNormalization()(x)
    x = Conv2D(64, (3, 3), padding='same', activation="relu")(x)
    x = MaxPool2D(pool_size=(2, 2))(x)

    x = BatchNormalization()(x)
    x = Conv2D(128, (3, 3), padding='same', activation="relu")(x)
    x = MaxPool2D(pool_size=(2, 2))(x)

    x = Flatten()(x)

    x = BatchNormalization()(x)
    x = Dense(128, activation="relu", kernel_regularizer=l2(1e-4))(x)
    x = Dropout(0.3)(x)

    x = Dense(64, activation="relu", kernel_regularizer=l2(1e-4))(x)

    output = Dense(2)(x)

    model = Model(inputs=input, outputs=output)

    model.compile(
        loss="mse",
        optimizer=Adam(learning_rate=learning_rate),
        metrics=["mse"]
    )

    model.summary()

    return model


def model_ana_cont_s1(input_shape=(32, 32, 3), learning_rate=1e-3):
    input = Input(shape=input_shape)

    x = BatchNormalization()(input)
    x = Conv2D(16, (3, 3), padding='same', activation="relu")(x)
    x = MaxPool2D(pool_size=(2, 2))(x)

    x = BatchNormalization()(x)
    x = Conv2D(32, (3, 3), padding='same', activation="relu")(x)
    x = MaxPool2D(pool_size=(2, 2))(x)

    x = BatchNormalization()(x)
    x = Conv2D(64, (3, 3), padding='same', activation="relu")(x)
    x = MaxPool2D(pool_size=(2, 2))(x)

    x = BatchNormalization()(x)
    x = Conv2D(64, (3, 3), padding='same', activation="relu")(x)
    x = MaxPool2D(pool_size=(2, 2))(x)

    x = Flatten()(x)

    x = BatchNormalization()(x)
    x = Dense(128, activation="relu", kernel_regularizer=l2(1e-4))(x)
    x = Dropout(0.3)(x)

    x = Dense(64, activation="relu", kernel_regularizer=l2(1e-4))(x)

    output = Dense(2)(x)

    model = Model(inputs=input, outputs=output)
    model.compile(
        loss="mse",
        optimizer=Adam(learning_rate=learning_rate),
        metrics=["mse"]
    )
    model.summary()

    return model


def model_ana_cont_s2(input_shape=(32, 32, 3), learning_rate=1e-3):
    input = Input(shape=input_shape)

    x = BatchNormalization()(input)
    x = Conv2D(16, (3, 3), padding='same', activation="relu")(x)
    x = MaxPool2D(pool_size=(2, 2))(x)

    x = BatchNormalization()(x)
    x = Conv2D(32, (3, 3), padding='same', activation="relu")(x)
    x = MaxPool2D(pool_size=(2, 2))(x)

    x = BatchNormalization()(x)
    x = Conv2D(32, (3, 3), padding='same', activation="relu")(x)
    x = MaxPool2D(pool_size=(2, 2))(x)

    x = BatchNormalization()(x)
    x = Conv2D(64, (3, 3), padding='same', activation="relu")(x)
    x = MaxPool2D(pool_size=(2, 2))(x)

    x = Flatten()(x)

    x = BatchNormalization()(x)
    x = Dense(128, activation="relu", kernel_regularizer=l2(1e-4))(x)
    x = Dropout(0.3)(x)

    x = Dense(64, activation="relu", kernel_regularizer=l2(1e-4))(x)

    output = Dense(2)(x)

    model = Model(inputs=input, outputs=output)
    model.compile(
        loss="mse",
        optimizer=Adam(learning_rate=learning_rate),
        metrics=["mse"]
    )
    model.summary()

    return model


def model_ana_cont_s3(input_shape=(32, 32, 3), learning_rate=1e-3):
    input = Input(shape=input_shape)

    x = BatchNormalization()(input)
    x = Conv2D(16, (3, 3), padding='same', activation="relu")(x)
    x = MaxPool2D(pool_size=(2, 2))(x)

    x = BatchNormalization()(x)
    x = Conv2D(32, (3, 3), padding='same', activation="relu")(x)
    x = MaxPool2D(pool_size=(2, 2))(x)

    x = BatchNormalization()(x)
    x = Conv2D(32, (3, 3), padding='same', activation="relu")(x)
    x = MaxPool2D(pool_size=(2, 2))(x)

    x = BatchNormalization()(x)
    x = Conv2D(32, (3, 3), padding='same', activation="relu")(x)
    x = MaxPool2D(pool_size=(2, 2))(x)

    x = Flatten()(x)

    x = BatchNormalization()(x)
    x = Dense(64, activation="relu", kernel_regularizer=l2(1e-4))(x)
    x = Dropout(0.3)(x)

    x = Dense(32, activation="relu", kernel_regularizer=l2(1e-4))(x)

    output = Dense(2)(x)

    model = Model(inputs=input, outputs=output)
    model.compile(
        loss="mse",
        optimizer=Adam(learning_rate=learning_rate),
        metrics=["mse"]
    )
    model.summary()

    return model
