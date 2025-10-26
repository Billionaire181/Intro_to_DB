USE alx_book_store;
SELECT
    COLUMN_NAME as "column"
    COLUMN_TYPE as "type"

FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = 'alx_book_store'
AND TABLE_NAME = 'Books'