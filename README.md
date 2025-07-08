\# Django Blog Application



This is a full-stack blog platform built using Django and Tailwind CSS. It includes secure user authentication, category filtering, search, pagination, post detail views, and author-specific permissions. The project demonstrates Django best practices and frontend interactivity using HTMX.



\## Features



\### Core Functionality

\- Custom user model with unique email

\- User registration, login, and logout

\- Blog post creation, listing, editing, and deletion

\- Paginated homepage (5 posts per page)

\- Case-insensitive search across title and content

\- Filter posts by category using dropdown

\- Post detail view with content, author, and categories

\- Author-only edit/delete access using Django’s permission system

\- Mobile-responsive design using Tailwind CSS

\- HTMX integration for dynamic filtering without page reloads



\## Setup Instructions



1\. Clone the repository  

git clone https://github.com/oveemanolkar/django-blog-app.git

cd django-blog-app



2\. Create a virtual environment  

python -m venv venv

source venv/bin/activate # On Windows: venv\\Scripts\\activate



3\. Install dependencies  

pip install Django



4\. Apply migrations

python manage.py makemigrations

python manage.py migrate



5\. Create a superuser (optional)

python manage.py createsuperuser



6\. Run the development server

python mange.py runserver



7\. Open the app in your browser: 

http://127.0.0.1:8000



\## Technical Highlights



\- Custom `User` model (`AbstractUser`)

\- Optimized queries using `select\_related` and `prefetch\_related`

\- CSRF protection and secure password handling via Django auth

\- Use of Django class-based views (`DetailView`, `UpdateView`, `DeleteView`)

\- Context processors to inject categories globally

\- Responsive UI with Tailwind CSS

\- HTMX-powered dynamic search and filter functionality



\## Bonus Features Implemented



\- Author-only post editing and deletion with permission checks

\- Dynamic filtering and search without full-page reloads using HTMX



\## Potential Enhancements



\- Add user profile pages with bio, avatar, and user post listings

\- Implement comment functionality

\- Write unit tests for models, views, and forms

\- Add inline code comments for complex logic



\## Author



\*\*Ovee Manolkar\*\*  

GitHub: \[https://github.com/oveemanolkar](https://github.com/oveemanolkar)



