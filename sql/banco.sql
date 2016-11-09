CREATE TABLE `dados` (
  `id` int NOT NULL AUTO_INCREMENT,
  `unidade` varchar(45) DEFAULT NULL,
  `uf` varchar(3) DEFAULT NULL,
  `modalidade` varchar(45) DEFAULT NULL,
  `numero_licitacao` varchar(70) DEFAULT NULL,
  `data_abertura` date NULL,
  `situacao` varchar(50) DEFAULT NULL,
  `dd` varchar(2) DEFAULT NULL,
  `telefone` varchar(10) DEFAULT NULL,
  `fax` varchar(10) DEFAULT NULL,
  `objeto` varchar(300) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;



