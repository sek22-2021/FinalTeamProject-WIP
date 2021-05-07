CREATE DATABASE calcData;
use calcData;

CREATE TABLE IF NOT EXISTS tblCalcNumbers
(
    `id` int(3) AUTO_INCREMENT,
   `num1` INT,
    `num2` INT,
    `add` INT,
    `subtract` INT,
    `multiply` INT,
    `divide` NUMERIC(2, 1),
    `square` INT,
    `squareRoot` NUMERIC(10, 9),
    PRIMARY KEY (`id`)
   );

INSERT INTO tblCalcNumbers (num1, num2, `add`, subtract, multiply, divide, square, squareRoot )
VALUES
    (2,1,3,1,2,2,4,1.414213562),
    (5,2,7,3,10,2.5,25,2.236067977),
    (4,1,5,3,4,4,16,2),
    (3,3,6,0,9,1,9,1.732050808),
    (6,4,10,2,24,1.5,36,2.449489743);
