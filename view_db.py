import sqlite3

# Connect to the database
conn = sqlite3.connect('golf_course_results.db')
cursor = conn.cursor()

# Execute a query to retrieve all records
cursor.execute("SELECT * FROM golf_course_results")

# Execute a query to retrieve all records from a chosen golf course
# cursor.execute("SELECT * FROM golf_course_results WHERE course = 'Valhalla'")

# Execute a query to retrieve all records from a selected wind speed
# cursor.execute("SELECT * FROM golf_course_results WHERE wind_speed = '10 to 15'")

# Fetch all results from the executed query
results = cursor.fetchall()

# Print column names
column_names = [description[0] for description in cursor.description]
print(column_names)

# Print each row in the results
for row in results:
    print(row)

# Close the connection
conn.close()
