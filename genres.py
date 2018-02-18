@app.route('/genres')
def genres():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    SQLquery = ("SELECT * from Genre")
    cursor.execute(SQLquery)
    genres=cursor.fetchall()
	
    SQLquery = ("SELECT * from Movie")
    cursor.execute(SQLquery)
    movies=cursor.fetchall()
	
    SQLquery = ("SELECT Movie.idMovie,Genre.Genre,Movie.MovieName from Genre,Movie WHERE Genre.Movie_idMovie=Movie.idMovie ORDER BY Movie.idMovie ASC")
    cursor.execute(SQLquery)
    gm=cursor.fetchall()

    SQLquery = ("SELECT Movie.idMovie,Genre.Genre,Movie.MovieName from Genre,Movie WHERE Genre.Movie_idMovie=Movie.idMovie ORDER BY Genre.Genre ASC")
    cursor.execute(SQLquery)
    genresort=cursor.fetchall()
    cnx.close()
	
    return render_template('genres.html', genres=genres, movies=movies, gm=gm, genresort=genresort)

@app.route('/addgenre', methods=["POST"])
def addgenre():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    SQLquery = (
        "INSERT INTO `Genre` (`Genre`, `Movie_idMovie`) "
        "VALUES (%s, %s)"
    )
    data = (request.form['Genre'], request.form['Movie_idMovie'])
    cursor.execute(SQLquery, data)
    cnx.commit()
    cnx.close()

    return redirect("/genres", code=302)
	
@app.route('/deletegenre', methods=["POST"])
def deletegenre():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    SQLquery = ("DELETE FROM `Genre` WHERE `Genre` = %s AND `Movie_idMovie` = %s")
    d = request.form['Genre'].split(':')
    data = (d[0], d[1])
    cursor.execute(SQLquery, data)
    cnx.commit()
    cnx.close()
	
    return redirect("/genres", code=302)
	
@app.route('/modifygenre', methods=["POST"])
def modifygenre():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    SQLquery = ("UPDATE `Genre` SET `Genre` = %s, `Movie_idMovie` = %s WHERE `Genre` = %s AND `Movie_idMovie` = %s")
    d = request.form['curGenre'].split(':')
    data = (request.form['Genre'], request.form['Movie_idMovie'], d[0], d[1])
    cursor.execute(SQLquery, data)
    cnx.commit()
    cnx.close()
	
    return redirect("/genres", code=302)