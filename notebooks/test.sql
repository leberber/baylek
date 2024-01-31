
DROP TABLE IF EXISTS test;
CREATE TABLE test (
    id serial PRIMARY KEY,
    num integer,
    data text
);
INSERT INTO test (num, data) 
VALUES (6000, 'HHH'), (800, 'BBB');
