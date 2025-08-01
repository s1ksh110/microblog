# Microblog Platform

A lightweight, full-stack microblogging platform built with Python, Flask, and SQLAlchemy, featuring user authentication, post management, tagging, pagination, a REST API, and a modern, interactive UI. Successfully deployed on Render, this project showcases web development skills suitable for a resume or portfolio.

## Features
- **User Authentication**: Secure signup, login, and logout using Flask-Login with password hashing.
- **Post Management**: Create, edit, and delete posts with Markdown rendering for rich text.
- **Tagging System**: Categorize posts with tags and filter by tag for better organization.
- **Pagination**: Display posts in manageable pages (5 per page) for scalability.
- **REST API**: JSON endpoints (`GET /api/posts`, `POST /api/posts`) for programmatic access.
- **Interactive UI**: Modern card-based layout with search bar, profile link, like/dislike counts, comments, and a "Followed Users" sidebar, styled with Tailwind CSS.
- **Unit Tests**: Ensures functionality with pytest.
- **Deployment**: Live on Render with automatic scaling.

## Tech Stack
- **Backend**: Python 3.10, Flask, Flask-SQLAlchemy, Flask-Login, Flask-Migrate, Flask-WTF
- **Database**: SQLite (development), PostgreSQL (production-ready)
- **Frontend**: HTML, Jinja2, Tailwind CSS
- **Testing**: pytest
- **Deployment**: Render
- **Version Control**: Git, GitHub

## Project Structure
```
microblog/
├── app/
│   ├── __init__.py        # App initialization and configuration
│   ├── models.py          # Database models (User, Post, Tag)
│   ├── routes.py          # URL routes and API endpoints
│   ├── forms.py           # WTForms for validation
│   ├── templates/         # HTML templates (base.html, index.html, etc.)
│   └── migrations/        # Database migration files
├── config.py              # Configuration settings (e.g., database URI)
├── microblog.py           # Entry point to run the app
├── requirements.txt       # Project dependencies
├── .env                   # Environment variables (e.g., SECRET_KEY)
├── Procfile               # Render deployment instructions
├── .gitignore             # Excludes development files
├── tests.py               # Unit tests
└── README.md              # Project documentation
```

## Setup Instructions
1. **Clone the Repository**:
   ```bash
   git clone <your-github-repo-url>
   cd microblog
   ```
2. **Create and Activate a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Set Up Environment Variables**:
   Create a `.env` file with:
   ```
   SECRET_KEY=your-secret-key-here
   ```
5. **Initialize the Database**:
   ```bash
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```
6. **Run the App Locally**:
   ```bash
   flask run
   ```
   Visit `https://microblog-py6n.onrender.com` to explore.

## Deployment
- **Platform**: Render
- **Steps**:
  1. Connect your GitHub repository to Render.
  2. Create a Web Service with:
     - Build Command: `pip install -r requirements.txt`
     - Start Command: `gunicorn -w 4 -b 0.0.0.0:$PORT microblog:app`
     - Environment Variables: `SECRET_KEY=your-secret-key`, `PYTHON_VERSION=3.10.8
  3. Deploy and monitor logs.
- **Live URL**: [https://microblog-py6n.onrender.com]

## API Usage
- **GET /api/posts**: Retrieve all posts in JSON format.
  ```bash
  curl https://microblog-py6n.onrender.com/api/posts
  ```
- **POST /api/posts**: Create a post (requires login).
  ```bash
  curl -X https://microblog-py6n.onrender.com/api/posts -H "Content-Type: application/json" -d '{"title":"API Post","content":"Created via API","tags":["api","test"]}'
  ```

## Running Tests
```bash
pytest
```

## Demo
- **Access**: Visit the [live Render URL](#deployment).
- **Dummy Users**:
  - Username: `john_doe`, Password: `password123`
  - Username: `jane_smith`, Password: `password123`
- **Sample Posts**: Includes "My First Post," "Another Post," and "API Post" with tags like "tech" and "blog."
- **Features to Showcase**:
  - Log in and create/edit/delete a post.
  - Filter posts by tag (e.g., `/tag/tech/1`).
  - Use the API with curl or Postman.
  - Explore the interactive UI with cards, likes, and followed users.

## Development Journey
This project was built over 7 days with the following plan:
1. **Day 1**: Set up Flask app, user authentication, and base templates.
2. **Day 2-3**: Implemented post CRUD and Markdown rendering.
3. **Day 4**: Added tagging system and pagination.
4. **Day 5**: Created REST API endpoints.
5. **Day 6**: Added Tailwind CSS styling and unit tests.
6. **Day 7**: Deployed to Render and finalized documentation.

## Skills Demonstrated
- **Backend Development**: Flask, SQLAlchemy, REST API design.
- **Frontend Development**: HTML, Jinja2, Tailwind CSS for responsive design.
- **Database Management**: SQLite, migrations with Flask-Migrate.
- **Testing**: Unit testing with pytest.
- **Deployment**: Render hosting, Git version control.
- **Security**: Password hashing, CSRF protection with WTForms.

## Future Improvements
- **User Profiles**: Add profile pages with bio and settings.
- **Comments System**: Implement post comments with a new model.
- **Search Functionality**: Make the search bar functional.
- **Social Features**: Add follow/unfollow and real-time like/dislike updates.
- **Image Support**: Allow image uploads for posts.

## Acknowledgments
- Built with guidance from xAI's Grok 3, leveraging its step-by-step support.
- Inspired by modern blog UI designs from Behance and Dribbble.

## Contact
For questions or collaboration, reach out via [].