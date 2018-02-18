@app.route('/rooms')
def rooms():
    connect = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = connect.cursor()
    SQLquery = ("SELECT * from TheatreRoom")
    cursor.execute(SQLquery)
    rooms=cursor.fetchall()
    connect.close()
	
    return render_template('rooms.html', rooms=rooms)

@app.route('/addroom', methods=["POST"])
def addroom():
    connect = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = connect.cursor()
    SQLquery = ("INSERT INTO `TheatreRoom` (`RoomNumber`, `Capacity`) VALUES (%s, %s)")
    data = (request.form['RmNum'], request.form['size'])
    cursor.execute(SQLquery, data)
    connect.commit()
    connect.close()

    return redirect("/rooms", code=302)
	
@app.route('/deleteroom', methods=["POST"])
def deleteroom():
    connect = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = connect.cursor()
    SQLquery = ("DELETE FROM `TheatreRoom` WHERE `RoomNumber` = %s")
    data = request.form['RoomNumber']
    cursor.execute(SQLquery, (data,))
    connect.commit()
    connect.close()
	
    return redirect("/rooms", code=302)
	
@app.route('/modifyroom', methods=["POST"])
def modifyroom():
    connect = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = connect.cursor()
    SQLquery = ("UPDATE `TheatreRoom` SET `RoomNumber` = %s,`Capacity` = %s WHERE `RoomNumber` = %s")
    data = (request.form['RmNum'], request.form['size'], request.form['OldNum'])
    cursor.execute(SQLquery, data)
    connect.commit()
    connect.close()
	
    return redirect("/rooms", code=302)