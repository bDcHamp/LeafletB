import sqlite3, os
db = r"db.sqlite3"
assert os.path.exists(db), f"{db} not found in current folder"
conn = sqlite3.connect(db)
cur = conn.cursor()
cur.execute("SELECT app, name FROM django_migrations WHERE app='blog' AND name='0016_alter_blogdetailpage_video'")
rows = cur.fetchall()
print("Before:", rows)
cur.execute("DELETE FROM django_migrations WHERE app='blog' AND name='0016_alter_blogdetailpage_video'")
conn.commit()
cur.execute("SELECT app, name FROM django_migrations WHERE app='blog' AND name='0016_alter_blogdetailpage_video'")
print("After:", cur.fetchall())
conn.close()
print("OK: migration history corrected.")
