# Install MYSQL

This took me awhile to figure out. So this is for MacOS. If you don't have MySQLm you can download it 2 ways.

1. https://www.mysql.com/

- In the header of the MySQL website, go to the Downloads tab.
- Scroll down and select MySQL Community (GPL) Downloads.
- Select MySQL Community Server.
- In the Select Operating System dropdown menu, select macOS.
- Find the required processor version and select Download.
- Then you will be prompted to either sign up or log in to your Oracle Web account. Just below the buttons, select No thanks, just start my download. The download will commence.

After MySQL is downloaded, you can proceed to the installation process.

- Double-click the downloaded DMG file to open a wizard-like installer. It will tell you it has to determine if the software it contains can be installed. Click Allow. Then you will see links to MySQL-related resources, including the documentation. Click Continue
- On the License page, accept the Software License Agreement by clicking Continue.
- Next, you need to choose the download destination. By default, it's your main hard drive. If you want to change it, click Change Install Location. If you don't, click Install.
- Enter your password, click Install Software, and wait while the files get installed on your Mac.
- On the Configuration page, select Use Strong Password Encryption. Click Next. Enter your MySQL root password, click Finish, and the installation will be complete.

2. Homebrew and Terminal (My preferred way)

- If you haven't previously installed Homebrew on your Mac, open Terminal and execute the following command:

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

- And so, in order to install MySQL, you need to run the following command:

```
brew install mysql
```

- The installation will take a while. After it's finished, you can start your MySQL server with the following command:

```
brew services start mysql
```

- To secure your MySQL with a root password, run the following:

```
mysql_secure_installation
```

**Current password is password set for root**

## How to configure MySQL from the command line

To enable remote access to MySQL, we suggest creating a user with access from a specific IP address ('username'@'192.168.1.100') or from any host ('username'@'%').

To start MySQL command line client, you can run this:

```
mysql -u root -p
```

The -u root flag in the command mysql -u root -p specifies the username to connect to the MySQL server, in this case, "root". The -p flag prompts for a password to authenticate the user. So when you run mysql -u root -p, it will ask you to enter the password for the "root" user.

```
!  IMPORTANT that the Password inputted here is the same password that is set in the settings file
```

### Create database tables

MySQL can be further configured from Terminal. For instance, it allows you to manage users. To create a new database user from Terminal and grant all privileges on all databases, enter the following command, replace "username" with the user you want to create, and replace "password" with the user's password.

Start by creating a database with the following command:

```sql
Create database mydatabase;
```

You can create users like this:

```sql
CREATE USER 'admindjango'@'localhost' IDENTIFIED BY 'password';
```

Grant all privilges to that user;

```sql
GRANT SELECT ON *.* TO 'admindjango'@'localhost';
```

!! I had issues on granting privileges without specifying the table, so I needed to do this (in the case my table or model is called booking):

```sql
GRANT ALL PRIVILEGES ON booking.* TO 'admindjango'@'localhost';
```

THen run this command'

```sql
flush privileges;
```

### Install MySQL DB API Driver

To interface a Python program with MySQL, ensure you have a DB API-compliant driver. There are a number of Python drivers for MySQL available. Django recommends mysqlclientto be used. Install it with pip installer.

```
pip3 install mysqlclient
```

### Enable MySQL

To be able to use MySQL, the DATABASES variable in the Django project’s settings file must be properly configured. By default, it is set to the connection parameters for SQLite. Remove those statements. You have to add MySQL-specific settings in their place.

You must configure at least one database in the DATABASES variable. For the configuration of the first database, its name should be ‘default’.

The settings include the database engine, name of the database, username, and password, along with the host IP address. This defaults to the localhost 127.0.0.10 and the port defaults to 3306.

```py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mydatabase',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        }
    }
}
```

** Must Remove when not use or else you won't be able to sign back in again **

The startprojecttemplate installs some Django apps by default. Some examples include admin, auth and sessions.
Remember that you need to create the necessary database tables for these apps. Run the migrate command to use the models in these apps and build their respective table structure in the current mysql database.

```
python manage.py migrate

```

Inside the MySQL terminal, run the following commands:

```
use mydatabase;
Show tables;

```

## MYSQL via VSCODE

Click on the + button and enter the following details:

```
domain name: localhost
```

```
user:root
```

```
password=''.
```

Note: Some users may encounter an error such as:
Client does not support authentication protocol requested by server; consider upgrading MySQL client
This usually indicates a user privilege issue. In such cases first run a command such as:

     ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password';

Then refresh privileges by running a command such as:

     flush privileges;

Now, the localhost appears in the explorer bar.

# Syntax in MySQL

DESCRIBE `table_name`;

## extra notes:

Since you are using Homebrew on macOS, the commands to stop and start the MySQL server will be different. Please use the following commands:

To stop the MySQL server:
brew services stop mysql

2. Start the MySQL server in safe mode:
   sudo mysqld_safe --skip-grant-tables
