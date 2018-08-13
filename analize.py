import pandas as pd
import numpy as np
import re

import matplotlib.pyplot as plt
from pylab import *

adata = pd.read_csv('D:\lastdata.csv', encoding='utf-8', lineterminator='\70', header=22,
                    names=["id", "bdate", "books", "city_id", "city_title", "university", "faculty",
                           "sex", "graduation", "alcohol", "life_main", "people_main", "political", "smoking",
                           "langs_count",
                           "relation", "text", "all_words", "uniq_words", "ttr", "mltd", "hdd"])


def deleteNaN(list):
    list = list[~np.isnan(list)]
    return list


def draw_hist(list1, list2, label1, label2, name):
    plt.hist(list1, histtype='step', label=label1, density=True)
    plt.hist(list2, histtype='step', label=label2, density=True)
    plt.legend(loc='upper right')
    plt.title(name)
    plt.show()
    return 1;


ttr_m = adata[adata.sex == 2].ttr
ttr_f = adata[adata.sex == 1].ttr

mltd_m = adata[adata.sex == 2].mltd
mltd_m = mltd_m[~np.isnan(mltd_m)]

mltd_f = adata[adata.sex == 1].mltd
mltd_f = mltd_f[~np.isnan(mltd_f)]

hdd_m = adata[adata.sex == 2].hdd
hdd_m = hdd_m[~np.isnan(hdd_m)]

hdd_f = adata[adata.sex == 1].hdd
hdd_f = hdd_f[~np.isnan(hdd_f)]

draw_hist(ttr_f, ttr_m, 'female', 'male', 'ttr')
draw_hist(hdd_f, hdd_m, 'female', 'male', 'hdd')
draw_hist(mltd_f, mltd_m, 'female', 'male', 'mltd')

books_yes_ttr = adata[adata.books == adata.books].ttr
books_no_ttr = adata[adata.books != adata.books].ttr

draw_hist(books_yes_ttr, books_no_ttr, 'yes', 'no', 'books_ttr')

books_yes_mltd = deleteNaN(adata[adata.books == adata.books].mltd)
books_no_mltd = deleteNaN(adata[adata.books != adata.books].mltd)

draw_hist(books_yes_mltd, books_no_mltd, 'yes', 'no', 'books_mltd')

books_yes_hdd = deleteNaN(adata[adata.books == adata.books].hdd)
books_no_hdd = deleteNaN(adata[adata.books != adata.books].hdd)

draw_hist(books_yes_hdd, books_no_hdd, 'yes', 'no', 'books_hdd')

univer_yes_ttr = adata[adata.university == adata.university].ttr
univer_no_ttr = adata[adata.university != adata.university].ttr

univer_yes_mltd = deleteNaN(adata[adata.university == adata.university].mltd)
univer_no_mltd = deleteNaN(adata[adata.university != adata.university].mltd)

univer_yes_hdd = deleteNaN(adata[adata.university == adata.university].hdd)
univer_no_hdd = deleteNaN(adata[adata.university != adata.university].hdd)

draw_hist(univer_yes_ttr, univer_no_ttr, 'yes', 'no', 'univer_ttr')
draw_hist(univer_yes_mltd, univer_no_mltd, 'yes', 'no', 'univer_mltd')
draw_hist(univer_yes_hdd, univer_no_hdd, 'yes', 'no', 'univer_hdd')

import datetime


def year(date):
    if (len(date) < 8):
        return False
    else:
        return True


b=adata[adata.bdate==adata.bdate]

import operator

date1=[x for x in b.bdate if len(x)>=8 and (2018-int(x[-4:]))<18 ]
b1=set(date1)
date2=[x for x in b.bdate if len(x)>=8 and (2018-int(x[-4:]))>=18 and (2018-int(x[-4:]))<30 ]
b2=set(date2)
date3=[x for x in b.bdate if len(x)>=8 and (2018-int(x[-4:]))>=30 and (2018-int(x[-4:]))<45 ]
b3=set(date3)
date4=[x for x in b.bdate if len(x)>=8 and (2018-int(x[-4:]))>=45 ]
b4=set(date4)

ttr1=[b[b.bdate==x].ttr for x in b1]
t1=list(flatten(ttr1))
ttr2=[b[b.bdate==x].ttr for x in b2]
t2=list(flatten(ttr2))
ttr3=[b[b.bdate==x].ttr for x in b3]
t3=list(flatten(ttr3))
ttr4=[b[b.bdate==x].ttr for x in b4]
t4=list(flatten(ttr4))


hdd1=[b[b.bdate==x].hdd for x in b1]
hdd1=list(flatten(hdd1))
hdd1=deleteNaN(array(hdd1))


hdd2=[b[b.bdate==x].hdd for x in b2]
hdd2=list(flatten(hdd2))
hdd2=deleteNaN(array(hdd2))

hdd3=[b[b.bdate==x].hdd for x in b3]
hdd3=list(flatten(hdd3))
hdd3=deleteNaN(array(hdd3))

hdd4=[b[b.bdate==x].hdd for x in b4]
hdd4=list(flatten(hdd4))
hdd4=deleteNaN(array(hdd4))

mltd1=[b[b.bdate==x].mltd for x in b1]
mltd1=list(flatten(mltd1))
mltd1=deleteNaN(array(mltd1))


mltd2=[b[b.bdate==x].mltd for x in b2]
mltd2=list(flatten(mltd2))
mltd2=deleteNaN(array(mltd2))

mltd3=[b[b.bdate==x].mltd for x in b3]
mltd3=list(flatten(mltd3))
mltd3=deleteNaN(array(mltd3))

mltd4=[b[b.bdate==x].mltd for x in b4]
mltd4=list(flatten(mltd4))
mltd4=deleteNaN(array(mltd4))

def drawdate(list1,list2,list3,list4,name):
    plt.hist(list1, histtype='step', label='<18', density=True)
    plt.hist(list2, histtype='step', label='>=18 and <30', density=True)
    plt.hist(list3, histtype='step', label='>=30 and <45', density=True)
    plt.hist(list4, histtype='step', label='>=45', density=True)
    plt.legend(loc='upper right')
    plt.title(name)
    plt.show()
    return 1;

drawdate(t1,t2,t3,t4,'age_ttr')
drawdate(hdd1,hdd2,hdd3,hdd4,'age_hdd')
drawdate(mltd1,mltd2,mltd3,mltd4,'age_mltd')

sp_t=adata[adata.city_id==2].ttr
sp_m=deleteNaN(adata[adata.city_id==2].mltd)
sp_h=deleteNaN(adata[adata.city_id==2].hdd)

msk_t=deleteNaN(adata[adata.city_id==1].ttr)
msk_m=deleteNaN(adata[adata.city_id==1].mltd)
msk_h=deleteNaN(adata[adata.city_id==1].hdd)

draw_hist(sp_t,msk_t,'spb','msk','city_ttr')
draw_hist(sp_m,msk_m,'spb','msk','city_mltd')
draw_hist(sp_h,msk_h,'spb','msk','city_hdd')

al1=adata[adata.alcohol==1].ttr
al3=adata[adata.alcohol==3].ttr
al5=adata[adata.alcohol==5].ttr

plt.hist(al1, histtype='step', label='negative', density=True)
plt.hist(al3, histtype='step', label='compromis', density=True)
plt.hist(al5, histtype='step', label='positive', density=True)
plt.legend(loc='upper left')
plt.title('alcohol')
plt.show()

rel4=adata[adata.relation==4].ttr
rel5=adata[adata.relation==5].ttr
rel1=adata[adata.relation==1].ttr
rel6=adata[adata.relation==6].ttr

plt.hist(rel1, histtype='step', label='не женат/замужем', density=True)
plt.hist(rel5, histtype='step', label='всё сложно', density=True)
plt.hist(rel4, histtype='step', label=' женат/замужем', density=True)
plt.hist(rel6, histtype='step', label='в активном поиске', density=True)
plt.legend(loc='upper left')
plt.title('relation')
plt.show()



