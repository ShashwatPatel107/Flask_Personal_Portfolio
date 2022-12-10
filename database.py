import sqlalchemy
from sqlalchemy import create_engine, text
# connect to my sql with sqlalchemy
connection_info = "mysql+pymysql://igvvuaw1xwb2wy1b5yol:pscale_pw_KtHujBeZ9vlQ1DAFKUQ1zOLKhttP9mwMxT4T26qY9rI@us-east.connect.psdb.cloud/shashwat_patel_projects_wd?charset=utf8mb4"
# args for secure connection
engine = create_engine(connection_info, connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem"
        }
    })
