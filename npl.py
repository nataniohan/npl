import numpy as np
import math 
import re 
import pandas as pd
from bs4 import BeautifulSoup
from google.colab import drive
import zipfile
import seaborn as sns
import spacy as sp
import string
import random
import matplotlib.pyplot as plt  


import tensorflow as tf
tf.__version__
from tensorflow.keras import layers
import tensorflow_datasets as tfds

#drive.mount("/content/drive", force_remount=True)

#path = '/content/drive/MyDrive/PNL_DATASET/trainingandtestdata.zip'
zip_object = zipfile.ZipFile(file = path, mode = 'r')
zip_object.extractall('./')
zip_object.close()

cols = ['sentiment', 'id', 'date', 'query', 'user', 'text']
#train_data = pd.read_csv('/content/trainingandtestdata/train.csv', header = None, names = cols, engine = 'python', encoding = 'latin1')

train_data.shape

train_data.head();

import numpy as np
import math 
import re 
import pandas as pd
from bs4 import BeautifulSoup
from google.colab import drive
import zipfile
import seaborn as sns
import spacy as sp
import string
import random
import matplotlib.pyplot as plt  


import tensorflow as tf
tf.__version__
from tensorflow.keras import layers
import tensorflow_datasets as tfds

#drive.mount("/content/drive", force_remount=True)

#path = '/content/drive/MyDrive/PNL_DATASET/trainingandtestdata.zip'
zip_object = zipfile.ZipFile(file = path, mode = 'r')
zip_object.extractall('./')
zip_object.close()

cols = ['sentiment', 'id', 'date', 'query', 'user', 'text']
#train_data = pd.read_csv('/content/trainingandtestdata/train.csv', header = None, names = cols, engine = 'python', encoding = 'latin1')

train_data.shape

train_data.head();

sns.countplot(train_data.sentiment);
