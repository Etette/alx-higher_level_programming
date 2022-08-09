-- Write a script that converts hbtn_0c_0 db to UTF8
-- convert db, first_table and name in first_table to UTF8(utf8mb4, collate utf8mb4_unicode_ci)

-- convert db hbtn_0c_0
ALTER DATABASE hbtn_0c_0
CHARACTER SET utf8mb4
COLLATE utf8mb4_uncode_ci

-- convert first_table
USE hbtn_0c_0;
ALTER TABLE first_table
CONVERT TO CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci

-- convert field 'name' in 'first_table'
USE hbtn_0c_0;
ALTER TABLE first_table
CHANGE name name VARCHAR(256)
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

