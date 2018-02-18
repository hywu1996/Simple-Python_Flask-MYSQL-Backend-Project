@app.route('/profile')
def profile():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    SQLquery = ("SELECT * from Attend")
    cursor.execute(SQLquery)
    attends=cursor.fetchall()
    
    SQLquery = ("SELECT * from Customer")
    cursor.execute(SQLquery)
    customers=cursor.fetchall()
    
    SQLquery = ("SELECT * from Showing")
    cursor.execute(SQLquery)
    showings=cursor.fetchall()
    
    SQLquery = ("SELECT Customer.FirstName,Customer.LastName,Showing.ShowingDateTime,Movie.MovieName from Attend,Customer,Showing,Movie WHERE Attend.Customer_idCustomer=Customer.idCustomer AND Attend.Showing_idShowing=Showing.idShowing AND Showing.Movie_idMovie=Movie.idMovie")
    cursor.execute(SQLquery)
    paidfors=cursor.fetchall()
    
    cnx.close()
    
    return render_template('profile.html', attends=attends, customers=customers, showings=showings, paidfors=paidfors)
    cnx.close()

@app.route('/myprofile', methods=["POST"])
def myprofile():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    SQLquery = (
        "DROP VIEW IF EXISTS `movie_view`"
    )
    cursor.execute(SQLquery)

    SQLquery = (
        "DROP VIEW IF EXISTS `profile_view`"
    )

    cursor.execute(SQLquery)

    data = (request.form['Customer_idCustomer'])

    stmt1 = (
        "CREATE VIEW `movie_view` AS SELECT `MovieName`, `Rating` FROM `Attend`,`Customer`,`Showing`,`Movie` WHERE  `Customer_idCustomer`=`idCustomer` AND `Showing_idShowing`=`idShowing` AND `Movie_idMovie`=`idMovie` AND `idCustomer` ="+data
        )
    # data = (request.form['Customer_idCustomer'])
    cursor.execute(stmt1)

    SQLquery = (
         "CREATE VIEW `profile_view` AS SELECT `FirstName`, `LastName`, `EmailAddress`, `Sex` FROM `Customer` WHERE  `idCustomer` ="+data
        )
    cursor.execute(SQLquery)
    cnx.commit()
    cnx.close()
    
    return redirect('/personalprofile', code=302)