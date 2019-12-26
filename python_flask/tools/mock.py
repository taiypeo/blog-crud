import sys

sys.path.append("..")
from app import db
from app.models import User, BlogPost

u1 = User(username="admin", is_admin=True)
u1.set_password("12345")

u2 = User(username="user1")
u2.set_password("12345")

u3 = User(username="Hackerman")
u3.set_password("12345")

post1 = BlogPost(
    title="Welcome to this blog!",
    creator=u1,
    markdown="**Welcome to this blog! *Have fun!***",
)
post2 = BlogPost(
    title="My first post here",
    creator=u2,
    markdown="""
# Hello there!

This is my **first** post on this blog!

I just *stole* this table from [https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)!
| Tables        | Are           | Cool  |
| ------------- |:-------------:| -----:|
| col 3 is      | right-aligned | $1600 |
| col 2 is      | centered      |   $12 |
| zebra stripes | are neat      |    $1 |
""",
)
post3 = BlogPost(
    title="My second post",
    creator=u2,
    markdown="""
# Post #2

## More cool markdown stuff!

```
pip install -r requirements.txt
python main.py
```

> I'm quoting someone here...
""",
)
post4 = BlogPost(
    title="Security check",
    creator=u3,
    markdown="""
Is it vulnerable? Let's find out!

<script>alert(1);</script>
""",
)

User.query.delete()
BlogPost.query.delete()

for user in [u1, u2, u3]:
    db.session.add(user)
for i in range(1, 30):
    post = BlogPost(title=f"Post #{i}", creator=u2, markdown=f"This is post *#{i}*.")
    db.session.add(post)
for post in [post1, post2, post3, post4]:
    db.session.add(post)

db.session.commit()
