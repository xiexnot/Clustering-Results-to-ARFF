# -*- coding: utf-8 -*-

import os
import sys
import math
import json
from collections import Counter

from tools_external_files import *

def count_individual_label(label)
	label_count = list(Counter(label))
	label_count.sort()
	return label_count

try:
	decoded = read_json(sys.argv[1])
except:
	print "help information:"
	print "python convert.py [filename of configure json file]"
	exit()

instance = read_dataset(decoded["dataset_filename"],'\t')

instance = Convert2FloatArray(instance,2)

if "clustering_filename" in decoded:
	label = read_clustering(decoded["clustering_filename"])
if "label_filename" in decoded:
	label = read_annotation(decoded["label_fielname"])
label_count = count_individual_label(label)


feature = read_feature(decoded["feature_filename"])

FILE = open(decoded["ARFF_filename"],"rU")

if "name" in decoded:
	FILE.write("@RELATION "+str(decoded["name"])+"\n")
else:
	FILE.write("@RELATION test"+"\n")

state = []
for i in range(len(feature)):
	state.append("REAL")
	if "people" in feature[i][1] or "audio" in feature[i][1]:
		state[i] = "INT"
	FILE.write("@ATTRIBUTE "+str(feature[i][1])+state+"\n")

FILE.write("@ATTRIBUTE class {")
# to be continued.
for i in range(label_count.__len__()):
	FILE.write(str(label_count[i]))
	if i != label_count.__len__()-1:
		FILE.write(',')
FILE.write("}\n\n")

FILE.write("@DATA\n")

for i in range(instance.__len__()):
	for j in range(len(instance[i])):
		if state[j] == "REAL":
			FILE.write(str(round(instance[i][j],1))+",")
		else:
			FILE.write(str(instance[i][j])+",")
	FILE.write(str(label[i])+"\n")

FILE.close()