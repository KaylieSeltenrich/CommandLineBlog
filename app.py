import dbcreds
import mariadb

def InsertPost():

    blog_post = input("Write your blog post: ")
    conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password, host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO blog_post (username, content, id) VALUES(?, ?, NULL)", [username, blog_post])
    conn.commit()
    cursor.close()
    conn.close()

def ReadPosts():

    conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password, host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM blog_post")
    rows = cursor.fetchall()
    print(rows)
    cursor.close()
    conn.close()



username = input("Please write your username: ")
print("Choose an option: ")
print("1: Write a new blog post")
print("2: See all blog posts")

user_choice = input("Please enter your selection: ")

if user_choice == "1":
    InsertPost()

elif user_choice == "2":
    ReadPosts()


else:
    print("Error: Invalid Input!")

