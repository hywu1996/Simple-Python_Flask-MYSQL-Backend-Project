@app.route('/buy')
def buy():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    SQLquery = ("SELECT * from Attend")
    cursor.execute(SQLquery)
    attends=cursor.fetchall()
	
    SQLquery = ("SELECT * from Customer")
    cursor.execute(SQLquery)
    customers=cursor.fetchall()
	
    SQLquery = ("SELECT Showing.idShowing,Movie.MovieName,Showing.ShowingDateTime from Showing,Movie WHERE Showing.Movie_idMovie=Movie.idMovie")
    cursor.execute(SQLquery)
    ms=cursor.fetchall()

    SQLquery = ("SELECT Customer.FirstName,Customer.LastName,Showing.ShowingDateTime,Movie.MovieName from Attend,Customer,Showing,Movie WHERE Attend.Customer_idCustomer=Customer.idCustomer AND Attend.Showing_idShowing=Showing.idShowing AND Showing.Movie_idMovie=Movie.idMovie ORDER BY Attend.Rating DESC")
    cursor.execute(SQLquery)
    paidfors=cursor.fetchall()

    cnx.close()
	
    return render_template('buyticket.html', attends=attends, customers=customers, ms=ms, paidfors=paidfors)

@app.route('/addbuy', methods=["POST"])
def addbuy():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    SQLquery = (
        "INSERT INTO `Attend` (`Customer_idCustomer`, `Showing_idShowing`) "
        "VALUES (%s, %s)"
    )
    data = (request.form['Customer_idCustomer'], request.form['Showing_idShowing'])
    cursor.execute(SQLquery, data)
    cnx.commit()
    cnx.close()
    
    return redirect("/success", code=302)
