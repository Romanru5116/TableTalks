    -- Example stored procedure definition (your_procedure.sql)
    CREATE OR REPLACE PROCEDURE your_procedure_name(param1 TEXT, param2 INT, param3 TEXT)
    LANGUAGE postgresql
    AS $$
    BEGIN
      -- Your procedure logic here
      INSERT INTO your_table (column1, column2, column3)
      VALUES (param1, param2, param3);
    END;
    $$;
