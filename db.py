
_DEBUG = True
dbhost = ""
dbuser = ""
dbpass = ""
dbname = ""
connected = False
dbhandle = None
wd = None
dbcursor = None
app = None

def selectQuery(query, args):
        if not connected:
            app.logger.error("query while not connected, arborted query: " + query)
            return None
        try:
            dbcursor.execute(query, args)
            if (_DEBUG):
                app.logger.error(dbcursor._last_executed)
            res = dbcursor.fetchall()
        except dbhandle.Error as e:
            app.logger.error(query)
            app.logger.error(args)
            app.logger.error(e)
            return None
        if res == None or len(res) < 1:
            return None
        rv = []
        for rec in res:
            rv.append(rec)
        return rv

def insertUpdateQuery(query, args):
    rv = False
    try:

        dbcursor.execute(query, args)
        dbhandle.commit()
        if (_DEBUG):
            app.logger.error(dbcursor._last_executed)
        rv = True
    except BaseException as e:
        app.logger.error(query)
        app.logger.error(args)
        app.logger.error(str(e))
        rv = False
    return rv

def get_list_country_available(Available):
    query = "SELECT CountryCode.country FROM CountryList WHERE Available = %s"
    args = [Available]
    return selectQuery(query, args)

def update_user(password, first_name, last_name, phone, email, country, token):
    query = "UPDATE `User` SET = `Password` %s, `First_Name` = %s, `Last_Name` = %s, `Phone` = %s, `Email` = %s, `Country` = %s WHERE `User`.`Token` = %s; "
    args = [password, first_name, last_name, phone, email, country, token]
    return insertUpdateQuery(query, args)


def create_user(username, password, token):
    query = "INSERT INTO User (ID,Username,Password,Token) VALUES (NULL,%s,%s,%s);"
    args = [username, password, token]
    return insertUpdateQuery(query, args)


def get_user_by_token(token):
    query = "SELECT User.Label as UserLabel, User.First_Name, User.Last_Name, User.Phone, User.Email, User.Last_Name, Country.Name as CountryName"\
            "FROM User"\
            "INNER JOIN Country ON User.Country = Country.ID "\
            "WHERE user.Token=%s"
    args = [token]
    return selectQuery(query, args)

print("dbhost = "" dbuser = "" dbpass = "" dbname = "" connected = False dbhandle = None wd = None dbcursor = None app = None".upper())