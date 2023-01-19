import pymysql
  
def mysqlconnect():
    # To connect MySQL database
    conn = pymysql.connect(
        host='mysql',
        user='root', 
        password = "password",
        db='db',
        )
      
    cur = conn.cursor()
    cur.execute("select * from students")
    output = cur.fetchall()
    print(output)
      
    # To close the connection
    conn.close()
  
# Driver Code
if __name__ == "__main__" :
    mysqlconnect()