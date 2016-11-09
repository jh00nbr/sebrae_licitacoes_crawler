#!/usr/bin/env python
#! -*- encoding: utf-8 -*- 

from selenium import webdriver
import time

url = {'GDF':'https://www.compras.df.gov.br/publico/em_andamento.asp','sebrae':'http://www.portal.scf.sebrae.com.br/licitante/frmPesquisarAvancadoLicitacao.aspx'}
driver = webdriver.Firefox()



driver.get(url['sebrae'])
#driver.find_element_by_link_text('...').click()

for numero in xrange(2,11):
        try:	
        	   
        #driver.find_element_by_link_text('...').click()
		driver.find_element_by_link_text(str(numero)).click()
	
		time.sleep(6)

	
		html = driver.find_element_by_id('blocoParticipeLicitacoes').get_attribute('innerHTML')
		html = html.encode('UTF-8')
	
		with open("data-raw/sebrae-"+str(numero)+".html","a") as htm:
			htm.write(str(html))
		
			htm.close()

        except:
            pass		





   
