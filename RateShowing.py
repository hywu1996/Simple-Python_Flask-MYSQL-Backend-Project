@app.route('/rate')
def rateshowing():
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
    
    cnx.close()
    
    return render_template('RateShowing.html', attends=attends, customers=customers, showings=showings)
    
@app.route('/rateshow', methods=["POST"])
def rateshow():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    SQLquery = ("UPDATE `Attend` SET `Rating` = %s WHERE `Customer_idCustomer` = %s AND `Showing_idShowing` = %s")
    d = request.form['Attend'].split(':')
    data = (request.form['Rating'], d[0], d[1])
    cursor.execute(SQLquery, data)
    cnx.commit()
    cnx.close()
    
    return redirect("/success", code=302)


