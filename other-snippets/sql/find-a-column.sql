-- Only works in MySQL, this is from: http://vanirsystems.com/blog/2010/08/12/mysql-find-a-column/

SELECT * FROM `information_schema`.`COLUMNS` WHERE TABLE_SCHEMA = "databasename" and COLUMN_NAME = "columnname";
