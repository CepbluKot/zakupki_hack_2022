-- Для работы скрипта нужно переименовать датасеты соответсвенно: table_1, table_2, table_3 
-- (так как постгрес не видит файлов с русским текстом в наименовании)
-- Не забудьте прописать директорию, где находятся ваши файлы

-- table_1
drop table IF EXISTS table_1;
create TABLE table_1
(
  product_name TEXT,
  price TEXT,
  product_vat_rate TEXT,
  product_msr TEXT,
  product_characteristics TEXT,
  okpd2_code TEXT,
  okpd2_name TEXT,
  inn TEXT,
  country_code TEXT
);

copy table_1
  from '/Users/igormalysh/Documents/codes/zakupki/data/contracts44fz.csv' -- Впишите вашу директорию
  (FORMAT csv, DELIMITER ';', HEADER, ENCODING 'utf8');


-- SELECT * 
--   FROM table_1;




-- table_1
drop table IF EXISTS table_2;
create TABLE table_2
(
  product_name TEXT,
  price TEXT,
  product_vat_rate TEXT,
  product_msr TEXT,
  product_characteristics TEXT,
  okpd2_code TEXT,
  okpd2_name TEXT,
  inn TEXT,
  country_code TEXT
);

copy table_2
  from '/Users/igormalysh/Documents/codes/zakupki/data/directory.csv' -- Впишите вашу директорию
  (FORMAT csv, DELIMITER ';', HEADER, ENCODING 'utf8');


-- SELECT * 
--   FROM table_2;





-- table_3
drop table IF EXISTS table_3;
create TABLE table_3
(
  product_name TEXT,
  price TEXT,
  product_vat_rate TEXT,
  product_msr TEXT,
  product_characteristics TEXT,
  okpd2_code TEXT,
  okpd2_name TEXT,
  inn TEXT,
  country_code TEXT
);

copy table_3
  from '/Users/igormalysh/Documents/codes/zakupki/data/price_offer.csv' -- Впишите вашу директорию
  (FORMAT csv, DELIMITER ';', HEADER, ENCODING 'utf8');


-- SELECT * 
--   FROM table_3;







-- country_directory
-- drop table IF EXISTS country_dir;
-- create TABLE country_dir
-- (
--   country_name TEXT,
--   country_code TEXT
-- );

-- copy country_dir
--   from '/Users/igormalysh/Documents/codes/zakupki/data/country_directory.csv' -- Впишите вашу директорию
--   (FORMAT csv, DELIMITER ';', HEADER, ENCODING 'utf8');


-- SELECT * 
--   FROM country_dir;