CREATE TABLE IF NOT EXISTS test_data (
    id SERIAL PRIMARY KEY,
    message TEXT NOT NULL
);

INSERT INTO test_data (message) VALUES
('Hello from PostgreSQL'),
('Docker Compose is working'),
('Flask backend connected to DB');
