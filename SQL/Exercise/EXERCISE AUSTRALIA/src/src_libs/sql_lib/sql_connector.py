connection = pymysql.connect(host="34.229.137.164", 
                            port=25001,
                             user='student',
                             password='lebowsky',
                             database= 'australia_fires_2',
                             cursorclass=pymysql.cursors.DictCursor)
                
cursor= connection.cursor()

query1 = """

SELECT * 
FROM fire_archive_M6_96619"""

data1 = pd.read_sql_query(query1, connection)
data1