# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 17:49:00 2019
@author: Kellie Higa
"""
#%%
with open('rosalind_ini5.txt') as dataset:
    lines = dataset.read().splitlines()
    print(lines)

    with open('rosalind_out5.txt', 'w') as output:
        i = 1
        while i < len(lines):
            output.write(str(lines[i]) + '\n')
            i += 2