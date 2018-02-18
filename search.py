@app.route('/search')
def search():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    s1 = ("drop table if exists BoughtTickets;")
    cursor.execute(s1)
    s1 = ("drop table if exists SearchTable;")
    cursor.execute(s1)
    s1 = ("CREATE TABLE BoughtTickets (Showing_idShowing int(11) NOT NULL, count int);")
    cursor.execute(s1)
    s1 = ("insert into BoughtTickets select Showing_idShowing, count(customer_idCustomer) from Attend group by Showing_idShowing;")
    cursor.execute(s1)
    s1 = ("create table SearchTable (Showing_idShowing int(11), count int, Genre varchar(45), idMovie int(11), MovieName varchar(45), MovieYear smallint(1), idShowing int(11), ShowingDateTime datetime, Movie_idMovie int(11), TheatreRoom_RoomNumber int(10), TicketPrice float, RoomNumber int(10), Capacity smallint(1));")
    cursor.execute(s1)
    s1 = ("insert into SearchTable select BoughtTickets.*, Genre.Genre, Movie.*, Showing.*, TheatreRoom.* from Showing join BoughtTickets on BoughtTickets.Showing_idShowing = Showing.idShowing join Genre on Genre.Movie_idMovie=Showing.Movie_idMovie join TheatreRoom on TheatreRoom.RoomNumber=Showing.TheatreRoom_RoomNumber join Movie on Movie.idMovie=Showing.Movie_idMovie;")
    cursor.execute(s1)
    s1 = ("alter table SearchTable drop column idShowing, drop Movie_idMovie, drop RoomNumber, add sub int;")
    cursor.execute(s1)
    s1 = ("update SearchTable set sub = Capacity - count;")
    cursor.execute(s1)

    query = ("select distinct ShowingDateTime from Showing order by ShowingDateTime")
    cursor.execute(query)
    showings=cursor.fetchall()

    query = ("select distinct Genre from Genre")
    cursor.execute(query)
    genres=cursor.fetchall()

    cnx.commit()
    cnx.close()

    return render_template('search.html', showings=showings, genres=genres)

@app.route('/searchQuery', methods=["POST"])
def searchQuery():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    
    selected = "False"

    genreInput = (request.form['Genre'])
    fromDate = (request.form['idShowing1'])
    toDate = (request.form['idShowing2'])
    selected = (request.form['seatsAvailable'])
    keyword = (request.form['SearchTitle'])

    # if selected != "True":
    #     selected = "F";

    # print(selected)
    # print(selected)
    # print(selected)
    # print(selected)
    # print(selected)
    # print(selected)

    # print(selected)
    # print(selected)
    # print(selected)
    # print(selected)
    # print(selected)
    # print(selected)
    # print(selected)
    # print(selected)
    # print(selected)
    # print(selected)
    # print(selected)
    # print(selected)
    # print(selected)

    clause=""
    if selected == "True":
        clause = " and sub > 0"

    i1 = ("drop view if exists search_results")
    cursor.execute(i1)

    i2 = ("create view search_results as select * from SearchTable where SearchTable.Genre = \"" + genreInput + "\" and SearchTable.ShowingDateTime between \'" + fromDate + "\' and \'" + toDate + "\' " + "and MovieName like \'%" + keyword + "%\'" + clause)
    if genreInput=="SearchTable.Genre":
        cursor.execute(i1)
        i2 = ("create view search_results as select * from SearchTable where SearchTable.Genre =" + genreInput + " and SearchTable.ShowingDateTime between \'" + fromDate + "\' and \'" + toDate + "\' " + "and MovieName like \'%" + keyword + "%\'" + clause)

    cursor.execute(i2)
    cnx.commit()
    cnx.close()
    return redirect('/searchresult', code=302)