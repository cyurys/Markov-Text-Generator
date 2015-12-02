#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
#import re
import json
import os  # listdir, path.join, path.isdir
#from collections import Counter

# punctuation to remove
RM_PUNCT = u"'\"”„+-—:;()"

# Markov random Text Generator
class MTG(object):
    def __init__(self, mtg_filename=None):
        if mtg_filename != None:
            with open(mtg_filename, 'r') as in_file:
                self.MC = json.load(in_file)
        else:
            self.MC = {}
            
    def train_from_seq(self, word_seq):
        for w1, w2, w3 in self.triples(word_seq):
            key = w1 + '+' + w2
            if key not in self.MC:
                self.MC[key] = []
            self.MC[key].append(w3)
            
    def train_from_text(self, text, remove=RM_PUNCT):
        text = text.replace('.', ' . ').replace(',', ' , ')
        word_seq = text.strip().split()
        word_seq = [word.strip(remove) for word in word_seq 
                    if len(word.strip(remove)) != 0]
        self.train_from_seq(word_seq)
        
    def train_from_file(self, text_file, remove=RM_PUNCT):
        with open(text_file, 'r') as f:
            text = f.read()
        self.train_from_text(text, remove=remove)
    
    # recursively train from files in directory
    def train_from_corpus(self, corpus_dir="corpus", verbose=False):
        textdirs = [corpus_dir]
        while textdirs != []:
            textdir = textdirs.pop()
            for textfile in os.listdir(textdir):
                path = os.path.join(textdir, textfile)
                if os.path.isdir(path):
                    textdirs.append(path)
                elif path.endswith('.txt'):
                    if verbose:
                        print "Processing file " + path
                    self.train_from_file(path)
        if verbose:
            print "Processing done!"
    
    # add data form another MTG
    def __iadd__(self, other):
        for key, value in other.MC.items():
            if key not in self.MC:
                self.MC[key] = []
            self.MC[key].extend(value)
        
    def save(self, mtg_filename):
        with open(mtg_filename, 'w') as out_file:
            json.dump(self.MC, out_file)        
    
    # generate all triples to build MC
    def triples(self, word_seq):
        if len(word_seq) < 3:
            return
        for i in range(len(word_seq) - 2):
            yield (word_seq[i], word_seq[i+1], word_seq[i+2])
            
    def choose_start_words(self, first_word=None, second_word=None):
        if second_word != None:
            return first_word, second_word
        elif first_word != None:
            if len(self.MC['.' + '+' + first_word]) != 0:
                second_word = random.choice(self.MC['.' + '+' + first_word])
            elif len(self.MC['.' + '+' + first_word.capitalize()]) != 0: 
                second_word = random.choice(self.MC['.' + '+' + first_word.capitalize()])
            else:
                return self.choose_start_words(None, None)
            return first_word, second_word
        else:
            first_word = random.choice(self.MC[random.choice(self.MC.keys())])
            return self.choose_start_words(first_word, second_word)
                  
    def generate_text(self, first_word=None, second_word=None, size=10000):
        w1, w2 = self.choose_start_words(first_word, second_word)
        gen_words = [w1.capitalize()]
        while not (len(gen_words) > size and w2 == '.'):
            gen_words.append(w2.capitalize() if (w1 == '.') else w2)
            w1, w2 = w2, random.choice(self.MC[w1 + '+' + w2])
        gen_words.append(w2)
        text = ' '.join(gen_words)
        text = text.replace(' ,', ',').replace(' .', '.')
        return text
