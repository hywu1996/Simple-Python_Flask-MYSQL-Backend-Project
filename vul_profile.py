@app.route('/vulprofile')
def vulprofile():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    query = ("SELECT * from Attend")
    cursor.execute(query)
    attends=cursor.fetchall()
    
    query = ("SELECT * from Customer")
    cursor.execute(query)
    customers=cursor.fetchall()
    
    query = ("SELECT * from Showing")
    cursor.execute(query)
    showings=cursor.fetchall()
    
    query = ("SELECT Customer.FirstName,Customer.LastName,Showing.ShowingDateTime,Movie.MovieName from Attend,Customer,Showing,Movie WHERE Attend.Customer_idCustomer=Customer.idCustomer AND Attend.Showing_idShowing=Showing.idShowing AND Showing.Movie_idMovie=Movie.idMovie")
    cursor.execute(query)
    paidfors=cursor.fetchall()
    
    cnx.close()
    
    return render_template('vul_profile.html', attends=attends, customers=customers, showings=showings, paidfors=paidfors)
    cnx.close()


    statement = "SELECT * FROM users WHERE name = '" + userName + "';"

@app.route('/myprofile1', methods=["POST"])
def myprofile1():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    stmt = (
        "DROP VIEW IF EXISTS `movie_view`"
    )
    cursor.execute(stmt)

    stmt = (
        "DROP VIEW IF EXISTS `profile_view`"
    )

    cursor.execute(stmt)

    data = (request.form['Customer_idCustomer'])

    stmt1 = (
        "CREATE VIEW `movie_view` AS SELECT `MovieName`, `Rating` FROM `Attend`,`Customer`,`Showing`,`Movie` WHERE  `Customer_idCustomer`=`idCustomer` AND `Showing_idShowing`=`idShowing` AND `Movie_idMovie`=`idMovie` AND `idCustomer` = '" + data + "'"
        )
    # data = (request.form['Customer_idCustomer'])
    cursor.execute(stmt1, data)

    stmt = ("CREATE VIEW `profile_view` AS SELECT `FirstName`, `LastName`, `EmailAddress`, `Sex` FROM `Customer` WHERE  `idCustomer` = '" + data + "'")
    cursor.execute(stmt, data)
    cnx.commit()
    cnx.close()
    
    return redirect('/personalprofile', code=302)