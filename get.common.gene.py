#!/usr/bin/env python
# -*- coding:utf-8-*-

import os 
import sys

common_gene = []
dict = {}
input_file = open('common.gene.txt','r')
GSE3630 = open('GSE3630.txt','r')
GSE65144 = open('GSE65144.txt','r')
common_gene_output = open('common.gene.expression.txt','w')
for line in input_file.readlines():
	line = line.strip()
	common_gene.append(line)
input_file.close()

for line in GSE3630.readlines():
	line = line.strip()
	items = line.split('\t')
	gene_symbol = items[7].strip()
	if gene_symbol in common_gene:
		dict.setdefault(gene_symbol,[]).append(items[1])
GSE3630.close()

for line in GSE65144.readlines():
	line = line.strip()
	items = line.split('\t')
	gene_symbol = items[7].strip()
	if gene_symbol in common_gene:
		dict.setdefault(gene_symbol,[]).append(items[1])
GSE65144.close()

for key in dict:
	common_gene_output.write(key+'\t'+ dict[key][0] + '\t' + dict[key][1] + '\n')
common_gene_output.close()




		
	
	
	
	
	
	
	
	

