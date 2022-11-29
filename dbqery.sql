CREATE TABLE `workers`.`workers` (
  `workerid` INT NOT NULL AUTO_INCREMENT,
  `firstname` VARCHAR(45) NULL,
  `lastname` VARCHAR(45) NULL,
  `age` INT NULL,
  `id` VARCHAR(45) NULL,
  `email` VARCHAR(45) NULL,
  `profession` VARCHAR(45) NULL,
  `salary` INT NULL,
  `experience` INT NULL,
  `department` VARCHAR(45) NULL,
  PRIMARY KEY (`workerid`));

ALTER TABLE `workers`.`workers` 
ADD UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE;
;