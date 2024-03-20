-- SQL script that creates a trigger that resets valid_email attribute
-- the attribute valid_email
DELIMITER $$
CREATE TRIGGER reset
BEFORE UPDATE
ON users
FOR EACH ROW
BEGIN
    IF NEW.email != OLD.email THEN
        SET NEW.valid_email = 0;
    END IF;
END $$

DELIMITER;
