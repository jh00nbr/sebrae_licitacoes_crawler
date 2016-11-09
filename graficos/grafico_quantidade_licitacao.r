library('RMySQL') # install.packages('RMySQL')
library('ggplot2') # install.packages('ggplot2')
library('plotly') # install.packages('plotly')

#install.packages('plotly')
#install.packages("devtools", dependencies = TRUE)

# By Jhonathan Davi A.K.A jh00nbr

setwd('/root/Área\ de\ trabalho/negocios_reais')

db <- dbConnect(MySQL(),user="root",password="",dbname="negocios_reais",host="127.0.0.1")
modalidade <- c('Leilao','Pregao Presencial','Pregao Eletronico','Concorrencia','Convite','Pre-qualificacao','Credenciamento')

mydata <- NULL
for (modali in modalidade){
  sqlQuery <- paste0("select count(numero_licitacao) from negocios_reais.dados where modalidade = '",modali,"';")
  query <- dbSendQuery(db,sqlQuery)
  dados <- dbFetch(query)
  print(paste(modali,dados))
  mydata <- rbind(mydata,data.frame(modali,dados))
 
}

names(mydata)[1] <- paste("modalidade")  
names(mydata)[2] <- paste("qnt_licitacoes_modalidade")

plot_ly(mydata,x=mydata$modalidade,y=mydata$qnt_licitacoes_modalidade,text= paste("modalidades"))
