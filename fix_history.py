import sqlite3, os, datetime

DB = "db.sqlite3"
assert os.path.exists(DB), f"{DB} not found; run from the folder that contains it"

def ensure_row(conn, app, name):
    cur = conn.cursor()
    cur.execute("SELECT 1 FROM django_migrations WHERE app=? AND name=?", (app, name))
    if cur.fetchone():
        return False
    cur.execute(
        "INSERT INTO django_migrations (app, name, applied) VALUES (?, ?, ?)",
        (app, name, datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"))
    )
    conn.commit()
    return True

conn = sqlite3.connect(DB)
cur = conn.cursor()

# sanity: show existing blog rows around the problem
cur.execute("SELECT app, name FROM django_migrations WHERE app='blog' ORDER BY name")
print("BLOG before:", cur.fetchall())

# 1) make sure wagtailmedia.0001 is recorded
added_wm = ensure_row(conn, "wagtailmedia", "0001_initial")
print("Inserted wagtailmedia.0001_initial?", added_wm)

# 2) make sure blog.0016 is recorded (so 0017 isn't 'before' it)
added_b16 = ensure_row(conn, "blog", "0016_alter_blogdetailpage_video")
print("Inserted blog.0016_alter_blogdetailpage_video?", added_b16)

# show after
cur.execute("SELECT app, name FROM django_migrations WHERE app='blog' ORDER BY name")
print("BLOG after:", cur.fetchall())

conn.close()
print("OK: migration history corrected.")
