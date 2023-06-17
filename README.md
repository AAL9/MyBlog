# Django-Based Blog 
## introduction:
this project is simply a django-based blog. It has anonymous commenting feature. It is connected to PostgreSQL DB.

NOTE: it does not has any styling :)
## Routes guide:
- / : this is the home route, it will display the "home" page.
- /post/<int:post_id> : this route will display the "post_page" of the id "post_id".
- /publish : this route will will display the "pulbish_page" that will allow the user to publish a new post at the blog.
## Functions in views.py: 
- Home: Will handles displying contents of the home page, will display all the posts.
- PostPage: Will display the desired post with its comments, it has a field in the end of the page to comment an anonymous comment for the chosen post.
- Publsih: Will display the "pulbish_page", it allows the user to make a new post at the blog.

## models:
- Post: this is a table that stores the posts that have been published in the blog. it contains three fields:
- - title: it stores the title of the post.
- - body: it contains the body (or contents) of the post.
- - post_date: it contains the date when the post have been created.


- Comment: this is a table that stores the comments published in the posts. it has three fields: 
- - post: this is a Foreign Key that carries the id of the related post that the comment have been created at.
- - comment: carries the comment itself.
- - post_date: it contains the date when the comment have been created at
