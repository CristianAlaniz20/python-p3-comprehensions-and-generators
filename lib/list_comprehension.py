#!/usr/bin/env python3

def return_evens(num_list):
    even_list = [number for number in num_list if number % 2 == 0]
    return even_list

def make_exclamation(sentence_list):
    exclamated_list = [sentence + "!" for sentence in sentence_list]
    return exclamated_list