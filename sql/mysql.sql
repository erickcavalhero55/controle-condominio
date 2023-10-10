-- MySQL Script generated by MySQL Workbench
-- qua 05 jul 2023 11:05:08
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema controle_condominio
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema controle_condominio
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `controle_condominio` ;
USE `controle_condominio` ;

-- -----------------------------------------------------
-- Table `controle_condominio`.`usuarios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `controle_condominio`.`usuarios` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(45) NOT NULL,
  `sobrenome` VARCHAR(45) NOT NULL,
  `rg` VARCHAR(45) NOT NULL,
  `cpf` VARCHAR(45) NOT NULL,
  `telefone` VARCHAR(45) NOT NULL,
  `celular` VARCHAR(45) NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  `genero` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `controle_condominio`.`cobrancas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `controle_condominio`.`cobrancas` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `cod_barras` VARCHAR(50) NOT NULL,
  `data_vencimento` DATE NOT NULL,
  `data_pagamento` DATETIME NOT NULL,
  `valor` VARCHAR(50) NOT NULL,
  `titulo` VARCHAR(50) NOT NULL,
  `observacao` VARCHAR(45) NOT NULL,
  `juros` VARCHAR(45) NOT NULL,
  `multa` VARCHAR(45) NOT NULL,
  `desconto` VARCHAR(45) NOT NULL,
  `total` VARCHAR(45) NOT NULL,
  `id_usuarios` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_cobrancas_1_idx` (`id_usuarios` ASC) VISIBLE,
  CONSTRAINT `fk_cobrancas_1`
    FOREIGN KEY (`id_usuarios`)
    REFERENCES `controle_condominio`.`usuarios` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `controle_condominio`.`encomendas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `controle_condominio`.`encomendas` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `titulo` VARCHAR(45) NOT NULL,
  `tipo` VARCHAR(45) NOT NULL,
  `nota_fiscal` VARCHAR(45) NOT NULL,
  `id_usuarios` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_encomendas_1_idx` (`id_usuarios` ASC),
  CONSTRAINT `fk_encomendas_1`
    FOREIGN KEY (`id_usuarios`)
    REFERENCES `controle_condominio`.`usuarios` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `controle_condominio`.`unidades`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `controle_condominio`.`unidades` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `numero` VARCHAR(45) NOT NULL,
  `bloco` VARCHAR(45) NOT NULL,
  `andar` INT NOT NULL,
  `id_usuarios` INT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_unidades_1_idx` (`id_usuarios` ASC),
  CONSTRAINT `fk_unidades_1`
    FOREIGN KEY (`id_usuarios`)
    REFERENCES `controle_condominio`.`usuarios` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `controle_condominio`.`veiculos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `controle_condominio`.`veiculos` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `placa` VARCHAR(45) NOT NULL,
  `marca` VARCHAR(45) NOT NULL,
  `nome_veiculo` VARCHAR(45) NOT NULL,
  `cor` VARCHAR(45) NOT NULL,
  `id_usuarios` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_veiculos_1_idx` (`id_usuarios` ASC),
  CONSTRAINT `fk_veiculos_1`
    FOREIGN KEY (`id_usuarios`)
    REFERENCES `controle_condominio`.`usuarios` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `controle_condominio`.`funcoes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `controle_condominio`.`funcoes` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `funcao` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `controle_condominio`.`rel_funcao_usuario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `controle_condominio`.`rel_funcao_usuario` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `id_usuario` INT NOT NULL,
  `id_funcao` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_funcoes_1_idx` (`id_usuario` ASC),
  INDEX `fk_funcoes_2_idx` (`id_funcao` ASC),
  CONSTRAINT `fk_funcoes_1`
    FOREIGN KEY (`id_usuario`)
    REFERENCES `controle_condominio`.`usuarios` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_funcoes_2`
    FOREIGN KEY (`id_funcao`)
    REFERENCES `controle_condominio`.`funcoes` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
