#!C:/Python38/python
print ("Content-type: text/html\n")

print('''
<!DOCTYPE html>
<html>
<head>
  <title>Registration form</title>
  <link rel="stylesheet" type="text/css" href="style.css">
</head>
<style>
  * {
  margin: 0px;
  padding: 0px;
}
body {
            background-image: url(i.jpg);
            background-repeat: no-repeat;
            -webkit-background-size: cover;
            background-size: cover;
 }

.header {
  width: 30%;
  margin: 50px auto 0px;
  color: white;
  background: black;
  text-align: center;
  border: 1px solid black;
  border-bottom: none;
  border-radius: 10px 10px 0px 0px;
  padding: 20px;
}
form, .content {
  width: 30%;
  margin: 0px auto;
  padding: 20px;
  border: 1px solid #B0C4DE;
  background: #a8a8a8;
  border-radius: 0px 0px 20px 20px;
}
.input-group {
  margin: 10px 0px 10px 0px;
}
.input-group label {
  display: block;
  text-align: left;
  margin: 3px;
}
.input-group input {
  height: 30px;
  width: 93%;
  padding: 5px 10px;
  font-size: 16px;
  border-radius: 5px;
  border: 1px solid gray;
}
.btn {
  padding-top: 20px;
  padding-bottom: 20px;
  padding-left: 1cm;
  padding-right: 1cm;
  font-size: 15px;
  color: white;
  background: black;
  border: none;
  margin-left:4cm;
  margin-top: 1cm;
  border-radius: 5px;

}
.error {
  width: 92%;
  margin: 0px auto;
  padding: 10px;
  border: 1px solid #a94442;
  color: #a94442;
  background: #f2dede;
  border-radius: 5px;
  text-align: left;
}
.success {
  color: #3c763d;
  background: #dff0d8;
  border: 1px solid #3c763d;
  margin-bottom: 20px;
}
  </style>
<body>
  <center><br><br><h1 style="color:white">Grofoods.com</h1>
  </center>   
  <br><br>
  <div class="header">
    <title>Registration form</title>
    
    <h2>Enter your details</h2>
  </div>
 
  <form action="register.py" method="post" >
   
    <div class="input-group">
      <label>Name</label>
      <input type="text" name="name">
    </div>
    <div class="input-group">
      <label>Email</label>
      <input type="email" name="email" >
    </div>
	<div class="input-group">
      <label>Phone</label>
      <input type="number" name="phone">
    </div>
    <div class="input-group">
      <button type="submit" class="btn" name="reg_user">Submit</button>
    </div>
    
  </form>
</body>
</html>
''')
