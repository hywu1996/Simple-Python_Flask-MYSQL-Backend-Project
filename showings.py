@app.route('/showings')
def showings():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    SQLquery = ("SELECT * from Showing ORDER BY ShowingDateTime ASC")
    cursor.execute(SQLquery)
    showings=cursor.fetchall()
	
    SQLquery = ("SELECT * from TheatreRoom")
    cursor.execute(SQLquery)
    rooms=cursor.fetchall()
	
    SQLquery = ("SELECT * from Movie")
    cursor.execute(SQLquery)
    movies=cursor.fetchall()
    
    SQLquery = ("SELECT Showing.idShowing,Showing.ShowingDateTime,Movie.MovieName, Showing.TheatreRoom_RoomNumber, Showing.TicketPrice, TheatreRoom.Capacity from TheatreRoom,Showing,Movie WHERE Showing.Movie_idMovie=Movie.idMovie AND TheatreRoom.RoomNumber=Showing.TheatreRoom_RoomNumber")
    cursor.execute(SQLquery)
    fullShowingID=cursor.fetchall()

    SQLquery = ("SELECT Showing.idShowing,Showing.ShowingDateTime,Movie.MovieName, Showing.TheatreRoom_RoomNumber, Showing.TicketPrice, TheatreRoom.Capacity from TheatreRoom,Showing,Movie WHERE Showing.Movie_idMovie=Movie.idMovie AND TheatreRoom.RoomNumber=Showing.TheatreRoom_RoomNumber ORDER BY Showing.ShowingDateTime ASC")
    cursor.execute(SQLquery)
    fullShowing=cursor.fetchall()

    cnx.close()
	
    return render_template('showings.html', showings=showings, rooms=rooms, movies=movies, fullShowingID=fullShowingID, fullShowing=fullShowing)

@app.route('/addshowing', methods=["POST"])
def addshowing():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    SQLquery = (
        "INSERT INTO `Showing` (`ShowingDateTime`, `Movie_idMovie`, `TheatreRoom_RoomNumber`, `TicketPrice`) "
        "VALUES (%s, %s, %s, %s)"
    )
    data = (request.form['ShowingDateTime'], request.form['Movie_idMovie'], request.form['TheatreRoom_RoomNumber'], request.form['TicketPrice'])
    cursor.execute(SQLquery, data)
    cnx.commit()
    cnx.close()

    return redirect("/showings", code=302)
	
@app.route('/deleteshowing', methods=["POST"])
def deleteshowing():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    SQLquery = ("DELETE FROM `Showing` WHERE `idShowing` = %s")
    data = request.form['idShowing']
    cursor.execute(SQLquery, (data,))
    cnx.commit()
    cnx.close()
	
    return redirect("/showings", code=302)
	
@app.route('/modifyshowing', methods=["POST"])
def modifyshowing():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    SQLquery = ("UPDATE `Showing` SET `ShowingDateTime` = %s, `Movie_idMovie` = %s, `TheatreRoom_RoomNumber` = %s, `TicketPrice` = %s WHERE `idShowing` = %s")
    data = (request.form['ShowingDateTime'], request.form['Movie_idMovie'], request.form['TheatreRoom_RoomNumber'], request.form['TicketPrice'], request.form['idShowing'])
    cursor.execute(SQLquery, data)
    cnx.commit()
    cnx.close()
	
    return redirect("/showings", code=302)