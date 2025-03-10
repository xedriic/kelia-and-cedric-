# -*- coding: utf-8 -*-
"""Untitled8.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/17721cjU5hOwxOQE1jea6U_A0URyhxA6B
"""

def sentence_operations(sentence1, sentence2):
  set1 = set(sentence1.lower().split())
  set2 = set(sentence2.lower().split())

  intersection = set1.intersection(set2)
  union = set1.union(set2)

  return intersection, union


file1 = "this is sample text about legal sample issues"
file2 = "This text legal discusses legal and ethical this issues in legal computing"

def  jaccard_similarity(file1, file2):
  set1 = set(file1.split())
  set2 = set(file2.split())
  intersection = set1.intersection(set2)
  union = set1.union(set2)
  similarity = len(intersection) / len(union) if len(union) != 0 else 0
  common_words = list(intersection)

  return similarity, common_words

intersection, union = sentence_operations(file1, file2)
similarity,common_words = jaccard_similarity(file1, file2)
print("intersection:", intersection)
print("Union:", union)
print("Similarity:", similarity)
print("Common words:", common_words)