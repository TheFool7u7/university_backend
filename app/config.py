class Config:
    # Configura la conexión a tu base de datos MySQL
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:nthn2001@localhost/gestion_universitaria2'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'contrasena123' 
