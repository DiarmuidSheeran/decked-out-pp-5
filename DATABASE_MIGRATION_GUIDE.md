# Database Migration Guide - ElephantSQL Alternatives

## ⚠️ ElephantSQL Shutdown Notice

ElephantSQL shut down on January 27, 2025. This guide provides free PostgreSQL alternatives and migration instructions.

---

## 🎯 Recommended: Neon (Best Free Option)

**Why Neon?**
- ✅ Generous free tier (0.5 GB storage)
- ✅ Serverless with auto-scaling
- ✅ No credit card required
- ✅ Database branching for development
- ✅ Doesn't pause/expire
- ✅ Great for Django/Heroku apps

### Setup Instructions for Neon

#### 1. Create Account
1. Go to [neon.tech](https://neon.tech)
2. Sign up with GitHub, Google, or email
3. No credit card required

#### 2. Create Database
1. Click "Create Project"
2. Choose a name (e.g., "decked-out-db")
3. Select region closest to your users
4. Click "Create Project"

#### 3. Get Connection String
1. In your project dashboard, click "Connection Details"
2. Copy the connection string (looks like):
   ```
   postgresql://username:password@ep-xxx.region.aws.neon.tech/dbname?sslmode=require
   ```

#### 4. Update Your Application

**For Heroku:**
```bash
heroku config:set DATABASE_URL="your-neon-connection-string"
```

**For Local Development (env.py):**
```python
os.environ.setdefault('DATABASE_URL', 'your-neon-connection-string')
```

#### 5. Run Migrations
```bash
python manage.py migrate
```

#### 6. Create Superuser
```bash
python manage.py createsuperuser
```

---

## 🔄 Alternative Options

### Option 2: Supabase

**Pros:** Full backend solution, includes auth and storage
**Cons:** Pauses after 1 week of inactivity

**Setup:**
1. Go to [supabase.com](https://supabase.com)
2. Create new project
3. Get connection string from Settings → Database
4. Format: `postgresql://postgres:[password]@db.[project-ref].supabase.co:5432/postgres`

### Option 3: Render

**Pros:** Easy Heroku migration, familiar interface
**Cons:** Free databases expire after 90 days

**Setup:**
1. Go to [render.com](https://render.com)
2. New → PostgreSQL
3. Choose free tier
4. Copy external database URL
5. Note: Database will be deleted after 90 days

### Option 4: Railway

**Pros:** Simple, modern interface
**Cons:** Requires payment method, $5/month credit

**Setup:**
1. Go to [railway.app](https://railway.app)
2. New Project → Add PostgreSQL
3. Copy connection string from Variables tab
4. $5 free credit per month

### Option 5: Aiven

**Pros:** Production-ready, multiple cloud providers
**Cons:** Limited to 1 free service

**Setup:**
1. Go to [aiven.io](https://aiven.io)
2. Create service → PostgreSQL
3. Choose free tier (1 GB)
4. Get connection string from service overview

---

## 📊 Comparison Table

| Provider   | Storage | Bandwidth | Expires? | Credit Card? | Best For |
|------------|---------|-----------|----------|--------------|----------|
| **Neon**   | 0.5 GB  | 10 GB/mo  | No       | No           | ⭐ Best overall |
| Supabase   | 0.5 GB  | 2 GB/mo   | Pauses*  | No           | Full backend |
| Render     | 1 GB    | Unlimited | 90 days  | No           | Quick tests |
| Railway    | ~1 GB   | Unlimited | No       | Yes          | Small projects |
| Aiven      | 1 GB    | Limited   | No       | No           | Production |

*Pauses after 1 week of inactivity, resumes on access

---

## 🔐 Security Best Practices

### 1. Never Commit Database URLs
Ensure `env.py` is in `.gitignore`:
```bash
echo "env.py" >> .gitignore
```

### 2. Use Environment Variables
**Heroku:**
```bash
heroku config:set DATABASE_URL="your-connection-string"
```

**Gitpod/Local:**
```python
# env.py
import os
os.environ.setdefault('DATABASE_URL', 'your-connection-string')
```

### 3. Rotate Credentials
If you accidentally commit credentials:
1. Reset database password in provider dashboard
2. Update `DATABASE_URL` in all environments
3. Remove from git history:
   ```bash
   git filter-branch --force --index-filter \
     "git rm --cached --ignore-unmatch env.py" \
     --prune-empty --tag-name-filter cat -- --all
   ```

---

## 📦 Data Migration (If Needed)

### Export from ElephantSQL (if still accessible)
```bash
pg_dump -h kandula.db.elephantsql.com -U username -d dbname > backup.sql
```

### Import to New Database
```bash
# For Neon/Supabase/etc
psql "your-new-connection-string" < backup.sql
```

### Alternative: Django Data Export/Import
```bash
# Export data
python manage.py dumpdata --natural-foreign --natural-primary \
  -e contenttypes -e auth.Permission > datadump.json

# Import to new database
python manage.py loaddata datadump.json
```

---

## 🚀 Quick Start (Recommended Path)

### For Production (Heroku)

1. **Create Neon database** (5 minutes)
   - Sign up at [neon.tech](https://neon.tech)
   - Create project
   - Copy connection string

2. **Update Heroku**
   ```bash
   heroku config:set DATABASE_URL="your-neon-connection-string"
   heroku run python manage.py migrate
   heroku run python manage.py createsuperuser
   ```

3. **Verify**
   ```bash
   heroku open
   ```

### For Development (Local/Gitpod)

1. **Option A: Use SQLite** (Simplest)
   ```python
   # env.py
   os.environ.setdefault('DATABASE_URL', 'sqlite:///db.sqlite3')
   ```

2. **Option B: Use Neon** (Production-like)
   ```python
   # env.py
   os.environ.setdefault('DATABASE_URL', 'your-neon-connection-string')
   ```

---

## 🆘 Troubleshooting

### Connection Errors
```
django.db.utils.OperationalError: could not translate host name
```
**Solution:** Check connection string format, ensure `?sslmode=require` is included

### SSL Certificate Errors
```
ssl.SSLError: certificate verify failed
```
**Solution:** Add to connection string: `?sslmode=require`

### Migration Errors
```
django.db.utils.ProgrammingError: relation does not exist
```
**Solution:** Run migrations: `python manage.py migrate`

### Heroku Deployment Issues
```
Error: Database connection failed
```
**Solution:** 
1. Check config vars: `heroku config`
2. Verify DATABASE_URL is set
3. Check database is accessible: `heroku pg:info`

---

## 📝 Update Checklist

- [ ] Choose database provider
- [ ] Create new database
- [ ] Get connection string
- [ ] Update production environment (Heroku)
- [ ] Update local environment (env.py)
- [ ] Run migrations
- [ ] Create superuser
- [ ] Test application
- [ ] Update documentation
- [ ] Remove old ElephantSQL references

---

## 💡 Tips

1. **Use Neon for production** - Most reliable free option
2. **Use SQLite for local development** - Simpler, no network dependency
3. **Keep backups** - Export data regularly with `dumpdata`
4. **Monitor usage** - Check provider dashboard for limits
5. **Plan for scale** - Consider paid tiers as your app grows

---

## 🔗 Useful Links

- [Neon Documentation](https://neon.tech/docs)
- [Django Database Configuration](https://docs.djangoproject.com/en/3.2/ref/settings/#databases)
- [dj-database-url Documentation](https://github.com/jazzband/dj-database-url)
- [Heroku PostgreSQL](https://devcenter.heroku.com/articles/heroku-postgresql)

---

## Need Help?

If you encounter issues during migration:
1. Check provider documentation
2. Verify connection string format
3. Ensure SSL mode is enabled
4. Test connection with `psql` command
5. Check Django logs for specific errors

**Current Project Status:** Using SQLite for local development. Update `env.py` with your chosen provider's connection string for production deployment.
