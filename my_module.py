#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 04:11:16 2021

MODULE my_module

@author: unknown
"""

def format_list_scientific(listtoformat,precision):
    for i in range(len(listtoformat)):
        listtoformat[i] = format(listtoformat[i],'.'+str(precision)+'E')
        
def new_func():
    print("New!")
    
