import sqlite3
import io
from minio import Minio

con = sqlite3.connect("database.sqlite")
cur = con.cursor()


url = "play.minio.io"
access_key = ""
secret_key = ""
bucket = "drone-logs"

client = Minio(
        url,
        access_key=access_key,
        secret_key=secret_key,
    )

objects = [obj.object_name for obj in client.list_objects("drone")]
import sys; sys.exit(1)
for row in cur.execute('select * from logs'):
    print(f'Moved {row[0]: 7}', end='\r')
    client.put_object(
        bucket, str(row[0]), io.BytesIO(row[1]), content_type='binary/octet-stream', length=len(row[1]), 
    )
cur.execute('delete from logs')
con.close()
print('finished')
