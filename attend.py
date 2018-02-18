@app.route('/attends')
def attends():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
	
    SQLquery = ("SELECT Customer.FirstName,Customer.LastName,Showing.idShowing, Showing.ShowingDateTime,Movie.MovieName, Attend.Rating from Attend,Customer,Showing,Movie WHERE Attend.Customer_idCustomer=Customer.idCustomer AND Attend.Showing_idShowing=Showing.idShowing AND Showing.Movie_idMovie=Movie.idMovie ORDER BY Attend.Rating DESC")
    cursor.execute(SQLquery)
    paid=cursor.fetchall()
	
    cnx.close()
	
    return render_template('attend.html', paid=paid)

@app.route('/addattend', methods=["POST"])
def addattend():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    SQLquery = (
        "INSERT INTO `Attend` (`Customer_idCustomer`, `Showing_idShowing`, `Rating`) "
        "VALUES (%s, %s, %s)"
    )
    data = (request.form['Customer_idCustomer'], request.form['Showing_idShowing'], request.form['Rating'])
    cursor.execute(SQLquery, data)
    cnx.commit()
    cnx.close()
	
    return redirect("/attends", code=302)
	
@app.route('/deleteattend', methods=["POST"])
def deleteattend():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    SQLquery = ("DELETE FROM `Attend` WHERE `Customer_idCustomer` = %s AND `Showing_idShowing` = %s")
    split_data = request.form['Attend'].split(':')
    data = (split_data[0], split_data[1])
    cursor.execute(SQLquery, data)
    cnx.commit()
    cnx.close()
	
    return redirect("/attends", code=302)
	
@app.route('/modifyattend', methods=["POST"])
def modifyattend():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    SQLquery = ("UPDATE `Attend` SET `Customer_idCustomer` = %s, `Showing_idShowing` = %s, `Rating` = %s WHERE `Customer_idCustomer` = %s AND `Showing_idShowing` = %s")
    split_data = request.form['Attend'].split(':')
    data = (request.form['Customer_idCustomer'], request.form['Showing_idShowing'], request.form['Rating'], split_data[0], split_data[1])
    cursor.execute(SQLquery, data)
    cnx.commit()
    cnx.close()
	
    return redirect("/attends", code=302)