-- Create table (SQLite syntax) - managed by SQLAlchemy normally
CREATE TABLE IF NOT EXISTS items (
  id INTEGER PRIMARY KEY,
  name TEXT UNIQUE,
  description TEXT
);

-- Insert sample rows
INSERT INTO items (name, description) VALUES ('First', 'First item');
INSERT INTO items (name, description) VALUES ('Second', 'Second item');

-- Query
SELECT * FROM items;


