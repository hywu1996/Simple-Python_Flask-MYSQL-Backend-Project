@app.route('/movies')
def movies():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    SQLquery = ("SELECT * from Movie ORDER BY MovieName ASC")
    cursor.execute(SQLquery)
    movieinfo=cursor.fetchall()
    cnx.close()
	
    return render_template('movies.html', movieinfo=movieinfo)

@app.route('/addmovie', methods=["POST"])
def addmovie():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    SQLquery = (
        "INSERT INTO `Movie` (`MovieName`, `MovieYear`) "
        "VALUES (%s, %s)"
    )
    data = (request.form['Name'], request.form['Year'])
    cursor.execute(SQLquery, data)
    cnx.commit()
    cnx.close()

    return redirect("/movies", code=302)
	
@app.route('/deletemovie', methods=["POST"])
def deletemovie():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    SQLquery = ("DELETE FROM `Movie` WHERE `idMovie` = %s")
    data = request.form['idMovie']
    cursor.execute(SQLquery, (data,))
    cnx.commit()
    cnx.close()
	
    return redirect("/movies", code=302)
	
@app.route('/modifymovie', methods=["POST"])
def modifymovie():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    SQLquery = ("UPDATE `Movie` SET `MovieName` = %s,`MovieYear` = %s WHERE `idMovie` = %s")
    data = (request.form['Name'], request.form['Year'], request.form['idMovie'])
    cursor.execute(SQLquery, data)
    cnx.commit()
    cnx.close()
	
    return redirect("/movies", code=302)