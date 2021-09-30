from users_app.config.MySQLConnection import connectToMySQL

class User:
    def __init__( self, first_name, last_name, email ):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    @classmethod
    def get_all_users( cls ):
        query = "SELECT * FROM users;"
        results = connectToMySQL( "users_schema" ).query_db( query )

        users = []
        for user in results:
            users.append(User(user['first_name'], user['last_name'], user['email']))

        return users

    @classmethod
    def add_user(cls, newUser):
        query = "INSERT INTO users(first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s);"
        data = {
            "first_name": newUser.first_name,
            "last_name": newUser.last_name,
            "email": newUser.email
                }
        result = connectToMySQL( "users_schema" ).query_db( query, data )
        return result