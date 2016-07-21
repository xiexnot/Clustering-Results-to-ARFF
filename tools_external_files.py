from math import log
from collections import Counter
import json

def find_max(X):
	result = X[0]
	for i in range(X.__len__()):
		if result < X[i]:
			result = X[i]
	return result

def find_min(X):
	result = X[0] 
	for i in range(X.__len__()):
		if result > X[i]:
			result = X[i]
	return result

def read_json(filename):
	FILE = open(filename,'rU')
	rawdata = FILE.read()
	
	decoded = json.loads(rawdata)
	
	FILE.close()
	return decoded

def read_clustering(filename):
	FILE = open(filename,'rU')
	clustering = FILE.read()
	clustering = clustering.split("\n")
	if clustering[clustering.__len__()-1] == "":
		clustering = clustering[:-1]
	FILE.close()
	for i in range(clustering.__len__()):
		clustering[i] = int(clustering[i])
	return clustering

def read_annotation(filename):
	FILE = open(filename,'rU')
	annotation = FILE.read()
	annotation = annotation.split("\n")
	if annotation[annotation.__len__()-1] == "":
		annotation = annotation[:-1]
	FILE.close()
	return annotation

def read_feature(filename):
	FILE = open(filename,'rU')
	feature = FILE.read()
	feature = feature.split('\n')
	FILE.close()
	if (feature[feature.__len__()-1])=="":
		feature = feature[:-1]
	for i in range(feature.__len__()):
		feature[i] = feature[i].split("\t")
		feature[i][0] = int(feature[i][0])
	return feature