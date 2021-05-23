#!C:/Python38/python
print ("Content-type: text/html\n")


import cgi

form=cgi.FieldStorage()


name=form.getvalue("name")
email=form.getvalue("email")
phone=str(form.getvalue("phone"))

#storing in database

import mysql.connector

#connection = pymysql.connect(host="sql6.freesqldatabase.com",user=" sql6414152",password="hnnpBcxV2a",database="sql6414152" )
connection = mysql.connector.connect(host="sql6.freesqldatabase.com",user=" sql6414152",password="hnnpBcxV2a",database="sql6414152")
cur = connection.cursor()


#Encrypting
import random 
from math import pow
  
a = random.randint(2, 10)
  
def gcd(a, b):
    if a < b:
        return gcd(b, a)
    elif a % b == 0:
        return b;
    else:
        return gcd(b, a % b)
  
# Generating large random numbers
def gen_key(q):
  
    key = random.randint(pow(10, 20), q)
    while gcd(q, key) != 1:
        key = random.randint(pow(10, 20), q)
  
    return key
  
# Modular exponentiation
def power(a, b, c):
    x = 1
    y = a
  
    while b > 0:
        if b % 2 == 0:
            x = (x * y) % c;
        y = (y * y) % c
        b = int(b / 2)
  
    return x % c
  
# Asymmetric encryption
def encrypt(msg, q, h, g, k):
  
    en_msg = []
  
    s = power(h, k, q)
    p = power(g, k, q)
      
    for i in range(0, len(msg)):
        en_msg.append(msg[i])
  
    
    for i in range(0, len(en_msg)):
        en_msg[i] = s * ord(en_msg[i])
  
    return en_msg, p
  
def decrypt(en_msg, p, key, q):
  
    dr_msg = []
    h = power(p, key, q)
    for i in range(0, len(en_msg)):
        dr_msg.append(chr(int(en_msg[i]/h)))
          
    return dr_msg
  
# Driver code
def encryption():
  
    msg1 = name
    msg2 = email
    msg3 = phone
    
    #msg1 = "shivani"
    #msg2 = "email"
    #msg3 = "8978978988"
    
    
    q = random.randint(pow(10, 20), pow(10, 50))
    g = random.randint(2, q)
    k = gen_key(q)# Private key for sender
    
    key = gen_key(q)# Private key for receiver
    h = power(g, key, q)
    
   
    en_msg1, p = encrypt(msg1, q, h, g, k)
    
    
    en_msg2, p = encrypt(msg2, q, h, g, k)
    
    
    en_msg3, p = encrypt(msg3, q, h, g, k)
    
    
    string_ints1 = [str(int) for int in en_msg1]
    en1 = " ".join(string_ints1)
   
    string_ints2 = [str(int) for int in en_msg2]
    en2 = " ".join(string_ints2)
   
    string_ints3 = [str(int) for int in en_msg3]
    en3 = " ".join(string_ints3)

    
    cur.execute("insert into register values(%s,%s,%s)",(en1,en2,en3))
    connection.commit()
    
encryption()

cur.close()
connection.close()


print(''' 
      
<!DOCTYPE html>
<html>
<head>
<title>Client</title>
<link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
<nav class="topnav">
  <h2 class="logo">NIDHI's &nbsp INVENTORY &nbsp MANAGEMENT</h2>
 
 
 
 
 
</nav>
<style>
  .topnav {
  overflow: hidden;
  background-color: black;

}
.logo{
  float: left;
  font-size: 0.6cm;
  padding-left: 0.5cm;
  padding-top: 0.4cm;
  padding-bottom: 0.4cm;
  color:  white;
  font-style: sans-serif;
}
.topnav a {
  float: right;
  color: #f2f2f2;
  text-align: center;
  padding: 0.8cm 0.8cm;
  padding-left: 0.6cm;
  padding-right: 0.6cm;
  text-decoration: none;
  font-size: 17px;

 }
 body {font-family: Arial, Helvetica, sans-serif;
             background-repeat: no-repeat;
              font-family: "Times New Roman";
            background-size: cover;
          }
* {box-sizing: border-box;

}
html{ background-image: url(kk.jpg);}

.topnav a:hover {
  background-color: #ddd;
  color: black;
}

.topnav a.active {
  background-color: #4CAF50;
  color: white;
}
.tp{
  padding: 0.5cm;
  background-color: #9ee6d8;
  color: #455ca8;
  margin-top: 2cm;
}
.tp:hover {
  background-color: #5F9EA0;
  color: black;
}

.tp.active {
  background-color: #5F9EA0;
  color: white;
}
.to{
  padding: 0.5cm;
  background-color: #9ee6d8;
  color: #455ca8;
  margin-top: 2cm;
}
.to:hover {
  background-color: #5F9EA0;
  color: black;
}
  </style>
<div class="header">
<h1>Welcome!!!</h1>
</div>
<div class="content">
  <!-- notification message -->
  

    <!-- logged in user information -->
    
    <p><strong><h2><center>''' +"  "+name.upper()+'''</center></h2> </strong>
   
</div>

</body>
</html>

      ''')
