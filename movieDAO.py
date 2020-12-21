import mysql.connector
import dbconfig as cfg
 
class MovieDao: 
    db = "" # stores database connection
    def __init__(self):
        self.db = mysql.connector.connect(
            host=      cfg.mysql['host'],
            user=      cfg.mysql['user'],
            password=  cfg.mysql['password'],
            database=  cfg.mysql['database']
        )
        #print("connection made")
 
    
    def create(self, movie): # creates new movie but also returns latest id
        cursor = self.db.cursor()
        sql = "insert into movies (title, director, year) values (%s, %s, %s)"
        values = [
            #movie["ISBN"],
            movie["title"],
            movie["director"],
            movie["year"]     
        ]
        cursor.execute(sql, values)
        self.db.commit()
        return cursor.lastrowid # lastrowid is equal to 0. Returns if successful... I think...
    
    def get_all(self):
        cursor = self.db.cursor()
        sql = "select * from movies order by id"
        cursor.execute(sql)
        results = cursor.fetchall() # comes back as tuple. We want them as dict objects
                                    # JSON on our html page in the end
        returnarray = []
        #print(results)
        for result in results:
            result_as_dict = self.convert_to_dict(result) # result is tuple so convert to dict
            returnarray.append(result_as_dict)
        
        return returnarray # will return array of dict objects


    def find_by_id(self, id):
            cursor = self.db.cursor()
            sql="select * from movies where id = %s"
            values = (id,)

            cursor.execute(sql, values)
            result = cursor.fetchone()
            return self.convert_to_dict(result)
    
        

    def update(self, movie):
        cursor = self.db.cursor()
        sql = 'update movies set title = %s, director = %s, year = %s where id = %s'
        values = [
            movie['title'],
            movie['director'],
            movie['year'],
            movie['id']
        ] 
        cursor.execute(sql, values)
        self.db.commit()
        return movie

    def delete(self, id):
        cursor = self.db.cursor()
        sql = 'delete from movies where id = %s'
        values = (id,)
        cursor.execute(sql, values)
        return {}
    
    def convert_to_dict(self, result):
        col_names = ['id', 'title', 'director', 'year']
        movie = {}

        if result:
            for i, col_name in enumerate(col_names):
                value = result[i]
                movie[col_name] = value
        
        return movie # this will be sent straight to the html file later on




movieDao = MovieDao()