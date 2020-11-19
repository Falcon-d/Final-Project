CREATE TABLE stock_results (
	index VARCHAR,
    predicted VARCHAR (30) NOT NULL,
	actual VARCHAR (30),
	difference VARCHAR (30),
	Date DATE );


ALTER TABLE stock_results
DROP COLUMN index;

select * from stock_results

CREATE TABLE sp_history (
	Date DATE,
    Close VARCHAR (30) NOT NULL,
	Volume VARCHAR (30),
	Open VARCHAR (30),
	High VARCHAR ,
	Low VARCHAR
);

select * from sp_history