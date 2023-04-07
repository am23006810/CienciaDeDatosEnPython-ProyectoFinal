DDL_QUERY =  '''
CREATE TABLE IF NOT EXISTS rose_wine(
    name VARCHAR(70),
    country VARCHAR(20),
    region VARCHAR(40),
    winery VARCHAR(50),
    rating float,
    number_of_ratings int,
    price float,
    year VARCHAR(10)
);
'''