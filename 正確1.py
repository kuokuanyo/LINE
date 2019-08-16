#import xlwt  # 寫入檔案
#import xlrd  # 開啟excel檔案
#from xlutils.copy import copy

#import os
#import re

import sys
import importlib
#import threading
importlib.reload(sys)

from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBoxHorizontal, LAParams
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed

#import logging

# 解析PDF檔案，轉為txt格式
def parsePDF(PDF_path, TXT_path):
    with open(PDF_path, 'rb')as fp:  # 以二進位制讀模式開啟
        praser = PDFParser(fp)  # 用檔案物件來建立一個pdf文件分析器
        doc = PDFDocument()  # 建立一個PDF文件
        praser.set_document(doc)  # 連線分析器與文件物件
        doc.set_parser(praser)

        # 提供初始化密碼
        # 如果沒有密碼 就建立一個空的字串
        doc.initialize()

        # 檢測文件是否提供txt轉換，不提供就忽略
        if not doc.is_extractable:
            raise PDFTextExtractionNotAllowed
        else:
            rsrcmgr = PDFResourceManager()  # 建立PDf 資源管理器 來管理共享資源
            laparams = LAParams()  # 建立一個PDF裝置物件
            device = PDFPageAggregator(rsrcmgr, laparams=laparams)
            interpreter = PDFPageInterpreter(rsrcmgr, device)  # 建立一個PDF直譯器物件

            # 迴圈遍歷列表，每次處理一個page的內容
            for page in doc.get_pages():  # doc.get_pages() 獲取page列表
                interpreter.process_page(page)
                layout = device.get_result()  # 接受該頁面的LTPage物件
                # 這裡layout是一個LTPage物件 裡面存放著 這個page解析出的各種物件 一般包括LTTextBox, LTFigure, LTImage, LTTextBoxHorizontal 等等 想要獲取文字就獲得物件的text屬性，
                for x in layout:
                    #print(x)
                    if isinstance(x, LTTextBoxHorizontal):
                        with open(TXT_path, 'a', encoding='UTF-8', errors='ignore') as f:
                            results = x.get_text()
                            
                            f.write(results + '\n')

PDF_path = r"C:\Users\User\Desktop\灰白.pdf"


TXT_path = r"C:\Users\User\Desktop\test.txt"
parsePDF(PDF_path, TXT_path)