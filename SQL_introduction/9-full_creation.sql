-- creates a table second_table in the database
CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT
);
INSERT INTO second_table (id, name, score) VALUES
    (1, 'John', 100),
    (2, 'Alex', 90),
    (3, 'Bob', 85),
    (4, 'George', 8);