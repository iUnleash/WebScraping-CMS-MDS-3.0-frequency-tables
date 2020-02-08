{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "import bs4\n",
    "import requests\n",
    "import itertools\n",
    "import lxml.html as lh\n",
    "import pandas as pd\n",
    "from bs4 import BeautifulSoup\n",
    "from urllib.request import urlopen as uReq\n",
    "import threading\n",
    "import _thread\n",
    "import time\n",
    "import queue\n",
    "from lxml import etree\n",
    "import urllib\n",
    "import csv\n",
    "import numpy as np\n",
    "import webbrowser\n",
    "import re"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "with open('AllUrls.csv', 'r') as f:\n",
    "    reader = csv.reader(f)\n",
    "    your_list = list(reader)\n",
    "my_urls = tuple(your_list)\n",
    "my_urls = list(itertools.chain.from_iterable(my_urls))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "--- 5426.109987974167 seconds ---\n"
     ]
    }
   ],
   "source": [
    "import time\n",
    "start_time = time.time()\n",
    "\n",
    "# To get HTML elements\n",
    "e_results = {}\n",
    "for i in my_urls:\n",
    "    uClient = uReq(i)\n",
    "    page_html = uClient.read()\n",
    "    e_results[i] = lh.fromstring(page_html)\n",
    "\n",
    "print(\"--- %s seconds ---\" % (time.time() - start_time))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "--- 8.83491826057434 seconds ---\n"
     ]
    }
   ],
   "source": [
    "start_time = time.time()\n",
    "df = [] #Rows\n",
    "df2 = [] #Headers\n",
    "for i in e_results:\n",
    "    df.append(e_results[i].xpath('//td/text()'))\n",
    "for i in e_results:\n",
    "    df2.append(e_results[i].xpath('//th/text()'))\n",
    "print(\"--- %s seconds ---\" % (time.time() - start_time))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [],
   "source": [
    "titles = []\n",
    "for i in e_results:\n",
    "    titles.append(e_results[i].xpath('//tr/td/strong/text()'))\n",
    "for y in range(len(titles)):\n",
    "    titles[y] = [i.strip() for i in titles[y]]\n",
    "    titles[y] = [i.split(':', 1)[0] for i in titles[y]]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['\\r\\n   \\t\\t\\t',\n",
       " '\\t\\xa0\\r\\n   \\t\\t\\t',\n",
       " '\\r\\n\\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t    Alabama\\r\\n   \\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t\\t\\t\\t99.89%\\r\\n   \\t\\t\\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t\\t\\t\\t0.11%\\r\\n   \\t\\t\\t\\t\\t',\n",
       " '\\r\\n\\t\\t\\t23534\\r\\n   \\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t    Alaska\\r\\n   \\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t\\t\\t\\t70.89%\\r\\n   \\t\\t\\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t\\t\\t\\t29.11%\\r\\n   \\t\\t\\t\\t\\t',\n",
       " '\\r\\n\\t\\t\\t632\\r\\n   \\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t    Arizona\\r\\n   \\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t\\t\\t\\t92.68%\\r\\n   \\t\\t\\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t\\t\\t\\t7.32%\\r\\n   \\t\\t\\t\\t\\t',\n",
       " '\\r\\n\\t\\t\\t13068\\r\\n   \\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t    Arkansas\\r\\n   \\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t\\t\\t\\t99.88%\\r\\n   \\t\\t\\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t\\t\\t\\t0.12%\\r\\n   \\t\\t\\t\\t\\t',\n",
       " '\\r\\n\\t\\t\\t17683\\r\\n   \\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t    California\\r\\n   \\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t\\t\\t\\t99.66%\\r\\n   \\t\\t\\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t\\t\\t\\t0.34%\\r\\n   \\t\\t\\t\\t\\t',\n",
       " '\\r\\n\\t\\t\\t107943\\r\\n   \\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t    Colorado\\r\\n   \\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t\\t\\t\\t99.36%\\r\\n   \\t\\t\\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t\\t\\t\\t0.64%\\r\\n   \\t\\t\\t\\t\\t',\n",
       " '\\r\\n\\t\\t\\t17210\\r\\n   \\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t    Connecticut\\r\\n   \\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t\\t\\t\\t99.92%\\r\\n   \\t\\t\\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t\\t\\t\\t0.08%\\r\\n   \\t\\t\\t\\t\\t',\n",
       " '\\r\\n\\t\\t\\t23148\\r\\n   \\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t    Delaware\\r\\n   \\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t\\t\\t\\t99.84%\\r\\n   \\t\\t\\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t\\t\\t\\t0.16%\\r\\n   \\t\\t\\t\\t\\t',\n",
       " '\\r\\n\\t\\t\\t4269\\r\\n   \\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t    District of Columbia\\r\\n   \\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t\\t\\t\\t99.84%\\r\\n   \\t\\t\\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t\\t\\t\\t0.16%\\r\\n   \\t\\t\\t\\t\\t',\n",
       " '\\r\\n\\t\\t\\t2431\\r\\n   \\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t    Florida\\r\\n   \\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t\\t\\t\\t99.92%\\r\\n   \\t\\t\\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t\\t\\t\\t0.08%\\r\\n   \\t\\t\\t\\t\\t',\n",
       " '\\r\\n\\t\\t\\t78255\\r\\n   \\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t    Georgia\\r\\n   \\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t\\t\\t\\t99.92%\\r\\n   \\t\\t\\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t\\t\\t\\t0.08%\\r\\n   \\t\\t\\t\\t\\t',\n",
       " '\\r\\n\\t\\t\\t34589\\r\\n   \\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t    Hawaii\\r\\n   \\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t\\t\\t\\t99.87%\\r\\n   \\t\\t\\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t\\t\\t\\t0.13%\\r\\n   \\t\\t\\t\\t\\t',\n",
       " '\\r\\n\\t\\t\\t3763\\r\\n   \\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t    Idaho\\r\\n   \\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t\\t\\t\\t98.61%\\r\\n   \\t\\t\\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t\\t\\t\\t1.39%\\r\\n   \\t\\t\\t\\t\\t',\n",
       " '\\r\\n\\t\\t\\t4309\\r\\n   \\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t    Illinois\\r\\n   \\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t\\t\\t\\t99.90%\\r\\n   \\t\\t\\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t\\t\\t\\t0.10%\\r\\n   \\t\\t\\t\\t\\t',\n",
       " '\\r\\n\\t\\t\\t68245\\r\\n   \\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t    Indiana\\r\\n   \\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t\\t\\t\\t99.92%\\r\\n   \\t\\t\\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t\\t\\t\\t0.08%\\r\\n   \\t\\t\\t\\t\\t',\n",
       " '\\r\\n\\t\\t\\t40261\\r\\n   \\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t    Iowa\\r\\n   \\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t\\t\\t\\t99.86%\\r\\n   \\t\\t\\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t\\t\\t\\t0.14%\\r\\n   \\t\\t\\t\\t\\t',\n",
       " '\\r\\n\\t\\t\\t23681\\r\\n   \\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t    Kansas\\r\\n   \\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t\\t\\t\\t99.60%\\r\\n   \\t\\t\\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t\\t\\t\\t0.40%\\r\\n   \\t\\t\\t\\t\\t',\n",
       " '\\r\\n\\t\\t\\t17315\\r\\n   \\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t    Kentucky\\r\\n   \\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t\\t\\t\\t99.96%\\r\\n   \\t\\t\\t\\t\\t',\n",
       " '\\t*\\r\\n   \\t\\t\\t\\t\\t',\n",
       " '\\r\\n\\t\\t\\t23260\\r\\n   \\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t    Louisiana\\r\\n   \\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t\\t\\t\\t99.88%\\r\\n   \\t\\t\\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t\\t\\t\\t0.12%\\r\\n   \\t\\t\\t\\t\\t',\n",
       " '\\r\\n\\t\\t\\t26741\\r\\n   \\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t    Maine\\r\\n   \\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t\\t\\t\\t99.77%\\r\\n   \\t\\t\\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t\\t\\t\\t0.23%\\r\\n   \\t\\t\\t\\t\\t',\n",
       " '\\r\\n\\t\\t\\t6010\\r\\n   \\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t    Maryland\\r\\n   \\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t\\t\\t\\t99.87%\\r\\n   \\t\\t\\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t\\t\\t\\t0.13%\\r\\n   \\t\\t\\t\\t\\t',\n",
       " '\\r\\n\\t\\t\\t25383\\r\\n   \\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t    Massachusetts\\r\\n   \\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t\\t\\t\\t99.91%\\r\\n   \\t\\t\\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t\\t\\t\\t0.09%\\r\\n   \\t\\t\\t\\t\\t',\n",
       " '\\r\\n\\t\\t\\t39583\\r\\n   \\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t    Michigan\\r\\n   \\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t\\t\\t\\t99.71%\\r\\n   \\t\\t\\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t\\t\\t\\t0.29%\\r\\n   \\t\\t\\t\\t\\t',\n",
       " '\\r\\n\\t\\t\\t40288\\r\\n   \\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t    Minnesota\\r\\n   \\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t\\t\\t\\t98.84%\\r\\n   \\t\\t\\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t\\t\\t\\t1.16%\\r\\n   \\t\\t\\t\\t\\t',\n",
       " '\\r\\n\\t\\t\\t24971\\r\\n   \\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t    Mississippi\\r\\n   \\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t\\t\\t\\t99.70%\\r\\n   \\t\\t\\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t\\t\\t\\t0.30%\\r\\n   \\t\\t\\t\\t\\t',\n",
       " '\\r\\n\\t\\t\\t16257\\r\\n   \\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t    Missouri\\r\\n   \\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t\\t\\t\\t99.87%\\r\\n   \\t\\t\\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t\\t\\t\\t0.13%\\r\\n   \\t\\t\\t\\t\\t',\n",
       " '\\r\\n\\t\\t\\t38556\\r\\n   \\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t    Montana\\r\\n   \\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t\\t\\t\\t93.69%\\r\\n   \\t\\t\\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t\\t\\t\\t6.31%\\r\\n   \\t\\t\\t\\t\\t',\n",
       " '\\r\\n\\t\\t\\t4200\\r\\n   \\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t    Nebraska\\r\\n   \\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t\\t\\t\\t98.93%\\r\\n   \\t\\t\\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t\\t\\t\\t1.07%\\r\\n   \\t\\t\\t\\t\\t',\n",
       " '\\r\\n\\t\\t\\t11459\\r\\n   \\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t    Nevada\\r\\n   \\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t\\t\\t\\t99.34%\\r\\n   \\t\\t\\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t\\t\\t\\t0.66%\\r\\n   \\t\\t\\t\\t\\t',\n",
       " '\\r\\n\\t\\t\\t6066\\r\\n   \\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t    New Hampshire\\r\\n   \\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t\\t\\t\\t99.95%\\r\\n   \\t\\t\\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t\\t\\t\\t0.05%\\r\\n   \\t\\t\\t\\t\\t',\n",
       " '\\r\\n\\t\\t\\t6555\\r\\n   \\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t    New Jersey\\r\\n   \\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t\\t\\t\\t99.89%\\r\\n   \\t\\t\\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t\\t\\t\\t0.11%\\r\\n   \\t\\t\\t\\t\\t',\n",
       " '\\r\\n\\t\\t\\t45763\\r\\n   \\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t    New Mexico\\r\\n   \\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t\\t\\t\\t90.49%\\r\\n   \\t\\t\\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t\\t\\t\\t9.51%\\r\\n   \\t\\t\\t\\t\\t',\n",
       " '\\r\\n\\t\\t\\t5856\\r\\n   \\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t    New York\\r\\n   \\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t\\t\\t\\t99.76%\\r\\n   \\t\\t\\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t\\t\\t\\t0.24%\\r\\n   \\t\\t\\t\\t\\t',\n",
       " '\\r\\n\\t\\t\\t108603\\r\\n   \\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t    North Carolina\\r\\n   \\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t\\t\\t\\t99.21%\\r\\n   \\t\\t\\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t\\t\\t\\t0.79%\\r\\n   \\t\\t\\t\\t\\t',\n",
       " '\\r\\n\\t\\t\\t37669\\r\\n   \\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t    North Dakota\\r\\n   \\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t\\t\\t\\t97.07%\\r\\n   \\t\\t\\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t\\t\\t\\t2.93%\\r\\n   \\t\\t\\t\\t\\t',\n",
       " '\\r\\n\\t\\t\\t5430\\r\\n   \\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t    Ohio\\r\\n   \\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t\\t\\t\\t99.94%\\r\\n   \\t\\t\\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t\\t\\t\\t0.06%\\r\\n   \\t\\t\\t\\t\\t',\n",
       " '\\r\\n\\t\\t\\t75440\\r\\n   \\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t    Oklahoma\\r\\n   \\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t\\t\\t\\t95.10%\\r\\n   \\t\\t\\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t\\t\\t\\t4.90%\\r\\n   \\t\\t\\t\\t\\t',\n",
       " '\\r\\n\\t\\t\\t18667\\r\\n   \\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t    Oregon\\r\\n   \\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t\\t\\t\\t99.32%\\r\\n   \\t\\t\\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t\\t\\t\\t0.68%\\r\\n   \\t\\t\\t\\t\\t',\n",
       " '\\r\\n\\t\\t\\t7824\\r\\n   \\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t    Pennsylvania\\r\\n   \\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t\\t\\t\\t99.96%\\r\\n   \\t\\t\\t\\t\\t',\n",
       " '\\t*\\r\\n   \\t\\t\\t\\t\\t',\n",
       " '\\r\\n\\t\\t\\t78367\\r\\n   \\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t    Puerto Rico\\r\\n   \\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t\\t\\t\\t100.00%\\r\\n   \\t\\t\\t\\t\\t',\n",
       " '\\t*\\r\\n   \\t\\t\\t\\t\\t',\n",
       " '\\r\\n\\t\\t\\t118\\r\\n   \\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t    Rhode Island\\r\\n   \\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t\\t\\t\\t99.81%\\r\\n   \\t\\t\\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t\\t\\t\\t0.19%\\r\\n   \\t\\t\\t\\t\\t',\n",
       " '\\r\\n\\t\\t\\t8073\\r\\n   \\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t    South Carolina\\r\\n   \\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t\\t\\t\\t99.87%\\r\\n   \\t\\t\\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t\\t\\t\\t0.13%\\r\\n   \\t\\t\\t\\t\\t',\n",
       " '\\r\\n\\t\\t\\t17598\\r\\n   \\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t    South Dakota\\r\\n   \\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t\\t\\t\\t94.48%\\r\\n   \\t\\t\\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t\\t\\t\\t5.52%\\r\\n   \\t\\t\\t\\t\\t',\n",
       " '\\r\\n\\t\\t\\t5744\\r\\n   \\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t    Tennessee\\r\\n   \\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t\\t\\t\\t99.91%\\r\\n   \\t\\t\\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t\\t\\t\\t0.09%\\r\\n   \\t\\t\\t\\t\\t',\n",
       " '\\r\\n\\t\\t\\t28910\\r\\n   \\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t    Texas\\r\\n   \\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t\\t\\t\\t99.86%\\r\\n   \\t\\t\\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t\\t\\t\\t0.14%\\r\\n   \\t\\t\\t\\t\\t',\n",
       " '\\r\\n\\t\\t\\t96965\\r\\n   \\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t    U.S. Virgin Islands\\r\\n   \\t\\t\\t',\n",
       " '\\t*\\r\\n   \\t\\t\\t\\t\\t',\n",
       " '\\t*\\r\\n   \\t\\t\\t\\t\\t',\n",
       " '\\r\\n\\t\\t\\t0\\r\\n   \\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t    Utah\\r\\n   \\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t\\t\\t\\t98.52%\\r\\n   \\t\\t\\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t\\t\\t\\t1.48%\\r\\n   \\t\\t\\t\\t\\t',\n",
       " '\\r\\n\\t\\t\\t6006\\r\\n   \\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t    Vermont\\r\\n   \\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t\\t\\t\\t99.81%\\r\\n   \\t\\t\\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t\\t\\t\\t0.19%\\r\\n   \\t\\t\\t\\t\\t',\n",
       " '\\r\\n\\t\\t\\t2565\\r\\n   \\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t    Virginia\\r\\n   \\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t\\t\\t\\t99.91%\\r\\n   \\t\\t\\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t\\t\\t\\t0.09%\\r\\n   \\t\\t\\t\\t\\t',\n",
       " '\\r\\n\\t\\t\\t29223\\r\\n   \\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t    Washington\\r\\n   \\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t\\t\\t\\t98.75%\\r\\n   \\t\\t\\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t\\t\\t\\t1.25%\\r\\n   \\t\\t\\t\\t\\t',\n",
       " '\\r\\n\\t\\t\\t16723\\r\\n   \\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t    West Virginia\\r\\n   \\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t\\t\\t\\t99.91%\\r\\n   \\t\\t\\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t\\t\\t\\t0.09%\\r\\n   \\t\\t\\t\\t\\t',\n",
       " '\\r\\n\\t\\t\\t9635\\r\\n   \\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t    Wisconsin\\r\\n   \\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t\\t\\t\\t99.24%\\r\\n   \\t\\t\\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t\\t\\t\\t0.76%\\r\\n   \\t\\t\\t\\t\\t',\n",
       " '\\r\\n\\t\\t\\t23372\\r\\n   \\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t    Wyoming\\r\\n   \\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t\\t\\t\\t97.94%\\r\\n   \\t\\t\\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t\\t\\t\\t2.06%\\r\\n   \\t\\t\\t\\t\\t',\n",
       " '\\r\\n\\t\\t\\t2384\\r\\n   \\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t    ',\n",
       " '\\r\\n   \\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t\\t\\t\\t99.52%\\r\\n   \\t\\t\\t\\t\\t',\n",
       " '\\r\\n   \\t\\t\\t\\t\\t\\t0.48%\\r\\n   \\t\\t\\t\\t\\t',\n",
       " '\\r\\n\\t\\t\\t1380600\\r\\n   \\t\\t\\t']"
      ]
     },
     "execution_count": 78,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "uClient2 = uReq('https://www.cms.gov/apps/mds/mds_notemp/mds30FreqStart.asp?isSubmitted=mds30Freq3&var=A1000A&date=30')\n",
    "page_html2 = uClient2.read()\n",
    "e_results2 = lh.fromstring(page_html2)\n",
    "e_results2.xpath('//td/text()')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "for y in range(len(df)): \n",
    "    df[y] = [i.strip() for i in df[y]][3:-4]\n",
    "for y in range(len(df2)):\n",
    "    df2[y] = [i.strip() for i in df2[y]]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "dfs = []\n",
    "for x,y in zip(df, df2):\n",
    "    cols = [x[i::len(y)] for i in range(len(y))]\n",
    "    dfs.append(cols)\n",
    "    # dfs.append(list(zip([col for col in cols])))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "alldfs = []\n",
    "for i in range(len(dfs)):\n",
    "    alldfs.append(pd.DataFrame(dfs[i]).T)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "df2headers = pd.DataFrame(df2)\n",
    "for i in range(len(alldfs)):\n",
    "    alldfs[i] = alldfs[i].rename(columns=df2headers.iloc[i])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "checkdf = []\n",
    "for i in range(len(alldfs)):\n",
    "    if 'State' in alldfs[i].columns:\n",
    "        checkdf.append(\"Yes\")\n",
    "    else:\n",
    "        checkdf.append(\"No\")\n",
    "checkdf = [i for i, e in enumerate(checkdf) if e == 'No']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "alldfs2 = [i for j, i in enumerate(alldfs) if j not in checkdf]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "titles = []\n",
    "for i in e_results:\n",
    "    titles.append(e_results[i].xpath('//tr/td/strong/text()'))\n",
    "for y in range(len(titles)):\n",
    "    titles[y] = [i.strip() for i in titles[y]]\n",
    "    titles[y] = [i.split(':', 1)[0] for i in titles[y]]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
    "titles = [i for j, i in enumerate(titles) if j not in checkdf]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "for i in range(len(alldfs2)):\n",
    "    for y in range(len(titles)):\n",
    "        alldfs2[i]['Measure'] = str(titles[i])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [],
   "source": [
    "dates = []\n",
    "for i in e_results:\n",
    "    dates.append(e_results[i].xpath('//h4/text()'))\n",
    "for y in range(len(dates)):\n",
    "    dates[y] = [i.strip() for i in dates[y]]\n",
    "    dates[y] = [i.split('\\t\\t\\t', 1)[1] for i in dates[y]]\n",
    "    dates[y] = [i.split(')', 1)[0] for i in dates[y]]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [],
   "source": [
    "dates = [i for j, i in enumerate(dates) if j not in checkdf]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [],
   "source": [
    "for i in range(len(alldfs2)):\n",
    "    for y in range(len(dates)):\n",
    "        alldfs2[i]['Date'] = str(dates[i])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [],
   "source": [
    "for i in range(len(alldfs2)):\n",
    "    alldfs2[i] = pd.melt(alldfs2[i], id_vars=['State','Date','Measure'])\n",
    "maindf = pd.concat(alldfs2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [],
   "source": [
    "maindf = maindf.dropna()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [],
   "source": [
    "maindf['value'] = [i.strip('%') for i in maindf['value']]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [],
   "source": [
    "maindf['value'] = [i.strip('*') for i in maindf['value']]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [],
   "source": [
    "maindf['value'] = pd.to_numeric(maindf['value'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [],
   "source": [
    "maindf['Date'] = maindf['Date'].replace({\"['Fourth Quarter 2011']\":\"10/1/2011\", \n",
    "                        \"['First Quarter 2012']\":\"1/1/2012\",\n",
    "                        \"['Second Quarter 2012']\":\"4/1/2012\", \n",
    "                        \"['Third Quarter 2012']\":\"7/1/2012\",\n",
    "                        \"['Fourth Quarter 2012']\":\"10/1/2012\", \n",
    "                        \"['First Quarter 2013']\":\"1/1/2013\",\n",
    "                        \"['Second Quarter 2013']\":\"4/1/2013\", \n",
    "                        \"['Third Quarter 2013']\":\"7/1/2013\",\n",
    "                        \"['Fourth Quarter 2013']\":\"10/1/2013\", \n",
    "                        \"['First Quarter 2014']\":\"1/1/2014\",   \n",
    "                        \"['Second Quarter 2014']\":\"4/1/2014\", \n",
    "                        \"['Third Quarter 2014']\":\"7/1/2014\",  \n",
    "                        \"['Fourth Quarter 2014']\":\"10/1/2014\", \n",
    "                        \"['First Quarter 2015']\":\"1/1/2015\",    \n",
    "                        \"['Second Quarter 2015']\":\"4/1/2015\", \n",
    "                        \"['Third Quarter 2015']\":\"7/1/2015\",      \n",
    "                        \"['Fourth Quarter 2015']\":\"10/1/2015\", \n",
    "                        \"['First Quarter 2016']\":\"1/1/2016\",     \n",
    "                        \"['Second Quarter 2016']\":\"4/1/2016\", \n",
    "                        \"['Third Quarter 2016']\":\"7/1/2016\",      \n",
    "                        \"['Fourth Quarter 2016']\":\"10/1/2016\", \n",
    "                        \"['First Quarter 2017']\":\"1/1/2017\",      \n",
    "                        \"['Second Quarter 2017']\":\"4/1/2017\", \n",
    "                        \"['Third Quarter 2017']\":\"7/1/2017\",      \n",
    "                        \"['Fourth Quarter 2017']\":\"10/1/2017\", \n",
    "                        \"['First Quarter 2018']\":\"1/1/2018\",      \n",
    "                        \"['Second Quarter 2018']\":\"4/1/2018\", \n",
    "                        \"['Third Quarter 2018']\":\"7/1/2018\",\n",
    "                        \"['Fourth Quarter 2018']\":\"10/1/2018\", \n",
    "                        \"['First Quarter 2019']\":\"1/1/2019\"})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [],
   "source": [
    "maindf['Measure'] = [i.strip(\"['\") for i in maindf['Measure']]\n",
    "maindf['Measure'] = [i.strip(\"']\") for i in maindf['Measure']]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "maindf.to_excel(\"DashboardOutput.xlsx\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "metadata": {},
   "outputs": [],
   "source": [
    "maindf.to_csv('DashboardTXTOutput.txt', header=True, index=False, sep='\\t')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
