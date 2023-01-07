onnect to the MySQL server as the root user

import os



-- Create the hbnb_dev_db database

os.system("mysql -u root -pyour_root_password -e 'CREATE DATABASE IF NOT EXISTS hbnb_dev_db'")



-- Create the hbnb_dev user

os.system("mysql -u root -pyour_root_password -e \"CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd'\"")



-- Grant all privileges on the hbnb_dev_db database to the hbnb_dev user

os.system("mysql -u root -pyour_root_password -e \"GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost'\"")

os.system("mysql -u root -pyour_root_password -e 'FLUSH PRIVILEGES'")



-- Grant SELECT privilege on the performance_schema database to the hbnb_dev user

os.system("mysql -u root -pyour_root_password -e \"GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost'\"")

os.system("mysql -u root -pyour_root_password -e 'FLUSH PRIVILEGES'")


