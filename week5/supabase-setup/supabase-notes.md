# Supabase Setup

1. Create Supabase Account [image1]
2. Create a new project [image2]
3. Create a Database. Keep the password safe. This is the master password for your database. [image3]
4. Go to the table editor [image4]
5. Create a table [image5]
6. Add columns to your table [image6]
7. Insert data into your table pt 1. [image7]
8. Insert data into your table pt 2. [image8]
9. Add more data. (At least 3 rows!)
10. Add some policies to allow view and reading of data
    0. Find find the RLS Policy for the table [image9a] [image9b]
    1. Allow Public to read [image9] Click on the first template to the left.
    2. Allow Public to write [image10] (Only for demo apps). Add a policy name, click "Insert", add "true" to the with check statement in the policy. And Click save.
11. Your table is set up and ready to connect to your app!