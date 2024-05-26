CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TEMP TABLE temp_table_single_column (
    "STT" TEXT,
    "Tên" TEXT,
    "Họ" TEXT,
    "Tên đệm" TEXT,
    "Họ và tên" TEXT,
    "Năm" TEXT,
    "Email" TEXT,
    "SĐT" TEXT,
    "Giới tính" TEXT,
    "Trường" TEXT,
    "Quốc gia" TEXT
);

COPY temp_table_single_column FROM '/data/data.csv' WITH (FORMAT csv, HEADER true, ENCODING 'UTF8');

INSERT INTO members_member ("unique_id", "full_name", "gender", "institution")
SELECT uuid_generate_v4(), "Họ và tên", "Giới tính", "Trường" FROM temp_table_single_column;

DROP TABLE temp_table_single_column;

SELECT * FROM members_member;
