# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 08:34:55 2021

@author: seaso
"""

from tabulate import tabulate

table = [['Condition', 'Definition', 'Percent of AFABs affected'], ['Endometriosis', 'Tissue that grows outside uterus', 11], ['PCOS', 'Irregular periods and cysts due to hormones', 10], ['Intersticial Cystitis', 'Chronic Urinary/Pelvic Pain', 2]]
print(tabulate(table))


"print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))"