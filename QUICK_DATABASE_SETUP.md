# Quick Database Setup Guide

## 🚀 Fastest Path: Use Neon (5 minutes)

### Step 1: Create Neon Account
1. Go to **[neon.tech](https://neon.tech)**
2. Click "Sign Up" (use GitHub/Google/Email)
3. No credit card required ✅

### Step 2: Create Database
1. Click "Create Project"
2. Name it: `decked-out-db`
3. Choose region: `US East` or closest to you
4. Click "Create Project"

### Step 3: Get Connection String
1. In dashboard, click "Connection Details"
2. Copy the connection string (looks like):
   ```
   postgresql://username:password@ep-xxx.region.aws.neon.tech/dbname?sslmode=require
   ```

### Step 4: Update Your App

**Option A: Use Setup Script (Easiest)**
```bash
./setup_neon_db.sh 'your-connection-string-here'
```

**Option B: Manual Setup**
```bash
# Update env.py
# Change the DATABASE_URL line to:
os.environ.setdefault('DATABASE_URL', 'your-neon-connection-string')

# Run migrations
python manage.py migrate

# Create admin user
python manage.py createsuperuser
```

### Step 5: Deploy to Heroku (if needed)
```bash
heroku config:set DATABASE_URL='your-neon-connection-string'
heroku run python manage.py migrate
heroku run python manage.py createsuperuser
```

---

## 🎯 Why Neon?

| Feature | Neon | ElephantSQL (Shutdown) |
|---------|------|------------------------|
| Free Tier | ✅ 0.5 GB | ❌ Shutdown |
| Credit Card | ❌ Not required | ❌ Not required |
| Expires | ❌ Never | ❌ Shutdown |
| Auto-scaling | ✅ Yes | ❌ No |
| Branching | ✅ Yes | ❌ No |

---

## 📋 Alternative: Keep SQLite (Local Only)

If you're just developing locally and don't need PostgreSQL:

**env.py:**
```python
os.environ.setdefault('DATABASE_URL', 'sqlite:///db.sqlite3')
```

**Pros:**
- ✅ No setup required
- ✅ Works offline
- ✅ Fast for development

**Cons:**
- ❌ Not suitable for production
- ❌ Different from Heroku
- ❌ Limited concurrent users

---

## 🆘 Troubleshooting

### "Could not translate host name"
**Problem:** Connection string incorrect or database not accessible

**Solution:**
1. Check connection string format
2. Ensure `?sslmode=require` is at the end
3. Verify database is running in Neon dashboard

### "SSL certificate verify failed"
**Problem:** SSL mode not configured

**Solution:** Add `?sslmode=require` to connection string

### "Relation does not exist"
**Problem:** Migrations not run

**Solution:**
```bash
python manage.py migrate
```

---

## 📞 Need Help?

1. **Check Neon Status:** [status.neon.tech](https://status.neon.tech)
2. **Neon Docs:** [neon.tech/docs](https://neon.tech/docs)
3. **Django Database Docs:** [docs.djangoproject.com](https://docs.djangoproject.com/en/3.2/ref/settings/#databases)

---

## ✅ Verification Checklist

After setup, verify everything works:

- [ ] Connection string updated in env.py
- [ ] Migrations completed: `python manage.py migrate`
- [ ] Superuser created: `python manage.py createsuperuser`
- [ ] Server starts: `python manage.py runserver`
- [ ] Admin accessible: `/admin/`
- [ ] Can create products
- [ ] Can create discount codes
- [ ] Heroku updated (if applicable)

---

## 💡 Pro Tips

1. **Use SQLite for local dev** - Simpler, faster
2. **Use Neon for staging/production** - Production-like environment
3. **Keep backups** - Export data regularly:
   ```bash
   python manage.py dumpdata > backup.json
   ```
4. **Monitor usage** - Check Neon dashboard for storage/bandwidth
5. **Use database branching** - Neon allows you to create branches for testing

---

**Current Status:** Your app is using SQLite locally. This works great for development. When you're ready to deploy to production, follow the Neon setup above.
