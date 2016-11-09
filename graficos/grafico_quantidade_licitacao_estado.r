library("plotly")
library("RMySQL")

# By Jhonathan Davi A.K.A jh00nbr

siglas_estados <- c("AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO")
db <- dbConnect(MySQL(),host="localhost",user="root",password="",dbname="negocios_reais")

qnt_estados <- NULL
for(sigla in siglas_estados){
  query <- "select count(numero_licitacao) from negocios_reais.dados where uf= '"
  XXX <- dbSendQuery(db,paste0(query,sigla,"';"))
  result_query <- dbFetch(XXX)
  qnt_estados <- rbind(qnt_estados,data.frame(sigla,result_query))
}

names(qnt_estados)[1] <- paste("sigla_estado")
names(qnt_estados)[2] <- paste("qnt_licitacoes")

plot_ly(qnt_estados,x=qnt_estados$sigla_estado,y=qnt_estados$qnt_licitacoes,text= paste("Licitações no estado de :"))
