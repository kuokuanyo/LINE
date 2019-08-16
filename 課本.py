# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 10:42:00 2019

@author: User
"""
import sys
import importlib
importlib.reload(sys)


#from urllib.request import urlopen

#PDFResourceManager：pdf 共享資源管理器,用於儲存共享資源，如字型或影象
from pdfminer.pdfinterp import PDFResourceManager,process_pdf

from pdfminer.converter import TextConverter

# 建立一個PDF裝置物件
from pdfminer.layout import LAParams

from pdfminer.pdfparser import PDFParser 
from pdfdocument.document import PDFDocument

#StringIO建立的是一個file-like object，擁有File Object的所有方法。
#StringIO還有兩個特殊的方法，就是getvalue()方法和close()方法。
#StringIO在記憶體中讀寫str
#BytesIO：操作二進位制資料,在記憶體中讀寫bytes
from io import StringIO
from io import open

#import PyPDF2




def readpdf(file):
    rsrcmgr=PDFResourceManager()
    retstr=StringIO()
    laparams=LAParams()
    device=TextConverter(rsrcmgr,retstr,laparams=laparams)
    process_pdf(rsrcmgr,device,file)

    device.close()
    
    content=retstr.getvalue()  #取得值
    retstr.close()
    
    return content




f=open(r'C:\Users\User\Desktop\chapter1.pdf','rb')
print(type(f)) #_io



#new=f.readlines()
#print(new)



####測試
#parser = PDFParser(f) 
#建立一個PDF文件物件儲存文件結構 
#document = PDFDocument(parser) 
#print(type(document))
#import logging 
#logging.Logger.propagate = False 
#logging.getLogger().setLevel(logging.ERROR)



pdf=readpdf(f)

result=str(pdf)
print(result)

with open(r"C:\Users\User\Desktop\123.txt", 'a', encoding='UTF-8', errors='ignore') as file:
    file.write(result + '\n')

f.close()
    