create table USER_EARNING_PATTERN (USER_ID INT,EARN_TYPE VARCHAR(50),EARN_DATE varchar(50), EARN_AMOUNT DOUBLE,PRIMARY KEY(USER_ID ))
create table BENEFITS (BENEFIT_ID INT, BENEFIR_DESC VARCHAR(150), DISCOUNT_AMT DOUBLE,DISCOUNT_START_DT varchar(50), DISCOUNT_END_DT varchar(50))
CREATE TABLE USER_SPENDING_PATTERN( user_id INT, transaction_date varchar(50), transaction_amount double,
 expense_type varchar(50),
expense_detail varchar(50),
   payment_option varchar(50),
   payment_detail varchar(50),
   benefit_availed varchar(10),
   benefit_id INT,
   PRIMARY KEY ( user_id )  
);

