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

def read_dataset(File_Name, Split_Symbol):
	f = open(File_Name,'rU')
	data = f.read()
	data = data.split('\n')
	line = data.__len__()
	if line != 1:
		while len(data[data.__len__()-1]) == 0:
			data = data[:-1]
			line -= 1
	for i in range(len(data)):
		data[i] = data[i].split(Split_Symbol)
		if data[i][len(data[i])-1] == '':
			data[i] = data[i][:-1]
	print "data[0]=",data[0]
	f.close()
	return data

def Convert2FloatArray(d, array):
	print "start to convert to float"
	if array == 1:
		for i in range(len(d)):
			if 'on' in d[i]:
				d[i] = 1
			elif 'off' in d[i]:
				d[i] = 0
			elif 'stand' in d[i]:
				d[i] = 0.1
		d = [float(i) for i in d]
		
	if array == 2:
		for i in range(len(d)):
			#if d[i][len(d[i])-1] == '\r':
			#	d[i] = d[i][:-1]
			for j in range(len(d[i])):
				if 'on' in d[i][j]:
					d[i][j] = 1
				elif 'off' in d[i][j]:
					d[i][j] = 0
				elif 'stand' in d[i][j]:
					d[i][j] = 0.1
		for i in range(d.__len__()):
			for j in range(len(d[i])):
				try:
					d[i][j] = float(d[i][j])
				except:
					pass
					print i," ",j
		d = [[float(j) for j in i] for i in d]
		
	print 'start to convert to float...done...'
	return d