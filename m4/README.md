# Task 4.1

## Part 1

I've created a database schema for Internet Service Provider, that consits of four tables:

![](./images/image1.png)

![](./images/image2.png)

![](./images/image3.png)

![](./images/image4.png)

![](./images/image5.png)

For "Clients" table, column named "tariff_id" is foreign key, which take its value from table "Tariffs":

![](./images/image6.png)

On MySQL server I've created database "internet_provider":

![](./images/image7.png)

I've switched to my databadse and created tables:

![](./images/image8.png)

Showing information about table:

![](./images/image9.png)

For filling tables previously was prepared CSV files with necessary data.
CSV file with tariffs info:

![](./images/image10.png)

Filling table 'tariffs':

![](./images/image11.png)

Other tables was filled in the same way.

Adding a single row into a table:

![](./images/image12.png)

![](./images/image13.png)

Examples of use different operators with SELECT:

![](./images/image14.png)

![](./images/image15.png)

Creating new user and changing his password:

![](./images/image16.png)

Granting access rights:

![](./images/image17.png)

Using different commands through the created user:

![](./images/image18.png)

## Part 2

I've created backup of my database:

![](./images/image19.png)

I've deleted table from database:

![](./images/image20.png)

and restored previous version of DB from backup:

![](./images/image21.png)

///



## Part 3

I've created AWS Dynamo DB table:

![](./images/image30.png)

List of items that I've added:

![](./images/image31.png)

Examples of use Query and Scan:

![](./images/image32.png)

![](./images/image33.png)

![](./images/image34.png)

![](./images/image35.png)