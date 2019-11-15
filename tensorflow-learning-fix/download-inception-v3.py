import tensorflow as tf
import os
import tarfile
import requests


inception_pretrain_model_url = 'http://download.tensorflow.org/models/image/imagenet/inception-2015-12-05.tgz'

inception_pretrain_model_dir = "inception_model"
if not os.path.exists(inception_pretrain_model_dir):
    os.makedirs(inception_pretrain_model_dir)

# get filename and file path
filename = inception_pretrain_model_dir.split('/')[-1]
filepath = os.path.join(inception_pretrain_model_dir, filename)

if not os.path.exists(filepath):
    print("download:", filename)
    r = requests.get(inception_pretrain_model_url, stream=True)
    with open(filepath, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
print("finish:", filename)

# unzip file
tarfile.open(filepath, 'r:gz').extractall(inception_pretrain_model_dir)

# model save file
log_dir = 'inception_log'
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

inception_graph_def_file = os.path.join(inception_pretrain_model_dir,
                                        'classify_image_graph_def.pb')
with tf.compat.v1.Session() as sess:
    with tf.compat.v1.gfile.FastGFile(inception_graph_def_file, 'rb') as f:
        graph_def = tf.compat.v1.GraphDef()
        graph_def.ParseFromString(f.read())
        tf.import_graph_def(graph_def, name='')

    writer = tf.compat.v1.summary.FileWriter(log_dir, sess.graph)
    writer.close
