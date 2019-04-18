from __future__ import print_function

import tensorflow as tf
import os
from PIL import Image
import numpy
import cv2

# IMAGE_PATH = 'C:\\Users\\Administrator\\Desktop\\ai\\FaceRank-master\\web_catimage\\' # the dataset file or root folder path.
# PATH = '3-19.jpg'
# MODEL_PATH='./model/model.ckpt'
#
# face_model = cv2.CascadeClassifier('C:/Users/Administrator/Desktop/cat/haarcascade_frontalcatface.xml')
#
# # Parameters
# learning_rate = 0.001
# #training_iters = 3000
# #batch_size = 10
# #display_step = 3
#
# # Network Parameters
# n_input = 128*128 # MNIST data input (img shape: 28*28)
# n_classes = 10 # MNIST total classes (0-9 digits)
# dropout = 0.75 # Dropout, probability to keep units
#
# # tf Graph input
# x = tf.placeholder(tf.float32, [None, 128, 128, 3])
# y = tf.placeholder(tf.float32, [None, n_classes])
# keep_prob = tf.placeholder(tf.float32) #dropout (keep probability)


# Create some wrappers for simplicity
def conv2d(x, W, b, strides=1):
    # Conv2D wrapper, with bias and relu activation
    x = tf.nn.conv2d(x, W, strides=[1, strides, strides, 1], padding='SAME')
    x = tf.nn.bias_add(x, b)
    return tf.nn.relu(x)


def maxpool2d(x, k=2):
    # MaxPool2D wrapper
    return tf.nn.max_pool(x, ksize=[1, k, k, 1], strides=[1, k, k, 1],
                          padding='SAME')


# Create model
def conv_net(x, weights, biases, dropout):
    # Reshape input picture
    x = tf.reshape(x, shape=[-1, 128, 128, 3])

    # Convolution Layer
    conv1 = conv2d(x, weights['wc1'], biases['bc1'])
    print(conv1.shape)
    # Max Pooling (down-sampling)
    conv1 = maxpool2d(conv1, k=2)
    print(conv1.shape)
    # Convolution Layer
    conv2 = conv2d(conv1, weights['wc2'], biases['bc2'])
    print(conv2.shape)
    # Max Pooling (down-sampling)
    conv2 = maxpool2d(conv2, k=2)
    print(conv2.shape)
    # Fully connected layer
    # Reshape conv2 output to fit fully connected layer input
    fc1 = tf.reshape(conv2, [-1, weights['wd1'].get_shape().as_list()[0]])
    fc1 = tf.add(tf.matmul(fc1, weights['wd1']), biases['bd1'])
    fc1 = tf.nn.relu(fc1)
    # Apply Dropout
    fc1 = tf.nn.dropout(fc1, dropout)

    # Output, class prediction
    out = tf.add(tf.matmul(fc1, weights['out']), biases['out'])
    return out


def get_pred():
    tf.reset_default_graph()
    IMAGE_PATH = 'D:/study/djangoforwx/softproject/wx/face/web_catimage/'  # the dataset file or root folder path.
    PATH = '3-19.jpg'
    MODEL_PATH = './model/model.ckpt'

    face_model = cv2.CascadeClassifier('D:/study/djangoforwx/softproject/wx/face/haarcascade_frontalcatface.xml')


    # Parameters
    learning_rate = 0.001
    # training_iters = 3000
    # batch_size = 10
    # display_step = 3

    # Network Parameters
    n_input = 128 * 128  # MNIST data input (img shape: 28*28)
    n_classes = 10  # MNIST total classes (0-9 digits)
    dropout = 0.75  # Dropout, probability to keep units

    # tf Graph input
    x = tf.placeholder(tf.float32, [None, 128, 128, 3])
    y = tf.placeholder(tf.float32, [None, n_classes])
    keep_prob = tf.placeholder(tf.float32)  # dropout (keep probability)

    # Store layers weight & bias
    weights = {
        # 5x5 conv, 1 input, 32 outputs
        'wc1': tf.Variable(tf.random_normal([5, 5, 3, 24])),
        # 5x5 conv, 32 inputs, 64 outputs
        'wc2': tf.Variable(tf.random_normal([5, 5, 24, 96])),
        # fully connected, 7*7*64 inputs, 1024 outputs
        'wd1': tf.Variable(tf.random_normal([32*32*96, 1024])),
        # 1024 inputs, 10 outputs (class prediction)
        'out': tf.Variable(tf.random_normal([1024, n_classes]))
    }

    biases = {
        'bc1': tf.Variable(tf.random_normal([24])),
        'bc2': tf.Variable(tf.random_normal([96])),
        'bd1': tf.Variable(tf.random_normal([1024])),
        'out': tf.Variable(tf.random_normal([n_classes]))
    }

    # Construct model
    pred = conv_net(x, weights, biases, keep_prob)
    pred_result=tf.argmax(pred, 1)
    # Define loss and optimizer
    # cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=pred, labels=y))
    # optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(cost)
    # #
    # # # Evaluate model
    # correct_pred = tf.equal(tf.argmax(pred, 1), tf.argmax(y, 1))
    # accuracy = tf.reduce_mean(tf.cast(correct_pred, tf.float32))

    # Initializing the variables
    # init = tf.global_variables_initializer()
    # saver=tf.train.import_meta_graph('E:\\djproject\\mysite\\tfwx\\face\\model\\model.ckpt.meta')
    saver = tf.train.Saver()
    # Launch the graph#

    with tf.Session() as sess:

        saver.restore(sess, "D:/study/djangoforwx/softproject/wx/face/model/model.ckpt")
        step = 1
        # Keep training until reach max iterations
        # list = os.listdir("./test_resize1/")
        # print(list)
        # print(len(list))
        batch_xs = []
        batch_ys = []

        # print(score)
        image = cv2.imread(IMAGE_PATH+PATH)
        gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

        face_locations = face_model.detectMultiScale(gray)

        print("I found {} face(s) in this photograph.".format(len(face_locations)))

        for (xh, yh, w, h) in face_locations:
            face_image = image[yh: yh + h, xh: xh + w]
            pil_image = Image.fromarray(cv2.cvtColor(face_image, cv2.COLOR_BGRA2RGB))
            img = pil_image.resize((128, 128))
        id_tag = PATH.find("-")
        score = PATH[id_tag-1:id_tag]
        print(score)
        img_ndarray = numpy.asarray(img, dtype='float32')
        img_ndarray = numpy.reshape(img_ndarray, [128, 128, 3])
        # print(img_ndarray.shape)
        batch_x = img_ndarray
        batch_xs.append(batch_x)

        batch_y = numpy.asarray([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        # print(type(score))
        batch_y[int(score)-1] = 1
        # print(batch_y)
        batch_y = numpy.reshape(batch_y, [10, ])
        batch_ys.append(batch_y)

        # print(batch_ys)
        batch_xs = numpy.asarray(batch_xs)
        print(batch_xs.shape)
        batch_ys = numpy.asarray(batch_ys)

        # Run optimization op (backprop)
        pred_result_test=sess.run(pred_result, feed_dict={x: batch_xs, keep_prob: 1.})
        # #loss, acc = sess.run([cost, accuracy], feed_dict={x: batch_xs,
        #                                                   y: batch_ys,
        #                                                   keep_prob: 1.})
        # print("Minibatch Loss= " +
        #               "{:.6f}".format(loss) + ", Training Accuracy= " +
        #               "{:.5f}".format(acc))

        print(pred_result_test+1)
        #saver.save(sess, "E:\\djproject\\mysite\\tfwx\\face\\model\\model.ckpt")

    print("Test Finished!")

    return pred_result_test + 1