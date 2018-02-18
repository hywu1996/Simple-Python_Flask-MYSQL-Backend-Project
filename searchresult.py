@app.route('/searchresult')
def searchresult():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    SQLquery = ("SELECT * from search_results")
    cursor.execute(SQLquery)
    searchresult=cursor.fetchall()
	
    cnx.close()
    
    return render_template('searchresult.html', searchresult=searchresult)