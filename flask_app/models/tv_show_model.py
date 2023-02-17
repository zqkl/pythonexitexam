from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
db = 'project'


class Shows:
    def __init__(self,data):
        self.id = data['id']
        self.title = data['title']
        self.network = data['network']
        self.release_date = data['release_date']
        self.description = data['description']
        self.users_id = data['users_id']


    @classmethod
    def create_show(cls,data):
        query = """
        INSERT INTO tv_shows(title,network,release_date,description,users_id)
        VALUES(%(title)s,%(network)s,%(release_date)s,%(description)s,%(users_id)s)
        """
        return connectToMySQL(db).query_db(query,data)

    @classmethod ##USE JOIN
    def one_show(cls,data):
        query="""
        SELECT * FROM tv_shows 
        WHERE id = %(id)s    
        """
        results = connectToMySQL(db).query_db(query,data)
        if results:
            return cls(results[0])

    @classmethod
    def tv_dashboard_page(cls):
        query="""
        SELECT * FROM tv_shows
        """
        results = connectToMySQL(db).query_db(query)
        print(results)
        return results

    @classmethod
    def delete_show(cls,data):
        query="""
        DELETE FROM tv_shows
        WHERE id = %(id)s
        """
        return connectToMySQL(db).query_db(query,data)

    @classmethod
    def edit_user(cls,data):
        query="""
        UPDATE tv_shows
        SET title = %(title)s, network = %(network)s, release_date = %(release_date)s
        , description = %(description)s
        WHERE id = %(id)s
        """
        return connectToMySQL(db).query_db(query,data)
        



    @staticmethod
    def validate_create(create_show):
        is_valid = True
        if len(create_show['title']) <  3:
            flash("Title must be atleast 3 characters long!")
            is_valid = False
        if len(create_show['network']) < 3:
            flash("Network must be atleast 3 characters long!")
            is_valid = False
        if len(create_show['description']) < 3:
            flash("Description must be atleast 3 characters long!")
            is_valid = False
        return is_valid


        #joinmethod