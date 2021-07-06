import tensorflow as tf
from tensorflow.keras.activations import sigmoid
from tensorflow.keras.layers import DenseFeatures

import pyrec.layers as my_layers


class FM(tf.keras.models.Model):
    """
    Factorization Machines

    """

    def __init__(self,
                 one_hot_feature_columns,
                 multi_hot_feature_columns=None,
                 k=16,
                 ):
        super(FM, self).__init__()
        if one_hot_feature_columns and multi_hot_feature_columns:
            self.input_layer = DenseFeatures(feature_columns=one_hot_feature_columns + multi_hot_feature_columns)
        elif one_hot_feature_columns:
            self.input_layer = DenseFeatures(feature_columns=one_hot_feature_columns)
        elif multi_hot_feature_columns:
            self.input_layer = DenseFeatures(feature_columns=multi_hot_feature_columns)
        else:
            raise ValueError('len(one_hot_feature_columns) + len(multi_hot_feature_columns) should greater than 0')
        self.fm = my_layers.FM(one_hot_feature_columns, multi_hot_feature_columns, k=k)

    def call(self, inputs, training=None, mask=None):
        inputs = self.input_layer(inputs)
        logits = self.fm(inputs)
        return sigmoid(logits)
