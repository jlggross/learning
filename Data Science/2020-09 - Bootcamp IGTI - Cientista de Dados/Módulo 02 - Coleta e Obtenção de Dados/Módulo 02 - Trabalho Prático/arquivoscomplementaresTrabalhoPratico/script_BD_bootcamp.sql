-- MySQL Workbench Forward Engineering

-- -----------------------------------------------------
-- Schema igti_tarefa2
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `igti_tarefa2` DEFAULT CHARACTER SET utf8mb4;
USE `igti_tarefa2` ;

-- -----------------------------------------------------
-- Table `igti_tarefa2`.`caracteristicasgerais`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `igti_tarefa2`.`caracteristicasgerais` (
  `idcaracteristicasGerais` INT NOT NULL AUTO_INCREMENT,
  `dsccaracteristicasGerais` VARCHAR(150) NOT NULL,
  PRIMARY KEY (`idcaracteristicasGerais`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `igti_tarefa2`.`estado`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `igti_tarefa2`.`estado` (
  `CodEstadoIBGE` INT NOT NULL,
  `NomeEstado` VARCHAR(45) NOT NULL,
  `SiglaEstado` CHAR(2) NOT NULL,
  `Regiao` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`CodEstadoIBGE`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `igti_tarefa2`.`cidade`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `igti_tarefa2`.`cidade` (
  `CodigoCompletoIBGE` VARCHAR(45) NOT NULL,
  `CodigoCidadeIBGE` VARCHAR(10) NOT NULL,
  `NomeCidade` VARCHAR(150) NOT NULL,
  `CodEstadoIBGE` INT NOT NULL,
  PRIMARY KEY (`CodigoCompletoIBGE`),
  INDEX `fk_Cidade_Estado_idx` (`CodEstadoIBGE` ASC),
  CONSTRAINT `fk_Cidade_Estado`
    FOREIGN KEY (`CodEstadoIBGE`)
    REFERENCES `igti_tarefa2`.`estado` (`CodEstadoIBGE`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `igti_tarefa2`.`tipounidade`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `igti_tarefa2`.`tipounidade` (
  `idTipoUnidade` INT NOT NULL AUTO_INCREMENT,
  `dscTipoUnidade` VARCHAR(150) NOT NULL,
  PRIMARY KEY (`idTipoUnidade`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `igti_tarefa2`.`imovel`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `igti_tarefa2`.`imovel` (
  `idImovel` INT NOT NULL AUTO_INCREMENT,
  `codRegistro` VARCHAR(45) NOT NULL,
  `Disponibilidade` CHAR(1) NULL DEFAULT NULL,
  `idTipoUnidade` INT NOT NULL,
  `areaImovel` DECIMAL(6,2) NULL DEFAULT NULL,
  `valorIPTU` DECIMAL(10,2) NULL DEFAULT NULL,
  `valorCondominio` DECIMAL(10,2) NULL DEFAULT NULL,
  `qtdeQuartos` INT NULL DEFAULT NULL,
  `qtdeBanheiro` INT NULL DEFAULT NULL,
  `qtdeSuite` INT NULL DEFAULT NULL,
  `qtdeSala` INT NOT NULL DEFAULT '1',
  `qtdeVagas` INT NOT NULL DEFAULT '0',
  `CodigoCompletoIBGE` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idImovel`),
  INDEX `fk_Imovel_TipoUnidade_idx` (`idTipoUnidade` ASC),
  INDEX `fk_Imovel_Cidade1_idx` (`CodigoCompletoIBGE` ASC),
  CONSTRAINT `fk_Imovel_Cidade1`
    FOREIGN KEY (`CodigoCompletoIBGE`)
    REFERENCES `igti_tarefa2`.`cidade` (`CodigoCompletoIBGE`),
  CONSTRAINT `fk_Imovel_TipoUnidade`
    FOREIGN KEY (`idTipoUnidade`)
    REFERENCES `igti_tarefa2`.`tipounidade` (`idTipoUnidade`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `igti_tarefa2`.`caracteristicageralimovel`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `igti_tarefa2`.`caracteristicageralimovel` (
  `idCaracteristicasImovel` INT NOT NULL AUTO_INCREMENT,
  `idcaracteristicasGerais` INT NOT NULL,
  `idImovel` INT NOT NULL,
  `temCaracteristica` TINYINT NULL DEFAULT NULL,
  PRIMARY KEY (`idCaracteristicasImovel`),
  INDEX `fk_caracteristicasGerais_has_Imovel_Imovel1_idx` (`idImovel` ASC),
  INDEX `fk_caracteristicasGerais_has_Imovel_caracteristicasGerais1_idx` (`idcaracteristicasGerais` ASC),
  CONSTRAINT `fk_caracteristicasGerais_has_Imovel_caracteristicasGerais1`
    FOREIGN KEY (`idcaracteristicasGerais`)
    REFERENCES `igti_tarefa2`.`caracteristicasgerais` (`idcaracteristicasGerais`),
  CONSTRAINT `fk_caracteristicasGerais_has_Imovel_Imovel1`
    FOREIGN KEY (`idImovel`)
    REFERENCES `igti_tarefa2`.`imovel` (`idImovel`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;

-- -----------------------------------------------------
-- Data for table `igti_tarefa2`.`tipounidade`
-- -----------------------------------------------------

USE `igti_tarefa2`;
INSERT INTO `igti_tarefa2`.`tipounidade` (`idTipoUnidade`, `dscTipoUnidade`) VALUES (1, 'Casa');
INSERT INTO `igti_tarefa2`.`tipounidade` (`idTipoUnidade`, `dscTipoUnidade`) VALUES (2, 'Casa geminada');
INSERT INTO `igti_tarefa2`.`tipounidade` (`idTipoUnidade`, `dscTipoUnidade`) VALUES (3, 'Apartamento tipo');
INSERT INTO `igti_tarefa2`.`tipounidade` (`idTipoUnidade`, `dscTipoUnidade`) VALUES (4, 'Apartamento cobertura');
INSERT INTO `igti_tarefa2`.`tipounidade` (`idTipoUnidade`, `dscTipoUnidade`) VALUES (5, 'Apartamento área privativa');
INSERT INTO `igti_tarefa2`.`tipounidade` (`idTipoUnidade`, `dscTipoUnidade`) VALUES (6, 'Flat');

COMMIT;

