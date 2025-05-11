import tensorflow.keras as keras
import math
import numpy as np

def class_encoding(y_train, nb_classes=100):
    '''like to_categorical.
        y_train must be an array
        nb_classes for the class count, if not all values in y_train
    '''
    ret = np.zeros((len(y_train), nb_classes))
    for i, y in enumerate(y_train):
        ret[i, int((y*10))] = 1
    return ret

def class_decoding(y_train, nb_classes=100):
    ''' from_categorical like function. It returns a float value between 0.0 and 9.9
        y_train the encoded values in an array
        nb_classes should be ignored. will not used
    '''
    ret = np.zeros((len(y_train), 1))
    for i, y in enumerate(y_train):
        ret[i] = (np.argmax(y))/10
    return ret




import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
def plot_dataset(images, labels, columns=10, rows=5, figsize=(18, 10), nb_classes=100):

    fig = plt.figure(figsize=figsize)
    
    for i in range(1, columns*rows +1):
        if (i>len(labels)):
            break
        fig.add_subplot(rows, columns, i)
        plt.title(labels[i-1])  # set title
        plt.xticks([0.2, 0.4, 0.6, 0.8])
        plt.imshow((images[i-1]).astype(np.uint8), aspect='1.6', extent=[0, 1, 0, 1])
        # yellow lines
        for y in np.arange(0.2, 0.8, 0.2):
            plt.axhline(y=y,color='yellow')
        ax=plt.gca()
        ax.get_xaxis().set_visible(False) 
        plt.tight_layout()
    plt.show()


def GetValueFromVektor10(_val):
#    print(_val)
    catmax = np.argmax(_val)
    catmaxminus = (catmax - 1) % 10
    catmaxplus = (catmax + 1) % 10

    val_catmax = _val[catmax]
    val_catmaxminus = _val[catmaxminus]
    val_catmaxplus = _val[catmaxplus]
    
    
    result_ist = catmax
#    print("GetVektorFromValue10: catmax " + str(catmax) + " catmaxminus: " + str(catmaxminus) + " catmaxplus: " + str(catmaxplus) + " values: " + str(val_catmax) + " " + str(val_catmaxminus) + " " + str(val_catmaxplus))
    if (val_catmaxplus > val_catmaxminus):
        result_ist = result_ist + val_catmaxplus / (val_catmax + val_catmaxplus)
        fitvalue = _val[catmax] + _val[catmaxplus]
    else:
        result_ist = result_ist - (val_catmaxminus) / (val_catmax + val_catmaxminus)
        fitvalue = _val[catmax] + _val[catmaxminus]
    return result_ist

def plot_dataset_analog(data_iter, columns=9, rows=5):

    fig = plt.figure(figsize=(18, 11*rows/5))
    
    for i in range(1, columns*rows +1):
        img, label = next(data_iter)
        fig.add_subplot(rows, columns, i)
        if (label[0].size == 2):
            output = str( round(
                    10*(np.arctan2(label[0][0], label[0][1])/(2*math.pi)  % 1),2))
        else: # ana-class100
            nb_classes=100
            output = (str(class_decoding(label[0].reshape(-1, nb_classes), nb_classes).reshape(-1)[0])) 
        plt.title(output)  # set title
        plt.imshow(img[0].astype(np.uint8), aspect='1', extent=[0, 1, 0, 1])
        ax=plt.gca()
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False) 
    plt.show()


def plot_dataset_it_hyb(data_iter, columns=9, rows=5):

    fig = plt.figure(figsize=(18, 11))
    
    for i in range(1, columns*rows +1):
        img, label = next(data_iter)
        fig.add_subplot(rows, columns, i)
        plt.xticks([0.2, 0.4, 0.6, 0.8])
        plt.title(str(GetValueFromVektor10(label[0])))  # set title
        plt.imshow(img[0].astype(np.uint8), aspect='1.6', extent=[0, 1, 0, 1])
        ax=plt.gca()
        ax.get_xaxis().set_visible(False) 
        # yellow lines
        for y in np.arange(0.2, 0.8, 0.2):
                plt.axhline(y=y,color='yellow')
    plt.show()

def plot_dataset_it(data_iter, columns=9, rows=5, nb_classes=100):

    fig = plt.figure(figsize=(18, 11))
    
    for i in range(1, columns*rows +1):
        img, label = next(data_iter)
        fig.add_subplot(rows, columns, i)
        plt.xticks([0.2, 0.4, 0.6, 0.8])
        plt.title(str(class_decoding(label[0].reshape(-1, nb_classes), nb_classes).reshape(-1)[0]))  # set title
        plt.imshow(img[0].astype(np.uint8), aspect='1.6', extent=[0, 1, 0, 1])
        ax=plt.gca()
        ax.get_xaxis().set_visible(False) 
        # yellow lines
        for y in np.arange(0.2, 0.8, 0.2):
                plt.axhline(y=y,color='yellow')
    plt.show()

def plot_acc_loss(history, modelname="modelname"):
    fig, (ax1, ax2) = plt.subplots(1, 2)
    fig.suptitle(modelname)
    fig.set_figwidth(15)

    if "loss" in history.history:
        ax1.plot(history.history['loss'])
    if "accuracy" in history.history:
        ax2.plot(history.history['accuracy'])
    if "val_loss" in history.history:
        ax1.plot(history.history['val_loss'])
    if "val_accuracy" in history.history:
        ax2.plot(history.history['val_accuracy'])
    if "student_loss" in history.history:
        ax1.plot(history.history['student_loss'])
    if "sparse_categorical_accuracy" in history.history:
        ax2.plot(history.history['sparse_categorical_accuracy'])
    if "val_sparse_categorical_accuracy" in history.history:
        ax2.plot(history.history['val_sparse_categorical_accuracy'])
    if "student_accuracy" in history.history:
        ax2.plot(history.history['student_accuracy'])
    if "val_student_accuracy" in history.history:
        ax2.plot(history.history['val_student_accuracy'])
    if "distillation_loss" in history.history:
        ax1.plot(history.history['distillation_loss'])

    ax1.set_title('model loss')
    ax1.set_ylabel('loss')
    ax1.set_xlabel('epoch')
    ax2.set_ylabel('accuracy')
    ax2.set_xlabel('epoch')
    ax1.legend(['train','eval'], loc='upper left')
    axes = plt.gca()
    axes.set_ylim([0.92,1])
    plt.show()


def plot_divergence(divergationset, title1, nb_classes):
    fig = plt.figure(figsize=(40, 10))
    fig.suptitle(title1)
    plt.bar(np.arange (0, nb_classes/10, 0.1), divergationset, width=0.09, align='center')
    plt.ylabel('count')
    plt.xlabel('digit class')
    plt.xticks(np.arange(0, nb_classes/10, 0.1))
    return fig


def confusion_matrix(predicted, y_test, nb_classes):
    ytrue = pd.Series(y_test.reshape(-1), name = 'actual')
    ypred = pd.Series(predicted.reshape(-1), name = 'pred')
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    pd.set_option('display.expand_frame_repr', False)
    pd.set_option('max_colwidth', None)
    return pd.crosstab(ytrue, ypred)


def predict_meter_digits():
    import numpy as np
    from tensorflow import keras

    max_delta = 0.11

    predictions = class_decoding(model.predict(xz_data.astype(np.float32)), 100).reshape(-1)

    # 9.9 <> 0 = 0.1 and 1.1 <> 1.2 = 0.1
    differences = np.minimum(np.abs(predictions-yz_data), np.abs(predictions-(10-yz_data)))

    # used for filtering
    false_differences = differences>max_delta

    # only differences bigger than delta. so small differences can be ignored in early stages
    false_predicted = differences[false_differences]
    false_images = xz_data[false_differences]
    false_labels = [ "Expected: " + str(y) + "\n Predicted: " + str(p) + "\n" + str(f)[-26:-4] for y, p, f in zip(yz_data[false_differences], predictions[false_differences], fz_data[false_differences])]

    print(f"Tested images: {len(yz_data)}. {len(false_predicted)} false predicted. Accuracy is: {1-len(false_predicted)/len(yz_data)}")

    # plot the differences (max difference can only be 5.0)
    plot_divergence(np.bincount(np.array(false_predicted*10).astype(int), minlength=51), "Divergation of false predicted", 51)

    # plot the false predicted images
    plot_dataset(np.array(false_images), false_labels, columns=7, rows=7, figsize=(18,18))