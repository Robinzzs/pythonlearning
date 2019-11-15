import tensorflow as tf
import os
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


############### bulid relationship with uid and name
class NodeLookup(object):
    def __init__(self):
        label_lookup_path = 'inception_model/imagenet_2012_challenge_label_map_proto.pbtxt'
        uid_lookup_path = 'inception_model/imagenet_synset_to_human_label_map.txt'
        self.node_lookup = self.load(label_lookup_path, uid_lookup_path)

    def load(self, label_lookup_path, uid_lookup_path):
        # load
        proto_as_ascii_lines = tf.io.gfile.GFile(uid_lookup_path).readlines()
        uid_to_human = {}

        # read line by line
        for line in proto_as_ascii_lines :
            # delete \n
            line = line.strip('\n')
            # as \t cut
            parsed_items = line.split('\t')
            # get uid
            uid = parsed_items[0]
            # get name
            human_string = parsed_items[1]
            # save relationship
            uid_to_human[uid] = human_string

        proto_as_ascii = tf.io.gfile.GFile(label_lookup_path).readlines()
        node_id_to_uid = {}
        for line in proto_as_ascii:
            if line.strip().startswith('target_class:'):
                target_class = int(line.strip().split(':')[1])
            elif line.strip().startswith('target_class_'):
                target_class_string = line.strip().split(':')[1].strip()
                node_id_to_uid[target_class] = target_class_string[1:-1]


        node_id_to_name = {}
        for key, val in node_id_to_uid.items():
            # get name
            name = uid_to_human[val]
            # relationship
            node_id_to_name[key] = name
        return node_id_to_name

    def id_to_string(self, node_id):
        if node_id not in self.node_lookup:
            return ''
        return self.node_lookup[node_id]


########################## import Session graph
with tf.compat.v1.gfile.FastGFile('inception_model/classify_image_graph_def.pb','rb') as f:
    graph_def = tf.compat.v1.GraphDef()
    graph_def.ParseFromString(f.read())
    tf.import_graph_def(graph_def, name='')

########################## loop fig and identify
with tf.compat.v1.Session() as sess:
    softmax_tensor = sess.graph.get_tensor_by_name('softmax:0')
    # loop
    for root,dirs,files in os.walk('images/'):
        for file in files:
            # load fig
            image_data = tf.compat.v1.gfile.FastGFile(os.path.join(root, file), 'rb').read()
            predictions = sess.run(softmax_tensor, {'DecodeJpeg/contents:0' : image_data})
            predictions = np.squeeze(predictions)

            # print fig path
            image_path = os.path.join(root, file)
            print(image_path)
            # show fig
            img = Image.open(image_path)
            plt.imshow(img)
            plt.axis('off')
            plt.show()

            # order
            top_k = predictions.argsort()[-5:][::-1]
            node_lookup = NodeLookup()
            for node_id in top_k:
                # get name
                human_string = node_lookup.id_to_string(node_id)
                # get score
                score = predictions[node_id]
                print('%s (score = %.5f)' % (human_string, score))
            print('')
