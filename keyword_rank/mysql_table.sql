create database amazon_db;

create table keyword_rank
(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    country_code VARCHAR(150)  NOT NULL,
    asin  VARCHAR(150)  NOT NULL,
    item_title  VARCHAR(2000)  NOT NULL,
    keyword  VARCHAR(500)  NOT NULL,
    keyword_type  VARCHAR(500)  NOT NULL,
    rank_page  INT DEFAULT 0,
    rank_rowid  INT DEFAULT 0,
    search_date  DATE NOT NULL,
    search_time  TIME NOT NULL,
    UNIQUE KEY `asin_keyword_searchdate` (`asin`,`keyword`,`search_date`)
)ENGINE=InnoDB CHARSET=UTF8;