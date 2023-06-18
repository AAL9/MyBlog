# Django-Based Blog 
## Introduction:
this project is simply a Django-based blog. It has an anonymous commenting feature. It is connected to PostgreSQL DB.

NOTE: it does not have any styling :)
## Endpoints guide:
- /: this is the home endpoint, it will display the "home" page.
- /post/<int:post_id> : this endpoint will display the "post_page" of the id "post_id".
- /publish: this endpoint will display the "pulbish_page" that will allow the user to publish a new post on the blog.
## Functions in views.py: 
- Home: Will handles displaying contents of the home page, and will display all the posts.
- PostPage: This will display the desired post with its comments, it has a field at the end of the page to comment an anonymous comment for the chosen post.
- Publish: Will display the "pulbish_page", it allows the user to make a new post on the blog.

## models:
- Post: this is a table that stores the posts that have been published in the blog. it contains four fields:
- - Id: stores the ID of the post.
- - title: it stores the title of the post.
- - body: it contains the body (or contents) of the post.
- - post_date: it contains the date when the post has been created.


- Comment: this is a table that stores the comments published in the posts. it has four fields:
- - Id: stores the ID of the comment.
- - post: this is a Foreign Key that carries the id of the related post that the comment has been created at.
- - comment: carries the comment itself.
- - post_date: it contains the date when the comment have been created at
