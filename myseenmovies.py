@app.route('/myseenmovies')
def myseenmovies():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    SQLquery = ("SELECT * from customer_view")
    cursor.execute(SQLquery)
    mymovies=cursor.fetchall()
	
    # SQLquery = ("SELECT * from Customer")
    # cursor.execute(SQLquery)
    # customers=cursor.fetchall()
	
    # SQLquery = ("SELECT * from Showing")
    # cursor.execute(SQLquery)
    # showings=cursor.fetchall()
	
    # SQLquery = ("SELECT Customer.FirstName,Customer.LastName,Showing.ShowingDateTime,Movie.MovieName from Attend,Customer,Showing,Movie WHERE Attend.Customer_idCustomer=Customer.idCustomer AND Attend.Showing_idShowing=Showing.idShowing AND Showing.Movie_idMovie=Movie.idMovie")
    # cursor.execute(SQLquery)
    # paidfors=cursor.fetchall()
	
    cnx.close()
    
    return render_template('myseenmovies.html', mymovies=mymovies)


# @app.route('/mymovies', methods=["POST"])
# def mymovies():
#     cnx = mysql.connector.connect(user='root', database='MovieTheatre')
#     cursor = cnx.cursor()
#     SQLquery = (
#         "DROP VIEW IF EXISTS `customer_view`"
#     )
#     cursor.execute(SQLquery)

#     stmt1 = (
#         "CREATE VIEW `customer_view` AS SELECT `MovieName` FROM `Attend`,`Customer`,`Showing`,`Movie` WHERE  `Customer_idCustomer`=`idCustomer` AND `Showing_idShowing`=`idShowing` AND `Movie_idMovie`=`idMovie` AND `idCustomer` = 1 "
#         )
#     data = (request.form['Customer_idCustomer'])
#     cursor.execute(stmt1, data)
#     cnx.commit()
#     cnx.close()
    
#     return redirect("/myseenmovies", code=302)