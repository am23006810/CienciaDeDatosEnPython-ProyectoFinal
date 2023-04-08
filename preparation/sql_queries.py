DDL_QUERY =  '''
CREATE TABLE IF NOT EXISTS rose_wine(
    Name VARCHAR(70),
    Country VARCHAR(20),
    Region VARCHAR(40),
    Winery VARCHAR(70),
    Rating float,
    NumberOfRatings int,
    Price float,
    Year VARCHAR(10)
);
'''