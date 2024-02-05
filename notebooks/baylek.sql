
DROP TABLE IF EXISTS test;
CREATE TABLE test (
    id serial PRIMARY KEY,
    num integer,
    data text
);
INSERT INTO test (num, data) 
VALUES (6000, 'HHH'), (800, 'BBB');

DROP TABLE IF EXISTS doctors;
nom	genre	specialite	address_dsp	daira	telephone	lat	lng
CREATE TABLE doctors(
    id serial NOT NULL,
    nom varchar(100) NOT NULL,
    genre varchar(8) NOT NULL,
    specialite varchar(100),
    address_dsp varchar(300)
    daira varchar(50), 
    telephone varchar(50), 
telephone

);
