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
import string


LOCATIONOFFILES="/Users/pradeesh/Library/Developer/Xcode/DerivedData/randGenerator-dhxzdwxjidiwkmaawdpcjdbgzfpu/Build/Products/Debug/"
TRUTHFILELOCATION = "/Users/pradeesh/Documents/LYNParser/text_analyzer/Code/train_22.csv"
COLUMNNAME = "Label"
STATE = 21 # so the experiments can be reproduced for future work
ScoreCalculation = 0.56



def FoldValidate(original,truth,file,iter=3):
	Val = StratifiedKFold(n_splits=iter, random_state=STATE, shuffle=True) # DO OUR FOLD here , maybe add the iteration
	truth = numpy.asarray(truth) # convert to numpy array
	original = numpy.asarray(original)
#	print("Truth is",truth.shape)
#	print("Original is",original.shape)
	scores = []
	tns = [] # true neg
	fps = [] # false positive
	fns = [] # false negative
	tps = [] # true positive
	for train_index,test_index in Val.split(original,truth):
		#scores.append(classifier.score(x_output, truth[test_index]))
		tn, fp , fn , tp = confusion_matrix(original[test_index], truth[test_index]).ravel()
		score = accuracy_score(original[test_index],truth[test_index])
		tns.append(tn)
		fps.append(fp)
		fns.append(fn)
		tps.append(tp)
		scores.append(score)

##	print("TP is,",numpy.mean(tps))
##	print("FP is,",numpy.mean(fps))
##	print("FN is,",numpy.mean(fns))
##	print("TN is,",numpy.mean(tns))
##	print("TP,FP,FN,TN is",numpy.mean(tps),numpy.mean(fps),numpy.mean(fns),numpy.mean(tns))
	if (numpy.mean(scores) > ScoreCalculation):
		print("Seed Value is ",file)
		print("TP,FP,FN,TN is",numpy.mean(tps),numpy.mean(fps),numpy.mean(fns),numpy.mean(tns))
		print("Avg Accuracy is,",numpy.mean(scores))




def getTruthLabel(filepath,columnName):
		df = read_csv(filepath)
		truthLabel = df[columnName].values
		return truthLabel


def read_csv(filepath):
		#parseDate = ['review_date']
		#dateparse = lambda x: pd.datetime.strptime(x, '%Y-%m-%d')
		#colName = ['customer_id','product_category', 'review_id', 'star_rating','helpful_votes','total_votes','vine','verified_purchase','review_body','review_date']
		#df_chunk = pd.read_csv(filepath, sep='\t', header=0, chunksize=500000, error_bad_lines=False,parse_dates=parseDate, dtype=column_dtypes, usecols=colName, date_parser=dateparse)
		df_chunk = pd.read_csv(filepath, sep=',', header=0, encoding = "ISO-8859-1")
		#df_chuck = df_chuck.fillna(0)
		return df_chunk


def calculateTruth(truthlabel):
#	truthlabel = numpy.asarray(truthlabel)
	noOf1 = 0
	noOf0 = 0
	mean = []
	Val = StratifiedKFold(n_splits=3, random_state=STATE, shuffle=True) # DO OUR FOLD here , maybe add the iteration
	for train_index,test_index in Val.split(truthlabel,truthlabel):
		labelled = truthlabel[test_index]
		noOf0 = numpy.count_nonzero(labelled == 0)
		noOf1 = numpy.count_nonzero(labelled == 1)
		avg = noOf1/(noOf0+noOf1)
		print(noOf0+noOf1)
		mean.append(avg)

	print(numpy.mean(mean))









def read_txt(filepath):
	os.chdir(LOCATIONOFFILES) ## just making sure we change it , i think it shouldn't be repeated , but yeah 
	x = numpy.loadtxt(filepath) #numpy handles \n into array
	#f = open(filepath,'r')
	#x = f.read().splitlines()
	#f.close()
	return x

# Inspired By https://stackoverflow.com/questions/3964681/find-all-files-in-a-directory-with-extension-txt-in-python
def getAllTxtFiles(path):
		os.chdir(LOCATIONOFFILES)
		files = glob.glob("*.txt")
		return files

if __name__ == '__main__':
		files = getAllTxtFiles(LOCATIONOFFILES)
		truthLabel = getTruthLabel(TRUTHFILELOCATION,COLUMNNAME)
		calculateTruth(truthLabel)
		#for file in files:
		#		generated = read_txt(file)
				#print(file)
		#		FoldValidate(generated,truthLabel,file)


