#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tues Mar 28 13:56:18 2023
@author: ashutosh
"""

from pymatgen.core import Structure
structure = Structure.from_file("POSCAR")

f1 = open('POSCAR','r')
f2 = open('POSCAR_cart','w')

i=0
while True:
    line = f1.readline()
    i+=1
    if i < 8:
        f2.write(line)    
    if i == 8:
        f2.writelines('Cartesian \n')
    if i > 8:
        break    
f1.close()

for i in range(structure.num_sites):
    f2.writelines("{:14f} {:14f} {:14f}\n".format(structure.cart_coords[i][0],structure.cart_coords[i][1],structure.cart_coords[i][2]))  
f2.close()
