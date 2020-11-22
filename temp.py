# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#load libraries for data manipulation and visualization
import pandas as pd
import numpy as np
# text/file processing libraries
import string
import re
import sys
from nltk.corpus import stopwords
from itertools import chain
# warnings
import string
import warnings
warnings.filterwarnings('ignore')

from tqdm import tqdm
from nltk.tokenize import word_tokenize

from tensorflow.keras.preprocessing.text import Tokenizer
import tensorflow as tf
from tensorflow.keras.layers import Embedding
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.preprocessing.text import one_hot
from tensorflow.keras.layers import LSTM,GRU
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Flatten,Activation, Dropout
from tensorflow.keras.layers import Conv1D, MaxPooling1D, GlobalMaxPooling1D 
from sklearn.model_selection import train_test_split

from sklearn.linear_model import SGDClassifier

from sklearn.svm import LinearSVC


from gensim.models import Doc2Vec
from sklearn import utils
from sklearn.model_selection import train_test_split
import gensim
from gensim.models.doc2vec import TaggedDocument
import re


