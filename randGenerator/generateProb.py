import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
warnings.simplefilter(action='ignore', category=UserWarning) # to surpress future warnings
import pandas as pd
import sys
import textstat
import numpy as numpy
import math
import gensim
from pprint import pprint
import os
import glob
from string import ascii_lowercase
#import Use_NN as nn
import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split , KFold , LeaveOneOut , LeavePOut , ShuffleSplit , StratifiedKFold , GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestRegressor , VotingClassifier , RandomTreesEmbedding, ExtraTreesClassifier , RandomForestClassifier , AdaBoostClassifier , GradientBoostingClassifier
from sklearn.model_selection import cross_val_score, cross_val_predict
from sklearn.svm import LinearSVC , SVC
from sklearn import preprocessing
from sklearn.metrics import f1_score , recall_score , accuracy_score , precision_score , jaccard_score , balanced_accuracy_score, confusion_matrix
from mlxtend.plotting import plot_decision_regions, plot_confusion_matrix
from matplotlib import pyplot as plt
from sklearn.neighbors import KNeighborsClassifier , RadiusNeighborsClassifier
import nltk
from nltk.tokenize import RegexpTokenizer
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from imblearn.pipeline import make_pipeline
from collections import Counter
from imblearn.over_sampling import SMOTE
from imblearn.under_sampling import NearMiss
import string
import xgboost as xgb




def read_csv(filepath):
    #parseDate = ['review_date']
    #dateparse = lambda x: pd.datetime.strptime(x, '%Y-%m-%d')
    #colName = ['customer_id','product_category', 'review_id', 'star_rating','helpful_votes','total_votes','vine','verified_purchase','review_body','review_date']
    #df_chunk = pd.read_csv(filepath, sep='\t', header=0, chunksize=500000, error_bad_lines=False,parse_dates=parseDate, dtype=column_dtypes, usecols=colName, date_parser=dateparse)
    df_chunk = pd.read_csv(filepath, sep=',', header=0, encoding = "ISO-8859-1")
    #df_chuck = df_chuck.fillna(0)
    return df_chunk


def read_txt(filepath):
	f = open(filename,'r')
	x = f.readlines()
	f.close()
	return x


def getAllTxtFiles(path):


if __name__ == '__main__':
