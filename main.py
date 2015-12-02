# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 15:48:44 2015

@author: yury
"""

import markovtextgen as mg

def train_and_generate():
    mc = mg.MTG()
    mc.train_from_corpus(corpus_dir="corpus/dickens", verbose=True)
    text = mc.generate_text(size = 1000)
    print text
    return mc

def train_and_save():
    mc = mg.MTG()
    mc.train_from_corpus(verbose=True)
    mc.save("stats.txt")
    return mc
    
def load_and_generate():
    mc = mg.MTG("stats.txt")
    text = mc.generate_text(size = 1000)
    print text
    return mc

def main():
    #mc = train_and_save()
    #mc = load_and_generate()
    #mc = train_and_generate()
    return mc
    
main()