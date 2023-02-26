# Move your drone CI logs to S3

Change the variables in the script to the values matching your setup.

```python
url = "play.minio.io"
access_key = ""
secret_key = ""
bucket = "drone-logs"
```


Install `minio` (see `requirements.txt`) in your python environment.

Run the script where your `sqlite` database `database.sqlite`.

Wait for the script to finish.
