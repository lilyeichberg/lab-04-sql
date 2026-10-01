DROP TABLE IF EXISTS posts;
DROP TABLE IF EXISTS users;

CREATE TABLE users (
    user_id INT PRIMARY KEY,
    username VARCHAR(50),
    email VARCHAR(100),
    created_at DATETIME
);

CREATE TABLE posts (
    post_id INT PRIMARY KEY,
    user_id INT,
    title VARCHAR(100),
    content TEXT,
    created_at DATETIME,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

INSERT INTO users (user_id, username, email, created_at) VALUES (1, 'alice', 'alice@example.com', '2026-09-01 10:00:00');
INSERT INTO users (user_id, username, email, created_at) VALUES (2, 'bob', 'bob@example.com', '2026-09-02 11:00:00');
INSERT INTO users (user_id, username, email, created_at) VALUES (3, 'charlie', 'charlie@example.com', '2026-09-03 12:00:00');
INSERT INTO users (user_id, username, email, created_at) VALUES (4, 'diana', 'diana@example.com', '2026-09-04 13:00:00');
INSERT INTO users (user_id, username, email, created_at) VALUES (5, 'ethan', 'ethan@example.com', '2026-09-05 14:00:00');
INSERT INTO users (user_id, username, email, created_at) VALUES (6, 'fiona', 'fiona@example.com', '2026-09-06 15:00:00');
INSERT INTO users (user_id, username, email, created_at) VALUES (7, 'george', 'george@example.com', '2026-09-07 16:00:00');
INSERT INTO users (user_id, username, email, created_at) VALUES (8, 'hannah', 'hannah@example.com', '2026-09-08 17:00:00');
INSERT INTO users (user_id, username, email, created_at) VALUES (9, 'ian', 'ian@example.com', '2026-09-09 18:00:00');
INSERT INTO users (user_id, username, email, created_at) VALUES (10, 'julia', 'julia@example.com', '2026-09-10 19:00:00');

INSERT INTO posts (post_id, user_id, title, content, created_at) VALUES (1, 1, 'First Post', 'Hello everyone!', '2026-09-11 10:00:00');
INSERT INTO posts (post_id, user_id, title, content, created_at) VALUES (2, 2, 'SQL Practice', 'I am learning SQL.', '2026-09-12 11:00:00');
INSERT INTO posts (post_id, user_id, title, content, created_at) VALUES (3, 3, 'Database Fun', 'Databases are useful.', '2026-09-13 12:00:00');
INSERT INTO posts (post_id, user_id, title, content, created_at) VALUES (4, 4, 'My Project', 'Working on a new project.', '2026-09-14 13:00:00');
INSERT INTO posts (post_id, user_id, title, content, created_at) VALUES (5, 5, 'Study Time', 'Time to study SQL.', '2026-09-15 14:00:00');
INSERT INTO posts (post_id, user_id, title, content, created_at) VALUES (6, 6, 'Lunch', 'Just had a great lunch.', '2026-09-16 15:00:00');
INSERT INTO posts (post_id, user_id, title, content, created_at) VALUES (7, 7, 'Weekend', 'Looking forward to the weekend.', '2026-09-17 16:00:00');
INSERT INTO posts (post_id, user_id, title, content, created_at) VALUES (8, 8, 'Class Update', 'Class is going well.', '2026-09-18 17:00:00');
INSERT INTO posts (post_id, user_id, title, content, created_at) VALUES (9, 9, 'New Idea', 'I have a new idea.', '2026-09-19 18:00:00');
INSERT INTO posts (post_id, user_id, title, content, created_at) VALUES (10, 10, 'Goodbye', 'See you next time!', '2026-09-20 19:00:00');
