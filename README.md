# Stories of Country

Stories of Country is a web platform that acknowledges the Traditional Custodians of the lands and waters across Australia. The platform is designed to share stories of land, ancestors, seasons, and community in a respectful and interactive way.

## Quick Start Guide

1. Extract the zip file
2. Create a Python virtual environment:
   ```bash
   python -m venv venv
   ```
3. Activate the virtual environment:
   - Windows: `.\venv\Scripts\activate`
   - Mac/Linux: `source venv/bin/activate`
4. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```
5. Create `.env` file in `livingarchive/settings/` (see Environment Configuration section)
6. Run migrations:
   ```bash
   python manage.py migrate
   ```
7. Create superuser:
   ```bash
   python manage.py createsuperuser
   ```
8. Run the server:
   ```bash
   python manage.py runserver
   ```

## Features

- Interactive 3D Map Visualization using Cesium.js
- Story Sharing Platform with Wagtail CMS
- Secure User Authentication and Group Management
- Community Engagement Tools
- Responsive Design for all devices
- Cultural Heritage Documentation System
- Email Verification System
- Admin Dashboard for Content Management

## Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.11 or higher
- Git
- pip (Python package manager)
- Node.js and npm (for frontend assets)

## Installation Guide

### 1. Clone the Repository

```bash
git clone <repository-url>
cd LeafletBuild-main
```

### 2. Set Up Python Virtual Environment

#### On Windows:
```bash
python -m venv venv
.\venv\Scripts\activate
```

#### On macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Environment Configuration

Create a `.env` file in the `livingarchive/settings/` directory with the following content:

```plaintext
DJANGO_SETTINGS_MODULE=livingarchive.settings.dev
DJANGO_SECRET_KEY=your-secret-key
WAGTAIL_ADDRESS_MAP_KEY=your-google-maps-api-key
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-gmail-address@gmail.com
EMAIL_HOST_PASSWORD=your-app-specific-password
DEFAULT_FROM_EMAIL=your-gmail-address@gmail.com
```

Replace the placeholder values with your actual credentials:
- Generate a secure Django secret key
- Get a Google Maps API key from Google Cloud Console
- For email functionality, use a Gmail account with an App Password

### 5. Database Setup

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create a Superuser (Admin Account)

```bash
python manage.py createsuperuser
```

### 7. Run the Development Server

```bash
python manage.py runserver
```

The application will be available at: http://127.0.0.1:8005/

## Project Structure

```
LeafletBuild-main/
├── blog/              # Blog app for story sharing
├── home/              # Home page app
├── livingarchive/     # Main project settings and core functionality
├── module/            # Additional functionality modules
├── search/           # Search functionality
├── user_group_management/  # User and group management
├── static/           # Static files (CSS, JS, images)
├── media/           # User-uploaded content
├── templates/       # HTML templates
└── manage.py       # Django management script
```

## Key Components

- **Blog**: Handles story creation and sharing functionality
- **Home**: Manages the main landing page and navigation
- **Living Archive**: Core project settings and main functionality
- **User Group Management**: Handles user authentication and group permissions
- **Search**: Provides search functionality across the platform

## Development

### Type Checking

The project uses Python type hints and mypy for type checking. Run type checks with:

```bash
mypy .
```

### Running Tests

```bash
python manage.py test
```

### Code Style

The project follows PEP 8 style guidelines. Run code style checks with:

```bash
flake8
```

## Deployment

For production deployment:

1. Update `livingarchive/settings/production.py`
2. Set environment variables for production settings
3. Collect static files:
   ```bash
   python manage.py collectstatic
   ```
4. Configure your web server (e.g., Nginx, Apache)
5. Set up WSGI/ASGI server (e.g., Gunicorn, uWSGI)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

This project acknowledges the Traditional Custodians of the lands and waters across Australia and pays respects to Elders past, present, and emerging.

1. Access the admin interface at `/django-admin/` to manage content
2. Create and manage stories through the web interface
3. Users can sign up and contribute their own stories
4. Interactive map is available for spatial navigation
5. 3D visualization provides immersive experience

## Common Issues and Solutions

1. **Email Verification Issues**
   - Check spam folder for verification emails
   - Verify Gmail app password is correctly set

2. **Map Loading Issues**
   - Ensure Google Maps API key is correctly set in .env
   - Check browser console for JavaScript errors

3. **Database Errors**
   - Run `python manage.py migrate` to apply all migrations
   - Check database file permissions

## Maintenance

### Regular Updates
```bash
git pull                           # Get latest code
pip install -r requirements.txt    # Update dependencies
python manage.py migrate          # Apply any new migrations
python manage.py collectstatic    # Update static files
```

### Backup Database
```bash
python manage.py dumpdata > backup.json
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
