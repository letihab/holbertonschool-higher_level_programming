---get the information_schema
USE `information_schema`;

SELECT TABLE_NAME, CREATE_TABLE_STATEMENT
FROM TABLES
WHERE TABLE_SCHEMA = 'hbtn_0c_0'
    AND TABLE_NAME = 'first_table';
