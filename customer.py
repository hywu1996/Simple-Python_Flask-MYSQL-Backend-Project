@app.route('/customers')
def customers():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    SQLquery = ("SELECT * from Customer ORDER BY LastName ASC")
    cursor.execute(SQLquery)
    customers=cursor.fetchall()
    cnx.close()
	
    return render_template('customer.html', customers=customers)

@app.route('/addcustomer', methods=["POST"])
def addcustomer():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    SQLquery = (
        "INSERT INTO `Customer` (`FirstName`, `LastName`, `EmailAddress`, `Sex`) "
        "VALUES (%s, %s, %s, %s)"
    )
    data = (request.form['FirstName'], request.form['LastName'], request.form['EmailAddress'], request.form['Sex'])
    cursor.execute(SQLquery, data)
    cnx.commit()
    cnx.close()

    return redirect("/customers", code=302)
	
@app.route('/deletecustomer', methods=["POST"])
def deletecustomer():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    SQLquery = ("DELETE FROM `Customer` WHERE `idCustomer` = %s")
    data = request.form['idCustomer']
    cursor.execute(SQLquery, (data,))
    cnx.commit()
    cnx.close()
	
    return redirect("/customers", code=302)
	
@app.route('/modifycustomer', methods=["POST"])
def modifycustomer():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    SQLquery = ("UPDATE `Customer` SET `FirstName` = %s, `LastName` = %s, `EmailAddress` = %s, `Sex` = %s WHERE `idCustomer` = %s")
    data = (request.form['FirstName'], request.form['LastName'], request.form['EmailAddress'], request.form['Sex'], request.form['idCustomer'])
    cursor.execute(SQLquery, data)
    cnx.commit()
    cnx.close()
	
    return redirect("/customers", code=302)