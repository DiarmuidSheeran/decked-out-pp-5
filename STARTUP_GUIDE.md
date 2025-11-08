# Startup Guide - Decked Out Project

## 🚀 Quick Start (Every Time You Open the Project)

When you open this project in Gitpod or a new environment, follow these steps:

### 1. Environment Will Auto-Setup

The dev container will automatically:
- ✅ Install Python 3.11
- ✅ Install PostgreSQL client
- ✅ Install all dependencies from `requirements.txt`

**Wait for the build to complete** (first time takes ~2-3 minutes)

### 2. Configure Environment Variables

Your `env.py` file contains your database credentials and API keys. **This file is NOT in git** (for security).

**If `env.py` doesn't exist, create it:**

```bash
cp env.py.template env.py
```

Then update with your actual credentials:

```python
# Database - Your Neon connection string
os.environ.setdefault('DATABASE_URL', 'postgresql://neondb_owner:npg_BhNsaz2wmD6U@ep-cold-pine-a45ch9j1-pooler.us-east-1.aws.neon.tech/neondb?sslmode=require')

# Stripe keys (from dashboard.stripe.com)
os.environ.setdefault('STRIPE_PUBLIC_KEY', 'your-key-here')
os.environ.setdefault('STRIPE_SECRET_KEY', 'your-key-here')
os.environ.setdefault('STRIPE_WH_SECRET', 'your-webhook-secret')

# Email (if using Gmail)
os.environ.setdefault('EMAIL_HOST_USER', 'your-email@gmail.com')
os.environ.setdefault('EMAIL_HOST_PASSWORD', 'your-app-password')

# AWS (if using S3 for media files)
os.environ.setdefault('USE_AWS', 'True')
os.environ.setdefault('AWS_ACCESS_KEY_ID', 'your-key')
os.environ.setdefault('AWS_SECRET_ACCESS_KEY', 'your-secret')
```

### 3. Run Migrations (First Time Only)

If this is a fresh database or first time setup:

```bash
python manage.py migrate
```

### 4. Create Superuser (First Time Only)

```bash
python manage.py createsuperuser
```

Or use the existing one:
- Username: `admin`
- Password: `admin123`

### 5. Start the Development Server

```bash
python manage.py runserver 0.0.0.0:8000
```

The server will be available at the Gitpod preview URL (shown in terminal).

---

## 📋 Common Commands

### Development Server
```bash
python manage.py runserver 0.0.0.0:8000
```

### Run Tests
```bash
# All tests
python manage.py test

# Specific app
python manage.py test bag.tests

# With verbosity
python manage.py test -v 2
```

### Database Management
```bash
# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Check migration status
python manage.py showmigrations

# Access database shell
python manage.py dbshell
```

### Static Files
```bash
# Collect static files (for production)
python manage.py collectstatic --noinput
```

### Create Admin User
```bash
python manage.py createsuperuser
```

### Django Shell
```bash
python manage.py shell
```

---

## 🔧 Heroku Deployment

### Login to Heroku
```bash
heroku login -i
# Use your API key as password if you have MFA enabled
```

### Link to Your App
```bash
heroku git:remote -a decked-out-tcg-store
```

### Deploy Changes
```bash
git push heroku main
```

### Run Commands on Heroku
```bash
heroku run python manage.py migrate
heroku run python manage.py createsuperuser
heroku run python manage.py collectstatic --noinput
```

### View Logs
```bash
heroku logs --tail
```

### Open Your Site
```bash
heroku open
```

---

## 🗄️ Database Information

### Current Setup
- **Provider:** Neon PostgreSQL
- **Database:** neondb
- **Region:** us-east-1
- **Connection:** Pooled for better performance

### Neon Dashboard
Monitor your database at: [console.neon.tech](https://console.neon.tech)

### Backup Database
```bash
# Export all data
python manage.py dumpdata > backup.json

# Export specific apps
python manage.py dumpdata products checkout > store_data.json
```

### Restore Database
```bash
python manage.py loaddata backup.json
```

---

## 🐛 Troubleshooting

### "Python not found"
The dev container should install Python automatically. If not:
```bash
# Rebuild the container
gitpod env devcontainer rebuild
```

### "Database connection failed"
Check your `env.py` file has the correct DATABASE_URL:
```python
os.environ.setdefault('DATABASE_URL', 'postgresql://...')
```

### "Module not found"
Reinstall dependencies:
```bash
pip install -r requirements.txt
```

### "Port already in use"
Kill the existing process:
```bash
pkill -f "python manage.py runserver"
```

### "Static files not loading"
In development, Django serves static files automatically. In production:
```bash
python manage.py collectstatic --noinput
```

---

## 📁 Important Files

### Configuration
- `env.py` - Local environment variables (NOT in git)
- `env.py.template` - Template for env.py
- `decked_out/settings.py` - Django settings
- `requirements.txt` - Python dependencies
- `.devcontainer/Dockerfile` - Dev container configuration

### Documentation
- `README.md` - Project overview
- `TESTING.md` - Testing documentation
- `BUG_FIX_DOCUMENTATION.md` - Bug fix details
- `DATABASE_MIGRATION_GUIDE.md` - Database migration guide
- `NEON_SETUP_COMPLETE.md` - Neon setup summary
- `HEROKU_NEON_SETUP.md` - Heroku deployment guide
- `STARTUP_GUIDE.md` - This file

---

## ✅ Verification Checklist

After starting up, verify everything works:

- [ ] Dev container built successfully
- [ ] Python 3.11 installed (`python --version`)
- [ ] Dependencies installed (`pip list`)
- [ ] env.py exists with correct credentials
- [ ] Database connection works (`python manage.py dbshell --command "SELECT 1;"`)
- [ ] Migrations applied (`python manage.py showmigrations`)
- [ ] Server starts (`python manage.py runserver`)
- [ ] Admin accessible at `/admin/`
- [ ] Can log in with superuser credentials

---

## 🔐 Security Reminders

### Never Commit These Files:
- ✅ `env.py` - Already in .gitignore
- ✅ `*.pyc` - Already in .gitignore
- ✅ `db.sqlite3` - Already in .gitignore
- ✅ `__pycache__/` - Already in .gitignore

### Protect Your Credentials:
- Database connection strings
- Stripe API keys
- AWS access keys
- Email passwords
- Django SECRET_KEY

**If you accidentally commit credentials:**
1. Rotate/reset them immediately
2. Update env.py and Heroku config
3. Remove from git history

---

## 📞 Quick Reference

### Your Credentials Location
- **Local:** `env.py` (not in git)
- **Heroku:** `heroku config` (environment variables)
- **Neon:** [console.neon.tech](https://console.neon.tech)
- **Stripe:** [dashboard.stripe.com](https://dashboard.stripe.com)

### Your Apps
- **Local Dev:** Gitpod preview URL (port 8000)
- **Production:** [decked-out-tcg-store.herokuapp.com](https://decked-out-tcg-store-b1147b8f9a0a.herokuapp.com/)
- **Admin:** `/admin/`

### Support Resources
- **Django Docs:** [docs.djangoproject.com](https://docs.djangoproject.com)
- **Neon Docs:** [neon.tech/docs](https://neon.tech/docs)
- **Heroku Docs:** [devcenter.heroku.com](https://devcenter.heroku.com)
- **Stripe Docs:** [stripe.com/docs](https://stripe.com/docs)

---

## 🎯 What's Been Fixed

This project includes a critical bug fix:

**Discount Code Bug (bag/contexts.py)**
- ✅ Discount codes now properly apply to shopping cart
- ✅ Percentage discounts calculate correctly
- ✅ Comprehensive test suite added

**Database Migration**
- ✅ Migrated from ElephantSQL (shutdown) to Neon
- ✅ 25x more storage (0.5 GB vs 20 MB)
- ✅ Better performance with connection pooling

---

**Last Updated:** 2025-11-08
**Current Branch:** main
**Status:** ✅ Production Ready
