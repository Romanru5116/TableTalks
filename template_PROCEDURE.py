pip install psycopg2
    import psycopg2

    try:
        conn = psycopg2.connect(
            host="your_host",
            database="your_database",
            user="your_user",
            password="your_password"
        )
        cursor = conn.cursor()
        print("Connected to PostgreSQL successfully!")
    except Exception as e:
        print(f"Error connecting to PostgreSQL: {e}")
      
        def call_stored_procedure(procedure_name, *args):
      try:
          cursor.execute(f"CALL {procedure_name}({', '.join(['%s'] * len(args))});", args)
          conn.commit()
          print("Stored procedure executed successfully.")
      except Exception as e:
          print(f"Error executing stored procedure: {e}")
    # Example usage
    --call_stored_procedure("your_procedure_name", "param1_value", 2, "param3_value")
