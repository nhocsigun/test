from flask import Flask, request, render_template_string
import boto3
import psycopg2
import os

app = Flask(__name__)

# S3 client
s3 = boto3.client('s3', region_name='ap-southeast-2')
bucket = os.getenv("S3_BUCKET")

# HTML form upload
HTML_FORM = """
<!doctype html>
<title>Upload to S3</title>
<h1>Upload File to S3</h1>
<form method=post enctype=multipart/form-data action="/upload">
  <input type=file name=file>
  <input type=submit value=Upload>
</form>
"""

@app.route('/', methods=['GET'])
def index():
    return render_template_string(HTML_FORM)

@app.route('/upload', methods=['POST'])
def upload():
    f = request.files['file']
    s3.upload_fileobj(f, bucket, f.filename)
    return f"{f.filename} uploaded to S3 bucket {bucket}"

@app.route('/db')
def db():
    conn = psycopg2.connect(
        host=os.environ['DB_HOST'],
        dbname=os.environ['DB_NAME'],
        user=os.environ['DB_USER'],
        password=os.environ['DB_PASS']
    )
    cur = conn.cursor()
    cur.execute('SELECT NOW()')
    now = cur.fetchone()
    cur.close()
    conn.close()
    return f"RDS time: {now[0]}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
