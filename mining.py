#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import requests,re,MySQLdb
from bs4 import BeautifulSoup
from HTMLParser import HTMLParser
from unicodedata import normalize

# Jhonathan Davi A.K.A jh00nbr / Insightl4b lab.insightsecurity.com.br
# Blog: lab.insightsecurity.com.br
# jh00nbr: http://jhonathandavi.com.br
# Github: github.com/jh00nbr
# Twitter @jh00nbr

__author__ = "Jhonathan Davi A.K.A jh00nbr"
__email__ = "jonatas.davi@outlook.com"

db = MySQLdb.connect(host='localhost',user='root',passwd='',db='negocios_reais',charset='utf8', use_unicode=True, init_command='SET NAMES UTF8')
cur = db.cursor()

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def remover_acentos(string, codif='utf-8'):
    return normalize('NFKD', string.decode(codif)).encode('ASCII','ignore')        

def remover_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

#Regex's
regex_objeto = r"(?<=Objeto:\s)(.*)(?=Data de Abertura\s)"
regex_dataAbertura = r"(?<=Data de Abertura :\s)(.*)(?=hSituação:)"
regex_situacao = r"(?<=Situação:\s)(.*)(?=Local)"
regex_localLicitacao = r"(?<=Local da Licitação:\s)(.*)(?=Telefone:\s)"
regex_telefone = r"(?<=Telefone:\s)(.*)(?=Fax:\s)"
regex_fax = r"(?<=Fax:\s)(.*)(?=\s)"

for x in xrange(1,20):
    with open("data-raw/sebrae-"+str(x)+".html","r") as html:
        arquivo = html.read()
        
    soup = BeautifulSoup(arquivo,'html.parser')
    resultado = soup.find_all('div',{'id':'resultadoBusca'})

    for b in soup.find_all('a',{'class':'unidade'}):
        unidade =  remover_tags(str(b.contents[0])).strip() # Unidade
        	
	unidade_uf = str(unidade.split('/')[1].strip()) # uf da unidade
	titulo =  remover_tags(str(b.contents[1])).strip() # TITULO
	modalidade = titulo.split('-')[0].strip() # Modalidade
	numero_licitacao = titulo.split('-')[1] # Numero da licitacao
    
	content = remover_tags(str(b.contents[2])) # Conteudo
    
	matches_objeto = re.finditer(regex_objeto, str(content))
	matches_dataAbertura = re.finditer(regex_dataAbertura,str(content))
	matches_situacao = re.finditer(regex_situacao,str(content))
	matches_localLicitacao = re.finditer(regex_localLicitacao,str(content))
	matches_telefone = re.finditer(regex_telefone,str(content))
	matches_fax = re.finditer(regex_fax,str(content))
          
	for matchNum,match in enumerate(matches_dataAbertura):
            data_abertura = remover_tags(str(match.group())).split()[0]
            data_abertura = data_abertura.split('/')[2] + "-" + data_abertura.split('/')[1] + "-" + data_abertura.split('/')[0]
            	
	for matchNum,match in enumerate(matches_situacao):
            situacao = remover_tags(str(match.group())).strip()
  
	for matchNum,match in enumerate(matches_localLicitacao):
            local_licitacao = remover_tags(str(match.group())).strip()

	for matchNum,match in enumerate(matches_telefone):
            telefone = remover_tags(str(match.group())).strip()
            telefone = telefone.replace(' ','')
            dd = telefone.split()[0].replace('(','').replace(')','') # Remove os () do DD

	for matchNum,match in enumerate(matches_fax):
            fax = remover_tags(str(match.group())).strip()
            if len(fax) < 2:
                fax = "N/A"
            else:
	    	fax = remover_tags(str(match.group())).strip() 	

        for matchNum,match in enumerate(matches_objeto):   
            objeto = remover_tags(str(match.group())) # OBJETO
            subQuery = ("'" + "NULL" + "','" + "Sebrae" + "','"  + unidade_uf +  "','" + remover_acentos(str(modalidade)) + "','" + str(numero_licitacao) + "','" + str(data_abertura) + "','" +  str(situacao) + "','" + str(dd) +  "','"  + str(telefone) +  "','" + str(fax) + "','" + remover_acentos(objeto) + "'")
            querySql = "INSERT INTO `negocios_reais`.`dados` (`id`, `unidade`, `uf` , `modalidade`, `numero_licitacao`, `data_abertura`, `situacao`, `dd`, `telefone`, `fax`, `objeto`)  VALUES ("+ subQuery +");"
            #cur.execute(querySql)
            print querySql                        		 
