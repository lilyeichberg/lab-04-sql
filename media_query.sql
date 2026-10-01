SELECT
    u.username,
    u.email,
    p.title,
    p.created_at
FROM posts AS p
JOIN users AS u ON p.user_id = u.user_id
WHERE p.created_at >= '2026-09-15 00:00:00'
ORDER BY p.created_at;
