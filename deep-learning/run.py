{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import sys\n",
    "import warnings\n",
    "\n",
    "if not sys.warnoptions:\n",
    "    warnings.simplefilter('ignore')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "import tensorflow as tf\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "import pandas as pd\n",
    "from sklearn.preprocessing import MinMaxScaler\n",
    "from datetime import datetime\n",
    "from datetime import timedelta\n",
    "from tqdm import tqdm\n",
    "sns.set()\n",
    "tf.compat.v1.random.set_random_seed(1234)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Date</th>\n",
       "      <th>Open</th>\n",
       "      <th>High</th>\n",
       "      <th>Low</th>\n",
       "      <th>Close</th>\n",
       "      <th>Adj Close</th>\n",
       "      <th>Volume</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2016-11-02</td>\n",
       "      <td>778.200012</td>\n",
       "      <td>781.650024</td>\n",
       "      <td>763.450012</td>\n",
       "      <td>768.700012</td>\n",
       "      <td>768.700012</td>\n",
       "      <td>1872400</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2016-11-03</td>\n",
       "      <td>767.250000</td>\n",
       "      <td>769.950012</td>\n",
       "      <td>759.030029</td>\n",
       "      <td>762.130005</td>\n",
       "      <td>762.130005</td>\n",
       "      <td>1943200</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2016-11-04</td>\n",
       "      <td>750.659973</td>\n",
       "      <td>770.359985</td>\n",
       "      <td>750.560974</td>\n",
       "      <td>762.020020</td>\n",
       "      <td>762.020020</td>\n",
       "      <td>2134800</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2016-11-07</td>\n",
       "      <td>774.500000</td>\n",
       "      <td>785.190002</td>\n",
       "      <td>772.549988</td>\n",
       "      <td>782.520020</td>\n",
       "      <td>782.520020</td>\n",
       "      <td>1585100</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2016-11-08</td>\n",
       "      <td>783.400024</td>\n",
       "      <td>795.632996</td>\n",
       "      <td>780.190002</td>\n",
       "      <td>790.510010</td>\n",
       "      <td>790.510010</td>\n",
       "      <td>1350800</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         Date        Open        High         Low       Close   Adj Close  \\\n",
       "0  2016-11-02  778.200012  781.650024  763.450012  768.700012  768.700012   \n",
       "1  2016-11-03  767.250000  769.950012  759.030029  762.130005  762.130005   \n",
       "2  2016-11-04  750.659973  770.359985  750.560974  762.020020  762.020020   \n",
       "3  2016-11-07  774.500000  785.190002  772.549988  782.520020  782.520020   \n",
       "4  2016-11-08  783.400024  795.632996  780.190002  790.510010  790.510010   \n",
       "\n",
       "    Volume  \n",
       "0  1872400  \n",
       "1  1943200  \n",
       "2  2134800  \n",
       "3  1585100  \n",
       "4  1350800  "
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df = pd.read_csv('../dataset/GOOG-year.csv')\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>0</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0.112708</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0.090008</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>0.089628</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>0.160459</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>0.188066</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "          0\n",
       "0  0.112708\n",
       "1  0.090008\n",
       "2  0.089628\n",
       "3  0.160459\n",
       "4  0.188066"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "minmax = MinMaxScaler().fit(df.iloc[:, 4:5].astype('float32')) # Close index\n",
    "df_log = minmax.transform(df.iloc[:, 4:5].astype('float32')) # Close index\n",
    "df_log = pd.DataFrame(df_log)\n",
    "df_log.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Split train and test\n",
    "\n",
    "I will cut the dataset to train and test datasets,\n",
    "\n",
    "1. Train dataset derived from starting timestamp until last 30 days\n",
    "2. Test dataset derived from last 30 days until end of the dataset\n",
    "\n",
    "So we will let the model do forecasting based on last 30 days, and we will going to repeat the experiment for 10 times. You can increase it locally if you want, and tuning parameters will help you by a lot."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "((252, 7), (222, 1), (30, 1))"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "test_size = 30\n",
    "simulation_size = 10\n",
    "\n",
    "df_train = df_log.iloc[:-test_size]\n",
    "df_test = df_log.iloc[-test_size:]\n",
    "df.shape, df_train.shape, df_test.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "def layer_norm(inputs, epsilon=1e-8):\n",
    "    mean, variance = tf.nn.moments(inputs, [-1], keep_dims=True)\n",
    "    normalized = (inputs - mean) / (tf.sqrt(variance + epsilon))\n",
    "\n",
    "    params_shape = inputs.get_shape()[-1:]\n",
    "    gamma = tf.get_variable('gamma', params_shape, tf.float32, tf.ones_initializer())\n",
    "    beta = tf.get_variable('beta', params_shape, tf.float32, tf.zeros_initializer())\n",
    "    \n",
    "    outputs = gamma * normalized + beta\n",
    "    return outputs\n",
    "\n",
    "def multihead_attn(queries, keys, q_masks, k_masks, future_binding, num_units, num_heads):\n",
    "    \n",
    "    T_q = tf.shape(queries)[1]                                      \n",
    "    T_k = tf.shape(keys)[1]                  \n",
    "\n",
    "    Q = tf.layers.dense(queries, num_units, name='Q')                              \n",
    "    K_V = tf.layers.dense(keys, 2*num_units, name='K_V')    \n",
    "    K, V = tf.split(K_V, 2, -1)        \n",
    "\n",
    "    Q_ = tf.concat(tf.split(Q, num_heads, axis=2), axis=0)                         \n",
    "    K_ = tf.concat(tf.split(K, num_heads, axis=2), axis=0)                    \n",
    "    V_ = tf.concat(tf.split(V, num_heads, axis=2), axis=0)                      \n",
    "\n",
    "    align = tf.matmul(Q_, tf.transpose(K_, [0,2,1]))                      \n",
    "    align = align / np.sqrt(K_.get_shape().as_list()[-1])                 \n",
    "\n",
    "    paddings = tf.fill(tf.shape(align), float('-inf'))                   \n",
    "\n",
    "    key_masks = k_masks                                                 \n",
    "    key_masks = tf.tile(key_masks, [num_heads, 1])                       \n",
    "    key_masks = tf.tile(tf.expand_dims(key_masks, 1), [1, T_q, 1])            \n",
    "    align = tf.where(tf.equal(key_masks, 0), paddings, align)       \n",
    "\n",
    "    if future_binding:\n",
    "        lower_tri = tf.ones([T_q, T_k])                                          \n",
    "        lower_tri = tf.linalg.LinearOperatorLowerTriangular(lower_tri).to_dense()  \n",
    "        masks = tf.tile(tf.expand_dims(lower_tri,0), [tf.shape(align)[0], 1, 1]) \n",
    "        align = tf.where(tf.equal(masks, 0), paddings, align)                      \n",
    "    \n",
    "    align = tf.nn.softmax(align)                                            \n",
    "    query_masks = tf.to_float(q_masks)                                             \n",
    "    query_masks = tf.tile(query_masks, [num_heads, 1])                             \n",
    "    query_masks = tf.tile(tf.expand_dims(query_masks, -1), [1, 1, T_k])            \n",
    "    align *= query_masks\n",
    "    \n",
    "    outputs = tf.matmul(align, V_)                                                 \n",
    "    outputs = tf.concat(tf.split(outputs, num_heads, axis=0), axis=2)             \n",
    "    outputs += queries                                                             \n",
    "    outputs = layer_norm(outputs)                                                 \n",
    "    return outputs\n",
    "\n",
    "\n",
    "def pointwise_feedforward(inputs, hidden_units, activation=None):\n",
    "    outputs = tf.layers.dense(inputs, 4*hidden_units, activation=activation)\n",
    "    outputs = tf.layers.dense(outputs, hidden_units, activation=None)\n",
    "    outputs += inputs\n",
    "    outputs = layer_norm(outputs)\n",
    "    return outputs\n",
    "\n",
    "\n",
    "def learned_position_encoding(inputs, mask, embed_dim):\n",
    "    T = tf.shape(inputs)[1]\n",
    "    outputs = tf.range(tf.shape(inputs)[1])                # (T_q)\n",
    "    outputs = tf.expand_dims(outputs, 0)                   # (1, T_q)\n",
    "    outputs = tf.tile(outputs, [tf.shape(inputs)[0], 1])   # (N, T_q)\n",
    "    outputs = embed_seq(outputs, T, embed_dim, zero_pad=False, scale=False)\n",
    "    return tf.expand_dims(tf.to_float(mask), -1) * outputs\n",
    "\n",
    "\n",
    "def sinusoidal_position_encoding(inputs, mask, repr_dim):\n",
    "    T = tf.shape(inputs)[1]\n",
    "    pos = tf.reshape(tf.range(0.0, tf.to_float(T), dtype=tf.float32), [-1, 1])\n",
    "    i = np.arange(0, repr_dim, 2, np.float32)\n",
    "    denom = np.reshape(np.power(10000.0, i / repr_dim), [1, -1])\n",
    "    enc = tf.expand_dims(tf.concat([tf.sin(pos / denom), tf.cos(pos / denom)], 1), 0)\n",
    "    return tf.tile(enc, [tf.shape(inputs)[0], 1, 1]) * tf.expand_dims(tf.to_float(mask), -1)\n",
    "\n",
    "def label_smoothing(inputs, epsilon=0.1):\n",
    "    C = inputs.get_shape().as_list()[-1]\n",
    "    return ((1 - epsilon) * inputs) + (epsilon / C)\n",
    "\n",
    "class Attention:\n",
    "    def __init__(self, size_layer, embedded_size, learning_rate, size, output_size,\n",
    "                 num_blocks = 2,\n",
    "                 num_heads = 8,\n",
    "                 min_freq = 50):\n",
    "        self.X = tf.compat.v1.placeholder(float32, (None, None, size))\n",
    "        self.Y = tf.compat.v1.placeholder(tf.float32, (None, output_size))\n",
    "        \n",
    "        encoder_embedded = tf.layers.dense(self.X, embedded_size)\n",
    "        encoder_embedded = tf.nn.dropout(encoder_embedded, keep_prob = 0.8)\n",
    "        x_mean = tf.reduce_mean(self.X, axis = 2)\n",
    "        en_masks = tf.sign(x_mean)\n",
    "        encoder_embedded += sinusoidal_position_encoding(self.X, en_masks, embedded_size)\n",
    "        \n",
    "        for i in range(num_blocks):\n",
    "            with tf.variable_scope('encoder_self_attn_%d'%i,reuse=tf.AUTO_REUSE):\n",
    "                encoder_embedded = multihead_attn(queries = encoder_embedded,\n",
    "                                             keys = encoder_embedded,\n",
    "                                             q_masks = en_masks,\n",
    "                                             k_masks = en_masks,\n",
    "                                             future_binding = False,\n",
    "                                             num_units = size_layer,\n",
    "                                             num_heads = num_heads)\n",
    "\n",
    "            with tf.variable_scope('encoder_feedforward_%d'%i,reuse=tf.AUTO_REUSE):\n",
    "                encoder_embedded = pointwise_feedforward(encoder_embedded,\n",
    "                                                    embedded_size,\n",
    "                                                    activation = tf.nn.relu)\n",
    "                \n",
    "        self.logits = tf.layers.dense(encoder_embedded[-1], output_size)\n",
    "        self.cost = tf.reduce_mean(tf.square(self.Y - self.logits))\n",
    "        self.optimizer = tf.train.AdamOptimizer(learning_rate).minimize(\n",
    "            self.cost\n",
    "        )\n",
    "        \n",
    "def calculate_accuracy(real, predict):\n",
    "    real = np.array(real) + 1\n",
    "    predict = np.array(predict) + 1\n",
    "    percentage = 1 - np.sqrt(np.mean(np.square((real - predict) / real)))\n",
    "    return percentage * 100\n",
    "\n",
    "def anchor(signal, weight):\n",
    "    buffer = []\n",
    "    last = signal[0]\n",
    "    for i in signal:\n",
    "        smoothed_val = last * weight + (1 - weight) * i\n",
    "        buffer.append(smoothed_val)\n",
    "        last = smoothed_val\n",
    "    return buffer"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "num_layers = 1\n",
    "size_layer = 128\n",
    "timestamp = 5\n",
    "epoch = 300\n",
    "dropout_rate = 0.8\n",
    "future_day = test_size\n",
    "\n",
    "earning_rate = 0.001"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "def forecast():\n",
    "    tf.compat.v1.reset_default_graph()\n",
    "    modelnn = Attention(size_layer, size_layer, learning_rate, df_log.shape[1], df_log.shape[1])\n",
    "    sess = tf.InteractiveSession()\n",
    "    sess.run(tf.global_variables_initializer())\n",
    "    date_ori = pd.to_datetime(df.iloc[:, 0]).tolist()\n",
    "\n",
    "    pbar = tqdm(range(epoch), desc = 'train loop')\n",
    "    for i in pbar:\n",
    "        total_loss, total_acc = [], []\n",
    "        for k in range(0, df_train.shape[0] - 1, timestamp):\n",
    "            index = min(k + timestamp, df_train.shape[0] - 1)\n",
    "            batch_x = np.expand_dims(\n",
    "                df_train.iloc[k : index, :].values, axis = 0\n",
    "            )\n",
    "            batch_y = df_train.iloc[k + 1 : index + 1, :].values\n",
    "            logits, _, loss = sess.run(\n",
    "                [modelnn.logits, modelnn.optimizer, modelnn.cost],\n",
    "                feed_dict = {\n",
    "                    modelnn.X: batch_x,\n",
    "                    modelnn.Y: batch_y\n",
    "                },\n",
    "            ) \n",
    "            total_loss.append(loss)\n",
    "            total_acc.append(calculate_accuracy(batch_y[:, 0], logits[:, 0]))\n",
    "        pbar.set_postfix(cost = np.mean(total_loss), acc = np.mean(total_acc))\n",
    "    \n",
    "    future_day = test_size\n",
    "\n",
    "    output_predict = np.zeros((df_train.shape[0] + future_day, df_train.shape[1]))\n",
    "    output_predict[0] = df_train.iloc[0]\n",
    "    upper_b = (df_train.shape[0] // timestamp) * timestamp\n",
    "\n",
    "    for k in range(0, (df_train.shape[0] // timestamp) * timestamp, timestamp):\n",
    "        out_logits = sess.run(\n",
    "            modelnn.logits,\n",
    "            feed_dict = {\n",
    "                modelnn.X: np.expand_dims(\n",
    "                    df_train.iloc[k : k + timestamp], axis = 0\n",
    "                )\n",
    "            },\n",
    "        )\n",
    "        output_predict[k + 1 : k + timestamp + 1] = out_logits\n",
    "\n",
    "    if upper_b != df_train.shape[0]:\n",
    "        out_logits = sess.run(\n",
    "            modelnn.logits,\n",
    "            feed_dict = {\n",
    "                modelnn.X: np.expand_dims(df_train.iloc[upper_b:], axis = 0)\n",
    "            },\n",
    "        )\n",
    "        output_predict[upper_b + 1 : df_train.shape[0] + 1] = out_logits\n",
    "        future_day -= 1\n",
    "        date_ori.append(date_ori[-1] + timedelta(days = 1))\n",
    "    \n",
    "    for i in range(future_day):\n",
    "        o = output_predict[-future_day - timestamp + i:-future_day + i]\n",
    "        out_logits = sess.run(\n",
    "            modelnn.logits,\n",
    "            feed_dict = {\n",
    "                modelnn.X: np.expand_dims(o, axis = 0)\n",
    "            },\n",
    "        )\n",
    "        output_predict[-future_day + i] = out_logits[-1]\n",
    "        date_ori.append(date_ori[-1] + timedelta(days = 1))\n",
    "    \n",
    "    output_predict = minmax.inverse_transform(output_predict)\n",
    "    deep_future = anchor(output_predict[:, 0], 0.3)\n",
    "    \n",
    "    return deep_future[-test_size:]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "WARNING: Logging before flag parsing goes to stderr.\n",
      "W0817 12:08:12.096583 140064997701440 deprecation.py:323] From <ipython-input-6-24d2a24c36ef>:91: dense (from tensorflow.python.layers.core) is deprecated and will be removed in a future version.\n",
      "Instructions for updating:\n",
      "Use keras.layers.dense instead.\n",
      "W0817 12:08:12.104836 140064997701440 deprecation.py:506] From /usr/local/lib/python3.6/dist-packages/tensorflow/python/ops/init_ops.py:1251: calling VarianceScaling.__init__ (from tensorflow.python.ops.init_ops) with dtype is deprecated and will be removed in a future version.\n",
      "Instructions for updating:\n",
      "Call initializer instance with the dtype argument instead of passing it to the constructor\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "simulation 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "W0817 12:08:12.294501 140064997701440 deprecation.py:506] From <ipython-input-6-24d2a24c36ef>:92: calling dropout (from tensorflow.python.ops.nn_ops) with keep_prob is deprecated and will be removed in a future version.\n",
      "Instructions for updating:\n",
      "Please use `rate` instead of `keep_prob`. Rate should be set to `rate = 1 - keep_prob`.\n",
      "W0817 12:08:12.305350 140064997701440 deprecation.py:323] From <ipython-input-6-24d2a24c36ef>:73: to_float (from tensorflow.python.ops.math_ops) is deprecated and will be removed in a future version.\n",
      "Instructions for updating:\n",
      "Use `tf.cast` instead.\n",
      "W0817 12:08:12.446460 140064997701440 deprecation.py:323] From <ipython-input-6-24d2a24c36ef>:33: add_dispatch_support.<locals>.wrapper (from tensorflow.python.ops.array_ops) is deprecated and will be removed in a future version.\n",
      "Instructions for updating:\n",
      "Use tf.where in 2.0, which has the same broadcast rule as np.where\n",
      "train loop: 100%|██████████| 300/300 [01:41<00:00,  2.97it/s, acc=96.7, cost=0.00409] \n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "simulation 2\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "train loop: 100%|██████████| 300/300 [01:40<00:00,  2.99it/s, acc=97.3, cost=0.00184] \n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "simulation 3\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "train loop: 100%|██████████| 300/300 [01:40<00:00,  2.98it/s, acc=96.7, cost=0.00351] \n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "simulation 4\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "train loop: 100%|██████████| 300/300 [01:40<00:00,  2.98it/s, acc=97.9, cost=0.00112] \n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "simulation 5\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "train loop: 100%|██████████| 300/300 [01:41<00:00,  2.97it/s, acc=98, cost=0.00113]   \n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "simulation 6\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "train loop: 100%|██████████| 300/300 [01:40<00:00,  2.98it/s, acc=97.5, cost=0.00165] \n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "simulation 7\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "train loop: 100%|██████████| 300/300 [01:41<00:00,  2.96it/s, acc=95.8, cost=0.00513]\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "simulation 9\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "train loop: 100%|██████████| 300/300 [01:41<00:00,  2.98it/s, acc=98, cost=0.000974]  \n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "simulation 10\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "train loop: 100%|██████████| 300/300 [01:40<00:00,  2.99it/s, acc=96.8, cost=0.00322] \n"
     ]
    }
   ],
   "source": [
    "results = []\n",
    "for i in range(simulation_size):\n",
    "    print('simulation %d'%(i + 1))\n",
    "    results.append(forecast())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAA3gAAAFBCAYAAAAlhA0CAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4xLjEsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy8QZhcZAAAgAElEQVR4nOzdeVyU1f7A8c/MACqLgisiqGh6NLXcEpVETdS2a8u9v26kJJbeNBVX0lxI3IJUXDCXvFmWmmllerW6hFlmZmnSNcseXEDcRcUEccRZfn/MgKDgCgzL9/16zWtmnnPmeb7n4Yh855znPDqr1YoQQgghhBBCiLJP7+gAhBBCCCGEEEIUDUnwhBBCCCGEEKKckARPCCGEEEIIIcoJSfCEEEIIIYQQopyQBE8IIYQQQgghyglJ8IQQQgghhBCinJAETwghhBBCCCHKCSdHByCEEEKIu6OU0gETgFcAT+AL4F+apl28rl51QAM0TdMeLmRf/YFwoAlwEVgNTNA0zXRdvSbAb8Anmqb1y7N9ODAaqAEkASM1TdtuL4sA+gMNgLPAIk3TZt1b64UQQhRERvCEEEIUOaVUhfoC0YHtfREIBQIBH6AKEFdAvRhg/y325QqMBGoCAUAPYGwB9d4GduXdoJQKAKKBfwDVgHeB9Uopg72Kzh6rF/AoMEwp9fwt4hFCCHEXKtR/wEIIIUApNR4YBNQGjgITNU1br5SqBJwGHtY0bZ+9bi0gFWigadoZpdSTwHSgIfAHMFjTtL32uinAYqCv7a1yw5Yg3HAse30D8Ba2kZ0MYA625MRZ0zSTUqoaEAs8DliA94A3NE0zF9CmDsB8oDlwGfgUGK1pWra9vAUwD2gHXAXma5o20x7DOOBle4xJwNOAAUjOicW+j2+BlZqm/VspFWZv18/YEpfFSqn3gGXAg4AV+C8wVNO0C/bP+9lj7ILtC9aPsI14nQK6apr2m71ebSDFfs7TbvrDhL8B72qadtT+2RjgG6XUEE3TsuzbOgMtgXfs7SyQpmmL87w9rpRaBXS/7jw/D1wAdgD35SlqCPyuadov9nofAIuwndOTmqa9lfdQSqkN2JLSNbdonxBCiDskI3hCCFHxHMKWZFQDooCVSqm6mqZdAT4DQvLUfQ74zp7ctQGWY5sOWANYCmy0J4Y5QoAnAE97YlTgsex1BwGPAa2BttgSq7zeB0zYEok2QC9gYCFtMgOjsI0+dcI2+vQqgFLKA0gAvsI2ynUfsMX+udH2mB8HqgIvAVmFHON6AcBhoA4wA9so1Zv2YzQH/IAp9hgMwCbgCLZkqB6wxp6ArgH65dlvCLAlJ7lTSl1QShU4rdJOd93rStimWeYcdyEwDFvSeSeCgN9z3iilqgJTsZ2z630JGJRSAfZjvgT8ii15zcc+rbRL3n0LIYQoOjKCJ4QQFYymaevyvP1YKfU60AHYgO26q6XARHv5C/b3AP8Clmqa9pP9/Qql1ASgI/CdfduCnNGk2zjWc9hG0o4BKKWisSVmKKXqYEu6PDVNuwxcUkrNzYmhgDb9kudtilJqKdAV26jdk8ApTdPm2MuNQE4bBgKvaZqm2d//z358jxtO3I1OaJqWMx3SBBy0PwDSlFKxwBv29x2wJX4Rea5p225/XgGsU0qN1zTNim3KZe6Il6ZpnjeJ4SvgNaXUWiAd22gk2KZbgu2aup80TftFKdXqNtoEgFLqJaA9+RPqadhGC48ppa7/SAa2UdPt2JLMC8Bj9vZcbwq2L5jfu914hBBC3D5J8IQQooJRSr2IbRSmoX2TO7aRL4CtgKv9mqrT2EbX1tvLGgD97Ytp5HDBlrjkOJrn9a2O5XNd/byvGwDOwMk8yYT++v3nOU5TbNM522NLbpyAnKTPD9tIYkFuVnYr17e1DtemYHrY403Pc5wj1y9YAqBp2k9KqSygm1LqJLYRxo23GcNy+76/xdbmOdimbR5TSvlgS/Da3UmjlFJPYxuJDNY07ax9W2sgGNtIakFeBgYALbAlub2ATUqpNpqmnciz72HYprR2sY8YCyGEKGKS4AkhRAWilGqA7TqxHsCPmqaZlVK/Yp/mZ3+/Fts0wdPAJk3TMuwfPwrM0DRtxk0OkTtic6tjAScB3zyf9cvz+ihwBahZUFJUgMVAIhCiaVqGUmoktgU/cvZV2IIeR4HGwL7rtl+yP7tiW1ESwPu6OtePTs20b2uladp5e6K0MM9x6iulnAppzwps0zRPYVud0lhIvPlommbBNkr4BoBSqhdw3P7oA9QF/rAnyVWAKkqpU0C9Qq5lfBTbz+yJnGsC7bphS9JT7ftyxzYl835N09pi+yJgk6ZpSfb6X9mT1c7AJ/Z9vwSMB4JyRm2FEEIUPUnwhBCiYnHDloTkXN81ANsCHHmtBj4HznFtqibY/vBfr5RKwLa4iCu2P/y35UkC7+RYa4ERSqnN2BKqnOmFaJp2UikVD8xRSk0GMgF/wFfTtO+4kQe2RCxTKdUMGJJzXGzXvsXak77F2EYd77dPNf03ME0p9Qe2kadWwHFN09KUUseBfvbpnv2xJYI34wH8BfyllKoHROQp+xlbQhutlHoD2zWD7TRN+8FevhLb9NAMbFM0b4v99gde2K4FbI5tFHOqpmkWpdSXXBs5Bfgntim3TxWS3D0CrAKe0TTt5+uK3yH/gihj7fseYn+/C5iolIrDtjhNMNAUe+KslOqLLQHurmna4dttnxBCiDsni6wIIUQFomnaH9im8f2IbYSuFfDDdXV+wpZw+WBbPCNn+25sC6MsxDb18CAQdg/HWgbEA3uxjb59ge1atpzk40Vsydgf9uN9gm1EqiBjsSUvGfb9fpwnjgygJ7api6eAA1xbHTIWW6IZjy1BfBfbSBf2tkZgS3RbYFs58maisC0W8xewGduCNTkxmO3Hvw/bqqTHsCVcOeVHgT3YEuLv8+5UKZWplOpSyDFrYjtvl7D9rJZrmvaOfZ9XNE07lfOwx3XV/hqlVH37vuvb9zUZ22I4X9i3Z9qTRDRNy7puX5mAMc8qnx9gSwC/tZ/HBcArmqb9aS+fjm1hnl159r3kFudTCCHEXdBZrXe6qJYQQghR9JRSjwFLNE1r4OhYHEEptRzbwi2THB2LEEKIskumaAohhHAIpVQVbCNp8dhuNfAG1xZ0qVCUUg2BZyl8ERMhhBDitsgUTSGEEI6iwzatMR3bFM39QKRDI3IApdQ0bNeqzdI0LdnR8QghhCjbZIqmEEIIIYQQQpQTMoInhBBCCCGEEOVEWbwGrxLwELblpm9Y5lkIIYQQQgghyjkDtpWld2G7b2yuspjgPcR1S0gLIYQQQgghRAXUBdied0NZTPBOAqSnX8JiKV3XD9ao4c65c5mODkOUAtIXRA7pCyKH9AWRl/QHkUP6gshxJ31Br9fh5eUG9twor7KY4JkBLBZrqUvwgFIZk3AM6Qsih/QFkUP6gshL+oPIIX1B5LiLvnDDJWuyyIoQQgghhBBClBOS4AkhhBBCCCFEOVEWp2gWyGw2kZ6ehsmU7bAYzpzRY7FYHHb80kavN1Clijvu7tXQ6XSODkcIIYQQQohyr9wkeOnpaVSu7Iqbm7fDkgknJz0mkyR4AFarFbPZREbGBdLT06hevbajQxJCCCGEEKLcKzdTNE2mbNzcqspIUSmh0+lwcnLG07MG2dlGR4cjhBBCCCFEhVBuEjxAkrtSSKfTA7IylBBCCCGEECWhXCV4QgghhBBCCFGRSYJXTLZt+5a+ff/BgAEvkJqa4uhwbpCRkcGqVSsKLc/Ozmb06OE88UQPnniiRwlGJoQQQgghhLhbkuAVkw0bPuPllwfz3nurqV+/4W1/zmy+4V6FxSIzM4PVqz8otFyv1xMS0o958xaVSDxCCCGEEEKUJl9//RWPPx7Mb7/9z9Gh3JFys4pmabJgwRz27k0kNfUI69evIy5uKTt37mDp0oVYLBY8Pb2IiJiAr68fe/bsZv782SjVnKQkjUGDhtC6dRvi4uZy6NABsrOzadOmPcOHj8JgMJCWdoZ582Zx7NhRAIKDexMaOoD4+K9Yt+4jTKarAAwdOpL27TtgsViIjX2LPXt24ezsgqtrFRYvXk5sbAyZmZmEhb1A5cqVWbJkeb42ODk58dBDAZw8eaLEz58QQgghhBCOkp5+nkmTxrNu3RqaNWtO7drejg7pjpTbBO+H306yfe/JYtn3ww/UJbBV3ULLw8PHkJSkERISSmBgF9LTzzN9eiRxce/g79+ITZs+JypqEsuW2aZIJicfJiJiAi1bPgBAdPQ0Wrduy/jxk7FYLERFTWLz5o306fMMU6dOplOnQGbMmAXAhQsXAAgI6EjPnr3R6XSkpqYwYsSrrF//BQcPJpGYuJuVK9eh1+u5ePEiAKNHj2PgwFDef391sZwjIYQQQgghyppNmzYybtxo0tPPM2bMOEaOHEulSpUcHdYdKbcJXmny++/7aNy4Kf7+jQB4/PE+zJkTQ1bWJQB8ff1ykzuA7du3sX//76xZswoAo9FI7dp1yMrKYt++vcyd+3ZuXU9PTwCOHz/GlCkTSUtLw8nJifPnz3Hu3Fl8fHwxmUxER0+jbdv2dO7cpaSaLYQQQgghRJmQlpbG66+PZePG9bRq9SBr1nxGq1YP3PqDpVC5TfACW918lK00qVLF9botVmbOnE29er75tmZlZRW6jylTJjJs2CiCgrphsVgIDn6Y7OxsatSoyYcfriUx8Rd27/6ZxYvjWL58ZTG0QgghhBBCiLLFarXy2WfrmDjxNTIzM5kwIZKhQ0fg7Ozs6NDumiyyUgJatGjFoUNJHDmSAsCXX26iSROFq6tbgfUDA4NYuXJF7oIrFy5c4MSJ47i6utKy5QOsXXttWmXOFM3MzEzq1vUBYPPmjWRnZwOQnp6O0WgkIKATgwcPw93dnRMnjuPm5obRaMRkMhVXs4UQQgghhCi1Tp48wYsvPs+QIQPx92/Eli3bGTlybJlO7qAcj+CVJl5eXkyaNJWoqImYzWY8Pb2IjJxWaP0RI8awaNECwsJC0Ol0ODu7EB4+Bh+fekRGTiM2NobQ0OfQ6w307Nmbfv3CCA8fzYQJY/Hw8CAgoDPVqlUD4MyZ08TETMdsNmM2m+nYsTMtWrRCr9fTq9dj9O//PB4eVW9YZAVg4MAXSUs7TUZGBs888zgBAZ0YP35ysZ0nIYQQQgghipvVauWjj1YSGTmB7OwrREXN5F//GoLBYHB0aEVCZ7VaHR3DnWoIJJ87l4nFci32U6eO4O3dwGFBATg56TGZLA6NoTQqDT+bklarlgdpaRmODkOUAtIXRA7pCyIv6Q8ih/SFknX0aCqjRw/nu++20qlTIHPnxtGo0X2ODgu4s76g1+uoUcMdwB9IyVt2WyN4SqnZwN+xJVetNE3bZ9/eFFgB1ADOAS9qmnZAKVUD+BBoDGQDB4BXNE1Ls3+uI7AUqGIPqJ+maWduqzVCCCGEEEIIcQcsFgvvv/8u06a9gdVqJTp6DmFhL6PXl78r1m63RZ8DQcCR67YvAd7WNK0p8Da2pA3ACrylaZrSNK0VcAiIBlBK6YGVwFD757bllAkhhBBCCCFEUTp8+BDPPvsk48ePoX37h9i2bScvvTSoXCZ3cJsjeJqmbQdQSuVuU0rVBtoCPe2bPgIWKqVq2Ufqvs2zi53AEPvrdoAxZ5/YksQU4KW7aoEQQgghhBBCXMdsNrNs2WLefHMazs4uzJv3NiEh/dDpdI4OrVjdS9rqBxzXNM0MYH8+Yd+eyz5iNwTYaN9UnzwjgZqmnQX0Sqnq9xCLEEIIIYQQQgCQlKTx5JO9iIycQJcuXfn++5944YXQcp/cQcmsohkHZAILi3Kn9osKc505o8fJyfHDrKUhhtJGr9dTq5aHo8MocRWxzaJg0hdEDukLIi/pDyJHcfeFadOm8eOPP9K8efN8j+rVy9/4ytWrV5k9ezZTpkzB3d2dVatWERISUmYSu6LoC/eS4B0F6imlDJqmmZVSBsDHvh3IXZylCfA3TdNylpdMBRrkqVMTsGiadv5ODn79KpoWi8XhK1jKKpoFs1gsFW51KFkRS+SQviBySF8QeUl/EDmKuy9cvnyZmTNn4ubmxtatWzEajbllNWvWomlTRZMmiqZNm9qfFXXr+pSZhCivfft+Y+TIoezd+yt9+jzDzJmzqF27NmfPZjo6tNtyl6to3uCuEzxN084opX4FQrAtmhICJOZZKXMmtuvtntA07Uqej/4CVFFKPWy/Dm8wsO5u4xBCCCGEEEIUbMeO7zEajaxY8RFBQd04ejSVAwc0kpKS7M8an3/+KX/9dSH3M+7uHjRp0iQ34ctJABs08MfJqfTdRjs7O5u5c2cxf/4cPD29ePfdD/nb355ydFgOc7u3SVgAPAt4AwlKqXOaprXAlpytUEpFAunAi/b6LYDXgSRgh31xlmRN057RNM2ilAoFliqlKmO/TULRNsvxtm37lqVLF+Li4kJU1Ezq12/o6JDyycjIYOPGz+jbt3+B5b/99j/efns+mZm2bxE6dXqYV18NL5Pf5gghhBBCVFQJCfG4urrSqVMgBoOBhg39adjQn549H82tY7VaOXPmTG7Cl5MAbtv2LWvXfpRbz8XFhUaNGtOkiaJJk6a5yV/jxvfh6urqiOaRmPgLI0cOZf/+P/i//3ueadPepHr1Gg6JpbSQG50XobxTNMeMCeeJJ/rwyCPBd7QPs9mMwWAojvDyOXnyBAMHhrJ585YCyw8fPoizswt+fvXJzs5mxIghPPXUszz66BN3fKzS8LMpaTL1RuSQviBySF8QeUl/EDmKsy9YrVY6dHiQZs2a8+GHH9/VPi5e/IsDB5LyPGxJYEpKMhaL7e9enU6Hn199mjRpip9ffapUcaVKlcpUrlyFypWvPVepUiXftpw6lSpVyvfe2dn5loMKly9fZtasN1m0aAF16ngze/a8fElrWVSiNzovi64m/cBVbVux7NtZBeHcNLDQ8gUL5rB3byKpqUdYv34dcXFL2blzB0uXLsRiseDp6UVExAR8ff3Ys2c38+fPRqnmJCVpDBo0hNat2xAXN5dDhw6QnZ1NmzbtGT58FAaDgbS0M8ybN4tjx2yXOgYH9yY0dADx8V+xbt1HmExXARg6dCTt23fAYrEQG/sWe/bswtnZBVfXKixevJzY2BgyMzMJC3uBypUrs2TJ8nxtaNTovtzXLi4uNG2qOHXqZDGcTSGEEEIIURwOHTrIkSMpDB064q73UbVqNdq1e4h27R7Kt/3KlSscPnzohlG/PXt2YzQauXz58l0fU6/X50v4bkwSK3Pw4AFSUpIJDQ3jjTemUbVqtbs+XnlTbhM8RwoPH0NSkkZISCiBgV1ITz/P9OmRxMW9g79/IzZt+pyoqEksW7YCgOTkw0RETKBlywcAiI6eRuvWbRk/fjIWi4WoqEls3ryRPn2eYerUyXTqFMiMGbMAuHDBNl86IKAjPXv2RqfTkZqawogRr7J+/RccPJhEYuJuVq5ch16v5+LFiwCMHj2OgQNDef/91bdsT3r6eb799htmzZpXHKdLCCGEEEIUg4SE/wLQo0fPW9S8c5UqVaJ58/tp3vz+AsutVitXrlzBaLycm/AZjUauXDHme399ecH182/LyMigVq3azJo1j65duxd528q6cpvgOTcNvOkoW0n6/fd9NG7cFH//RgA8/ngf5syJISvrEgC+vn65yR3A9u3b2L//d9asWQWA0Wikdu06ZGVlsW/fXubOfTu3rqenJwDHjx9jypSJpKWl4eTkxPnz5zh37iw+Pr6YTCaio6fRtm17OnfuckexZ2VdYty40Tz/fD+aNm12T+dBCCGEEEKUnISEr2nWrDl+fvVL/Ng6nc4+8la5xI9d0ZXbBK8sqVLl+otSrcycOZt69Xzzbc3Kyip0H1OmTGTYsFEEBXXDYrEQHPww2dnZ1KhRkw8/XEti4i/s3v0zixfHsXz5ytuKy2g08tpro+jQoSMhIeVuHRwhhBBCiHIrMzOTH3/czqBBQxwdiihhclfuEtCiRSsOHUriyJEUAL78chNNmihcXd0KrB8YGMTKlSswm82AbRrmiRPHcXV1pWXLB1i79tq0ypwpmpmZmdSt6wPA5s0byc7OBiA9PR2j0UhAQCcGDx6Gu7s7J04cx83NDaPRiMlkKjCGK1euMG7cKO6/vyUDBw4ukvMghBBCCCFKxvfff8fVq1cJDu7l6FBECZMRvBLg5eXFpElTiYqaiNlsxtPTi8jIaYXWHzFiDIsWLSAsLASdToezswvh4WPw8alHZOQ0YmNjCA19Dr3eQM+evenXL4zw8NFMmDAWDw8PAgI6U62a7ULTM2dOExMzHbPZjNlspmPHzrRo0Qq9Xk+vXo/Rv//zeHhUvWGRlU2bNpCY+At//fUXP/+8E4Du3XvQv//LxXeihBBCCCFEkUhIiMfd3YMOHTo6OhRRwuQ2CUUo720SxDWl4WdT0mT5a5FD+oLIIX1B5CX9QeQojr5gtVpp0+Z+2rRpx3vv3d6lOcLxiuo2CTJFUwghhBBCiHJk//4/OHHiuEzPrKAkwRNCCCGEEKIcSUiIB4rn9gii9JMETwghhBBCiHJky5Z4WrZ8AG/vuo4ORTiAJHhCCCGEEEKUE3/9dYGff94p0zMrMEnwhBBCCCGEKCe++24rZrOZHj0kwauoJMETQgghhBCinEhIiMfT05N27do7OhThIHIfvGKybdu3LF26EBcXF6KiZlK/fkNHh5RPRkYGGzd+Rt++/QssP3v2LOPGjcJsNmOxmKlfvyGvvTaRqlWrlnCkQgghhBDidlgsFrZs+Zru3Xvg5CR/5ldUMoJXTDZs+IyXXx7Me++tvqPkzmw2F19QeWRmZrB69QeFlnt6evL228t4//3VfPDBx9SuXZsVK/5dIrEJIYQQQog799tv/yMt7YxMz6zgJLUvBgsWzGHv3kRSU4+wfv064uKWsnPnDpYuXYjFYsHT04uIiAn4+vqxZ89u5s+fjVLNSUrSGDRoCK1btyEubi6HDh0gOzubNm3aM3z4KAwGA2lpZ5g3bxbHjh0FIDi4N6GhA4iP/4p16z7CZLoKwNChI2nfvgMWi4XY2LfYs2cXzs4uuLpWYfHi5cTGxpCZmUlY2AtUrlyZJUuW52uDk5NT7jc/ZrOZy5cv4+bmXrInUgghhBBC3LaEhHh0Oh3duwc7OhThQOU2wfvp5C/8eHJXsey7U92HCKjbrtDy8PAxJCVphISEEhjYhfT080yfHklc3Dv4+zdi06bPiYqaxLJlKwBITj5MRMQEWrZ8AIDo6Gm0bt2W8eMnY7FYiIqaxObNG+nT5xmmTp1Mp06BzJgxC4ALFy4AEBDQkZ49e6PT6UhNTWHEiFdZv/4LDh5MIjFxNytXrkOv13Px4kUARo8ex8CBobz//uqbtjUs7AVOnz5F48b3ERMTe8/nTgghhBBCFI+EhHjatGlLrVq1HB2KcKBym+CVJr//vo/GjZvi798IgMcf78OcOTFkZV0CwNfXLze5A9i+fRv79//OmjWrADAajdSuXYesrCz27dvL3Llv59b19PQE4PjxY0yZMpG0tDScnJw4f/4c586dxcfHF5PJRHT0NNq2bU/nzl3uKPb331+NyWRi3rxZfP75p4VesyeEEEIIIRzn3Llz7Nmzm7Fjxzs6FOFg5TbBC6jb7qajbKVJlSqu122xMnPmbOrV8823NSsrq9B9TJkykWHDRhEU1A2LxUJw8MNkZ2dTo0ZNPvxwLYmJv7B7988sXhzH8uUr7yg+JycnHn30Sd56a7okeEIIIYQQpdDWrQlYrVa5/52QRVZKQosWrTh0KIkjR1IA+PLLTTRponB1dSuwfmBgECtXrshdcOXChQucOHEcV1dXWrZ8gLVrr02rzJmimZmZSd26PgBs3ryR7OxsANLT0zEajQQEdGLw4GG4u7tz4sRx3NzcMBqNmEymAmM4ffpUbkJpsVj47rtvaNTovns/GUIIIYQQosglJMRTs2ZNHnywjaNDEQ5WbkfwShMvLy8mTZpKVNREzGYznp5eREZOK7T+iBFjWLRoAWFhIeh0OpydXQgPH4OPTz0iI6cRGxtDaOhz6PUGevbsTb9+YYSHj2bChLF4eHgQENCZatWqAXDmzGliYqZjNpsxm8107NiZFi1aodfr6dXrMfr3fx4Pj6o3LLKSmnqEhQvnAVYsFgtNmihGjowoztMkhBBCCCHugtlsZuvWBHr2fBS9XsZvKjqd1Wp1dAx3qiGQfO5cJhbLtdhPnTqCt3cDhwUF4OSkx2SyODSG0qg0/GxKWq1aHqSlZTg6DFEKSF8QOaQviLykP4gcRdEXdu36iSee6Mk777zH00//vYgiEyXtTvqCXq+jRg13AH8gJV9ZkUcmhBBCCCGEKDFbtsSj1+vp1u0RR4ciSgFJ8IQQQgghhCjDEhK+5qGHAvD09HJ0KKIUkARPCCGEEEKIMur06VPs3furrJ4pckmCJ4QQQgghRBn1zTcJAPToIQmesJEETwghhBBCiDIqISEeb++6tGjR0tGhiFJCEjwhhBBCCCHKoKtXr/Ltt98QHNwLnU7n6HBEKSEJnhBCCCGEEGXQrl0/kZFxUaZninwkwSsm27Z9S9++/2DAgBdITU1xdDg3yMjIYNWqFbesZ7VaGTHiVZ54okcJRCWEEEIIIW5XQkI8zs7OBAV1dXQoohRxulUFpdRs4O/YbjDeStO0ffbtTYEVQA3gHPCipmkH7qWsPNmw4TNefnkwjzwSfEefM5vNGAyGYorqmszMDFav/oC+ffvftN6nn36Mt7c3Bw9qxR6TEEIIIYS4fVu2fE3Hjp3x8Kjq6FBEKXLLBA/4HJgPfH/d9iXA25qmrVRK9QOWAo/cY1mRubjjB/7avq2odwtAtYeDqNo5sNDyBQvmsHdvIqmpR1i/fh1xcUvZuXMHS5cuxGKx4OnpRUTEBHx9/dizZzfz589GqeYkJWkMGjSE1q3bEBc3l0OHDpCdnU2bNu0ZPnwUBoOBtLQzzJs3i2PHjgIQHNyb0NABxMd/xbp1H2EyXQVg6NCRtG/fAYvFQmzsW+zZswtnZxdcXauwePFyYoqSycAAACAASURBVGNjyMzMJCzsBSpXrsySJctvaMfRo6ls2RLPhAlT2L79u2I5l0IIIYQQ4s4dP36M/ft/Z8qUGY4ORZQyt0zwNE3bDqCUyt2mlKoNtAV62jd9BCxUStUCdHdTpmla2j23ppQIDx9DUpJGSEgogYFdSE8/z/TpkcTFvYO/fyM2bfqcqKhJLFtmmyKZnHyYiIgJtGz5AADR0dNo3bot48dPxmKxEBU1ic2bN9KnzzNMnTqZTp0CmTFjFgAXLlwAICCgIz179kan05GamsKIEa+yfv0XHDyYRGLiblauXIder+fixYsAjB49joEDQ3n//dUFtsFisRATM53Ro8fh5HQ73wMIIYQQQoiSsmXL1wBy/ztxg7v9y90POK5pmhlA0zSzUuqEfbvuLsvuKMGrUcM93/szZ/Q4OV27pLB6UBeqB3W5y+bdvZwYdDodBoMOJyc9f/75O/fd15QmTe4DoE+fp5kzJ4YrVy5jMOjx86tP69atc/fxww/b2L//dz7+eBUARqMRb+86ZGcb2bdvL3Fxi3OPU7NmdQBOnTpBVNQk0tLO4OTkxPnz5/jrr/PUr++H2WwiJmYa7ds/RGBgEE5OegwGPaDLd87y+vDDD2jbth3NmzfnxIkTN617K3q9nlq1PO7qs2VZRWyzKJj0BZFD+oLIS/qDyHE3feH777+hYcOGdO7cTlbQLEeK4vdCmR2aOXcuE4vFmvveYrFgMlkcGJEtucuJwWq1YjZbMZksmM1WrFZyyywW27PZbMFstlC5cpV8sVutVmbOnE29er759p+VlQXk7Cd/WydPfp1hw0YRFNQNi8VCcPDDZGUZqVatOh98sJbExF/YvftnFi5cwPLlKzGbLYC10HOWmLiHgwcP8MUXmzCbzWRkXOTpp59gxYqPcHNzL/AzhbFYLKSlZdzRZ8q6WrU8KlybRcGkL4gc0hdEXtIfRI676QtXrlzh668T+Oc/Qzh7NrOYIhMl7U76gl6vu2HAK7fsLo9/FKinlDIA2J997NvvtqzcatGiFYcOJXHkSAoAX365iSZNFK6ubgXWDwwMYuXKFZjNZsA2DfPEieO4urrSsuUDrF17bVplzhTNzMxM6tb1AWDz5o1kZ2cDkJ6ejtFoJCCgE4MHD8Pd3Z0TJ47j5uaG0WjEZDIVGMNbb83js88288kn/2HRon/j4eHBJ5/8546TOyGEEEIIUbR27txBVtYlmZ4pCnRXI3iapp1RSv0KhAAr7c+JOdfR3W1ZeeXl5cWkSVOJipqI2WzG09OLyMhphdYfMWIMixYtICwsBJ1Oh7OzC+HhY/DxqUdk5DRiY2MIDX0Ovd5Az5696dcvjPDw0UyYMBYPDw8CAjpTrVo1AM6cOU1MzHTMZjNms5mOHTvTokUr9Ho9vXo9Rv/+z+PhUbXARVaEEEIIIUTpk5AQT6VKlQgMDHJ0KKIU0lmt1ptWUEotAJ4FvIGzwDlN01oopZphu92BF5CO7XYHmv0zd1V2mxoCyddP0Tx16gje3g3uYDdFL+8UTXFNafjZlDSZeiNySF8QOaQviLykP4gcd9MXOnduR/36DViz5rNiiko4wl1O0fQHUvKW3c4qmuFAeAHb/wQCCvnMXZUJIYQQQgghCpecfJiDBw/w0kuDHB2KKKXu9ho8IYQQQgghRAn75hvb7REeeaTnLWqKikoSPCGEEEIIIcqIhIR4Gje+j0aNGjs6FFFKSYInhBBCCCFEGZCVlcUPP3wvq2eKm5IETwghhBBCiDJgx47vMRqN9OghCZ4onCR4QgghhBBClAEJCfG4urrSqVOgo0MRpZgkeMVk27Zv6dv3HwwY8AKpqSmODucGGRkZrFq1otDykydP0LVrAGFhL+Q+/vrrQglGKIQQQgghclitVhIS4gkK6kalSpUcHY4oxe7qRufi1jZs+IyXXx7MI48E39HnzGYzBoOhmKK6JjMzg9WrP6Bv3/6F1nF3d+f991cXeyxCCCGEEOLmDh48QGrqEYYNG+noUEQpJwleMViwYA579yaSmnqE9evXERe3lJ07d7B06UIsFguenl5EREzA19ePPXt2M3/+bJRqTlKSxqBBQ2jdug1xcXM5dOgA2dnZtGnTnuHDR2EwGEhLO8O8ebM4duwoAMHBvQkNHUB8/FesW/cRJtNVAIYOHUn79h2wWCzExr7Fnj27cHZ2wdW1CosXLyc2NobMzEzCwl6gcuXKLFmy3JGnTAghhCh2VqsVo9HIpUuXuHQp87rnS1SrVo3AwC7odDpHhyrEDRIS4gHo0UNujyBurtwmeNpvp/hz76li2XezB7xRrbwLLQ8PH0NSkkZISCiBgV1ITz/P9OmRxMW9g79/IzZt+pyoqEksW2abIpmcfJiIiAm0bPkAANHR02jdui3jx0/GYrEQFTWJzZs30qfPM0ydOplOnQKZMWMWABcu2KZNBgR0pGfP3uh0OlJTUxgx4lXWr/+CgweTSEzczcqV69Dr9Vy8eBGA0aPHMXBg6E1H6C5dusTLL4ditVoJDu5FSEio/KcnhBCiyFitVsxmM2azGZPJhMWS89ps327CbDaTnX0lNwnLm5Dd6nVWVtYN2y0Wy01j6tbtEaKj58gS9KLUSUiIp1mz5vj51Xd0KKKUK7cJXmny++/7aNy4Kf7+jQB4/PE+zJkTQ1bWJQB8ff1ykzuA7du3sX//76xZswoAo9FI7dp1yMrKYt++vcyd+3ZuXU9PTwCOHz/GlCkTSUtLw8nJifPnz3Hu3Fl8fHwxmUxER0+jbdv2dO7c5bZirlGjJuvXf4GXV3XS088zbtxoPDyq8re/PV0k50QIIUTZkpFxkT//3G9//MGff/5JZubF3GTMYrElaTkJ2/WJW0H1bpVs3S4nJyfc3Nxxc3PL83DH29s793XOdldX93x18j7v3PkDM2dOo2vXjowaFcHQoSPkWidRKmRmZrBz5w/861+vOjoUUQaU2wRPtbr5KFtpUqWK63VbrMycOZt69Xzzbc3Kyip0H1OmTGTYsFEEBXXDYrEQHPww2dnZ1KhRkw8/XEti4i/s3v0zixfHsXz5ylvG5OLigotLdQC8vKrTq9ej/Pbb/yTBE0KIcu7y5cscPJjE/v1/5Enm9udeGgDg6upGs2bN8PKqjpOTE3q9AScnJwwGAwaDHoPB9jqnzGDQ32Y9A05OBnt5Tj0DLi4uuLt7FJCYueHq6oaLi0uRzDBp2bIVTz75FJMmjSc6ejqffPIxs2bNIzDw9r4cFaK4bNv2HVevXpX734nbUm4TvNKkRYtWREdP5ciRFBo0aMiXX26iSROFq6tbgfUDA4NYuXIFY8eOx2AwcOHCBbKyLuHjU4+WLR9g7drVvPDCi4BtiqanpyeZmZnUresDwObNG8nOzgYgPT0dg8FAQEAn2rfvwI4d33PixHEaNGiI0WjEZDLh5HRjN0hPP4+HR1WcnJwwGo1s377ttkf/hBBClH5Xr14lOfkwf/75R75kLjn5cO7ImouLC/fd15QOHTrSv/9LNGt2f+4UMb2+fC7E7e1dl3//ewVbtvRl3LixPPPMEzz3XAhTpsygZs2ajg5PVFBbtsTj7u5Bhw4dHR2KKAMkwSsBXl5eTJo0laioiZjNZjw9vYiMnFZo/REjxrBo0QLCwkLQ6XQ4O7sQHj4GH596REZOIzY2htDQ59DrDfTs2Zt+/cIIDx/NhAlj8fDwICCgM9WqVQPgzJnTxMRMz50q07FjZ1q0aIVer6dXr8fo3/95PDyq3rDIyt69v/Lvfy9BrzdgNpvo3Plh/v7354r1PAkhhCh6FouFo0dTcxO4nGTu4MGk3C8D9Xo9/v6NaNbsfp5++u80b34/zZrdj79/I5ydnR3cAsfo0aMX27btZN682bz99ny+/vorIiOnERLSr9wmt6J0yrk9Qrduj1TYf4/izuisVqujY7hTDYHkc+cysViuxX7q1BG8vRs4LCgAJyc9JlPRXE9QnpSGn01Jq1XLg7S0DEeHIUoB6QsiR3H3BZPJxLFjR0lOPoym5b9WLueab7Bd992sWfPc0bjmze/nvvuaUqVKlWKLrazTtD+JiBjJzp07CAjoxFtvzaV58/vvaZ/yu0HkuFVf+P33fXTv3pl5897mhRdCSzAyUdLu5PeCXq+jRg13AH8gJW+ZjOAJIYSosA4fPsSPP/5AnTp18Pb2oW5dH6pXr15qVwzOysriyJEUUlKSSU4+TErKYVJSkklJSebYsaOYTKbcujVr1qJ58/vp2zc0N5lTqhlVq1ZzYAvKJqWasWHDl6xZs4qoqEn06PEwQ4YMZ8yYcbi6Xn8dvRBFa8sW2+0R7vTeyqLikgRPCCFEhXT0aCpPPtmTs2fP5tteqVIl6tSpS926tkdO4uft7W1/rou3d10qV65c5DFZrVbOnz+fL3HL+zh9Ov/tf6pV86RhQ38efLANTz31LA0b+tOwoT9NmzajVq1aRR5fRabT6QgJ6UevXo8xdepk4uLmsmHDZ7z55ix69nzU0eGJciwhIZ5WrR7E27uuo0MRZYQkeEIIISqcrKwswsL6cuVKNv/5Tzx6vY5Tp05y8uQJTp60PZ86dZL//e9X/vvfL7l8+fIN+6hevbo9+aubm/jVreuTLyksaDTQYrFw4sTxAhO45OTDZGRczFff27suDRv60717j9wErmFDf/z9G+HlVb1Yz5O4UY0aNZg/fxHPP9+XiIiR9O37HE8++RTTp0fj41PP0eHlOnv2LDt37qBTp0Bq1Kjh6HDEXbpwIZ1du34iPHyUo0MRZYgkeEIIISoUq9XKqFFD2bdvL6tWrSUg4Oar0lmtVv766wInT57k1KmT+RLBU6dsz3v3/o+zZ9O4/rp2FxeX3BE/L69qHDp0mNTUI7mLm4DtHm5+fvXx929E+/YP2RO4RjRs6E/9+g1kCmAp1alTIN988wOLF8cxZ04MW7du4fXXJ/HSS/8qcHXq4nb16lV27/6ZrVu3sHXrFv73v0QAAgO78Omn/5GFYcqo777bitlspkeP3o4ORZQhkuAJIYSoUOLi5rF+/adMmjSF4OBb/9Gk0+nw9PTC09PrpgtrXL16ldOnT9kTwGvJX85oYFpaGko1p3fvx/ONxNWr5+uQhEDcOxcXF0aMGMNTTz3L+PFjmDRpPGvXrmHWrLm0adOu2I+fkpKcm9Bt376NzMwMDAYD7dt3YPz4SVitVmJiZvDvfy+RG2SXUQkJ8Xh5edGuXXtHhyLKEPkfRQghRIWRkPBfZsyYwtNPP8vw4UU75cnZ2RlfXz98ff0KLJdVE8uvhg39+eijT/nPfz5n4sRxPProI7z00iBef31ykS5qk5mZyY4d37N16xa++SaB5OTDAPj51eeZZ/5B9+49CArqmntMq9VKYuIvTJ8+he7dg2nSpGmRxSKKn8ViYcuWr+nevQcGg8HR4YgyRBI8IYQQFcKhQwcYPHggLVq0Yt68RaV2pUxRNul0Ovr0eYZu3R4hOno67777Dps2bWT69Gj69Hnmrvqb1Wpl377f2Lp1C99+u4WffvqRq1evUqVKFQIDuzBw4Ct07x5M48b3Fbh/nU7HnDlxdO0awPDhr7Bp09cyWlyG7N37K2fPptGjRy9HhyLKGJmQXUy2bfuWvn3/wYABL5CamuLocG6QkZHBqlUrblrn5MkTjB0bTkjIs/Tr939s2vR5CUUnhBBF6+LFv3jxxRCcnZ1YsWK1XNcmik3VqtWYOXMW//3vVurU8WbQoDBCQv5OSkrybX3+7NmzfPrpWoYNe4WWLZvQo8fDTJ/+BufOnWPQoCGsW7cBTTvC6tWfMGjQEO67r8lNk8c6derw1ltz2bPnFxYsiC2qZooSkJAQj06no3t3uT2CuDPyNU4x2bDhM15+efAd37PEbDaXyDB8ZmYGq1d/QN++/Qsst1qtTJgwlgED/kVQUDesVisXLqQXe1xCCFHULBYLr746iOTkw3zyyUb8/Oo7OiRRAbRu3Zb//ncry5e/w5tvTicoKIDRo1/j1VfDcXFxya13/eIoe/f+itVqpXr16nTt2p3u3YPp1u2Re1oiv0+fZ3j22f8we3Y0PXv2plWrB4uiiaKYbdkST9u27ahZs6ajQxFlTLlN8JL/+JnkfTuLZd/+LTvif3+HQssXLJjD3r2JpKYeYf36dcTFLWXnzh0sXboQi8WCp6cXERET8PX1Y8+e3cyfPxulmpOUpDFo0BBat25DXNxcDh06QHZ2Nm3atGf48FEYDAbS0s4wb94sjh07CkBwcG9CQwcQH/8V69Z9hMl0FYChQ0fSvn0HLBYLsbFvsWfPLpydXXB1rcLixcuJjY0hMzOTsLAXqFy5MkuWLM/Xht27f8LV1Y2goG6AbZqHLMcthCiLYmKmEx//FdHRc+jc+WFHhyMqEIPBwKBBQ3jyyaeYNGk8M2dO5ZNPPmby5KlkZp5n48bNfP/9d7mLo7Rr9xCvvTaB7t178OCDbYr0C98335zNDz9sZ9iwV4iP/45KlSoV2b5F0Tt79ix79vxCRMTrjg5FlEHlNsFzpPDwMSQlaYSEhBIY2IX09PNMnx5JXNw7+Ps3YtOmz4mKmsSyZbYpksnJh4mImEDLlg8AEB09jdat2zJ+/GQsFgtRUZPYvHkjffo8w9Spk+nUKZAZM2YBcOHCBQACAjrSs2dvdDodqakpjBjxKuvXf8HBg0kkJu5m5cp16PV6Ll603V9p9OhxDBwYyvvvry6wDcnJyVStWo1Jk8Zx/PhR6tXzY/jwUdSp413cp08IIYrMhg2fMXfubEJDwxgwYKCjwxEVVN26Prz77gckJPyX8ePHEhr6TwB8ff1yF0fp0iWIatU8iy0GL6/qzJu3kJCQfxATM4PIyKnFdixx77ZuTcBqtRIcLNffiTtXbhM8//s73HSUrST9/vs+Gjduir9/IwAef7wPc+bEkJV1CbD9gs9J7gC2b9/G/v2/s2bNKgCMRiO1a9chKyuLffv2Mnfu27l1PT1t/xkcP36MKVMmkpaWhpOTE+fPn+PcubP4+PhiMpmIjp5G27bt6dy5y23FbLGY2bNnF++8s4IGDRqyZs1KZsyYwoIFS4rknAghRHHbt+83Rox4lYceCuDNN2fLoirC4YKDe7NtWxe2bPmazp3bU726T4n2yx49ehEaGsbbb8+nd+/Hb3kPSOE4W7bEU7NmLR54oLWjQxFlULlN8MqSKlWuv9jfysyZs6lXzzff1qysrEL3MWXKRIYNG0VQUDcsFgvBwQ+TnZ1NjRo1+fDDtSQm/sLu3T+zeHEcy5evvGVMdep4o1RzGjRoCEDv3o/z7rtL77RpQgjhEOfOnaN//xCqVfNk+fKV+a55EsKRXF1d+dvfnnLYbTOiombw3XffMnz4K3zzzQ+4u7uXeAzi5sxmM1u3bqFXr8fkBvXirkivKQEtWrTi0KEkjhxJAeDLLzfRpInC1dWtwPqBgUGsXLkCs9kM2KZhnjhxHFdXV1q2fIC1a69Nq8yZopmZmUnduj4AbN68kezsbADS09MxGo0EBHRi8OBhuLu7c+LEcdzc3DAajZhMpgJj6NgxkDNnTnP27FkAdu7cwX33Nbn3kyGEEMXs6tWrDBz4ImfOnGbFitXUqVPH0SEJUWq4u3sQF7eYI0dSmDp1sqPDEQXYs2c36enpMj1T3DUZwSsBXl5eTJo0laioiZjNZjw9vYiMnFZo/REjxrBo0QLCwkLQ6XQ4O7sQHj4GH596REZOIzY2htDQ59DrDfTs2Zt+/cIIDx/NhAlj8fDwICCgM9Wq2W5yeubMaWJipmM2mzGbzXTs2JkWLVqh1+vp1esx+vd/Hg+PqjcsslKlShVGjoxg7NhwrFYr1apVY8KEKcV5moQQoki88cYEfvjhexYuXErr1m0dHY4QpU6nToG88spQlixZyGOPPUn37j0cHZLIY8uWeAwGA127dnd0KKKM0lmtVkfHcKcaAsnnzmVisVyL/dSpI3h7N3BYUABOTnpMJotDYyiNSsPPpqQ5auqNKH2kL5Ss1as/ZOTIoQwePIypU2c6Opx8pC+IvBzdH4xGI8HBXcjIyOC7737E09PLYbFUdNf3heDgIFxdXdm48SsHRiUc4U5+L+j1OmrUcAfwB1Lylt3zCJ5S6glgGuAMnAfCNE1LVko9ad+usz+iNE37zP6ZpsAKoAZwDnhR07QD9xqLEEKIimvXrp947bVRdO3aXVYIFOIWKleuzMKFS3nssR5MmPAaixYtc3RIAjh9+hR79/7KpElTHB2KKMPu6Ro8pZQXtkTteU3TWgHLgMVKKR3wIRCqaVprIBRYoZTKOd4S4G1N05oCbwOyeocQQoi7dvLkCQYM6Efduj688857ODnJFQhC3Err1m0ZNSqCTz75mE2bNjo6HAF8800CYFvxVIi7da+LrNwHnNY0Lcn+/gugN1ATsADV7Ns9gZOaplmUUrWBtsBH9rKPgLZKqVr3GIsQQogKyGg0MmBAXy5dusSHH36Ml1d1R4ckRJkxalQEDz7YhoiIEZw5c8bR4VR4CQnx1K3rw/33t3B0KKIMu9evOJMAb6XUQ5qm7QL62rf7Ac8BG5RSlwAP4PE8Zcc1TTMDaJpmVkqdsG9Pu90D2+ec5jpzRo+Tk+MXBS0NMZQ2er2eWrU8HB1GiauIbRYFk75QfKxWKwMGDGfPnl9Yv349XbqUjvufFkb6gsirtPSH1atX0rZtWyZOHMP69evlnpEOUKuWB1evXuW7777hn//8J7VrV3V0SMJBiuL3wj0leJqm/aWU+icwVylVGfgSuACYgNeBpzRN+0EpFQisVUrdf88R212/yIrFYnH4AieyyErBLBZLhVtYwNEXz4vSoyT6gtFoJDHxF+rUqYOfXwOcnZ2L9XilyTvvLGLFihVERLxOYGCPUv3vTn4viLxKU3+oVcuP11+PZMqUiSxcuJTnn+976w+JIpPTF3bs2M7FixcJDOxeavqGKFl3ucjKDe75IgVN0xKABAClVB0gAvACfDRN+8Fe5wf7SF5z4AhQTyllsI/eGQAf4Oi9xiKEEBXNrl0/MXLkUA4csM2UNxgM+Pr64e/fKM+jMf7+jahfvwGVK1d2cMRFZ9u2b3njjYk8/vjfGDNmnKPDEaJMe+WVV/nqq81MnDiOhx8OwtfXz9EhVTgJCfE4OzsTFNTV0aGIMq4oVtH01jTtlH0BlZnYFlDRAF+llNI0TVNKNQfqAIc0TTuvlPoVCAFW2p8TNU277emZZcG2bd+ydOlCXFxciIqaSf36DR0dUj4ZGRls3PgZffv2L7B869YEVqy4dm+8tLTTPPhgW2bOnFVSIQohbuLy5ctER09nyZKF1Kvny6JFyzCZTCQnHyI5+TApKcl8+uk6Ll78K/czOp0OH596uYlfw4aN8rz2x83NzYEtujMpKckMGtSfJk2asnDhEvR6mR4vxL0wGAwsWLCYbt06M2LEUNat+1z+XZWwLVvi6dgxEHf30jF1V5RdRbHM2HT7FEwXIB4Yr2maUSk1BPhEKZUzZ/ElTdPO218PxraqZiSQDrxYBHGUKhs2fMbLLw/mkUeC7+hzZrMZg8FQTFFdk5mZwerVHxSa4HXvHkz37tdiHzDgBXr27F3scQkhbm3nzh8ZOfJVDh8+RP/+LxMZGYWHx43Xa1itVtLTz5OcfDjfIyUlmS+/3MTZs2fz1a9du851I3/Xkr9q1TxLqnm3lJmZSf/+IVitVlas+Ej+GBKiiDRs6M/UqTMZO3YE7723jJdffsXRIVUYx44dZf/+P4iK6ufoUEQ5UBRTNAcWsn0VsKqQsj+BgHs9dmm1YMEc9u5NJDX1COvXryMubik7d+5g6dKFWCwWPD29iIiYgK+vH3v27Gb+/Nko1ZykJI1Bg4bQunUb4uLmcujQAbKzs2nTpj3Dh4/CYDCQlnaGefNmceyYbUZrcHBvQkMHEB//FevWfYTJdBWAoUNH0r59BywWC7Gxb7Fnzy6cnV1wda3C4sXLiY2NITMzk7CwF6hcuTJLliwvtD2a9idpaWd4+GGZMiCEI126dIk335zKsmVL8POrz6ef/ocuXQr/d6nT6ahevQbVq9egXbuHbii/ePEvUlKS8yV+ycmH+fbbb1izJv+v7+rVq+dO9+zatTu9ez/mkBsjWywWhg8fjKb9yccfr8ffv1GJxyBEeRYaGsaXX25i6tRIunV7hMaNmzg6pAphy5avAQgOltsjiHtXbm8UlH3oPFcOnL91xbtQqUl1XBoXvgx3ePgYkpI0QkJCCQzsQnr6eaZPjyQu7h38/RuxadPnREVNYtmyFQAkJx8mImICLVs+AEB09DRat27L+PGTsVgsREVNYvPmjfTp8wxTp06mU6dAZsywTZW8cOECAAEBHenZszc6nY7U1BRGjPh/9u48Lqqqf+D4ZxgYYNiGRdkRBRxZVEDccM0lS8uneiqzMi3TJ7XcLTMzzeqxRS0tl8ce28wns1/lgpZlC64pgjsOmyKL7DsDDLP8/gBGSVRUlkHP+/XyNcPMnXvPnXu8c7/3nPM9U/nhh10kJSUQFxfDpk1bMTMzo6SkBIDZs1/h+efH8fnnm2+4v1FR2xg+/P67KnGDIJiagwf3M2PGVFJTLzBx4mRee20xtrYND65uLHt7B7p1C6Vbt9Cr3isvLyc19UK9wO/8+RSio//gu++2YG5uzsCBg3nggX9w//0P4OzsfFtlaayVK98nKmo7b775DoMG3dMi2xSEu4lEImHlyo8ZOLA3L774Ajt2/CzmlWwBe/fuwcfHF39/EVALt0/8j20BZ86cxs+vs/FO88iRo1m+/F3U6nIAvLy8jcEdwP790cTHnzHeQa+srKR9e1fUajWnT59k5cpPjMsqFDXdpjIy0lm8+DVyc3MxNzenoCCf/Pw8PDy80Gq1LFu2lPDwCCIjB9xU2TUaDb/88jOrV4u56AWhNZSVlfHWW2+wbdclMAAAIABJREFUceMGfH078uOPu4iM7N/s27WxsSEoKPiquZj0ej1xccfYuXM7O3ZsY/bsl5g3byaRkf154IF/MHLkg7i6ujZLmXbvjuLdd9/mscee4F//mtYs2xAEAdzc3Fm2bDkvvDCRTz75iBkz5rR2ke5oVVVVREf/wRNPPCWmqBCaxB0b4Mn8rt/KZkqsreV/e8XAO+98gKenV71X1Wr1NdexePFrvPjiLAYOHIxer2fYsP5oNBqcnV346qtviYs7RkzMEdauXc3GjZsaXbbo6N/x8PAUd5QEoRVER//B7NkvkZZ2kcmTp/Dqq4taPRGKmZkZPXr0pEePnixa9CanT59kx45t7Ny5jVdemc38+XPo3bsvDzwwmlGjRl91HrtV587FM3XqJMLCwvngg4/ERZAgNLOHH36UXbt28t577zB06L2EhHRt7SLdsaKjo1Gr1aJ7ptBkRHqkFhAc3JXk5ARSUy8AsHv3TgIClMjlDV+o9es3kE2bvkCn0wE13TAzMzOQy+WEhHTj228vd6us66JZVlaGu7sHAFFR29FoNAAUFhZSWVlJ7959eeGFF7G1tSUzMwMbGxsqKyvRarXXLXtU1HZGjRp9W/svCMLNKS0tYe7cmTz66GjMzc3Ztu0n3nrr3VYP7v5OIpHQtWt3FixYxIEDMURH/8XcufMpLi5m4cL5hIUFcf/9Q/j444+4cOH8LW+nqKiQ8ePHIpfL+eyzr7G2tm7CvRAEoSESiYR3312BQuHIiy/+i6qqqtYu0h1r165dWFlZ3XQvK0G4FhHgtQBHR0cWLnyTJUteY/z4J9izZzeLFi295vIzZsxBKjVjwoSxPPPMGObMeYnc3JpZJBYtWsqpUycYN+5xxo8fy86dPwIwffpsFiyYy3PPPUVmZgYODg4A5ORkM3PmVMaPH8v48WPp0yeS4OCu2Ns7cO+99zN+/BO88MJzDZYjOzuLU6dOMHz4fU38jQiCcC2//76XgQP78NVXnzFlykv89tsB+vTp29rFuiGJREKXLoHMm/cqf/55iEOHjvHaa29QXa3lzTdfp1ev7gwdOoAPP/yApKTERq9Xq9UyefKzpKen8dlnX+Ph4dmMeyEIwpWcnZ1ZsWI1Z8+e5oMPlrV2ce5Yu3btol+/Acjlf+/RJQi3RmIwGFq7DDfLFzifn1+GXn+57FlZqbi5dWi1QgGYm5uh1epvvOBdxhSOTUtr186O3NzS1i6GYAIaWxdKSop5443X+PrrLwkI6MyHH35Cz553RrLh1NQL7Ny5nZ07t3Hs2FEAAgODGDVqNA8++BBdugRes8vl4sULWbNmFStWrObppxue1qWtEOcF4UptqT7MmDGVLVs2s2PHz3fMeclUpKQk06dPGP/+9/tiWgrhps4LZmYSnJ1tAToCF658TwR4TUgEeA0zhWPT0trSD7fQvBpTF3799WfmzJlBdnYW06bNYN68V7GysmqhEraszMwMoqK2s3Pndg4fPojBYMDPz58HH3yIBx4YTdeu3Y3B3nffbWHq1Ek899wkli1b3solv33ivCBcqS3Vh9LSEgYN6otMJmPv3v0m1128KWVnZxEXF0tCggprayvs7Oyxs7PH3t4eOzs77O3tsbWt+bspztOffrqOBQte5siRE/j6dmyCPRDaMhHgiQCvzTCFY9PS2tIPt9C8rlcXiooKef31V9myZTNKZRc++mgN4eERLVzC1pOdnc3u3TvZsWMbBw/uQ6fT4ePjWxvodWPWrBcJD49g69Ztd8Q0LeK8IFyprdWH/fujeeSRB5g4cTL//vcHrV2cJlFUVMjx43EcPx5LXFwsx4/HculSZqM/L5PJsLOzqw0AHYzP6wLBK4PBugDRzs6h3vuTJk0gMzOdffuONuOeCm1FUwV4d2wWTUEQBFP200+7mDdvJnl5ucyaNZfZs1/B0tKytYvVolxdXZkwYSITJkwkPz+fn3/exY4dP7Jhw1qqq6vx9vbh00+/vCOCO0Fo6/r3H8ikSS+wYcM67r//AQYOHNzaRbop5eXlnDp1ojaQO0ZcXGy95E+dOvnRt28/wsLCCQ3tQVBQENXV1ZSUlFBaWkppaUnt85rHsrJSSkouv1bzr5SLF1ONf5eUlKDX3/jG/8yZM5tz14W7kGjBa0KiBa9hpnBsWlpbuzMrNJ+/14WCgnxee+0V/u//viUwMJhVq9bQvXtYK5bQ9BQXF/H773vp3j3MOH/onUCcF4QrtcX6oFarGTq0P5WVlfz55yHs7R1au0gN0mg0nD172tgqd/x4LCrVOWOw5enpRWhoOKGhYcZHBwdFk5fDYDBQXl5uDAavDBJLS2teq6hQ8+KLLyCT2Tf59oW2R7TgCYIgtDE7d27nlVdmU1hYwNy585k5cy4ymay1i2VyHBwUPPTQP1u7GIIg/I1cLufjj9czatRwXnvtFVavXtfaRUKn05GYmFDbzfIYx4/HcubMaeN0Uc7OzoSGhjNy5IOEhYXTvXs4rq6uLVI2iUSCra0ttra2uLm5X3O5thjsC6ZNBHiCIAjNLC8vjwUL5vLjj98TEtKNb775nq5du7V2sQRBEG5ajx49mTFjNitXfsDIkQ9y//2jWmzbBoOBCxfOG8fMnTgRx4kTx1GrywGwtbWje/dQJk2aUtvVMhxvb59rZukVhDuVCPAEQRCa0datW5k6dSrFxcXMn7+Ql16aJcaUCYLQps2ZM59fftnDnDnT6dmzNy4uLk26frVaTUpKMklJCSQmJpCcnEhiYiLJyUnGYM7S0pKQkK6MHfsUoaHhhIX1wN8/ADMzMcWzIIgAr5lER//B+vUfI5PJWLLkHXx8fFu7SPWUlpayffv3PPXUteeV+vLLjezZsxup1By5XM68eQvo1MmvBUspCG1b3Rxu3buH8d13OwgKCm7tIgmCINw2mUzGxx+v5957BzFv3kw2bvzqplvJDAYD2dlZJCYmkJSUeEUwl0Ra2kXjchKJBG9vH/z9A+jbN5LOnbsQFhZOly5B4maZIFyDCPCaybZt3zNx4gsMGTLspj6n0+mQSqXNVKrLyspK2bz5y2sGeImJKrZt+55Nm7ZibW3N1q3fsGbNR3zwwapmL5sg3AmionawZs0qJk+ezOLFyzA3F6dbQRDuHEFBwbz88mu89dYb/N//fcujj45pcLnKykrOn08xBnB1wVxSUhJlZZfHncnlNvj7B9CzZ2+efHIc/v4B+Pt3plMnP6ytrVtqtwThjnDHXnEkJyeQlKRqlnX7+yvx8+t8zfdXrVrOyZNxXLyYyg8/bGX16vUcPnyQ9es/Rq/Xo1A4Mm/eAry8vImNjeGjjz5AqQwkIUHFpElTCA0NY/XqlSQnJ6LRaAgLi+Cll2YhlUrJzc3hww/fJz09DYBhw0Ywbtyz7NnzE1u3/g+tthqAadNmEhHRC71ez4oV7xEbexQLCxlyuTVr125kxYp3KSsrY8KEJ7GysmLduo1/2wsJWq2WyspKrK2tKS8vo127lhmULAhtXVraRWbOnEb37mGsWrWKkhJNaxdJEAShyU2bNp2ff97Fq6/Oo0uXIEpKiklKSryiW2UCFy+mcmXGdk9PL/z9AxgzZiz+/p0JCOiMv38A7u4eYqycIDSROzbAa03Tp88hIUHF2LHj6NdvAIWFBbz11iJWr/4PHTt2YufOH1myZCEbNnwBwPnzKcybt4CQkJqkC8uWLSU0NJz5819Hr9ezZMlCoqK2M3r0w7z55uv07duPt99+H4CioiIAevfuw/DhI5BIJFy8eIEZM6byww+7SEpKIC4uhk2btmJmZkZJSQkAs2e/wvPPj+Pzzzc3uA8BAZ0ZM+YpHnvsQWxt7bC1teOTT/7T3F+dILR51dXV/Otfz6HT6fjPfz6rndtOBHiCINx5pFIpq1evY8iQfgwZ0s/4urW1NX5+AYSFhfPYY0/g7x9AQEBnOnXyx8bGphVLLAh3hzs2wPPz63zdVraWdObMafz8Ohvncxo5cjTLl79rHCjs5eVtDO4A9u+PJj7+DN988zVQ072hfXtX1Go1p0+fZOXKT4zLKhQ187ZkZKSzePFr5ObmYm5uTkFBPvn5eXh4eKHValm2bCnh4RFERg5oVJmzsi6xf/+ffPPNj7i4uLB585e8/fZi3nvvwyb5TgThTvXuu28TE3OE9es33lFzuAmCIDSkUyc/Nm36lvj4M/j717TGeXp6iWQnzchgMKDRVFFVVUVVVWXtv4ae13+0tbWnU6eA2kDbtrV3Q2hGd2yA15ZYW8v/9oqBd975AE9Pr3qvqtXqa65j8eLXePHFWQwcOBi9Xs+wYf3RaDQ4O7vw1VffEhd3jJiYI6xdu5qNGzfdsEy//fYrnTr5GzNj3XffKDZuFC14gnA9v/++l1WrVjBu3AQefvjR1i6OIAhCi+jffyD9+w9skW3p9fo7Jng0GAzodDpKS0spLMxvVJBWVVWJRqOp1+31ShKJBJnMEisrK2QyS2xs7HBycsHS0pLc3Bzi4o4QF3cEd3dP/Pw64+3tK5LV3IBWq21z4+jbVmnbqODgrixb9iapqRfo0MGX3bt3EhCgRC5vuJtCv34D2bTpC+bOnY9UKqWoqAi1uhwPD09CQrrx7bebefLJZ4CaLpoKhYKysjLc3T0AiIrabpzgs7CwEKlUSu/efYmI6MXBg/vIzMygQwdfKisrr1lpPTw8+PnnKCoqKrC2tubQoQN07CgyaApCQwwGAxkZ6UydOgk/P3+ee+55Tp8+jlqtRqGwxcOjE7a24m6pIAhCY+l0OkpKiigoyKewsIDCwprHysoKzMykWFiYY2Ehw9y87tGigdfqP1pYWNQuZ1HvuVQqbdT4P4PBgFarRautprq65t/VzzVotVqqqzXXeL/+39cK1ADMzc2RySyxtLTC0tIKR0fn2ueWf3u8/Fwmk113X0pKiklJSSQ5OYH9+3/H3NyCDh064ufXGVdX97t6HKTBYKC0tISCgnwKCvKMj5WVFQwfPgp3d8/WLmKjiQCvBTg6OrJw4ZssWfIaOp0OhcKRRYuWXnP5GTPmsGbNKiZMGItEIsHCQsb06XPw8PBk0aKlrFjxLuPGPY6ZmZThw0fw9NMTmD59NgsWzMXOzo7evSNxcHAAICcnm3fffQudTodOp6NPn0iCg7tiZmbGvffez/jxT2BnZ39VkpVBg4Zw9uxpJk58GgsLGXZ2dixY8Eazfk+CYIq0Wi0VFWrUajVqdTkVFeWo1era12qel5eXsnbtWkpKinn22QkcO3YYAAsLC7RaLfAXPj4dCQwMoV0717v6B1QQBOHvKisrrgrkiosL0ev1AJiZSVEoHPH09MbW1q42gLocMNUFVhUV5fWCp7rP34hEIrkqCJRKpeh02quCs8aSSqVXBZMymSVyue1VAaazswMaDVhZ1Q/epNKmv0y3t3cgNDSC7t17kJ19ieTkBFJTz5OcnICtrV1tF84A7O0dmnzbpkSv11NUVFgvkCsszDceY4lEgkLhiIeHFy4u7Wjf3q2VS3xzJNe7c2CifIHz+fll6PWXy56VlYqbW4dWKxSAubkZWm3jTiZ3E1M4Ni2tXTs7cnNLb7yg0Gr0ej0VFeoGg7eaAK7muUZTddVnzcykyOVy5HIbrK3lbN++ja+++oIFCxbxxBNPGl+3sLDA0tLAwYN/kZh4rrbbdDsCA0Po0KFTi0yJIpgOcV4QrnQ31ge9Xl/bKnc5kCsszKei4vIQFGtrOY6Ozjg6OuHkVPNob6+4pW6ZOp2ugUCwulGv1fVwaqjFrzGtgjdT3tauC9XV1aSlXSA5OYFLlzJqy+SKn19nfH07IZNZtlrZmkJ1dTWFhfn1WuaKigqMNwDMzc1xdHTGyckZJycXnJycUSgcmyXAvpGbqQtmZhKcnW0BOgIXrnxPBHhNSAR4DTOFY9PSWvtkLVytvLyMrKxMsrMvkZ19idLSkquWkUgkWFvLkcvlWFvb1D7WBHJ1QZtcLkcmszS2wh0+fIiHHrqfhx56hLVr/3tV61xdXaiuriYlJZFz505TXFyEtbU1SmUwAQGBYo6nu0RLnBfqupCJMTWmr7nqg06npbCwgPz8PAoK8jAYDMZARCaTGbszymQWta/LjEHLzQYm11NVVWkM4Opa54qKCtHrdQCYmZnh4OBoDOQUippHK6u773xoStcM5eVlnD+fRHJyAsXFRZiZSfHx6UCnTp3x8DD95DmVlZW1QdzllrmSkmLj+5aWlsYgrubRBTs7e5PZLxHgiQCvzTCFY9PSTOlkfbdSq8vJyso0BnV1AZ1MZomrqzuOjk5XBHI1wZylpdVNneQLCvIZMqQ/MpmMvXv3YWdnf9Uyf68LBoOBzMx04uNPk5mZhpmZlI4d/QgM7IqTk/Pt77hgspr6vFDTGlJce/GcV/uYT2VlJV5eHQgP74VC4dhk22stxcVFaDRVODu3M5mLsKbQFPVBp9NRVFRAfn4u+fl55OfnUlhYYBzXJZNZIpVKja1SjSGVSo2B3+Ug0OKKILB+QFj3WBPQ5Rtb5+oyhQNYWVnj6OhUr2XO3l4hejHUMsVrBoPBQH5+HsnJCVy4kERVVRXW1tZ07BiAn18Ajo6t+3ul1+tRq8uvaJWrOQdeWe9sbGzrtco5Obkgl9uY9DCJpgrwxBg8QRDuCGp1OdnZl2qDukuUltbcsZPJZLRv745SGYybmzuOjs5NcnI3GAzMnDmN3Nwcdu36tcHgriESiQRPT288Pb0pLi4iPv40KSkJJCcn4OrqTmBgV7y8fO6oC1nh9lVXV1NUVFBvrEhhYQE63eXWEIXCCS+vDshkliQmxrNjx3f4+XWme/cebTIlenFxESdOHOPChWSg5s67p6cP3t4d8PDwwsJC1solbFk1wVxhbTCXW1sPLnczk8kscXZ2ITi4O87OLjg7t8PGxtZ4vtPr9fWSf1z5qNFc/dqVj2VlpfWWvV4GRwcHhfEmWl23t6uzhQumTiKR4OLSDheXdkRE9CEj4yLJyYnEx5/i7NmTODo6104B5t/kvVC0Wm3tGPeG/tUNqVAb66FEIsHe3gFXV3djIOfo6IyVlVWTlqstEQGeIAhtUkWF2tg6l5WVaeyCYWEhw9XVDaUyEFdXDxwdnZolWNqwYS0//bSLt95aRvfuYbe0DgcHBX369CcsrCdJSec4d+4Mf/yxB1tbO7p0Ccbfvwsy2d11EVunsDAfKyv5Xdl9taJCbWyNa6iLkUxmiZOTM507BxkvZhwc6o9RCgkJ5dSpOFSqM5w/n0SXLiGEhIRiaWn6Y2lKS0s4ceIY588nIZVKCQkJxdHRmYyMVNLTL5KSkoiZmRlubp54e3fAy8unTQaw11OXAKIumMvPrwnqLwdzMpyc2hEY2BVn53Y4O7tga2t33ZtXZmZmyGSy2z6nGAwG9HodGk39QNDCQlY7bkm0yt1ppFIpPj4d8fHpSGVlJefPJ5GSkkhMzCGOHTuMp6c3fn6d8fLyue64NYPBQFVV1XUDN7W6vMGx7xYWFsbhEu7unsjlNtjY2ODoWNO9V3RLr0900WxCootmw0zh2LQ0U+xu0dZVVKhrg7lLZGdnUlxcBNSc9Nu3d8fNzR03Nw8cHZ2bvfXrxIk4Ro4cxtChw/nii/9d96LqZuqCXq8nLe0C8fGnycnJwtzcAj+/zgQGhtzxGc3q6HQ6jh8/ypkzJ7G0tKJ//8F4evq0drGaREPddWtScufVC+iuTDhha2tnbAWpe7yyVeZGyspKOX48hpSURGQyS7p2DaVLl+BWSR5wI2VlpZw8GUtycgJmZmYolcGEhHSvNyZLr9eTk5NFenoqaWmpxq7XTk7OeHl1wNvbFyenpmmlb2519UGv11NcXFQvmCsoyDeOVbOwkNW2yLng5FTTonKjYE5oW9rqNUNRUQHJyYmkpCRSUaFGJpPh6+uHq6s7lZUVlJeXG1vbysvLqKhQG3sdXMna2rp2nHtN0FYXyF3+J79rWuzFGDwR4LUZpnBsWlpbPVmbksrKinpdLouLCwEwN7fA1dUNV1cP3NzccXJyadHujKWlJQwdOgCNRsNvv+2/4bi5W60L+fl5xMef4sKFZPR6PZ6ePgQGhuDu7nnHXtgVFxexb99eCgry8fPrbOyCFhTUjbCwnm26ZcBgMGAwVJCcfLFeQFczjcbllNx1XYvqArqmanErKMgnNvYImZlpyOU2hIX1pGNHf5PoCqxWl3PyZBxJSecA6Nw5kJCQMOTy63frMxgMlJQUk5Z2gbS0VPLycjAYDMjlNnh51XTldHPzMKlgVqOpori4mOLiQtTqYjIyLlFQkGe86LWwsMDJycXYKufs3A47O/s79v+8UKOtXzPo9XqysjJJTk7g4sXzV3Qdv5xx+sp/dUFcXTIzUzgPmQoR4Jl4gBcd/Qfr13+MTCZjyZJ38PHxbdWy/V1paSnbt3/PU0+Nv+YyX331GXv27Ean0xEUFMLLL792S107TOHYtLS2frJuDTWThaeRkZFGdnYmRUV1AZ25sYXO1dUDZ+eWDej+XsYpUyaybdsP/PDDLvr06XvDz9xuXaioUKNSnSUhIZ7KygoUCke6dAmhU6cAzM1N58L1dhgMBhIS4omJOYS5uTl9+w7Cx8cXrVbLsWOHUanO4uLSjgEDhjZ6rKMpKSkp4uDBaHJysoCai/grU3LXdDFqma5tly5lEBv7F/n5eSgUToSH98LT07tVAoiKCjWnTx9HpYrHYNATENCFrl3Dbrm7ZWVlBRkZaaSlXSAzM92Y5t7Dwwsvr5qunC2RoVGv11NaWkJJSRElJcUUFxcbn1dWVhiXq6sHNcFcTUBnb+8ggrm70J10zaDRaCgvL8Xa2gZLS0tRn2+SCPBMPMCbM2c6o0aNZsiQYTe1Dp1O10I/8pk8//w4oqL2Nvj+kSOH+eSTD1m37jOsrKx477238fDwYty4CTe9LVM4Ni3tTjpZt4SKigoOHfqT9PSLmJub066dm7HLpSllzvv66y+ZNetFXn31dWbNmteozzRVXdDpdFy4kEx8/CkKCvKRySwJCOhCly7BbXr8UWVlBQcPRpOenoq7uxf9+g2+quUmNTWFgwejAQN9+w7C17dT6xT2Jun1es6ePcWJEzFIpVIGDBiAvX3rd68zGAykpqYQF3eU0tISXF3dCQ/vTbt27Vtk+5WVlZw5c5xz586g1+vx8+tMt27h2NraNdk2dDotWVmZpKVdJD091ZhZr10719pxex1wcFDc8nEwGAxUVlZeEcQVGZ+XlpbUS0JiZWWFvb0Ce3sH7O0VODjUPHbq5El+fvl1tiLcLcQ1g1DHZAI8pVI5ClgKWAAFwASVSnVeqVRaASuBYUAlcEilUk2u/Uxn4AvAGcgHnlGpVImN3KQvJh7grVq1nB07fkShcMLNzY3Vq9dz+PBB1q//GL1ej0LhyLx5C/Dy8iY2NoaPPvoApTKQhAQVkyZNITQ0jNWrV5KcnIhGoyEsLIKXXpqFVColNzeHDz98n/T0NACGDRvBuHHPsmfPT2zd+j9jGuRp02YSEdELvV7PihXvERt7FAsLGXK5NWvXbmTevBkcOXKYjh39sLKyYt26jfX2ZfPmL7l06RJz5rwCwJ9//sZ//7ueL7/cctPfiykcm5YmTtaNl55+kYMH/0Sj0RAe3gulMsgku+KdOxfPiBGDiYjozbff/tDoMjZ1XTAYDOTkZBEff4q0tFQAfHw6EhTUlXbtXJtsOy0hMzOdAwd+p6qqivDw3gQGhlzzgrusrJTo6L3k5eUQENCFnj0jTboFs7CwgIMH/yQ/PxcfH1969epPhw6uJnVe0Ol0JCae4+TJWCorK+jQoSNhYT2xt1c0y/aqqqo4e/Yk8fGn0Wqr6dTJn27dejT7+FKDwUBBQb5x3F5BQR4Adnb2xmCvfXu3Bm8k6XRaSkpqWuNqgrjLrXEajca4nJmZFHt7+3oBXF1Ad61utuJ3Qqgj6oJQxySmSVAqlY7UBGqRKpUqQalUPg2sBe4D3qMmsOusUqkMSqXyyiuPdcAnKpVqU+1n1gNDbqcsf1eWf4LyguNNuUojG6dQbJ27X/P96dPnkJCgYuzYcfTrN4DCwgLeemsRq1f/h44dO7Fz548sWbKQDRu+AOD8+RTmzVtASEg3AJYtW0poaDjz57+OXq9nyZKFREVtZ/Toh3nzzdfp27cfb7/9PgBFRTWJJnr37sPw4SOQSCRcvHiBGTOm8sMPu0hKSiAuLoZNm7ZiZmZGSUnNgPTZs1/h+efH8fnnmxvcB6UykO3bf6SoqAhbW1t+++0XsrKymuw7FAStVktMzGESEs7i6OjE8OGjcHR0au1iNUitVjN58gRsbGxZs2ZDqwagEokEV1d3XF3dKSsr5dy5MyQmniM1NQV3dy/CwiJwcWmZlphbpdNpiY09Qnz8aRQKR4YNG3nDOZVsbe24777RxMUd5cyZE+TmZjNw4DCTm+dNp9Nx+vRxTp2KQyaTMXDgMDp06GiS3ZSkUildugTj5xfAmTMnOXv2JBcvXiAgoAvduvW44Ri4xtJoNLWp1U9RXa2hQ4dOdO/eo8WOnUQiMSYp6d69B+XlZaSnXyQtLZVz585w9uwpZDJLPD29cXZ2oaystDaQK6asrP6Fllxug729go4d/Y0BnL29AzY2tibT00AQBOF2b3/6A9kqlSqh9u9dwFdKpdILeAbwUqlUBgCVSpUNoFQq2wPhwPDaz/wP+FipVLZTqVS5t1kek3TmzOnauUJquhWNHDma5cvfNXYZ8fLyNgZ3APv3RxMff4ZvvvkaqOnO0r69K2q1mtOnT7Jy5SfGZRWKmjutGRnpLF78Grm5uZibm1NQkE9+fh4eHl5otVqWLVtKeHgEkZEDGlXmHj168sgjjzF79jRkMkt69OiJVPpXk3wfgpCfn8u+fb9RUlLcJhJovP76fM6di2fLlh9wdTWdVjJbWzsiIvrQvXsPEhIZkajAAAAgAElEQVTOcvr0cXbt+hFv7w6Ehka0+kS0DSksLGDfvt8oKipAqQymR4/ejW6JMzMzo0eP3ri7e7J//+9ERX1Pr1798PdXmkQAlZeXy8GDf1JUVEDHjv707BnZJuZhsrCQERoagVIZxMmTsSQkxJOSkkhQUDeCgrrdclr96upqzp07w5kzJ9BoqvD29iU0tEer10sbG1uUyiCUyiCqqzVkZmaQnp5Kenoq588nYW5ugb29Ay4u7fHz61wvkBOp2AVBaAtuN8BLANyUSmVPlUp1FHiq9nU/arpevqFUKu8ByoCFKpVqP+ANZKhUKh2ASqXSKZXKzNrXGx3g1TZJGuXkmGFufvnumcI1DIXrrc1NdTvqyiCRSJBKJZibmyGVSpBILr9XO40NUqkZUqkZcrm8XtnBwHvvrcDT06veutVqtXEb9ZeHJUsWMn36LAYNuge9Xs/gwZHodFoUCnv+97/viI2N4ejRv1i3bjVffLEZqdQMkFy1nis9+eRTPPlkzSH99dc9dOzY6brLX4uZmRnt2jXd2Iq24m7c5xvR6/UcPXqUgwcPIpfLeeyxx/DxMe0U+Fu2bOGrrz5n/vz5PP74Q7e0jpaoCx4e/YmM7EVsbCwxMTHs2PF/KJVKIiMjcXJq/ZZRg8HA8ePH+fPPP7G0tOThhx+mU6dbG0vXrl0g/v4+7Nq1i0OHoikszGHYsGGtNsdbdXU1hw4dIiYmBhsbGx566CH8/PwaXNa0zwt2+PjcT2FhH/bv38/Jk7EkJsbTp08funfv3uibMNXV1Zw4cYIjR45QUVFBx44d6devn0ndHLmSh4czERHd0Ov1VFZWYm1t3WI3DEy7PggtSdQFoU5T1IXbCvBUKlWxUqkcA6ysHXO3GygCDEAnIE6lUs1TKpW9gR1KpdL/tktc6+9j8PR6fatPUXBlkhWDwYBOZ0Cr1dOlSwhJSQkkJ6fQoYMvUVHbCQhQYmlpjU6nx2CgXtn79RvI559/xty585FKpRQVFaFWl+Ph4UlISDc2b97Ek08+A9R00VQoFJSWltK+vTtarZ4dO35Eo9Gg0+nJzc1HKpUSEdGHsLCe7N+/j4sX0+jQwZfKygoqKzXXvHuen5+Hs7MLJSUlfPnlZ0yYMOmWvmO9Xn/X9S1v7v70Go2G5cuXcfLkCcaMeZJRo0ab/J3lsrJS9u//nZycLDp06ESfPgOwtLQ06bpx/nwKzz8/iYiIXrz00rxbKmtLj63w8wvGy8ufs2dPEB9/moSEBDp1CqBbt/BWy0BZUaHm4ME/ychIw9PTm8jIQVhby2/7exk48F7OnDnB8eMxZGRkMmDAUFxc2jVRqRsnOzuLQ4f+pKSkGH//LkRE9EYma7het51xNub06TMYf/8gYmOP8Pvvv3P0aAxhYT3x9fW7ZvCj0+lISIjn9Ok4KioqcHf3ZPDgCOPY0Lax71BeXtYi22k79UFobqIuCHVucQzeVW57hLpKpfoV+BWgdpzdPCAV0FLT/RKVSvWXUqnMAzoDFwFPpVIprW29kwIeQNrtlsVUOTo6snDhmyxZ8ho6nQ6FwpFFi5Zec/kZM+awZs0qJkwYi0QiwcJCxvTpc/Dw8GTRoqWsWPEu48Y9jpmZlOHDR/D00xOYPn02CxbMxc7Ojt69I3FwqBm0npOTzbvvvoVOp0On09GnTyTBwV0xMzPj3nvvZ/z4J7Czs78qyQrArFnT0OsNaLVa/vnPxxk4cHBzfUXCTUhMTGDKlOc5efI47du7snfvL7i7e/Dcc5N4+ukJODubVrc8g8FASkoiR44cAKB//3vo2NHfJLrUXY9Go+Ff/3oWqVTK+vUbTT6AvpKlpSVhYb3o0qVrbbbCs5w/n4S/fxe6dQtDLrdpsbLUJNH5g+rqanr16odSGdRkx97MzIyuXcNo396dffv28tNP226YrKWpVFdXExd3hHPnzmBra8ewYSPx8PC68QfbEBeX9gwfPorMzHRiY4+wb99vnDlzkvDwXvX2VafTkZys4uTJONTqclxd3Rk4cBiuru6tWHpBEIS7V1Nk0XRTqVRZSqXSDNgAlKpUqplKpXIP8IFKpdpTmzXzIOCvUqmKlErlH8CnVyRZmahSqe5p5CZ9MfEsmkJ9pnBsWlpz3I0zGAx8+eVnLFr0KtbW1qxY8TEjRtzPr7/u4T//Wcu+fX9gZWXFP//5OJMmTSEoKLhJt38rqqoqOXx4P6mpKbRv70b//vdcMxW6Vqvl9OmTBAQosbFpuQDkWl5//VXWr/+Ezz/fzMiRD9zyekzhzmz9iaQlKJVBhISEYm3dfHOCXTmHnaOjEwMGDEGhaL6uolVVlRw8+Cdpaal4efkQGTm42ca/ZWamc/jwPsrKSunSJZiwsF6NugFgCnXhVhkMBs6fTyIu7ijl5WW4u3sSFtaToqJCTp6MpayslHbtXAkNjcDNzcPkb+CYgrZcH4SmJeqCUMeUpkn4FOgHyIA9wCyVSlWpVCo7ARupmQqhGnhNpVLtrv1MF2qybzoChdRMk6Bq5CZ9EQFem2IKx6alNfXJOj8/n1mzXuSnn6IYOPAe5s17hby8bMrLy/D19SMgQEl2dg4bNqzju+++oaKigv79B/L88y8wYsT9rZLA5NKlDA4c+IOKCjWhoT0JDu52VZY5rVbLgQP72L79B6KitlNQUIBCoeDZZ5/nuef+1Wpjdvbs2c3TT49h4sTJ/PvfH9zWukzph7u0tISTJ2NJSUlEKpUSGBhCUFD3Jh+7VlCQz759v1FcXEhgYFfCw3silTb/lAYGg4Fz585w7NhhrKysGTBgSJO2Imk0VcTEHCYpSYW9vQN9+w7C1dWt0Z83pbpwq3Q6LSrVWU6ejEOjqQLA2dmF0NAIPDxaZ8L0tupOqA9C0xB1QahjMgFeK/BFBHhtiikcm5bWlCfrP/74jRdf/BdFRYU899wkgoMDqaqqxN7eAYXCkfT0i+j1epyd2+Hvr0ShcGbLls189tkGMjLS8fHxZeLEyTz55NM4ODTP/FZX0um0xMUd5ezZUzg4KOjffwjOzi7G97VaLQcP7mfbth/YtWs7+fn52NjYMmLEfQwePJSfftrF7t07sbCw4LHHnuCFF16k5p5Qy8jMzOCeeyLx9PRm165fb7sVyBR/uIuLizhx4hgXLiRjYSEjOLgbgYEhWFjcWrbEOgaDgfj4U8TGHsHS0pJ+/e5plW6L+fl5REfvpayshG7dwunaNey2U9inpaVy+PA+KisrCArqRvfuPW56Hj5TrAu3SqPRkJSkws7ODi+vDiKwuwV3Un0Qbo+oC0IdEeCJAK/NMIVj09Ka4mRdVVXF228vYd26j/Hy8uaJJ8bg5uaGu7sXQUFd8fDwQiKRUFlZSUpKIklJ5ygqKkQqldKhQyd8ff2IjT3Ghg3r+OuvQ8jlNowZM5ZJk6bg7x/QRHtaX/0U+EH06NEHc3NzdDodBw/uZ/v2H4mK2kZeXh5yuQ0jRtzH6NGPMGTIsHrdBVNSkli37hO++eZrKisrGT58BFOnTicysn+zXkhqtVoeeeQBTp48wd690fj53f73ZMo/3IWF+Rw/HkNaWiqWlpaEhISiVAbf0gTianU5Bw78waVLGXh7d6Bv30GtOkVAdbWGv/7aT0pKEq6u7gwYMOSWxh5WVlZy9OhBzp9PQqFwIjJy0C0ncjHluiC0PFEfhDqiLgh1RIAnArw2wxSOTUu73ZP1uXPxTJw4jsTEBCIjI/nHP/5Bly7BBAaGXHMck8FgID8/l6QkFefPJ1FdXY2dnT3+/koqKir56qsv+OGH79BoNAwZMozJk6cwePDQJpmc98qWG5nMksjIQbi7e3L48EG2bfuenTu3k5eXi1wu5957Lwd1N5pIOT8/n88//5T//nc9eXl5dOsWytSpL/Hggw81S9KTZcveYsWK91izZgOPPjqmSdbZFn648/JyOH48hszMdKyt5XTtGkZAQJdGd+29ePEChw79iVarpWfPSAICuphEi05dgp+//tqPVGpO//6D8fRs3LQcBoOB1NQUjhw5gEajoWvXMEJCQm+ru3NbqAtCyxH1Qagj6oJQRwR4IsBrM0zh2LS0Wz1ZazQaVqxYxurVHyGTyRg37hkee+wJAgICb6o1RKvVkpqaQlKSiuzsS0gkEjw9vXF0bMevv+7hiy82kpOTjb9/ABMn/osxY57E1rbhVLs3Ul5exoEDf5CVlYmnpxdSqSW7d0exc+d2cnNzkMvlDB9+H6NHP8TQoffeMKhrSEVFBd99t4W1a1eTlJSIl5c3kydP4emnx18zacvN2rfvTx59dDRPPPEUH320pknWCW3rhzs7+xJxcUfJycnCxsaWbt3C8fPrfM2bANXV1cTEHCIx8RxOTi4MGDCkRboB36zi4iKio3+lsLCAoKBuhIX1vG6gplar+euv/aSlXcDZuR2RkYNwdLz9BDFtqS4IzU/UB6GOqAtCHRHgiQCvzTCFY9PSbvZkXV5exuHD+3nrrSWcOXOGrl27smzZ8trkFLeXIKWkpJikJBXJyQlUVKixsrLG29uXxMQkvv76C+LiYrG3d+DJJ8fx3HOT8PXt2Oh1X7iQzMGDf5KcnExGRhb790eTk5ONtbU1w4aN4B//eJihQ+9tsqyYer2eX375mTVrVnHo0AHs7R145plnmTTpBdzdPW55vbm5udxzTyQKhYKff/6jSbN4trUfboPBwKVLGRw/fpS8vFzs7Ozp3j0CX99O9QK9/Pxc9u37jZKSYoKDuxMaGtEqyXwa68qsni4u7RgwYOhV8wIaDAaSkxOIiTmETqeje/cIgoK6NkkrN7S9uiA0L1EfhDqiLgh1RIAnArw2wxSOTUtr7H/Q3Nxs4uNP8dNPu/jmm2+oqqpi7txXmDFjbpNdVNbR6/VkZqaRmKgiPT0Vg8GAi0t7qqo0REVFERW1Hb1ez4gRI5k8eQr9+g24Zje7yspKvvzyU3bvjuLMmTMUFRVhZWVlDOqGDRvR7FMdxMbGsHbtx+zY8SNmZmY88shjTJnyEsHBITe1Hr1ez9ix/+TQoQP89NPvTT69RFv94TYYDKSnp3L8eAyFhQUoFI6Ehkbg5dWBs2dPcvx4DFZW1vTrNxh3d8/WLm6jpaamcPBgNGCgb99B+Pp2AqCsrIzDh6PJzEynfXs3IiMHYm/ftK2RbbUuCM1D1AehjqgLQh0R4Jl4gBcd/Qfr13+MTCZjyZJ38PHxbdWy/V1paSnbt3/PU0+Nb/B9jUbD/PlzUKnOAhAVtbfe+/v3R7NmzUfodDqUykAWLHjjml0ITeHYtLTr/QfV6/WkpqYQH3+aS5cy2L17N9HR0XTu3IUNGz4nMDCo2ctXUaEmObkmMUtJSTHm5hbY2tpz5MgRvvtuCwUFBQQFhTBp0gs88shjWFtbo9frOXLkL7Zs2cTOndspLi5GJpMxfPgI/vGPRxg2bMQtd/O8HampF9iwYS2bNn2JWl3OoEH3MHXqdAYPHtKocWCrV3/I0qWLeP/9Dxk//rkmL19b/+E2GAxcuJDCiRMxlJQUY2lpRVVVJT4+HenbdwCWlq2XSOVWlZWVEh29l7y8HAICuuDo6Exs7BHAQHh4L5TK4GYZQ9jW64LQtER9EOqIuiDUEQGeiQd4c+ZMZ9So0QwZMuym1qHT6Vqkm9OlS5k8//y4qwK3Olqtlri4YygUCmbOnFpvObVazRNPPMwnn2zA29uHZcuW4urqxrPPTmpwXaZwbFpaQ/9Bq6oqSUw8x7lzZ1CryykpKeWrr77i/PkUJk+ewsKFS1o866DBYCA3N5ukJBUXLiSj1WqxtpZz4cJFdu7cTnz8WZycnLjnnmEcPLifS5cyMTc3Jzg4hKeeeoZHHx3TZGPgbldRUSFffvkZGzasIzs7i8DAYKZOfYmHH34Umazh9P8xMUcYPfo+Ro58kA0bPhcX9deh1+s5fz6JhIR4/P2V+PsrTSKRyq3S6/XExR3lzJkTALi7e9K378Bmrc93Sl0QmoaoD0IdUReEOiLAu0GAF5tXwrG8kmYpQA8Xe8Jd7K96vS7AW7VqOTt2/IhC4YSbmxurV6/n8OGDrF//MXq9HoXCkXnzFuDl5U1sbAwfffQBSmUgCQkqJk2aQmhoGKtXryQ5ORGNRkNYWAQvvTQLqVRKbm4OH374PunpaQAMGzaCceOeZc+en9i69X9otdUATJs2k4iIXuj1elaseI/Y2KNYWMiQy61Zu3Yj8+bN4MiRw3Ts6IeVlRXr1m1scF8bCgR/++1XfvppJ++99yEA586d5a23FrNp07cNruNuD/CKi4uIjz9FcnICOp0OV1d3Tpw4yerVH2Jv78Dq1WsZMmR4K5e4Jq38hQs1iVlyc7MBKC0tIzo6mqNHjxIQ4E9gYCAPPPAPBg0aettzpjWXqqoqfvjhO9asWcW5c/G4ubkzadIUnnlmQr0EIEVFhQwdOgCJxIzfftuHvb1Ds5RH/HCbtqysTCoqKvD17dTsAauoC8KVRH0Q6oi6INRpqgDv5ic7Em5o+vQ5JCSoGDt2HP36DaCwsIC33lrE6tX/oWPHTuzc+SNLlixkw4YvADh/PoV58xYQEtINgGXLlhIaGs78+a+j1+tZsmQhUVHbGT36Yd5883X69u3H22+/D0BRUREAvXv3YfjwEUgkEi5evMCMGVP54YddJCUlEBcXw6ZNWzEzM6OkpCbonT37FZ5/fhyff775pvcvOzsLV1d349+urm7k5GTf1nd2pzEYDGRmphMff4qMjDTMzKR06uSPi4srixYt4LfffuXee+/jww/X4OLicuMVtgALCxkBAV0ICOhCUVEhSUkqUlISGDVqJKNGjcTS0pK+fQfi49P4JCytwdLSkieeeIoxY57k999/5ZNPVrN06SJWrHiPp58ez+TJU/Dy8mbWrJe4dCmTnTv3NFtwJ5g+N7dbT84jCIIgCKbojg3wwq/RytYazpw5jZ9fZzp2rBnMP3LkaJYvfxe1uhwALy9vY3AHNePb4uPP8M03XwM1CS3at3dFrVZz+vRJVq78xLisQlHTIpGRkc7ixa+Rm5uLubk5BQX55Ofn4eHhhVarZdmypYSHRxAZOaCldvuuo9frKSzMJzv7EufPJ5Kfn4+VlTWhoREEBAQSHf0HEyfeT3l5Oe++u4IJEyaabBc3hcKRiIg+hIX1JCPjIvn5eSiVwbc0xUFrkUgkDBkynCFDhnPq1AnWrFnNp5+u49NP1xER0Yu//jrE4sVvEx4e0dpFFQRBEARBaDJ3bIDXllhb//2i2cA773yAp6dXvVfVavU117F48Wu8+OIsBg4cjF6vZ9iw/mg0GpydXfjqq2+JiztGTMwR1q5dzcaNm26rvK6ubsTFxRj/zs7Oon1719taZ1uk1WrJy8shJyeL7OxL5ObmGLvItm/fnn79BuPr60dVVRVvvLGAzz//L8HBXVm/fiOdOytbufSNI5VK8fHpaPKtdjfStWt31q79lIULF7Nhwzq+/PIz7rtvJC+8MK21iyYIgiAIgtCkRIDXAoKDu7Js2Zukpl6gQwdfdu/eSUCAErm84TTy/foNZNOmL5g7dz5SqZSioiLU6nI8PDwJCenGt99u5sknnwFqumgqFArKysqM84BFRW1Ho9EAUFhYiFQqpXfvvkRE9OLgwX1kZmbQoYMvlZWVaLVazM1vrhr06dOXlSvfIy3tIt7ePvz44//ddDKZtqiqqpKcnGxyci6RnZ1FQUEeen1NUh2Fwgk/vwDat3ejfXs3fH3dyc0t5dSpk0yZMpGEBBVTprzEggWLsLS0bOU9uXt5enqxePFbLFiwCKlU2uRTUQiCIAiCILQ2EeC1AEdHRxYufJMlS15Dp9OhUDiyaNHSay4/Y8Yc1qxZxYQJY5FIJFhYyJg+fQ4eHp4sWrSUFSveZdy4xzEzkzJ8+AiefnoC06fPZsGCudjZ2dG7dyQODjVjinJysnn33bfQ6XTodDr69IkkOLhm4t57772f8eOfwM7OvsEkK88//wy5udmUlpby8MMj6d27L/Pnv45cbsPLLy/g5ZdnotfrCQhQMmPG3Gb7/lpLWVkZOTlZ5ORcIicni6KiQgDMzMxwdm5HYGBXXF3dadfO9aqgTa/Xs2bNat5+ezFOTs5s3bqNQYPuaY3dEBpwrayagiAIgiAIbd0dm0WzNYiJzhtmCsfmRgwGA8XFRcbWuZycLMrLywCwsLCgXTtX2rd3w9XVHWfndtdt9bx0KZM5c17k119/5f77H2DlytU4OTm31K4IJkZkRxPqiLogXEnUB6GOqAtCHZFFUxBug16vJz8/zxjQ5eZmUVVVBYCVlTWurm4EBXWjfXs3HB2dbtiVT6PRsHfvL2zZsplffvkJCwsLli9fxdNPjzfZRCqCIAiCIAjCnUcEeMJdIycni8zMdHJyssjNzUan0wFgZ+eAt7evcfycnZ19o4Iyg8HAqVMn2LJlM99/v5X8/HzatWvPxIn/Yu7cmdjbt2/uXRIEQRAEQRCEekSAJ9zxqqqqOHr0ACkpSUgkEhwdnencOdAY0F2dxfT6srOz+O67b/n2283Ex59FJpNx332jGDNmLPfcMwxzc3PR3UIQBEEQBEFoFSLAE+5oGRlpHDoUTUWFmm7dwgkK6nZLCTYqKyv56acotmzZzO+/70Wv19OjR0/ee28lDz30CAqFYzOUXhAEQRAEQRBujgjwhDtSdXU1x44dJiEhHgcHR+65516cndvd1DoMBgNHjx5hy5bNbNv2PSUlxXh4eDJ9+mwef3ws/v4BzVR6QRAEQRAEQbg1IsAT7jjZ2Zc4cOAPyspKCQrqRlhYBFJp46t6WtpFtm79hm+//R8pKcnI5XJGjRrN44+PpX//gUil0mYsvSAIgiAIgiDcOjHLbzP573/XU11d3ezb2bVrBxcvpjb7dgAeffRBUlKSWmRbt0Kr1XL06CF+/nkHACNGjCYiok+jgruysjK++eZrHnnkAXr0CGHZsrdwd/dg1aq1nD6dyCef/IdBg+4RwZ0gCIIgCIJg0kQLXjP57LMNjB07DgsLi6ve02q1151H7Wbs2rUDBwcFPj4NzzOn0+nuiqAkLy+HAwf+oLi4CKUyiPDw3g1+91fS6/UcOLCPLVs2s3PndtTqcnx9O/Lyywt4/PGx1/xOBUEQBEEQBMFUiQCvGSxf/i4AU6Y8h0RixurV61m1ajlSqZSLF1NRq9X8+98f8Pzz44iK2gvUTI595d+HDu3nyy83UlWlwcLCgpdemk1ISNd624mK2o5KFc+HH37Ahg1rmTZtBrm5Ofz8827kcjnp6RdZtGgpjo7OfPjhe2Rn18z1NmzYCJ555jmgplXuvvtGcfToX+Tn5zF27NP8859jADhxIo7ly5cBEBoajsFgwNTodDpOnozl9OnjWFvLGTZsJB4eXtf9TEpKElu2bGbr1i2kp6dhZ2fPI488yuOPP0nv3n3EvHWCIAiCIAhCm3XHBnhbtmzmf//b1CzrHjv2acaMefKa78+Z8wo//LCVtWs3IpdfTsGfmJjAxx//B2tray5dyrzm5zMy0vn88/+yYsVqbGxsSUlJZu7c6Xz/fVS95UaNGs3u3TsZO3Yc/foNAGpa9M6ePcXnn/8PT8+aQGfmzKlMmPA8oaHhVFdXM2PGFAIDg+jZsw9QkyFy/frPuHQpk2eeGcP99z+Iubk5b7yxgEWLlhIeHsHevb/w/fdbb/k7aw6FhQXs3/87hYX5+Pl1pmfPvshkltdcfuvWb/jss0+JiTmCmZkZgwbdw8KFi7n//gewtrZuwZILgiAIgiAIQvO4YwM8UzR48NBGBRJ//XWIjIx0pk2bbHxNp9NRUJCPk5PzDT/ftWuoMbirqKggLu4YRUVFxvfV6nIuXLhgDPCGDbsXAHd3D+zs7MnNzaG6uhorKyvCwyMAGDp0OO+//3bjd7YZ6fV6zpw5yYkTMchklgwefC8+Pr7X/cy2bd8zbdpkOndW8vrrb/LYY2Nwc3NvmQILgiAIgiAIQgu5YwO8MWOevG4rW2uQyy8Hd1KpFL3+cpdHjUZjfG4wGOjduy+vv/7mbW/HYNAjkUj49NMvrznu78p54czMzNDptNdYc+t3XSwpKWL//j/Iy8uhQ4eO9O49ACsrq+t+Jjs7i5dfnkVYWDg7d/5yw7F5giAIgiAIgtBWiSyazUQut6G8vOya7zs5OaPVaklPTwPgl19+Mr7Xq1cf/vrrECkpycbX4uPPNLgeG5vrb0cut6F79zA2bfrc+Fp2dhb5+XnXLb+PTweqqqo4cSIOgN9//5WystLrfqY5GQwG4uNPs2PH/1FSUsyAAUMYOHDYDYM7g8HArFkvUlFRwccf/0cEd4IgCIIgCMId7Y5twWttTzzxFNOnv4ClpRWrV6+/6n1zc3NmzJjDrFnTUCgU9O3b3/iet7cPixYtZdmypVRVVaHVVtO1a3cCA4OvWs/o0Y/w8ccr2bz5K6ZNm9FgWRYtWsqqVSt45pma5ClyuQ2vvroIZ2eXa5ZfJpOxePHbLF++DIlEQvfuYbi6ut3s19AkyspKOXjwT7KyMvH09KZv34HI5TaN+uymTV/w6697eOed9wgI6NzMJRUEQRAEQRCE1iUxxcyIN+ALnM/PL6vXxTErKxU3t9ZNa29uboZWq2/VMpiiWz02BoOBpCQVMTGHMBigZ8+++PsrG53l8sKF8wweHEmPHj3ZuvVHzMxarsG6XTs7cnNbr8VTMB2iLgh1RF0QriTqg1BH1AWhzs3UBTMzCc7OtgAdgQtXvida8ASTpFaXc+hQNBkZabi6utOv32Bsbe0a/XmdTsdLL72Aubk5q1atadHgThAEQRAEQRBay20HeEqlchSwFLAACoAJKpXq/BXvvwEsBrqqVKrTta/1AdYD1tREnE+rVKqc2y2L0PYZDIb/Z++9g+TI7jvPT7rK8q5ttW80gIbHwIwfjgVnyCUl7pKiSOrYHYcAACAASURBVOmk3VtFSEEtV3daaeVO2ouTIcVY7Z0UjJEoL62kU5xIiW5JLTUzAMeBg8EAA8wMXMO1RZvqLu8rzbs/srrQDTPwgwaQn0DivTSV9ar6V5nvm7/f+z3Gxs7w5pt7sSyT++9/hHXrNl7z3HRf+crzvPnmGzz//J80M4q6uLi4uLi4uLi43O3ckFtjeHg4Bvx34LMjIyObgT8DvrJk/3bgIWB8yTYZ+Dvg8yMjI2uBV4Ev3Ug7XO4OqtUqr766m9de20M4HOHjH/8U69dvumZxd+zYUb70pd/mYx/7YT796c/eota6uLi4uLi4uLi4rDxu1IO3GpgbGRk52Vj/Z+Bvh4eHW4EC8IfAjwEvL3nNDqA6MjLyemP9j3G8eD91g21BCHHNYsDl1iKEzdVMrzA5OcYbb7xGvV5j27b72bhx63WFVdbrdT7/+Z8hHI7we7/3B649uLjcodQqJUyjhrBthBDOtUQI7EYpRGO7fb6+bPultl3mXKF4By23eQy3i4uLi4vLzeJGBd5JoHN4ePj+kZGRt4D/pbG9D/gM8HcjIyNjw8PDS1/TxxKP3sjIyMLw8LA8PDwcHxkZSV/tGzcGFTYpFPxUKgVCocht7dSrqjvWCxyxbVkm+XyGcDhIW9vF4+eEEMzNzXH48GGOHj1KW1sbH/3op2lra7vu9/31X/91jh59j29961usXz94Ix/hhrnUZ3a5N3Ft4dJYpkEulSSzMEt2fpbswmyzXi1ffvqXW8Hwtkd49KM/ij8UuaXv49qCy1Jce3BZxLUFl0Vuhi3ckMAbGRnJDQ8Pfwb4/eHhYS/wP4EsEAJ2Ar96wy28DBdm0fT7Y2Qy8+TzmVv1lldElmVs282iuYgsK/h8QXy+SDMjULlcYnp6iunpKWZmzlGrVZEkic2bt7Fly3ZAue5MUm+99SZf+tKX+PEf/0kefvip25qRys2I5bLIvW4LQgiqpTz59ByF7DyF9ByFTJJCOkkpn2JpJmdvIEwo1k7X0BZCsXY8Xj+SJCFJslPKcnMdSVq+T5JgSf3iY5fsW3I+gLFj+znx1m7OHjvE5kc/ztCWR29JYqZ73RZcluPag8siri24LHKdWTQv4qZOkzA8PNyB4537beDzQL2xqweYA/49kAH+amRkZFPjNa3A2MjIyKVbeDEDXGKahJWA+wO9GMsymZubbYq6bNZx0nq9Prq6eujq6iGR6Mbn89/Q+5RKJZ5++lFM0+Tll39AKBS+Gc2/blxbcFnkVttCZv4co0f2kZw8hap58Oh+NK8Pj+7H4/WhNUqP7kfTfXi8fmfRfage702LeDCNGoXMfEO8zZHPJJ16JolZrzWPU1SNUKydUKyNUKzDqcfbHUGn+25KW66HfHqOt/d8jbmJk8Q6etnxzI/e9LBN97rgshTXHlwWcW3BZZEVM03C8PBw58jIyGwjecoXgT8eGRn5AvCFJceMAR8fGRk50jjONzw8/FhjHN7ngK/daDtcVgZCCHK5TFPQzc3NYFkWsizT3t7J9u0P0NXVQyzWclNDaX/rt/4LY2OjfOMb373t4s7F5VZTr5YZP3GA0SP7yCSnkBWF9p41jresUiCfmcOoVTBqFd7vIZ4kSY7o0/1oDdHXFIUNMdjcrvvQvH40TadUyFBIJylkHG9cPp2kUswuO7c/FCMUb2dgw4OEl4g4fyjqeNVWGOF4B0986vNMjrzNoVe+wUt///8wtPVRtjz6cTzeG3sA5eLi4uLi8kFyM+bB+53h4eFHAQ/wAlcIyxwZGbGHh4d/EviTRljnGPATN6EdLreJarXKzMw5ZmYcUVculwAIhyOsWbOerq4eOjoSaJp2S95/z56X+Ku/+nM+97n/yCOPPHZL3sPF5XYjhM3cxClGj+xj6vQ72JZJtK2b7U/9CH3rdqD7Apd8jVGvYVTL1GsV6tUyRqOs1yoYtbJTrzpisF4rUy5knH3VMrZtvW+bNI+XUKyd9t7VhGIdhBsiLhhtQ9U8t+qruGVIkkTfuh10Dm7gyA/+mdOHX2Xq5GG2PvGvGVh/v5u0ycXFxcXljuCmhmh+QAzghmjeVmzbZn4+yfT0JDMzUywszAOgaR4Sie5m6OW1TEx+vWSzGR5//CEikQgvvvgqXq/3lr/n1XCv2ILLlblRWyjl04wefZPRo29Szqfx6H761u9k1aYHibX33sSWLkcIgWUaDTF4Xhia9Rq+YIRQvAOvP3RXi55McoqDu79KamaMtu4htj/zaaKtXdd9Pve64LIU1x5cFnFtwWWRFROi6eLwxhuvIsuCSKSVjo5OotH4XdXxKRTyzbDL2dlzGIaBJEm0trazZct2urt7aWlpuyWJCd6PX/3V/8zCwjx/+7f/34oRdy4uN4plGkydfpfRI/uYm3BmoenoX8vWx36I7tVbUNRb4w1fiiRJqJoHVfPgD0Vv+futRGLtPTzz2Z/n7JF9vPvat3nh7/4rw9ufYsNDH0Hz6Le7eS4uLi4uLpfEFXg3CY9HZ3z8DCMjI411D21tnXR0dNLe3klLSxuKotzmVl491Wql6aWbnp6iUMgDEAgEGRgYoqurh87ObnT99nVyvvWtr/P1r3+NX/mVX2fr1m23rR0uLjeL9Nwko0f2MX7iAEatQiAcZ9PDH2Fg44MEwvHb3bx7EkmSGdr8CD2rt/DOa9/mxIHdjJ84yLYnP0nPmq131YM8FxcXF5flONP5zBJt7UK+g/rxbojmTaS1Ncjo6DTJ5Cxzc7MkkzPk8zkAFEWhtbWdjo4E7e2dtLV13LIxadeCZZlks1my2TSZTIpMJk02m6ZSqQCgqiodHQm6unrp6uohHL698wwuMjc3y+OPP8jg4Cq+850XUdWV9azCDbdwWeRKtlCrlJoJU7Lz55AVlZ41W1m16SHae9esyIQk9zIL02c58NJXyS1M0zmwnu1P/Qih2NXN3eleF1yW4tqDyyKuLawsCpkkM2PHmR09TnLqFJZp8OSPfJ6OvuErv/gGcUM0VyCSJBEKhQmFwgwNrQWgUimTTM42Rd977x1CCIEkScTjrbS3dzZF360MMRRCUCwWmgJuscznc80se4qiEInE6OrqJRaLE4+30tbWseI8j0II/tN/+o9UKhWef/5PV5y4c3G5ErZtMzcxwuiRfZw78y62ZRHr6GX705+mf90ON2vjCqa1axXP/sQvcerwqxzZ+898729+l/UPfJj19+/6QEJnXVxcXFxuLqZRIzl5mpnRY8yOHaeYWwAgGG1j1eZHSAxuoL137W1u5bXh9oxvMT6fn/7+VfT3rwKgXq8zPz/XFH0jI8c4fvw9ACKR6DLBd71JSmq1KplM+gIxl8E0jeYxwWCIWCxOf/8qotE4sVicUCj8gY+hux7+7u/+Oy+99AJf/OJ/ZfXqNbe7OS4uV00xu8Do0TcZO7afciGDx+tnaMtjDG56iFhb9+1unstVIssKw9ufom/tdg6/8g2OvvE/GT/2Ftuf+TSJgfW3u3kuLi4uLu+DEIJ8epbZsePMjB5n/txpbMtCUT109K1h7Y6nSAysIxi9uuiMlYgbonkTuR4Xu2VZLCzMk0zONEWfYThCzO8P0NGRaIzjSxCJRJeFR1qWRS6XJZNJNYRchkwmRaVSbh7j8ejEYvGmiHPqMbQ7MIU5wNjYKE8++Qg7dtzP1772zRUrSN1wC5dFYlGdQz94ndGjzmTkINE5sI5Vmx6ia9Um1+tzFzA7PsLbe75GIZOkZ819bHvy3+APxS46zr0uuCzFtQeXRVxbuPUYtQpzk6eaXrpyIQNAuKWTxMAGOgfW09a96rbfk90QzbsERVHo6HCSsYATupXNphtj+GaZmTnH6OhpAHRdp729E0VRyWTS5PPZZnilLMtEIjESiS6i0ZammPP5/CtizNzNwLIsfu7nPoeqqnz5y3+0YsWdy/UhhM381BmC0bY7PmujEILUzChjx95i8uTb1KsVApEWNj3yMQY3PnDJzr/LnUtn/zDP/eSvMHJwD8f2vcDs2DE2PvyvWLvtiVs2KN+2bSrFLMXsAqVcimJugWIuRTG7QLWYI9zSQUtikJbEAC2JgUvOk+ji4uJytyKEILcw3RR089NnEbaN6tHp6Btmw4PP0jmw/q5NYOYKvBWGLMvE463E462sX78JIQSFQp65ufMePtu2icXi9PX1Nz1z4XD0rhc8X/nK87z55hs8//yf0N3dc7ub43ITyS5Mc3D3V1k4dxaQaO9dTf+6nfSs2XpHjUcr5VKMHX+LsWNvUczOo6gaqzftJLF6B+29q92EKXcxiqqx4cHn6Fu3k7f3/CPvvPpNxo6+yY5dP0pb99B1ndM0ahRzKUrZBUfAZR0hV8qlKOVT2Nb5ieglWSYQihOMthKOd5BLzXB8/4sIYQMQirXT0jVIa2KAlq5BIi2drj26uLjcVdSrZeYmRpgZPc7s2HEqJSfRYbStm3U7nqZzYD2tXavuqGyY14sbonmTePbZJ6jXazz55C4+/OHneOCBh1ZElsy7hWPHjvLss0/w7LMf5S/+4m9WvFfSDbe4OkyjztF932Pk4B40j49Nj/wrapUi48cPUMzOIysKicGN9K/bQWJwI+oKDC026lUmTx5m/Nh+klOOt729ZzX9Gx6gd+19dHW3ubZwjyGEYPrMe7z9/X+iXMgwsPFBtn7oh+nt71pmC0IIquVCwwu3QDHb8MI1RFy1lF92Xk33EYy0EIi0Eoy2Eoy0EIy2Eoi04g9FkeXlnRbTqJGenWBhZpTU9BgL06PUqyXnXB4v8UQ/rUu8fHfSw5S7Afc+4bKIawvXhxA2meRUcyxdamYMIWw03Udn/zo6B9aTGFiPLxi53U29am5WiKYr8G4S3/zmP/HVr/6/vPLKKxiGQSgU5oknnuLDH36Op5/+MB0dHbe7iXcs9Xqd5557imRyjlde2Udra+vtbtIVcS/WV2b67FHe3vM1Svk0gxsfZOvjn0D3BQGn45uZm2T8xAEmRt6mWsqjebx0r9lK/7odtPeuva0ea9u2SU6eZOzYfqZOvYtl1glG2xjYcD8D6+8nEGlpHuvawr2LadQ4tu9fOHFwD5rmZeuju8hl846Ay6Yo5lJYZn3JKyT8oehFIi4QbSUYacXjvbGQeyEExew8CzNjpKZHSc2MkVuYbob6h+MdDS/fIC1dA4TjHa6X7xbiXhtcFnFt4dIIYVMrFykXspSLWcqFDJWCU5YLWQqZOWoV56FVrKOPxMB6EoPriXf2X/TA607BFXgrTOCB80cZHZ3m1VdfYffuF3jppReYmZkGYOvWbTzzzIfZtetZtm3bseKmHljJfPGLv8Uf/MF/42//9h947rmP3u7mXBXuxfrylAsZDn3/60ydfodwvIMduz5De8/qyx7viKlTjJ84wNSpw5j1Gt5AmN612+hfv5N4R98H5tHNp2YZPbaf8eNvUSnm0HQfvWu3MbjxAVoSg5dsh2sLLrnUDG/v/hrJqdMoqtYQby0EI45wCyx64sLxD3yAv1Gvkp4dZ2F6jNSMI/rqVSdRl6b7aOnsb4Z2xhMDeHTfB9q+uxn32uCyyL1oC0II6tVyQ6w5gq3SKJtirphdFooOICsq/mAUfyhKINJCe+9aOgfW4fVfX+b5lYYr8FaYwJt943eQAb9/GN/A4yiRDoQQHD16hN27X+DFF/+FAwf2Y9s2LS0tPPXULnbtepannnqGWOzuHOB5M3jrrTf5oR96jh/7sZ/g93//+dvdnKvmXrxYXwnbtjh9+DXe2/tdhG2z4eHnGN7xNIpy9UOBTaPOzOhRxk8cZGb0KLZlEYy20b9uB/3rdxKKtd/0dtcqJSZOHGTs2H7ScxNIkkznwHoGNtxP99DmK3bIXVtwAaczEw7K5Iv2ig4xF0JQyCRJzTghnanpUXKpWUAAEuGWzuY4vtauQUKx9hX9eVYy7rVhZWMa9Q9sWMCttoViLsXM2aNUywVkRUGWFWRFbdQbpaI2ti+tn9+nXG6frCLJ8rLrgBACo1ZxxFohQ7mYXeZ5WxRv1pLpu8CZgsYXjOAPxfA1RJw/FMMfiuJrlLoveFdfc1yBt8IE3puHvoMwJ0ko86jlGt6iQqBlM9rATuTWASRJIpNJ8/LLe3jxxX/h+99/iVQqhSzL7Nz5ALt2PcuuXc+xceOmu9pwr4VSqcTTTz+KZVl8//t7CYXCt7tJV417415OanacAy/9A9nkFJ0D69nx9KcJRm8s1LZeLTN16h3GTxwgOXkaEMQ6+uhft4O+4e03FHNvWSYzo8cYO7afmbNHsW2LSGsXgxsfoG/dTnyBq7dF1xZcFrlTbaFeq5CeHSc1PeqEd86MYdQqAAQiLfSv20n/uh2EWzpvazvvNO5Ue7ibsW2Lc6ff49ShV5g/d4ZwvMMZxzW4gbbuoVvmYb/ZtmDbNqmZMWbOHuHc2aPkUzONPRLOw5qbjdQQf47gsy0T06gtP0KS8AYiS0RbQ7gFz4s4byB0z4eFuwJvhQm8549OMF2u0aHW2WK/y4B0BtU00Bfy6AUZvXsr6sB2lMQ6JEXFsiwOH36bF1/8F3bvfpF33jkEQCLRxa5dz/LMM8/y+ONPXPdk53cDv/Irv8Bf//Vf8I1vfJdHHnnsdjfnmnBv3A71WoX3Xv8Op995HW8gxPanPkXPmvtu+kOMciHLxMjbTJw4QCY5hSRJtPeuoW8xE+dVhJUtjvsbO7afiZGD1ColdH+I/nU7GNj44HVPRO7agssid4stCGGTT8+xcO4sk6cOk5w4iRCCaFs3/et20rduuzsVyFVwt9jD3UCtUuLskTc4ffg1yoUMgXCc3rXbyM6fIzl1Gtsym5NgO4k7NtzwQ8ql3AxbMGoVZsdPMH32KDOjR6lVSkiSTFvPEF2rNtG1aiOhWDu2bWNbJrZtOaVlXVBvlM1jrEscv3iMU7fM5fslWW6KtvPiLXzHjov7IHEF3goTeIZtc7pm8L3TM8xXDUIqbNUmWVN/Ex0DLVdGn82i1iS03q2oA9tQe7cgeZyO59zcHHv2vMhLL73Ayy/voVDIo2kaDz/8GLt2fZhdu55jaGj1PePd27PnJT772U/ysz/7c/zmb37hdjfnmrnXb9xCCCZPHuLQy1+nWiqw5r4PsfnRj6F9AON38qlZxk8cZPzEAUq5FLKi0rVqI/3rdpIY3HDRE9hyIcv4iQOMHdtPPjWLrCh0D21mYMODdPavu+F0yve6Lbic5261hUopz+TIIcZPHCA9Ow5ItPUM0b9uBz1r7nPn4LsMd6s93EnkFmY4eegVxo+/hWUatPesZs32J+latamZyMs0aiQnTzMzdpzZ0WMUcwuAM/XIYpbGtp7VNxTOeb22UMylmD5zhOnRI8xPnsa2LTy6n87B9XSv2kTnwHo3O+4dhivwVpDAE0Lw/a9+mVAkwtr7P8KsEmLvXIbT+QqaDJt9edYb+wjZKRRLQ59J45lbQEJG6VqPOrAdtX8bcsB54mkYBvv37+Oll15g9+4XOHHiOAADA4Ps2vUsP/Ijn2H79p238yPfUjKZNE888TCRSIQXX3wVr9d7u5t0zdzLN+5idp6Du7/G7PgJYu097Nz1WeKdfR94O4QQpGfHGT9+gImTh6iVC2i6j57VW+lbt4NaucDYsf3MTYwghKAlMcDAxgfpW7vtpt4Q72VbcFnOvWALhcw8EyMHGT9+gEImiSwrdA6up3/dTrpWbVqRU53cLu4Fe1iJ2LbNzOhRTh16hbmJkyiKRt/6Hazd9gTRq4jUKGSSzXnWkpOnsCwDRdFo611NYmADicH11zwe/GptwbZt0rNjTJ9ZHnoZirU7XrqhTbR2DbqesjsYV+CtIIEHcOrwa7y3939g1usMbnqITQ9/lKzsZe9shnfSBWwBa/wmm8U7tNZPIssefEYAbfwccnoWALltlePZG9iOHO1qeusmJsbZvftFdu9+gddee4VKpcInPvFJfuM3/i/6+wdu46e+NXzucz/Ft7/9Tb73vT1s2XLf7W7OdXEv3rgt02Dk4B6O7XsBSZHZ/MjHWX3fh27rdAaL2LbF3MRJJk4cZOrUO82xAf5QjIENDzCw4f5bkqAF7k1bcLk095ItCCHIJKeYOHGQiRMHqZRyqJpO9+ot9K/bQUf/8D3fCb2X7GElUK9VGD2yj1OHX6WUS+ELRllz34dYtfnh5hQ914pp1Jmfanj3xo5TyCQBCEZam2P32ntXo2r6+57n/Wzh/UMvN9K1atMtu3+5fPC4Am+FCTyAoE/w6nf/idPvvo4sq6zb+TTDO5+mgsq+ZJY3kzkqlk2XV+I+bZTu8psoksDr78NX1pDGTiPmzwIghTsaYm8HSvsQUqOTXCwW+aM/+jJ/9EdfxjRNfvqnf5af//lfJBKJ3s6PftP45jf/iZ/5mX/Pr/7qb/ALv/DLt7s51829duNOTp7iwO6vUkjP0bPmPrY9+Un8oZVpk6ZRZ3bsOB6vn7aeoVs+oPteswWXy3Ov2oJt28xPnWbixEEmTx3GqFXQfcHmVCctiYF7ZvjBUu5Ve/igyafnOHXoVcaOvYlp1GntWsXa7U/QPbTlhkPwL6SYXWiIvWPMTZzCMuvIikpbz1DDu7fhkplnL7SFUi7FubNHmD7rhl7ea7gCbwUKvMU/SiEzz3t7v8PkyUPo/hAbH/oIQ5sfwUTiUCrP3rksC1WDiCazzZdiqLoXzS6gedsJhDfiyVaxx9/Bmj4OtoXkDaH2b0Md2IbSvRFJ9TAzM83v/u5v8w//8PfEYjF+6Zd+jX/7b38KTftg51C6HspGhdlyktnSHDOlOQr1Eg90biNWD/Hkkw8zOLiK73znRVT16tPnrzTulRt3tVzgnVe/xdix/QTCcbY//Wm6Vm283c1aUdwrtuByZVxbcDz9s2PHGT9xkOkzR7Asg0A4Tl8jE2ekNfGBtUUIgVGvUi3lqRRzVEo5hBB09K75QJLEuPZw6xDCZnbsBCcPvcLs2HFkRaFveAdrtj1OvOODGTJgmQbz584yM3aM2dFj5NNzAATC8SXevbVoHp2WlgAj773H9NmjTJ85Qs4NvbxncQXeChZ4i6RmxnnntW8xP3WaYLSNLY99nJ419yGAkVyJ12ezjBYqeGSJrcE6660D+GtjSIqXYMt9BCObYG4Sc+xtzIl3waiA6kGOJkBWkCSFI5PzfOGre3jjxBirEq38+o99hGe2r0dSNJBlkBTH+ycrIDmltKR+/pjzdRrHS94gamIdkn59A+QL9WJDxCWbgm62NEeufv470mQVj+yhaJQ4+H9/n+kj4+ze/Tpr1wzf6J/jtnK337iFsBk98ibvvPYtjHqVdTufYcODz7njay7B3W4LLlfPB2ELwraxU+POiqojaTqSqoOmg6yuKE+ZUaswdeY9Jo4faI6FjbZ109eY6iQQvr45Yhfn4KqW8lRKOSpFp1wUcucFXR7LrF/yHOGWzvMJNG5Renz32nDzMepVxo7t59ShVylkkngDYVZveZShLY/ivYbpbW4FpXy6mahlbuIkplFDlhXinf2UcvNUSgU39NLFFXh3gsAD50YzM3qMd177NvnUDC2JAbZ+6BO09QwBcK5UZe9clnfTBYSAdSGZrfII0dJBQOCLrCXU+gAefy/27Ajm2CHswjwIG2wLhJPudvfh03zxH19mNJnh4bXd/B//+mE2drc0j8G2EEvq2DYI68ofSpJROlaj9G5B7d2M3NJ30WSWuXqemdIcs6VkU9DNlZMUjVLzOK+i0xFoJ+HvoDPQTiLglHFvDFvY/Pbzv8VXfucP2Pa/Psbjn9rFRwaeZlv7FuQ7ZD4UIQR2qYSZyWBmM7R0t1EOtSLfAR7VayW3MMOB3f/AwrmztHavYuczn/lAn7rfabidOJdFbqUtWOlJjJN7MU/vQ5Szlz5Ikpuij4bwWxR/lyolTT9//NJjF49TdSRvEEm98Qc71VKeiZOHmDhxkNTMGABt3UP0rd9JbyMT56JwWxRnlVKOaqNeXSrkinksy7joPVRNxxeM4A2E8QUieINO6QuEm9tty2Ju4gQzY8eZnzrTSI+v0d67pin4gtG2myKUb6U9CGFTzC6QSU5hmQaSJDcnuJZkuTmhtSQryLLcKJX32d6oKwqSJK+oBwXghEaeOvwqo0f2YdSrxDv7WbvtCXrW3oeirLxoIMsyWTh31knUMnWa1o4ELd3DbuiliyvwVprAGz+dIhT2EYx48OgXX0xs22bs2Jsc+cE/Uynm6BraxNbHfrg5MWyubvLGXJb98zmqlk2PX2OHd5ZEaS9YJTRvG8HW+wnEtyArl76ZGobB3/zNX/J7v/e7ZDIZPvOZH+fXfu2/kEh0XfJ4IQQI4Qg921nEEgFoFxewJt7FnHwPMzVOVpWZD0WYb+0iGQiQlExmywtUrWrznAHVT2egnc5AhyPi/O10BtqJ6pHL3hBGR8/y1FOPsnPn/fznL/+fvDDxMnPlJO3+Vp7rf5r7O7ah3EBYQtWyOJOvMFao0OHzsDEWxKde/fmEZWHmsk3xZmYyl6wLY3mHQlJV9L4+vINDeFcN4Vs1hNrauuJujFeLadQ5tu97nDi4B83jZevjn2Bw44P3/KSkV8IVeC6L3PTJjMtZzNP7ME7txU5NgqSg9G5GW/0gkuZFGDWEWYPLlMKogXmZYy7j2bokHj+yP4LkjyL5Ikj+yAXrUWR/BPTAVV3/itmFZibOfHrOmVMrGKVSymNb5kXHax6vI9qWiDdfMIz3AvGmea4tI3MzgcboMWbGjlPMzgPO5O6JgfV0DqxvhthdDzfLHoQQlHIp0nMTZOYmm6VRr175xddJUyQ2ooJkRUHVdHRfAN0XdBZ/cPn6km2qpt/wvVAIQXLyJCcPvcL0maNIskTvmm2s3f4ELYmBm/NBbwF2vY6xMI8xP48xn8RMpYivGcDuXY3W1na7m+dym3EF3goTeF/9ywOkkiVkWaK9K0TvQIye6WVJUQAAIABJREFUwRjtiTCyfP4iZhp1Th56mRP7X8I0agxuephND38UXzACQM2yeXvBGaeXrhnEPCo7QmWGam8iVaeQFB1feC0eXzuatw3N146iLRdPuVyW3//9/8af//kfo6oq/+E//G98/vP/O4HA+4daWrZFvl4gXc2SqWVZqKQdr1x5jrlSkrp9XsCETIv2ukWHGiQR6aUrsZmuxGZCnuA1XbSLxSKf/ewnOXHiOK+88gbd3T3Ywubw/BG+N7abc8UZWrwxPtz/FA8ldqLJV34SJ4RgtlLnZK7EyVyZ8WIFW4AigSVAkSTWRvxsbQmx1qsg53PLBJtxgXiz8jlHCC9BUlXUWAw1GlteNuoByWDu0BGqZ89QHRtF1J3OkhIK4x1yxJ53cBXewUFk762fG+56sSwTy6izMH2Wt/f8I6V8moGND3Lf45+47qxj9xquwHNZ5GbYgjBrmGNvY5zci3XuKAiB3DaItuZR1KEHkH03JwxNCBvM+sUisCkAG/VqAVHOIso5RDmHXck5HsRLCURZRfJHkHyLAvC8CJT90ca6s19SVIQQZOfPOVk4i7nzAu4CIXelDIU3i2J2gdnx48yMHSc5cRLTqCPLCq3dQ03BF2lNXPU98HrsQQhBuZBpCrn03ASZ2UnqtTIAsqIQbe0m1tlHvKOXWHsvmu5DLE5YbVtOGK+9WLewbXvZ/qXHONtthFjc3zh26XkarzPrNWqV4rLFti4dKSQrakP0BRqib+kSuEggeryBJfPS1Rk//hYnD71KPjWD7gsytOVRVm99rNmXup0IIbDyeYz5pCPiFuYxkkmMhXnq80ms7HIPu6SqCNN5cKG1d+DfsNFZ1q1D8btzSN5ruAJvhQk8y7SpFA2OHD7H1FiG+dkiAB5dobsvSs9gjJ6BGJGYD0mSqFWKHN33L5x553UkWWZ4x1Os2/lMcyJoWwhOZEu8PpthrFhFV2S2RyQ2chS9chrLOP/Hl2RPU+xp3jY83nY0XxsTU/N84Qu/ybe//Q06Ojr5hV/+ZZ78+IfJm+dFXLaaa9ZztTyC5d9pTI8uC6lMBDro8LaiZ2awJt/FnHwXe8EZ7yH5Iii9m1F7t6D2bLzk2D0hBKdPn2rM8fci+/btpV6v84d/+Kd8+tOfvejYI6njfG9sD2P5CaJ6hF19T/Bo1wN4LvBiVkyL0/kyJ3NlTuVK5A3nptLhVRnUZbpys4THTlI0VU75opyKJyj7Aqj1Gn1jJ1l1+ihd50aRbRvZ70eNxVGj0YZoizcEXBStUZeD7y9kl/5AhWVROzfliL2zZ6mePUN9dqbxx5PwdHXjG3K8fN7BITyJRDNr6pUQQmCZBqZRwzLqmM2l1txuGvXGPqdumsvXrSWvaa6bzrqw7eZ7heMd7HjmR2nvXXNVbXNxcAWeyyLXawtC2FjTJzBO/QBz9AAYVaRgC9rqh1HXPoISvXSUxu1CCAFG1RF85SyiIfqc9dyydVG99Pch6cElAjCMHO9FW7UTObwyxiRZpsHC9CizY47gyy1MA+ALROgcWEfnwHo6+oYvOcm7adpUy3UGh9quaA+VYs4RcrPnvXO1itO/kGSZSGsX8Y6GmOvoI9KaWDEhiUIITKNGrbwo+EpOWS5eIARLzrZqCaNWuczZJDxeP7o/SK1UoF4rE23rZu32J+kb3n5Lxki+H7ZhYKZSDRGXpN7wxi0KOlGrLWm6hBqNobW1obW1Lys9be3IwSDBep6p1/dTPnqE8sgIolYFWcY7uAr/ho0ENmzCOziIdAcnn3O5OlyBt8IE3vNff49cuU48qNMe8xHze1CrJpV0heS5PMW882MPhfWm2OsZiGHWcry397tMjBxE9wXY8NBHGNry6LIL9GSxyt65DEfSzkV9IOSj3avQolSJSTki1hxybQajmoQl4ZIGMjmhsPe9Cf76z3YzeXKWWH8Lm3/iYTo296DKKjE9Qswba5TRZetxbwyveuUno3Y5izV1BHPiXcxzR6FWcsbutQ+h9G6m3raWN46PsWfPi7z00otMTIwBsG7dep5++sN85CMf46GHHm6eTwgb06hj1CoY9Sr1aoXR9FnePneQ+cIcfjwMBfsI+HqZlQLMqWEyWgghyShWnUh+mmBqlGBqFK1eWtZW2YaY7aHN24LRs47TbT2c1MNUJRmfLLE5GmBre5T+oBf5BsJHrvQDtUolqqOO2Ks0hJ9ddtoq+3x4B1bhHVrlhHYODqGEQs3XlvJpJk8eYmLkEJm5SeBafgcSqqahaDqq5kFVPSiaB3VxXbv0utcXWrFjGVY6H1RiDSufRwmFkG5y2m+Xm8e12oKVOYd56gcYp95AlNKgedFW3Y+65lGUxFokSXY60emUcz0ZPUt1dJTa9Dm0eAt6T6+z9Drl0uvISkHYJqJSWCIAFwVh7vx6OYsopgCQW/tRV92PtuqBFSP2AMqFLLPjJ5gdO87s+AlHqEgS4XgPvsgAqF2UykGy6SqFXBUhYGi4jR2P9dPS5ojAarnQEHITpBtirlrKAyBJEuGWRFPIxTv6iLZ1feDC5lZjWSb1RSHYFIOlZYJQVjSGNj9Ca/eqWzbkYXFcfT2ZxFhINj1wzbDKTGZZZI/k8aC1tqG1ty8rPW1tqK2tyFdIQLbsobBpUjl7hvKxI5SPHaU6Oup46r1efOvWE9iwEf+GTWgdHXfskI/3Q9g2ol5yogOqJagWnXqtiKg2lsW6sNHWPIK29lFnXPBdgCvwVpjAe2H/BCen85ybK7CQq2ItaZumyHSGddpUBa8hsIp1bNPxjLR2BOkdjBGJlJk59X3mp04RjLSy5UM/RM+a+5o/XtM2OZ2b4425LLMVQclUsTnfkbPtMradQbKzBMjSIuXpV8t0qTYRyUYVFi+8MsLzf/kqM3N5Hn9kI7/6iz/NuvX3gdZK1Y5QqEoUynXyJYNCuY5h2oSDHqJBnVhQJxL0EPZ7loWcXoiwLezkWU69+SK7X/oe33/7OPtG56mbNj5d48H7tvDIYx9ix9YthP0apXyaSjFHvVbBrFcboq7GpUSLqeoUon0U4v0UYn2YHuemGKhkaCnM0pqeIpycQM7nUUwL2QY9HMXX0YW/pw9vTy/JmbNMnjxErVJC0330rrmP7uEdZEMJ3s0UOZ4tYdiCiEdlSzzE1niQhP/axwpca0dOCIExN7dE8J2hNjXpJMMBREcbha4YKbVGtpQBINbRS2ffMJrua4iy88JMUS8t2hRVe9/PYhoWxUKNYr5GIVelkK9RzFWpVAw0TUH3qs3Fo6uXWNfw6AqK4o7LW+RWCDyrUKAyeobqGcdWqpOj2NShZDte53gLWrwFNR5Ha2lBjTXKeAuy339Xdgouh7BtrGLxfNj1RWUWJAm9qxtPVxd6dw+erm60trar9qRfCdsWZNNlvLqG5lXQtMuLcLuSb4yr+wH2wpjzsKxnE9qaR1AHtmFXDapjo8sEnVVoiIDGuF9PVw9mOkVtahIrn2+eW4lEm2JP7+lB7+nF05m4I7wCdmEBc/QtjLNvYSed+WJXgtgTQlApGWRSJTKpMpmFMumFIrmFKezaFJo0iyJlkCRA0tH8vUTaV+MPd3HyvTMIY4FotIIs0lSKi6F7EuF4e1PIxTt7ibZ1f2ChqPcKzli4BUfALSycD6ecn8dcmMeuLh/DqEQiy8Vbeztaq+OJUyKXzzNwNbzffcIqlSifOEb52FHKR49iLDhjQdV4i+Pd27gJ//oNKMGVN2xCWOYSYVZoiLPSkvrFoo1amcs+uJYVx7vvDSF5A4h6GTs1iaQH0TY8hbZxlzPe9w7GFXgrTODB+T+KZduk8zWSmQrJbIX5TIW5TJn5rLNeN2wCQASJMBJBJCQASeAPpvGKd6CeQY5GKa1OMKWXmSvPY4vz4XJBLUDU24lP7URVW7AJUbN1CoaCueRr8ckSAWR8toHfKKBXZnjjO1/lW9/4HrVqnU9+bCs/8xOPEIv6yVZ0kkW/sxQCZCs6lpCxbQlbSNgCBBIBn4eAz0vYrxMK6IT8Ol7V4uzRt3h7/2vs3/8Dps454SqJ9lY2r+5huL+Dwe42tCUdCVmS8Acj+CKteLx+NN2H5vE6i+5F1XxkNT/nhJcJU2G27vzkvYpEl6igjh+m5djbrJrKojU+tN2WoNY9SKG9n1Ssh7ytUqwYlKoG5apJJOChM+4lThKyJ8lNn8AyavgCEXrXbSexdjuzWox300VO5kvYAtq8miP2WkK0eq8uW9zN6NRXsilG33qZqTPvkSmnAfBWLWJ5g1gZIok+PIlG9kpbAMIJjbIXk+fYzgNGYYMQ2LagLmQqlkbF1ijbHipCo2J7KOOhIjzUueDzCYGXGh4MLFnFRKMuFATvfyPTNBmP1xF8uq426ip6QxReuL5UMGoe5bpvlMI0satV7EoFu1rBrlaxKhVEtYpVrTS2V7GrVRS/H09XF55EF572jlvWyb1RWxCm2QzxLZ85RW12DIs8UosHuVVH7vQjBSSQQKp7kZMa1tkq1mwaI52GC8bASLoXrSV+sQhcXI/F7ogOP4Bt1DGz2YsTHy0ts9mLvgMkCSUYQPF7UDSnE2IU6ljF8x06SdPwJM4LPk93N3p3N2q85bL2KYSgVKyTni+Rmi+RThZJzTsdf9tyrlFLx2l398do7wohCxNz/DDGqb1Yk++BsJFb+1EGH8T2dFObSTYFnZGca76fJ9GFd3CwMZ53FXpP70V/OzOXo3ZuitrkBPWpKWpTk9RnpptjflAU9K4uPIvevsaiRlZuJ+mSYq+lH3XoYrEnhMCuVLAKeax8AbOQb9Sd0swXnPXGftuoo8Zizm+hxflNaC2tKLEYFU+Youkhm605Yq4h6Oq184lfNI9CrMXvLK1+oi1+AgFBOTvO3ITj4auWl18PLBHAluIkBobYuH0TLYne5nCNG/6uhLihaJQ7GWHbmNnMMuF2vlzAyl0wFs7jQWttRWttg3g7lUAb4UQL4Z52J5RSv3UC+1ruE/Vk0vHuHT1K+cQx7IrjLdb7+h2xt2Ej3qHVy7J4i8WEepYFloGwDKc0jWXrWPVLbLvUcRduM5ef16g6Ys14n0Q/qscRanrQycarBxrCLXh+0ZfX0bwXZXK3Zk9ivPs9zPHDICtoax5G2/wRlHj3df89bieuwFthAm/mz/4YOzmLrXqQdB3Z60XWvY3SWZca9QoqeUNitlJhqppjzshTLNvINQ/+cgRvLYBHHsenHEWRqhQ8EdKJfiJtffRFEsT1FioVQb5cp1AynLJcJ182yJfqVISNEtBQAxpaQEMJqKgBDVk9/zS6mkrxzt//KUde+Aa618u/+bFP8e8+9TAteg7JTAP25T9sg+nZHD94a5S9b53lrcMTVGsmukdlx9ZeHrl/kEd2DtCTiCGE1BAEMhIgCYEsLGTLxJFsMrLmAy1AWY0xZrUxbkY5Z4WpooEQRK0iHcVZuufP0j17Bq1eB1OQlbzMhVVm2wzORT3k891UZgYwaj4sWybi1YgqCiHAYwpMy6Zm2piAhUBgEtaSRJUpvPYMEjaKHiPevYmONduY84YYqVSZrDgJA7r9OltbQmyJhwh7Lt8Jvt5Ofb1aZur0u0yOvM3cxEmEsAnF2ukb3k7v8Db8kt4Yy+d4+oyFeSeLpSRhSxI1xU9V9lNR/FRlHxXZ55SSl6rkw5KWew4UYeGlhp8qPqmOT6rho45PruOX6nglE1nGEYjVCla5jFWpYFZqGJaEoeiYsgdT9mDIHszGuqE4dUvzYapeTFnHkD0YqJi8fwihJIGuSegaeBSBJll4JAtN1NHsOppVQzUrqEYFtVZCqRZQqwWkcgHMizPsXfI9dH35GAlZRmtvdzr0iS48iQSeRDeeROKGb+rXagtmLkvlzBkqo6eozp/BqM0jRRXkFg9Sq46kn/8dK1oUj78Tj68DSfZQzh6lXp4GJLzhIfzRTXikBFY2j5lOYaRSmOk0RtopzXQKq3BB2yTJeVIdXyoCW5qiUI3FkVRl+QPWC+8jjfXmmF5xqeMu2NeoiCXH2qXi8qRH2QxmJtsQbhnsYvGi70/yeC5KgKT4NGSpimRkkSpzUJxCsh1bkXxhJF8Yu5jGrpQxKzhL2embmBUJu74kFEtT8bS3IiV6qLauouRvJ295yeRN0vMlatUlNqjK1GXIGhZFITARhBoP9vyNB3uyZNGuzpFQzxGVMuieEFh+SKUwzk01xakaizmh2w1Bp/cPoPivL526ME3qc7PUpiapTU465dTksuQPSii8xNvnhHlqnYkVMfWLbdSxCgWsfAEjOYUx+h71qVNYmTS2AbbkRUhe7LrAKpXOi9kLkP0BlHAINRRGCYdRQmGEopJNlcjmDPIVKAovJU+UshbBXpLkyyPqhDSDiF8iGtWJtYdo7W0l3NOGGri8J0UIm+z8NKnZcXr6+5D1FkoleGPPGcbPpAlFvDz81CpWDV9/xuWFap2TuTIncyXO5isENIX+oJf+oI/+oJcOv45yE0SfEAJjYZ7a6CjV8VGsUgnZ40Hy6EiahuzRkXSPs01rlB6Ps92jNY9d3C5p2jV5zRfDKJteuPkl3rgFR8Qte7gjSU40Q1ub44lra0NrbUVtaaWiR5jPCebO5Zk9lyc9f354h6rKhGM+IlGvUy5ZAiH9faOaLtduUS0gCgvYhXlEMYXPA+VCGWGbzazm2KYzvZVtOQJqcbqrJfuEaWJkylTnK9RSVeo5A4QzI4onIiNavFTaIhSCEbJ6DEtS8FpVdLuGbtWculVDb5Y15MsO+5BA1UDRnLmWFQ2psb5sm6I506ksFWfLxFrIEXM3YXqVpdjZWepHXsAYeR2sOkrvZjybP4LSveGOilpxBd4KE3ip7/4PxLkJKvkidrWKqNUcT0HN8RZgX1kwAdiyRMUbIR3oIa13UPYV8KhnkDAwzB7McjvCtLCFjSVsZFVC1VU8Xh2P34vu96L7PPgCOl6/B69PxefT0H0aVVVhwRSkDJuUIUhbEqPjE/zgL7/M5FuvE+zo4tF/97Nsf/gRwnYRv5nHMqpYRgUsC8usM3ZqlBPvHef4eyeYm3GeJLd1tLJlx31s3bmN4c2b0Lw+LCFhmjamaWKaFqZpYtsWMgJZtpGFwCObhOUqXtUipbUyqfYwJ7c6T6JElW57lj5pmj55Br96DSm7l2CaMrYtY9kKkqRh2RqmqVGrK9RqCtWaSr2mYNQ1DAOwMmDNgZnCsgSGFaNm91LW+il1xCh3+jFCjugMlixaCiYdNYFPVdA8Ch6P44EKhnRKpfqSjq7zn3D+c7YJgRBgW3UqubOUsyNUCxMgbBQtjC+6Bl94DYq3FQnpgtc6JzTqlhNOma9SKlz8Hfn8GqGIl2BYJxR2ymDYSyjilF7f9U98bBt17LLjFbPKZexKGbtcxmqUdkMM2o19zjHOsbWKgWGK5QJR8TSFoKnoGIqOIZ8vTUXHki/fuZQQeBThiEOPhMej4PWpeH0aul/HG/TiC3nxhXx4/R50VSDnU9jJGeozM9RnpqlPT1OfTy7rFKjxlobgc7x9esPrd7XhMO93sbYNg+rEOJXx41Tnz1CvJsFnIrV6kCIa0mLHQShoeiueUA8efwcebwearx1ZuVh8GtUFSul3KaXfxTLySLIHf3QDgfhm9ODARX9vu1ZzssemU8tEoJlONYXghVOA3BYkCSUUujhz7bIyiqSAPT+GlTyDlTyLMT9GyTApa37KnjDVWB+VcDeVQBsVb4QyGpYATZbQsFGtOlrjAYJWLyJXCxj5CuWsQaUiU637qIgAdXxIlkCyBapRJ1jJELByyKKMIdmkFA/pUCd6oo/u9jA9bUFW9caYPXMKfXI/gemjZApBZowuklIXFdXxmKlWjUh1DskoUJagHIlhd/bga2slHtaJhXRiIS/xkE4srOPXb97k5Vah0PT21Ra9feemEKaJAGqeIPWOVVRj3ZS8LZTwoWoKoYBMyCcR9EmEdEFAF8jCBstyQrQsC2FZjXXrgvUL9puX3m9Xq46oK+Qdj8WlTERTkb0eZNlCpoasgRIOoyUG8PSvR+1wxiHKwRBlWyOfN8ilK+QyFbKZMrl0pTk+bpFgWCcaUgl7bYJShYCRx1+aR8rON38nFwpI2edrPByJo7a0LilbUFucRF2SLF90bZgay7B39xnS8yUSPREeeWaI9sSVx03WLZvRQoWRRubodM35vbboGqt9EqW6wURNkG9c1jySoEc16ZPr9MlVuqUKum0gLBPsRU/MYt0phWVilSrUF/LUUgXq6TJGpoJtNPo2MsiajLAEwhZX84z40sgSkiKBLIPSWGQJFBkhNxZAqlpIlSoYF3z3gYCTwKThiWuKudY2tJYWJFXFNCySswVHzE3lmZ3OUy0735lHV+joCtPZHSbeFqRcqpPPODaSy1bIZypY1nkDkRWJcNQRf4uiLxz1Eg5AQMpBKdUUcnZhAVFcwC4sXDrLrKSAojhhiLIKstJYVKTFuqI29jvbhaxQVAJk1CAZNUgaHylDI41OTg9Suw5PsC6Brkj4FBldkfEqCj5NQVcUfKqCV5Ebi1P3qUuOU2Q0WbqtgkpUi9SP7cE4+hKikkeO9+LZ8hzq0ENId0AeAVfgrTCBBxCL+zgycZbp4izTpdlmma6kUWzwGAK/rdKtxelUIrQpEeKSn5jkx2OK86JwcalVsSpVFuoSk1KJippCIGOKFsBGwgIsJMlEwkLCRMIG6eq/FwHU9TBHz2X47j/vJjk9TeeadTz4079I28btlBbmmDywl8kDe5k+vB+jUkZWVTo37aB356P03v8oke7+G/8xC0G8lKNv6hQ9I0eIz80gC4Hik/H2dODfuAX/Ax9CjcUQwkDYBqZRJz2fIzOfI5MqkM8WEJaBolig1bF9ZUJhhe6WOJGADsLAtqrOYlawrQq29f7zBJmmwDRsTFNQM1Qqho95q4NZbzdJXzsVzYskBNFSiUi6jHe+SrUgYVkyLAljXPx6Fr8nSTJRpVk80iQqM0iSjY0Pk15M+rCJgSQjSYuvlRb/NUrnPKomEwjpTQEXCOuEIjqhiJdQSEd7Hy/j7UZYFla5jFnOY5WzWJUCVq2ArOooehjVH0H2BlF8fscDrihYpk21alCrmOfLikGteon1JaVpXL63oXkUfH4NX8DjlD4Vj6ij1UuopSxKfgE5NYM0N4laLSI1VLYSCjVE33nx50l0OSGOS34Pixdr52l3ktLYu1QWzmBWk9ieKlJcQ/Ke92pKlo6mt6HH+tGDXWi+DlRP7Jp/Y0IIasVxSul3KWePIew6ihYhEN9EIL4FzXt18y0JIbCKBcxUw/OXSZ9/YNVs05K2NTdJy/dcxbHNDY1C8QfOi7dIBElVMWybkmFRMi2KdYNidp5CPkWxmKdUq1K2oKz6nUULULuECG58MrySiY8qCjaWpGGiYtgKhpCxruOaJtk2qmmgGgaqaaCYBqploAkTjyTQMfBkM+j5Et5iCW+lhK9aJhKLorf3kPImmKkHSKUN6hWn4yoUiZomkxM2czWT2gXvqWtKQ/TpTdH3/7P3Jj+SZHl+3+cttvnusWdEZmVkbdlVNd0908MeqmfEGYkYiRRGOkgCJEAYUEPqIAgYQpTOOgggoIt0IqCDFkAL/wABOkhDSRSJmeGwqW72zqqOrqyq3JdYfTO39b2ng1l4eGRGZmVVZVVlddsHePE2cw9zc3Mz+77f7/3esBsyaPv0Oj79lk+v7eM/Y97fuaPiHLNJxvFhzMnhnJPDmKMHY0YnKcWSMUSblHY+xgrN3O9ipL/8JoRlTFRMiYrJIm8VU6Jiinb1gIFSiDotl8/q+qwtCNC9PqrXRXV7S1a3LqpX1UVwNl+6nBwyfvefc/zBLxgfxUxNj6naZMqQWarOjbl6vqI/iOivVOnUxXKw0sLzn33cnLWY6aQeGKkHSI7qwZE6t/H5YF9OSEynh1hdp+ytIFfXUWsb+Jsb+GsbPLgz42ffu0s6L3jz1zb5y793jU737Dx2znGUFeyNKkH30TShdA5PCK75Ja/l+1w7epf+w59WQc9qxl6Pu50r3G1f5m77CgfROk5IhLNsJPvsxHe5HN/h8uwe3TymSCTFDPKZo5gabHZ20GTHQ/ZCGIS4rRZu6FdPJTGUc4cr7UKsU9raNbBeZ7d0CGsQ1iFcNUgirUXYaorBaRv2NKeaelBPPxCAFzh0ACqgysOqXCqPTLUp/S6EfVS7TxmsMTMDjuOQR0dwdJwvvv/+SsTWTo+tnT6bOz1W1p49R9k5RzzNGO2fMHp4xPhwwuQkZTwzTBNFaZeu5Vg6ckZXTeh6Cd2Wo9/36K206a8N8AZriO46srPK+vY6h4dPeiQAlNZynJUcZwXHWcFRWnCSFRxlVV4uPcdLYBB4rNSpb3LaD+8R3tjD++kPEZMxuReQBwGFH5L7AbkfkochZadH0elSRm3yqEURhNW2nkemNJlQZNVT5jORQFCLQ19JAinruiCQdVvdflYWZ69ZbF+V9Se0kC6+K1NQ3vgu+U/+AfbkLqI1wHvn9/Hf+lcQ4cs3X/GUl0bgXb9+/Q+Avwt4wDHwR8AE+PvAa0AOvA/8x3t7ewf1a/4l4L8DonqH/nBvb2//Of/lLi+hwPvvf/q/8rPDdzH1PDkpJFutDbY7W1xqb7Hd3mS7c4mVcID8lAtDz8ZH/Owv/g9ODh4g0Dgq65Q1srLgG0lRCkojKQqJdQqHAhRuUZZoIfEl+AICDL4zBLZAFTF/9rO/4O//0/+b43nMdrfH/Xry/nqrxbe3L/Pt7ct8c2uH0PdxQtRJLpVP69VN7NR1kMe3UwqnPdAaaUrWbn9ImCV46+tE198iuvYKXitHnHxQReYsUjJaHHV/g0P9Kvtxl4ODdDGSNliJ2Lrc59LlPluXe9go4x/e+VP+yf1/RmkNv7n5Tf7a1b/Kdmfr3DF1zmJNVom9U9FXprX4q9rS+Qnx+BF5MkLLFEqTAAAgAElEQVRKg/YkWlfi65Ah79tdbrhXmNNCU7Ar7rHKiNJpSqvOciuxxuDKHEyGNQ7jFClt5nRJXQvjqtFJRz2NrhqrxOEWo8oOzh6MHdjcYHOLLarcLJWpfyPLwvBMbFaN4nHhWNcX/XVZiLNtRV2o5nY4Am0IVUno1UkXBLok1CWBqsqBLgjUaV7gqxJfFSj59N+xsZLc+uTGp7B1cj6lDSidjyHAuICyzi0BVoTV4rtCoKRA1vvsjEWUrlrTybjK+mIsrnTYwlDmhiItydKCdF484XV4SuALAmnwbUpQTvHSEwI7wxMZgUgJfEc4bBGtdvFXuvgtiKf3sTqFnjyzypUgyhAvWCdcfZVo9RpetHmhVe6zYm1BMt4jPv4J6eQDwOG3tmmvfIPW4B2UVwUscs6Rl5YkK5mnZZVn5bl6kpc4V58Tp+ePODtPENUxh/r8eMp2i/NJiOr/CkcGZDgy58ipUgFV2TlSW7lXX4R0hsgVRLIkUiWRLAjcnNBOCUkIyYhEWrkki5LIC3G2RTz3SeYFSk6IwjlhUNTHAkoUk6zF0bzFYdbmKI3IZQ8vHNDqDOj3I3odnzDUGAe5teRFQTqbkM2mZElKXpTkpopqXHg+SatD8ZSFsSMl6XqajqcIHdh5ST5KifdjzLRA5YZOoFkbtgj6ISbSTLOS42nGySTleJoxmmUXnrtRoOm1ffp16rU82kriWYfILeW8IJlmTE6ScwMiUctjuNZiuNZmZbWaUzZYEcj8kGz/FsIIpOpRmhbTBGZzy3RumcxKprOSyTQnTc7PgQwjj/4wrK0dtdVjGNIbREStZweCWuZUjI5PLSzHCaO6PBkli3mPAFo5ujqmaw/pqgm9nma4e5XVt75Be2sHsJTZCGsSlNdFed3K/f0Z5IVhHOeM45xJnY9n2aJ8ms+nMVE6pVfE9MuYXhnTL2YMiinDYkrLnpftE9XiyB/yYPAWSWsHByS6YLzTw650oOth/WrfWnnClfgBXxu/xxujn+I5g0OQtTbI+1cxw11yr0tmBJmBzAjSUpCWMDOSY6kZS0WuIG2H2HoOZ3s6ZuPRXTYe3iU8PGY+d+xHKxSbbcI1xdZgznZ/xlr7SWuqdYKTtMNxMmSUrzArV8no42uNryW+pxa5pyW+JwkW5bpPK5wsiM2EsTlhko84yU84So8pTMFmsMmQPt25j57mFJMRdj6CZEKRQF6GpLbLpFwhcdX1TVGyqg9Z1/us6316wQw/8iHqo9sDgt4KulOvw9gaIPwIG5/UFrhD3PQAe2qByx/73F6I6KyTRVtM1QYzN2RatpikPtOZYzzOyLPzv4NuL1i4fPbWO0woyX3FXEEsYGIN48IwKcpzTpO+FAsBtxqeibmVwGPge6inCCLnXOVZM5thZlNMPMPO4qo8m2HiWd13lmw8O2ehdoDRuhKFQUjZG1D2+pTdHkWrQ9FqU9TisPQDcu1TaE0hFTmSzDkyY8mNfW4jrxJiIQ6fFI2Srqfo+Zqep+l6mp6v6Gi9OA7OOczdn5H/5E+qtUO1j3f9r+B//a89NThTaar7YJUMxjquXep+IZbJl0LgXb9+fUgl3n57b2/vF9evX/9D4A+B/wD4xt7e3j+ut/uvgZW9vb3/6Pr16xL4BfBHe3t7f379+vX/Anh1b2/vbz3nv93lJRR4//D2n+K8koFcYbu9xUZrDf0ci3J/XjhXue8l84J5nJPEOfO4qPJ5ThIvt+fnbuhZnvAX3//fuPfwF7x+7Zt88+u/zavX3qBVWzfCUBEFgtCXRD6EGgJtUdjKlacscWWBK6qyLYvqAlH32aJY2q66cETXXiW6/jW81dXF/k/HGQ/vjnlw54QHtw45GVUXR4FlVR2y0Z6xtdNj++3X6Fx7+0J/7kk+5f+9/Wf86b2/IDM5Pb/LMBhUS0KE/bNyvUxEz+8+VYA75zh5dIdbP/8+t/d+QJ5OCKOQ1cuvo4eXuS8H3DYeB6qD+ZjvXmA5nZkoakl3Vq4Fl+OsvMjFUql6l5xaRF+AchYPi+8sPmYpL/EpK3FPiWdLAlEgnUWIOkiLsNVIqnDV3ESRo0+TzNGiWOTyGVZj6wSl9citR2E8cutTWI/ceBTWIzOawvikpSY3GiVLApGjVY4vCwKV46u8FopVHupnC8OsVMxzTVJoksJjXudJoet2Dwd4yuIrgyctnrJ4yuApS+hZIs8RKEugLZ40aGlQ59Lz+yBlc005j9CqT299l+G1d/DaGy/8ZmGsJckM87So8guEWpFNGaiP2Axv0g/GWCe4NVrlpw82+dmDAXl5NnrQFhmrcsaKmrEiZ6zKGQM5RwgoncQ4SYmkdJISheG0TWGcpECReRGZH1F49QOBH1D6Icb3Mb6PDXy4YF6XsxZZFIRlStfF9JnRYU4oM0JZoOvBgo7OiEjxKRCiOnWnmc8sD5nlIXEeMS8j0jKiyALKOMDGEpnZytlBgPUVM+s4KUqMKgjbKZv9jN01w2Yvox/OCcQU4ZYt/gLl9/GCFXSwig5WqnK4ivYHT4gD5xyr/YDjSU5hLbPCMCsM06I8y0vDrK6ftuUX3eecQxYWlVsCB73AY7UTsLnSohd6KONQpcOmlcA6OpozPklIxin5vIDMoI1jeQ9zHAmQYglalsGwZNgvWO0W9MOUtp8QyhjNDHGBzBbSQweri+PhhafHZJXSeExG6UJ4jU/OyqdLCJ1yak3rLQnA3qAKrFAJuflCyE1GKaY8+x0qLc/Nj+qvRAzqcqvjA45idJPk1vcYHd9magpmQZc47BHLiIQQg6It5rRJ6AhDgEAYybwIGCcBxzPN/szj4UhwOH0y4JQAui1vIaZ77SoCdVU+E9idyKM3aHH/4YRsMiV79IjyYB97eADHhzA6ZO4sd7Z2+fDaN5isDUAJZFmy/egmu/s3ePX4BituTBF43FXrfOQ2uFmucduskbqL5zcJZ1nLx+zkR1wujthKDllJT5DOYoXg0dZV7l17i4NLVxgPBqT1Mgyakk1xyBYHbIlDNnVCK9ogaG8TdXYI2tvgHPn8Hll8j3x+lyy+j6vFq1ABQWsHv7VD0N7Bb19GqJBRNuYwOeYwOeYoOeIgOeIwPeYoOWZWnLd8tnWL1WgFJRR3Z/cpbIEqfFaSTdazy4SzAeVxNeANEHV8uqst/LZC6gxbjjGzEXY+RmYTAhPTkwldmdATKT05xxMXX9eN9Mj9IUU4xLRWsa0VaK8iuuuo3jpeq4OnFU5VvlW5s6TWkZSGpLQkpWGSFkySgllaMC8MibXkzlFKsPr89UJmBp0YdFISFpaWE3QRdKWi5Sl0oFCeqmIraAlKYITAiMplN8sNWWHIckNa51lhcA6UEmgp0UqgVGUhU6quP94uwbMlfpHi5Qk6n6PzFJXO0dkcmc6RaYJIYkQ6h3lcpeLiaTXC95HdHrLbRfQG2MEQ0+thuz3KVoey3cGEUSUQPZ8MUX0eY8ltlWenuXGkxhAX5kKxGElJS0kCBJ4DbR1hMmbz5F9wZfQzusWEQ7nDj/Q3uVlu1AOYprpPlk++43/+732TX3t19cLP9SJ5WQTet4H/eW9v7526vgIcAet7e3uHS9v9u8B/sre39/v1a/6nvb29X6v71oCbe3t7z2sv3eUlFHjw1V7QuBKDeS36lsTfvBKFSVzUwjB/YhTqFM9XtNo+UdsjavmPlSsXuFbtBvd4pERrHUf7Mx7enfDg7piHd8fEs+oC4QeKzZ0el2oL3Wo7Qzz8GeWdn2DuvQcmB+Wjdt6qFll/5RvI7nn3s1kR890H3+dhvM9JOuIkG3OSjcjN+YuQFJJB0F9aF/C8ABwGA9peC+ccB3dvcOvn3+fu+z+myBKCVpcrb/4GV67/BkHL493vf5f7N35MnsZ4Qcjl177OK29+i83L13AUSxbDJ3OzqJ+5kzr79HmIhVMktZ0icQEpIQkBiavbFuWqz3KxiA3IiKgemENR5REpgShB+ljh46SHEz5WeFihqxyNEwqDopL6EoPEIiu3Hecw1lE6qrJzWOcoravrVXv1HVC5aCzcN8TCZaPKq7onHL4oqRzrcjxytM3wXIq2CcrOUTZGmRmYOdakOPO0RXQriW2dxjqNcZXFtTCK3EhyI8kKSVoIkkKQl5LCSHKjKIykNApjJNYqnJFgFRoPzwpc4WMzD710vTICciXOJ3Eq892ZBde5pfmbZ/M2qctwaqStjm/+DFfUxXfsK1qBphVorvTGvL1ym0v9fTxd4oyAKQTHMeHJMerxcy5oIzurOCGYO81UBsxkwFSGTGXETLeY6hYz3WHmdYh1u7LkLyGcpV3EdIop3WJK28a0XfVA3ZIpLZUR6Qw/MDhfL7lvnn5uDyO7lHQoXJvctchMi8S0SMqIpIwoTGVdyecF5TjDxjnMC06f3UotST1JogQz4QgCzeWNDpfX21xe73Blo8Ow++TyKKZMKLMjyuyYIjuiTI8X5fO/T4kOBkuCp0obWzuMxiVCelV6Dm+O3NRisCyZFpUAnOQlh5OUo1nGJCtIncP4EvfY8iTCOvS8RM9LvLjKe0Kw3XVsrVo63RzPm4OMcWYCZoJ2M6Q4f41PCs0oCRglYZ1X5UkW0Asta52U1XbCSithGM7pBsm5QZ/M+MzLLnPTIbN9MtejoIcRPZT0IDeVJ0JqKNKCYl6QxQXZvKjmcy1/JikIOz5BqwoipkMPFWqcLym0ILGWkgQrUqwoMNJgBJRSkQmPhJCUAHhycEW5EmUN+WNWdOEsLZHSIaYj5nSY0xUxbRIiYekoRctrEbYGRK0Bnj9A+z2U10Pqp7v8Pf7MkBvLB9M5eycz3h9NOal19Gp6zMajuySHbcpJxCA/4s3RD+iN7p57P9nuoNbXkSvr2OEadrBK0R2gpmPUwztw7zbm/h1cXp2rp2uuBtd28XbXEWs+RozJ5/fJk4fgDFPX4pHYYV9d4aEdclB4uNqzY6sVnAveMgjOD9Q454jje5yMb5DEdyDdJzDx4siPjOVeaXhgLPdLw6GFfjBgLVplLVphLVplNVqpyuEqvgg4OYw5eDjlwd0x9+6cEI9ri7twpK0xceeYefcEb8VyZX2Dq70rXO1e4ZXeDpE+Px8tKwzHteX7eJJyNE4Yj6ek8YgimVKWGSeuzUS2yHWAqAWV9CRCizqv6qflZw7a2VN3VJDOoZ1AAx6CAEE5y3FxiZvm2NxQFgZXWDAWYRzSVa5yuk7ignMYoMRVgeSEwEpACYSq9tH4kkxLjIXSVoHnjHGUts6Nre7Vpf1EK+w+jrYlLZPSMintOr+wXlZ19RR7XqZ8Eh2RetFisDDzWuRBRO5X30tRmMrLQ0qMlrjQw4U+LvSxoY8NA0ydHr+fCGtppTOiJMZPM4Iso5XMaSUx7WRGez6jHU+ITMnVP/5jwleufoaj8ny8LAKvD3wI/PW9vb3vXb9+/W8Dfw/4zb29vR/U20jg/wL+9729vb9Xi72/tbe39wdL7zMHLu/t7R0/x7/dBT761Dvd8JkpC0M8y5lNM+JZRjzNiGc58TQ71zabZiTzi4MzaE/S6Qa0OgGeJ3lwd7IINd3rh7zy6gpXrlVpY6v71ChVtshIb7/L/MYPmN/455SjKvCLt3aZ1mvfovX6twivfK2K6vQYzjniYs5hfMJRcsLR/JjD+QlHdTqcH3OUjDD2/MOOrzxWW0PWWkNWoxVWgh7B0Yzs5h2Ob36Ira2S2vPZfvMdtq6/Te/KK2SUpGVGUqSkZXaunJQpaZGRlilJ3ZcWadVeZuSmQAKhEESizqXAQ2BxWE4FgMDTHoEOCbyAUEcEXkikI0IvJPJahF4LrSKQLQwhVoSU1iMzkmlpmeaGWV5ZD6ZZSVyYJy70UoAW9WifrFwhlRBoKer2eoSwbq/qS9tIea799DVKCAprSctqhC4tzSI/bctKQ1q7eDwvnhQEWtUTwcGXsBpqrg1avDpo88qgi6eezzXMOUdWGOKkWnojrpfhiJMqzecJWRyTzWOKJMGUBUZUorHIJGUmsKnDpAaXlmdRJKVARhrV8lAtD932US0PqeQ598YzF9rzbo9SClqhRzvStEOPduTRVoa2GeNnJ3jpMTI+xIwPKMcHlKNH2GxefSag7EXk633m/Q4z2SJ1PYx3CRNdZu4PmeAzzi0nac44KxeCfJmur+kHHoPQYxBoep6kK3NaNqZlJwTlCV5xRJmPybMJRTHj8fWOtAzxVISWIX60QmvtGkFvEz8c4od9lA6f+t1MRgkfvX/Ih+8f8tH7hwvr0HC1xbU31rj2xhq7r6/S7rxYN1jnHGU+I5sfks4Pqzw+IKvL1l58HRRCIZWHVD5Seo+V/bruIaV/1ndB3TnF4X7K7btzPro/58FJjreqEX2PNFRMhc/E+eesTS0S+kwYiCkrKmU9hM22z0a7TdhawY+GBOEQPxqidEiSlZxMU04mlRvoaJJyMs1Ic0NeGorCUpSWvA6q5YsJoZzSUlM63oyuP6MXzOn4ZxY752CcBhzFEUfziKM44rAuj5MAlCTwJIGvEJ6k9BXOl0hfEkQCPxRIX+G0xlxwjYfK8hS4DM+WKGsRBoRRCOsh8QmEIpKCgYu5MnuPlfltNBkpgpmTTHSLiddj4veY+H3GQZ+p7j7hpaEp6TCnI+I6n9MhpiszhoFmGPm0ox5+OMAPB3hhHykDDgrFe/sz3j2I+TCrrOCeydmd3uTVyQe8YQ7Z3LxEuPMm/vYbvP+ozT/6kxtMxilf+7UNfuc3h4TzY9IHD0kePCR98ID04UOyg8NzUWul79N+9RrtN14jem0HtRmSqxnzyV3mk7tYU30vUvm0epdp9y7T6l+h3buCH60sro1JYfhwFHPjZMYHJzEfjmKy+lqshEMKC85gXUFpM4zNK7nhChwlvoShVgwU9IQhsgm+S9EYPGHptAZ0OmsE/gpF1mNyJDl5FHP0YMLxfryYdhB1/GqZkat91nZ69Dc6pLbk1ughd8b73Jse8SgeMc0zBBohPNp+j47fJ9RtPBngUOTGkJaOzDhy6z52CSCBI5SCQEEgJJ6UeEKhEUgH0oKoRixxpcUWVSozUw065YasKMmLUytbSVZYPC0JfUXo6yoPNFGgCXxF5GvCQJ/1B4pAKzQGUc6R5RxXznFlXOVmXg1m2gRBgpQZWuf4XnUdMkaB8PH8iLDVRvshSoUoHaJ0UM2DVyFCBQjp40Sd8HHCw+JTOg9jBcY6itKeCUVjKYylLC3WOYypBh+trYSjsadtVb81DmMsLk1gHiPmU2Q8QyYxKpmhkhid1imb46VzvHz+Md/SxVjtkXV7JL0BSadH0ukyjzrEQUjsB8yjNvNWlzR4Mjqxbw1/5xtXeOOVrQve+aXgc5mD9/vAfwmEwP8J/DHwe3t7ez+p+/9bYAf4d/b29uyLEniNBe+rgTGWNCmeYhXMSeYFeVayttll63Jlpev2n/4A9yycc7jxI8o7P6a8/RPMg70qCpgXonfeQV35OiLqVgEirKnXh7N12OHqplTlFlfXrTHMbMrIpIxsxolNGdmckTtNBRPO/OOVcaxMLE7AcU9iP2ZysEAQ6oBABYSqygMdECi/qi+XT7dZahNCMi/mzMukSkXCvJzX+ZN14y62vp7uS0tHtLyIlm7R8iIiHRLhEThJJH3ayqejAtpeQEsFtFRESwf4QtfhrZeDZCw5l55F2lja5Gn9p0nWSSzaT5eEQFTrMuZOkDtHbiGzkLuzG/WpO0eVO/IlF4/UWA7SnGkdNUILuBRIrviwowquyIyeSaBMoUirNX2K03L2WFt2rh/3/MLTCI+JW+XErnFcrnBSDjjOexTWq4+Gox+mrLQyVjo5q92S1a4jCNUiPPVpaGpw2OnRIkqbmxzgsrNJ+w6IgyHTwQ7HnS1G0ZCx12WqWsyEz9xpUqso3ZNWJU2BdAmZnVHYmEg51sKIndaAa50+26Gmbae44oQyH2PyEWU+oszH1e9qCaU7qGCA9s8nFQzQXr+KDvecZGnBvVtj7t464d7NE0bHlYU2bHlcvjpgZ3fI5asDeoMXs6bYp8E5hymmlNkxrSBjPJ7ibLEIFmVtlZ9PZdXnnuz7NEjdRnhDYrXBSAwZ0+XYRByXiqPMMV8aLFFCsBp4rIUe65HPeuhX5dAn0s//3Tx+DFJjmZeGWZ4yTcZM0ymzbM4sz5gXJXPjSJ0mJSAjICV4qqeBR0FEWi/vkhKJjLaCrufRDUJ6YYd+1KPfGtIKB5/JFdoVKS6ZYOdjXDLGzcfY+YQ4mTPKC0alZWxlNQCiO0yCPhO/R6yfdEqK6hnXHRHjU3LfrTOj2m7ImFfEfa6IB1ziAC0lUgf1Q3aAPLX6Kh/wODrIeHR/TlkqNrZXuHxtAz8IEdJHSA+sxE5mlCdjaIOLMvLkIXnyAFtWAzsIhR9t4re2F8kL155qWXbOMc4n3J3e5+7sAXdn97k7fcBx5lBqEynbCDwC3SJQLTwZoqSPFD6g6iBxkFtH8QnmYC2jqeb2Fs59AguTqz09Cjyq6QkeJZ6o6mepwBMlnqCe5yXw3BzfTPHdnJAMj/JxI1B1KGWA1CFSRVXSIUpFSBUi9WlbXV+Uo9qSL1hb67D/6BhbzjFlXOdz7LnyUp+Z48zjIZfOkLqF1C2Uai3KEDKd5ExOxsTTGVIUeJ6h1RaEoUNrg3PZM9/3/IdWSBUgZXWeSuVXx0EFSN2qru3BEO0P0f4AqV7MsgjO2mqO4HSCieMqCJPW55M6X0c9e31dZy3lrR9S/PQfkD36gFlrjez132V+5VvMVERqDL+13qfjff5Tr14KC97jXL9+fRO4Bazu7e3F169f/2+AbwD/1t7eXlZv07hoNnwhuCLF3HtvIfhc/DzjB09BqCpss1S10DirGyGZKMlYS0ZaMFYCW6Z4WUpgHYF1+NIj6qwSdTcI+9u0BjuEq6/gdzaQn2Ddn8+Cc47cFmeCcJEnxOmYeH7EfH5CnE2YFzHzMiNxJYmERD59nh+Aco7IWFq2yiPraNX54/XH2z/dI+PHsSwUBSAfE44CZwomIuR+e5v77R3ut3Z42NqirJdiaBcztuN7bM/vsxPfYys7JNQKdIDwQ4QOwQ8ROgAvqtuCui1E+CHogP6wy/h4cuHiso+3GZNTljnjRHIU+5wkEaOkxTjrkpVnAx++iml5x4T+CYF/ggomZJHHNOgThyskfp9Ud8hUi0JEWBHhCKvPfu6csDiXYF2Ms3Osi8HN0aLAV4ahKnldZbwmZnQpsAimukdWZmib0BXgPe5CKQO8YAU/GJ4Jt1MR5/eRz1jq4uMoS8vDu6eCbsTBwynOVR4B21cGXN4dsHN1yOpG+6Vc9+gzL3pfL1Z8sShcFoQG5bVRXh/hdSgRlLaktCWFLSgW5SqfFSUnmWGUWyaFYFoIZqUiMefnmGlR4IkUTyQo5ggxwxMaT7VRsoUQIeBj8CitJLeC1DiS8ukP8xJoaVUlBaEsCMkJ3JzATvHNGK88JiSj6wd0wzatcLBwe/WCVZTfey53188T5xwUCW4+wSZjivmYcRwzzjLGWcnIOEZWMRE+Y9Um0RHb5SGvygmvdRz9XgeiDg6Ls3n1HZu8HgTIcTY/+55tjjPVNrjnW/sTBF64Xgm5di3ows2nDqgYa3g0P6hE3Ow+96aVoFueF7cWrXK5s12l7iW2WpushAPUBe/pnGM+yzncn3F8EHO4H3NwMGM0SrBCYFVlje2uRnRWQjqDEj+s3IezYkZWppROUaJx0sdzWe2avyTOKCuBRomHwdeKQHn4OkCdiiwVkiM4KRL2sykP0hF34gPGZUbqHE76XOle5mrvCjudS2ipa9d4AyZHuBxxLi+QNkfYAukKpK1TXVauXMytv/C8QWCEQrpqQsPTtimFh5FelQuNkT5Gepi6/TS30scIr3pOWXbirOtaaiIVEMiA5EBwfDPn4Ucxyayaw7z9yoBrb66y+1qfqA3OZFiT4WyGNflSOTtXrs7H03KGKeMnppVI3T4TfMGgzqt6FdTocXd8R2YqD6ekTElNuignZUJSpuSmwJMaX/kEyseXHr7yFylQPp70qj7l4Uv/wvPz3Lm//yH5T/6E8qPvARL92m/hf+Ovo9Y+f/dMeIkE3vXr17f29vYe1q6Y/wMw3dvb+zvXr1//r4DvAH+wt7c3X9peUgVm+Q+Xgqy8tre39zef81/u0gi8hk9IZd17WEWwlBKEqixOp0JNVGJN1PmiTZwKuk/2sLi+3uXR7XvYk/vYkzofVWWXTM429ELkcBs52EENt5HDHeRwG9FZfeEPqM4U2Mk+dvwIN36IHT/Ejh9V9fno3Lais4rsbyL7W8j+JnRWyXHMTVYlmxObnMRmxDYnMTlzmzOv82TRn5N+zANIIDQt6dGSPpH0UPU8NLgo2Ezdfu6n7x7bbmlRarf0Gli4LFUGxkrsOakW378Tilz2ycWAlAE5fUpai//jiTm+mOCLKb6YosTZfJLl8eTl66ryBEmWU9oS4wylNUvlktIajKvyp41JCxGhzZCgXMOzKyjXQ6g2zvMxocJeEMpdGIMsC5Stw/RLQ6gsHU/QDSXDtsdqJ6Tjt2jp2lqrIwLlX3ijLZJHxMc/Jpm8j5AB2u+Ty4CjsuBeNuOD+IAPZofk9QydS+1NrvWvcq1/lVf7V9mIPvnCzdY6Dh/NuHvzhHu3Tnhwd4IpLULA5k6PnatDLu8O2NzuodSX+4D/PDzPPcJYQ2oqd+0qz0hNWtXLjMRUeVZvk5xuu9guIzUZZS3kPhsCKXp4egWthig5QIgeiB6IJ91cnTM4l9Ypw7kU6zK0KPGlI1SVmOt4Hl3PZxAE9P0WXb9N1+/Q8dp0/A6+PO8u7Wqr+GcRcdbZc7+15d9e8Vj7eRG8VDbl4rhWbQW5LRZi+bRtUTZPvs/yb1wJSc/v0Q/qVJcHS/VB0CPS0VN/O85ZDh4c8//92Q2OHo0Yrnr8+jTqrnEAACAASURBVG9tsb4ZLgSh8vv40dZTLShJmXKvtsjdm1aC7n78iLI+f7TUbLc3udzZZqdbCbqdziWip7hLm9JyfBhzdBBztD/jaD/maD8mTc4s0J1ewOp6m9XNDmsbHVbW2/SH0dOnY5QJ2fw++fweZT5eWMIWwk0/bhl78jr2rHNjf37Irckdbk3vcHNyh3vT+5TP8Hj5JHhU0ypCKYiEIKynWSySrCySc+uYuyolp2Xr+HSrAH8CHERxn97JFr3RFkFS2VtMbw6bMf52QTRQRCok1CGhDpbKIZEOCFVIVPcFKgAHWTFhnjwiTQ7Js2NMPoJiiixnKJuec7M0wNwpJg5G1nFclhyWOSfWMjb2hR4DJdQFgrASf4Hy8VQlCD1jUId30Ye3iIqc3/7dv017+50XuCcX8zIJvP8R+B3Ap5pr959RLY/wM6pomadRDT7a29v7t+vX/DbVMgkhZ8skPHrOf7lLI/AaXnKeubh1Ol0Sfmci8AnhN7iEHF4k/J7+kOOsxc2OavH2mIibnZ+TIaIesreJ6G8hB2diTvY2KkvUC8JYQ1KmxAtX0SqPyzlJnS+3W1dFFT3d03MLvC8Wkaj/Li8kz9NFllvucaeLT5weiGVn0bNbzunDgcPDMsQwqJIYUF3uAEo0YxQjNCM0E5TIz95NgO9pnBEoqfCERkmFEhpPKpTUVMtrh9XyD84nryOOZlaRGkVq5BPzQrSAridoK0FoHDq1yNigM4tMLMQFRVyQJsVTgyLVH50g8ggjjzDUdVkThh5BvUh8GHkE4WlZE4Re5XZoLKasc2MxpWWep9yfPOT+9BEPpgccxIcUhUE4SShC1oJVhv4KQ69PV/fAisUcDFPW72OqpSzK0nL4aEaWVg+ZK+ttLl8dcHl3yKUrffzg83GVsc5irKF0BmPNQpQbV2IeEwl20WfOvaZ0JcbahYg3zmJsiRdKTqbTap7tqWh7TMwVz+mGWblpP/7AVbty6wBPenhSo6WHlmqpXiVvkT+tvX6tuNi1aV4ajtJq1L+lFZESFKb6Pc/yGdMiJi5iZnnMtIiZ5TPiYs60mDHLY2ZF/FSXcU9qOl6Hjt+uRJ/XwZP6bFDk9LhaQ7E8WLLUfq7uDPYTuE4/C4HAU9Ux86S3OFbe4lh6546fJzWeevJYSyGxuuD+yQHjbMI4nzDOJszLJwNBedI7J/hOBeFgSRz2/B73P5jwT//Rh0xGKa+8usJv/9VXGa61F+/jnGOUjReulafWucPkaLFN22txpbPDTvcSO61LbIVbrOgVTFlF5i4KQ5EbysKeqxeFYTpKOTqIGR3NF89nWktW1tusrLdZ2+iwutFmdaNNEH56S/4XQWlLDpIjnHP1POfTJV4EArm05Evd97T8KX2Ss4FjgWBjo8f+/uQT3cPOepa3X74nutPNF9sVtjib92/Sx8qVdSw+KUnvS8oHIWJcifgimjNd2eekf4+kPbooRtE5pJDP/M1JoC8lG17AmvYYKk1fQlc4Whi8x6yZVvo43UF4PXQwxA9WiKINwmAVIySFcxTOkduS3ObkpiAzOYXJyUxObgtyU7XnNn/OvqpunUUA/+nX/yZvrL/17A/+AnhpBN6XwC6NwGt4yfk054JLZ5jRfezxvYW1z57cP29d00Fl8autfiJoLVnkHmEn+9W8w1O8sBZutXhbssqJoP3kTjR8LKeLDN+epdyJU+7MUh4m2encf4a+5nIn5JV2yJVOyO5Wn48ejBnlZTVnJy8rl626nD4WLEYCPV/T9zUD36vyQDPwNX3fY+BrQvUx0dqWsNZVa/slJVlSib40KRdtywvCL/c9a3H4F4HDgXRIBUopfE/jaY3SElWH6R6stNjZHXD56rAOc/8xn9XZc+7HcZGQFHPix+ajPj6okJn8Y62oLwIt9ZIwOx31Dgh1uBBmi5FxFSzlwbm2QPmfej3Vl4VqXl5Wi70Zs1oMzor4nAg8bS9tgZbVAIkWGi1VVReqFqfVwIle6lfyfP1p7UpqtDh7P18tC7fzou3j3Ls+CRfdJ3KTM86mteAbM84mjJYEYFUfk18wEBDpkL7uM3z0CuqDNTCCwRsC2084jseM4xmmsEirEVbRokVLtAkI8ZyPNBpbQlGvC1peECr+aQgB7W5tlVsIuc4zrXINZ7ysz4+zScbN9w/58BeH3L89wjlodTx2Xuuxfi2ivanI7ZOC0Tiz8Aqp8trCp8JneoucYsuEMj+hzEZ1frJUH/F4cK4FQp3NV5UeQngIqRf1c32n7eIZfdKrFrWSPq3w818iARqB1wi8hpeaF3kuVMLvwZMWv1PhpzSytyTcFiJuCxH1Xsq5SL9s5MZyf54tBN+dOGWcX+weFylZibWgEmvLwq3va7q+Rr0E31lZVgGSsuS8EMzSolpEXkuUqsVYXZa1MFvuk6ou66ovdSl3Zne4ObvDh+Nb3JrcJquXK+n6HV7t73Kt9wrX+lcJVXCBKKsEXFwmT1iAkzJ95mfylU+7DiBUBRRq0dYRgQpq4aBqC6taCInTuj7Xrp7Y/lQcLLY93X7ptRsbveYe0bDg094nKnGcnom/U+G3JAIn05jgoy2G+1cQjwWrUVrg+Qrf13ieQvsKz1N4y7kv0d5y/aysH9/Wq37zzb3m0/NVeH5Mk4JbN4746BeH3PnohLK0BKHm6uurvPrmGpevDfG8z2dW/TLOWUw+rgRfPrlgLnJ54RxlZ8vPFLhq4/W/Qdjd/fw+WE0j8BqB1/AS80WcCy6LcUWKaA3rCJYNLxOTvOROnCJDD5WXC2tc8BWYK/ZFYp3l/uwhH45v8dHkFh+Ob51zGXscKeSSSDuft2vRdhoNtr0oV7mWn38EtGfR3CMalvm8zwfrLEejCcpqwsCvxVkjxF5GvmrXhqIw3PnwhI9+ccjNG0fkWYn2JFeurXDtzTV2X1956d1w4Sxw1bmIxo8JRGsLysLQXX0L+ZTlWF4kL0rgfbl3u4aGhk+NCNqNm+VLTM/XvON3vnI37i8aKSSXu9tc7m7zu3wHgGk+4+bkNsaaJ4Tcs9x6GhoazpBCsj4cfNm70fBLiOcpXr2+xqvX1zDG8uDOmI9+Ua0/+tEvDpFScOXakNff3uDaG2t4FwQCexkQQoDQCKmRnF9OZzpOufHePjfenXK4P+Pf/PenXLm28iXt6SenEXgNDQ0NDS8VXb/D19fe/rJ3o6GhoaHhY1BKcnl3yOXdIf/yv/Y6+w+mfPDzA268d8CtD36O1pKrr6/y+lvrvPLaKlq/vF4s8ziv9v3dfR7eqwLfbWx3+Z3ff42dq8Mvee8+GY3Aa2hoaGhoaGhoaGj4TAgh2Nzusbnd4zv/6qs8vDvhxnv7fPDzAz74+QGer7j25hqvv7XO5d3hS7G8TZaWfLh3wI339rl3qwoks7Le5i//3jVef2ud3iD6+Dd5CWkEXkNDQ0NDQ0NDQ0PDC0MIwaUrfS5d6fM7v/8692+PeP/dfT7cO+QXP3tEGGlevb7O629tcOlK/wuNtlrkhps3jrjx3j63PzzGGkdvEPKt77zC629tsLL+1Z/+0gi8hoaGhoaGhoaGhobPBSnFwo3zd//1N7jz0TE33jvgF//iEe/+6AGtjs9rX6vE3uZ293OZZ22M5faH1f+9+f4hZWFpd3x+7VvbvPH2Butbn8///bJoBF5DQ0NDQ0NDQ0NDw+eO0pLdN9bYfWONojDc/uCY99/d590f3uen379Htx/y+luV2FvdaH8m0WWtO2c5zLOSMNK8+c4mb7xdWQ5/mUTdMo3Aa2hoaGhoaGhoaGj4QvE8xWtfW+e1r62TpSU33z/kxnsH/Oif3eGH373DYLXFG2+t8/rbGwxWWs/1ns45Ht2fcOPdA278fJ8kLqq5f2+s8frbL8/cv8+bRuA1NDQ0NDQ0NDQ0NHxpBKHm+te3uP71LZJ5sQh88r0/v8X3/vwWa5udhWWv2w/PvdY5x9F+XC9rsM90kqGUqKN3bnD1tRX0F7AI+8tEI/AaGhoaGhoaGhoaGl4KopbHO7+xzTu/sU08zfjg5we8/94+3/3HH/Hdf/wRWzu9ar7eTq+aV/fuPidHc4SAK9dW+PZf2eXam2v4wa+uzPnV/eQNDQ0NDQ0NDQ0NDS8t7W7AN759mW98+zKTUcKN9yrL3p//PzcW22xf6fP1v/QGr15fJ2p5X+Levjw0Aq+hoaGhoaGhoaGh4aWmN4j41nde4VvfeYWTw5j9B1N2rg7p9IIve9deOhqB19DQ0NDQ0NDQ0NDwlWG41ma49tVfr+7z4pc/jExDQ0NDQ0NDQ0NDQ8OvCI3Aa2hoaGhoaGhoaGho+CWhEXgNDQ0NDQ0NDQ0NDQ2/JDQCr6GhoaGhoaGhoaGh4ZeEJsjKC6I8iMmQOOcQQnzZu9PQ0NDQ0NDQ0NDQ8CtII/BeEPM/v8NskiH7Ad7VAf5uHzkIG7HX0NDQ0NDQ0NDQ0PCF0Qi8F0Tn33id4Cjl5GePyH76iOwnjyqxtzvAvzpADcMvexcbGhoaGhoaGhoaGn7JaQTeC0KGmsGvX6LY6WCTguLWmOLWiOzHj8h+XIk9f3eAtztADRqx19DQ0NDQ0NDQ0NDw4mkE3ueAjDyCr60RfG1tIfbymyPSHz8i/fEj5CDE3+1XYq/fiL2GhoaGhoaGhoaGhhdDI/A+Z86JvfmS2PvRI9IfPUIOQ/yrA7zdfiP2GhoaGhoaGhoaGho+E43A+wKRLY/grTWCt9awcUFxe0R+c0z6o4ekP3pYib3dAd7VAaoffNm72/Apcc7hnPuyd6OhoaGhoaGhoeFXkEbgfUnItkfw1jrBW+vYOD+z7P3wIekPl8Te7gDVa8Tey4IzFpuUuHmBjXPsvC7Pc+y8wMYFLimJWx5yq43e6aEvdZBB81NraGhoaGj4tNikoLgzwc4LvCs91ErURCpvaHgKzVPnS4Bs+wRvrxO8XYm9/NaYYknsqZUIb7dfWfaeQ+w556C0uMLiSosrzMfULZTmybpxCCVASpCiLguEquoogZBPaVvkcrFN1SbPbbN4rRIILauyrl/zBeNyU4m0OrlasC3K8wKXlk++UEtky0O2PPRmB9nSeIUj/uiE/MYJCFCrLfROF2+7i1prfSmfr6GhoaGh4auEmWYUt8cUt8eY/fmiPfvxI2TXryKVXxughtGXuJcNDS8fjcB7yZBtn/DtdcK317GzWuzdGpH+4CHpDyqxJ4fhkkAztSA7E2yU9vn/oQDhKfBkJbC0rOptHykFzjowDqyr3ts67HKbsXVe1bEvyDVRUIlD/bj4OxWE9b4qUQnC5b66LrQ4/x5K4tLySRFXJ4onj5sIFKIWb95qhGx7i7pseYi2j/DkE6OI6+td9h9NMEdzintTyvtTsp9UEVWFr9CXOgvBJ9v+izlmDQ0NDQ0NX2Gcc9iTlLwWdfYkBUAOQ8JvbuK90ke0vEr03RyR/Wyf7Kf7VaTya8M6eF3j9dTQ0Ai8lxjZ8QnfWSd851TsjShujikfzhZCTHgSEegq16oSM54837/cpqu2RV3JF7rPzp0JPfeYCMS4SjBe1FZanLG40oGphWpdd6YWsKberrSQldgL+p4bASKqRJoahOjt7kK0ydaZiBP60x8fIQV6vY1eb8Ovb2GzkvLBjPLelOL+lOLWmASq9RJ3eujtLnqr/cK/k191nLG43OAyU+V1wjkQtRV52cosHisrAWLJ6izOrNmL9oaGLwFn7JlreJxXHgdxjktK5CBEr7dQ621k2NzqG15enHWYg7i21E2wsxwAtdEm/EvbeK/0UN3zoi14c5XgzdWzSOUfjRbxDNRKiLc7rILXdRux1/CrSXPV/4pQib0Nwnc2vuxdeSaLB2IFwvti//epuKzEoXtSJBqL8HVlhQv1F/5gLgONvzvA3x1Uo5SjlOL+lPLelOznh2TvHoAS6K0Oeru27vWDL3yOgbMOl5xaOvPKypmZaj/0kkvtuXzJYvpEXy2iPuXnWLgcL4mzU7FmL2hzeXlOzGE+54A3gkoonroei/PiMAk1RolqICbUyEAjQrVUV9X5GHzx52TDy4tzrvI4qEWbnRW4+amIOxNyj1OdS4ri7oSsPvVlz0ett9HrLfR6GzkIm3Ot4UvFGUv5YFaJujuTavqDFOhLHYKvb+Bd6SGjj3+IOBepPM7Jb9ZTXH7wgPQHD1BrrcqNc3eAbH/BDyW/5LjcYKYZdpJhpzl2ktX1HFeY6v4W6mowParvd1FdDzWibhO+auZSfg58ZoF3/fr1PwD+LuABx8Af7e3tfXT9+vU3gf8FWAWOgL+xt7f3fv2ap/Y1NHxaTh+ovwoWMCEEahhV8wbe2cCVlvLhbCH40u/dJwVE28Pb7qJ3uuhLXaSvPtP/daV95hxDOy9wSQEvWhOdutwq8fS8nnvpyictbh/r+uvJSjj5CuErZN+r3Gv9pXSurkFyZm227vnKxoF7rL1uO1c2dSRV41BSUk4z7GSOzcoLXYHPfY5QLwTfOfEXqlocVg/wIqjz5sb4lcQV5ky8LeVnlrjiyfNeS2T7/2/v3mIkue46jn/r1pe5z453ba/ttTfgnAjLCoRYICdBAuUhL5ECRIAlk7xEIgiCeEACIYF4gBCFPAVsHClChBjlASEFXhA8RWAhICExOIpybIVdO+waZ3Z3ZufW16ri4Zzqru7p2Yunt3um+/eRWlV1qmfmaPrMmfOv869TCeFiQrK+4i5WLVZ8WWUg6yDvZqTXDuhuHtDd3HeZA9/bct8nCYnvW+gFfdHZBS0ENUF5JyXb69AKItKdVj+DoJxNEAYu02SG/r7zdkrnyg6dN3boXNlxfWESkjy0QnJhheShFYJj/I8LF/tZT+lui04R7H3jKs1vXCU6t0jl4hrJo6t3FDwKZK1uL3jLdlukO22yXRfQDa9JENRjwpUqycPuc8yaXfKm69vS6wfu/aP+lYdBKfiLCWuJ3xZBYNI7p2Dwzh2rRzfGrOMCtaetta8aY54F/hz4EPAC8Jy19kVf/gXgZ/yX3uqcyNwJ4pDk4RWSh1cAyPbavWCvfXmb9ms33GItZxdIzrt0zmij3rsKn+e5C4hKgdpA4Lbv9vN2eviHJ/1FYpLzS6V7DCsEC7EbNNZi1zH30md9MJP61Npiv9svG34PvZnUEdsi7TbNXepwJXI/t9oPyA4FbEXQlkQnejbi7NllNjd3e8d5mrnPqtkla3V7+3mrS9ZMyVtdd3zQobPVcP8Uj5qFDOgHerWYsF6kGLvPLayPJ91Y7l6e5+T7HdIdd4U73WlxpZXS3GqQ74/4Wwxwn9ViQrSxQPJoKWhbckHc3Qxugjh02QAPLPXqk+22SX3Al27u03rlrf4s32qV+OwiUW+Wb/LZA0fJfaB7kv/Ohw3Mbuy03X4xu+EHxru3+R7AyMDP7QNhSBBydAZBkWpeiUYMml1/ca/7hWLly84bN+m+uQdZTlBz2SzJhVXiB5fuyUXZaLlK9OQ5ak+eI73ZonN5m/alLRr/foXGf1whfmCJ5DEf7M3xxY1i7FC0zXI7zXZb5K3BfipYSIhWqm6GdaVKuFwhWnbbILl1cJ5nee//W9Yobzu94/ygQ+d64/bBoG/HYT0hXEoIlyq9V7CQnJi+a5qC4zyvyxjzFPCX1ton/PEZ3Izc/cCrwIa1NjXGRL78cdy1/JHnrLWbd/BjHwMuXb++5xb7OEGGB3Iyv8bZFnr3J/jFWtLrDcAtABOuVnvplKOCgKAeD9xTGC4O3mMYLiS37ZTleI7bFnopqq3UBYTN7mCA6IPCrNElb3SObgsVv2DQUJsIfCAYLrjUmdM0iJ62XhqlD+B6g3m/PzADF4dU1utk1cj9HS654C0sgrcp/O7zTkr3WoN0c98HfQf9AV0S+nuI+zN9x5ldGfi5We5m5xvdfptudv0V/8P7RZ2CWtxrp2E96fdv9dIFjXo8sSyOI2c3dkYMjP3sRuQHxeFShZWVOjvbDfIsg4w7yybIBxc1y7NS1kA2lEHgsw5umTkQh6X0OX/7QikQ7KXY1WJ37/4dDJzdypc7fuXLfcDdZpJcWHX3051dnFo/k241aF/epnNpm2y3DQHE55fdzN4jq2Nr43drLP8nioumWf/iau9Ca+YuxOaN4qJTaSZu6GJTsJj4dlp16d3Lfn+5MrELhb2L1o0uWbPjt13yckDY6JI1OodT1cPABX2Lld7f2kAAWItPdAB4N20hDAM2NpYALgKXy+eOG+CtAv8DfMha+3VjzKeAzwPvBf6qCPz8e78DPIsL8Eaes9Z+8w5+7GPApbddaZFTrnvQ4eD1LQ4ubdPdaRItVYiXqsTL5W2FeLFyKtJVZbzyPCdrpXT3WnT32qR7bbq9ly/bd8ejrpBGi4lrR0sV37aKly9brLj7LAOfQlbMGsxYOllZ2urSudGgvd1w260mna0Gna0GWXlwFAYkazUq63WS9TqVM3V3fKbufm8n/PeT5zmdrSbNqzs0ru7SvLpD+1p/afrKfQvUzi9TP79C7fwyybp7Dlme52TNLulBh/SgQ7fR6e2nBx3S4ePm0WngYT0mridEC/7l9wG6+74973dcOz4Y3YbDWky8WOm1V7dN+mW+fwzv4OJW2ujQ2W7S9p93Z7vpjrcbZEMDy3i5QrJWJ1mvkazVqazVSNbrJKu1Y6fXH1fWzUgP2u73v9+he8R+etAmHXFvJ0AQBUQL/ne5kPT2owX3u23faLD32nXamy6oq5xdYOmHN1h6fIPK2cUT1f7zPKf1g332vrvJrr1Gd6dFEAUsXFxn+V1nWXzHmbv6zPLcZaIUrywtPYoqzchK5/Lu4eM8Ld6X+wXn+gvP5Wn/fD50vrfY3N1MeAQQr1RdP7Xm+qhkvUZlrU68WiM8ZdkeWTeju9Okc7NF52aT7k2/v+P2h9tzEIckqzXi1SrJas29VqrEfj86nYtSjTfAAzDGfBD4A6AG/APw68BHgOfvZYCnGTw5ydQWpHBS20KRLtNP5e327sEsp/gOz0TcVrHoTHm/CP5Kx4BLIWPEuXLwGIeDz8gcehxKrywOS49FGVFWPFbliAV/8m7mZ2GKmTg/I7PTOnSvSbhUIVyp9Gdkitdi5ZYzEye1LdxK3k7pXjvws3wHbpbPB7VBJYIwIG8dkU7l3xP4+0p795fWYsLaiPK7XGhooA03StuGb9PlK/yjxgtJ2E9r9ulexEFpVu6I2Y3lai89LVyp9lPU7nJgfFLbQ57l/ZnUoRS6Q7MoQ6l00bkFP1N3elawzPOc9NoB7UvbdC5vu/YSBcQPLhNEQekWhMO3GBRlx31EVBCH5AGHFzErniccldYYKD8/2D+ruDhf3h/4Xv5ZxkEtdrNYc3Tx193z2u6/dt029ceHZreTkGi5QrhU9bN+CeFKlfj88kQuUpyIGbxhxpj7gdcBA/wXStGUOaW2IIXT3hbyNHMDudIiPC4VDJcOltPbz6E/0Cmdy/Oh99M/zktfX94OrIpbfkxKMajqZm9vMaCA0rMy3QAo72bk+53Bt5VT6vyrSK97u4Oj094WwM8Q32z1UjqBEcFbf/8kpPwO3KPc6JTSmftpzUVgSJb3U7t8mlrU2x/vwHhW2kORMh5Uo1O/eEme56Rv7dO+vO3uGSwHXXE5+Co/h7cIwkaXHf7a8kUqd9Hp3LmVU98WTqM8d+niw8Ff+VXc8rD4wYskD63c8zqNK8AbxyqaD1hr/88YEwKfBl6w1r5ujHkZeAZ40W+/VQRwtzonIiInRxCFREsVWKpMuyqH9J6h2S0W8hl6dmb5USm9/X7AWJQRBYOB3HJ1avfinHRBEBCt1YjWavD4xrSrc0eCwM1cUIuJqB/5vuJCxEkISk+L8u92FgRBMLA4kcy2IAj8itUxbCwcOl/cZ503U8K10zEjXRjHX+QfGmPeB1SAfwJ+x5d/EviSMeb3gS3gY6WvudU5ERGR2wrCAPyKqiLHFZTTh0Vk7gVBQFBP4BTOTB87wLPWfuKI8u8CP3G350REREREROTtmZ+7LEVERERERGacAjwREREREZEZoQBPRERERERkRijAExERERERmREK8ERERERERGaEAjwREREREZEZoQBPRERERERkRijAExERERERmRHHftD5FEQAYRhMux4jndR6yeSpLUhBbUEKagtSpvYgBbUFKdxpWyi9Lxo+F+R5PsYqTcT7gX+ZdiVERERERESm7APAS+WC0xjgVYGngDeBdMp1ERERERERmbQIeBD4OtAqnziNAZ6IiIiIiIiMoEVWREREREREZoQCPBERERERkRmhAE9ERERERGRGKMATERERERGZEQrwREREREREZoQCPBERERERkRmhAE9ERERERGRGxNOuwCwwxrwT+BKwAVwHPmatfW26tZJpMMZcBpr+BfDb1tp/nFqFZGKMMZ8Dfh54DHjSWvttX67+YQ7doj1cRn3E3DDGbABfBn4IaAOvAb9ird00xvwk8AWgDlwGnrXW/mBadZV77zbtIQdeATL/9l+21r4ynZrKJBhjvgpcxH3me8CnrLUvj2PcoBm88XgBeM5a+07gOVyHLfPro9baH/UvDdzmx1eBnwJeHypX/zCfjmoPoD5inuTAZ621xlr7JPA94DPGmBB4Efg13zf8M/CZKdZTJmNkeyidf7rUNyi4m30ft9a+21r7Y8DngL/w5cceNyjAOyZjzDngPcBXfNFXgPcYY85Or1YiMmnW2pestd8vl6l/mF+j2oPMH2vtDWvt10pF/wY8Cvw40LTWvuTLXwB+YcLVkwm7RXuQOWStvVk6XAWycY0bFOAd3yPAFWttCuC3V325zKe/Nsb8tzHmeWPM2rQrI1Ol/kFGUR8xh/ys3a8Cfw9coDS7a629BoTGmDNTqp5M2FB7KHzNGPOyMeaPjTHVKVVNJsgY80VjzBvAHwEfZ0zjBgV4IuP1AWvtu4GngAD4synXR0ROFvUR8+tPcffZSAhKggAAAdRJREFU6DMXONweLlhr34tL7f4R4PemVTGZHGvtJ6y1F4DfBf5kXN9XAd7xfR94yBgTAfjteV8uc6ZIybLWtoDngfdNt0YyZeofZID6iPnkF915HPhFa20GvEEpNc8Ycx+QWWtvTKmKMkEj2kO5b9gBvoj6hrlirf0y8NPA/zKGcYMCvGPyK169DDzji54BvmWt3ZxerWQajDGLxphVvx8Av4RrGzKn1D9ImfqI+WSM+TTunruP+MAe4D+BujHm/f74k8DfTKN+Mlmj2oMxZt0YU/f7MfBR1DfMNGPMkjHmkdLxh4EbwFjGDUGe5+Oq69wyxrwLt5zpOrCFW87UTrdWMmnGmHcAfwtE/vUd4DestW9OtWIyEcaYzwM/BzwAXAOuW2ufUP8wn0a1B+DDqI+YK8aYJ4BvA68CDV98yVr7s8aYp3Gr49XoPybhralUVCbiqPYAfBbXFnIgAf4V+E1r7d406in3njHmfuDvgEUgxQV3v2Wt/eY4xg0K8ERERERERGaEUjRFRERERERmhAI8ERERERGRGaEAT0REREREZEYowBMREREREZkRCvBERERERERmhAI8ERERERGRGaEAT0REREREZEYowBMREREREZkR/w/0L/4SVaStnwAAAABJRU5ErkJggg==\n",
      "text/plain": [
       "<Figure size 1080x360 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "accuracies = [calculate_accuracy(df['Close'].iloc[-test_size:].values, r) for r in results]\n",
    "\n",
    "plt.figure(figsize = (15, 5))\n",
    "for no, r in enumerate(results):\n",
    "    plt.plot(r, label = 'forecast %d'%(no + 1))\n",
    "plt.plot(df['Close'].iloc[-test_size:].values, label = 'true trend', c = 'black')\n",
    "plt.legend()\n",
    "plt.title('average accuracy: %.4f'%(np.mean(accuracies)))\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
