# sql_from_csv

This little script takes a `.tsv` or `.csv` file and reads its column names. Then it creates a `.txt` file (same filename) with a `CREATE TABLE` SQL statement, that has all the correct names for the columns. 

Currently all column types are set to `STRING` because I generally work with SQLite which is very flexible with data types.


