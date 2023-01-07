import mysql.connector



-- Connect to the MySQL server as the root user

conn = mysql.connector.connect(user='root', password='your_root_password', host='localhost')

cursor = conn.cursor()



-- Create the hbnb_dev_db database

cursor.execute('CREATE DATABASE IF NOT EXISTS hbnb_dev_db')



-- Create the hbnb_dev user

cursor.execute("CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd'")



-- Grant all privileges on the hbnb_dev_db database to the hbnb_dev user

cursor.execute("GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost'")



-- Grant SELECT privilege on the performance_schema database to the hbnb_dev user

cursor.execute("GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost'")



-- Commit the changes

conn.commit()



-- Close the connection

conn.close()


