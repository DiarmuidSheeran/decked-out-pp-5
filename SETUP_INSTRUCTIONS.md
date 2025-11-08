# Development Environment Setup Instructions

## Issue: Python Not Found

If you encounter the error `python: command not found`, this means the dev container needs to be rebuilt with the updated Dockerfile.

## Solution

The Dockerfile has been updated to include Python 3 and all required dependencies. Follow these steps:

### Option 1: Rebuild Dev Container (Recommended)

1. **Stop the current environment:**
   ```bash
   gitpod environment stop
   ```

2. **Start and rebuild:**
   ```bash
   gitpod environment start --rebuild
   ```

   Or if already in the environment:
   ```bash
   gitpod env devcontainer rebuild
   ```

3. **Wait for the rebuild to complete** (this may take a few minutes)

4. **Verify Python is installed:**
   ```bash
   python --version
   # Should show: Python 3.x.x
   ```

### Option 2: Manual Installation (Temporary)

If you need Python immediately and can't rebuild:

```bash
# This is a temporary workaround - changes will be lost on restart
apt-get update
apt-get install -y python3 python3-pip python3-venv python3-dev postgresql-client libpq-dev build-essential
ln -sf /usr/bin/python3 /usr/bin/python
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## After Python is Installed

### 1. Install Project Dependencies

```bash
pip install -r requirements.txt
```

### 2. Set Up Environment Variables

Create a `.env` file or set environment variables for:
- `DATABASE_URL` - PostgreSQL database connection
- `SECRET_KEY` - Django secret key
- `STRIPE_PUBLIC_KEY` - Stripe public key
- `STRIPE_SECRET_KEY` - Stripe secret key
- `STRIPE_WH_SECRET` - Stripe webhook secret
- `AWS_ACCESS_KEY_ID` - AWS S3 access key (if using S3)
- `AWS_SECRET_ACCESS_KEY` - AWS S3 secret key (if using S3)
- `EMAIL_HOST_USER` - Email configuration
- `EMAIL_HOST_PASS` - Email password

### 3. Run Database Migrations

```bash
python manage.py migrate
```

### 4. Create a Superuser (Optional)

```bash
python manage.py createsuperuser
```

### 5. Run the Development Server

```bash
python manage.py runserver
```

The server will start on port 8000.

### 6. Run Tests

To verify the bug fix and all functionality:

```bash
# Run all tests
python manage.py test

# Run specific app tests
python manage.py test bag.tests -v 2

# Run with coverage (if installed)
coverage run --source='.' manage.py test
coverage report
```

## What Was Fixed

The dev container Dockerfile now includes:

- ✅ Python 3 with pip, venv, and development tools
- ✅ PostgreSQL client and development libraries
- ✅ Build essentials for compiling Python packages
- ✅ Convenient `python` symlink (instead of requiring `python3`)

## Troubleshooting

### "Permission denied" errors
Run commands with appropriate permissions or ensure you're in the correct directory.

### "Module not found" errors
Reinstall dependencies:
```bash
pip install -r requirements.txt
```

### Database connection errors
Ensure your `DATABASE_URL` environment variable is set correctly.

### Port already in use
Kill the existing process:
```bash
lsof -ti:8000 | xargs kill -9
```

## Additional Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [Gitpod Dev Container Documentation](https://www.gitpod.io/docs/configure/workspaces/workspace-image)
- [Project README](README.md)
- [Bug Fix Documentation](BUG_FIX_DOCUMENTATION.md)
