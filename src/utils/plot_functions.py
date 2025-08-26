import matplotlib.pyplot as plt
import math
import numpy as np
import pandas as pd


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


# Plot dataset distribution (100 classes: 0.0 .. 9.9)
def plot_dataset_distribution(data):
    _, inverse = np.unique(data, return_inverse=True)
    bincount_result = np.bincount(inverse)
    fig = plt.figure(figsize=(40, 10))
    fig.suptitle("Distribution of data")
    plt.bar(np.arange (0, 100/10, 0.1), bincount_result, width=0.09, align='center')
    plt.ylabel('Count')
    plt.xlabel('Class')
    plt.tight_layout()

    return plt.xticks(np.arange(0, 100/10, 0.1))


# Plot analog dataset (with class label)
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


## Plot analog result dataset (with predicted, expected and filename label)
def plot_dataset_analog_result(images, labels, columns=7, rows=7, figsize=(18, 10)):

    fig = plt.figure(figsize=figsize)
    
    for i in range(1, columns * rows + 1):
        if (i>len(labels)):
            break
        fig.add_subplot(rows, columns, i)
        plt.title(labels[i-1])  # set title
        plt.imshow((images[i-1]).astype(np.uint8), aspect='1', extent=[0, 1, 0, 1])
        # yellow lines
        ax=plt.gca()
        ax.get_yaxis().set_visible(False) 
        ax.get_xaxis().set_visible(False) 
        
        plt.tight_layout()
    plt.show()


def plot_loss(history, validation):
    plt.semilogy(history.history['loss'])

    if (validation):
        plt.semilogy(history.history['val_loss'])

    plt.title('model loss')
    plt.ylabel('loss')
    plt.xlabel('epoch')
    plt.legend(['training','validation'], loc='upper left')
    plt.grid(True)
    plt.show()

    return plt


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


def plot_divergence(divergationset, title, filename=None):
    fig = plt.figure(figsize=(40, 10))
    fig.suptitle(title, fontsize=28)
    plt.bar(np.arange(0, len(divergationset)/10, 0.1), divergationset, width=0.09, align='center')
    plt.ylabel('Count')
    plt.xlabel('Deviation')
    plt.xticks(np.arange(0, len(divergationset)/10, 0.1))
    plt.show()
    
    # Save plot
    if filename:
        fig.savefig(filename, bbox_inches='tight')
    
    return fig


def confusion_matrix(predicted, y_test, nb_classes):
    ytrue = pd.Series(y_test.reshape(-1), name = 'actual')
    ypred = pd.Series(predicted.reshape(-1), name = 'pred')
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    pd.set_option('display.expand_frame_repr', False)
    pd.set_option('max_colwidth', None)
    return pd.crosstab(ytrue, ypred)
