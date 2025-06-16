    -- Example stored procedure definition (your_procedure.sql)
   CREATE OR REPLACE PROCEDURE add_and_log_user(IN user_name VARCHAR(255), IN user_email VARCHAR(255))
LANGUAGE plpgsql
AS $$
BEGIN
  -- Insert the user
  INSERT INTO users (name, email) VALUES (user_name, user_email);

  -- Log the action
  INSERT INTO audit_log (action, details) VALUES ('add_user', 'User ' || user_name || ' added.');

  -- Commit the transaction (optional, if not part of a larger transaction)
  COMMIT;
END $$;
