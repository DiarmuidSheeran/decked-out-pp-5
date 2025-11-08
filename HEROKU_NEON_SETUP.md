# Update Heroku to Use Neon Database

## ✅ Your Neon Database is Ready!

Your local environment is now connected to Neon. Here's how to update Heroku:

---

## 🚀 Update Heroku (Production)

### Step 1: Set the Database URL

Run this command to update Heroku with your Neon connection string:

```bash
heroku config:set DATABASE_URL='postgresql://neondb_owner:npg_BhNsaz2wmD6U@ep-cold-pine-a45ch9j1-pooler.us-east-1.aws.neon.tech/neondb?sslmode=require'
```

### Step 2: Run Migrations on Heroku

```bash
heroku run python manage.py migrate
```

### Step 3: Create Superuser on Heroku

```bash
heroku run python manage.py createsuperuser
```

Follow the prompts to create your admin account.

### Step 4: Verify Deployment

```bash
heroku open
```

Your site should now be running with the Neon database!

---

## 📋 Optional: Import Existing Data

If you have data from your old database that you want to migrate:

### Export from Local (if you have data)

```bash
python manage.py dumpdata --natural-foreign --natural-primary \
  -e contenttypes -e auth.Permission > data_backup.json
```

### Import to Heroku

```bash
heroku run python manage.py loaddata data_backup.json
```

---

## 🔍 Verify Everything Works

### Check Heroku Config

```bash
heroku config
```

You should see `DATABASE_URL` pointing to your Neon database.

### Check Database Connection

```bash
heroku run python manage.py dbshell --command "SELECT current_database();"
```

Should show: `neondb`

### Check Logs

```bash
heroku logs --tail
```

Look for any database connection errors.

---

## 🎯 What's Different Now?

| Before (ElephantSQL) | After (Neon) |
|---------------------|--------------|
| ❌ Service shutdown | ✅ Active and maintained |
| Limited features | ✅ Serverless auto-scaling |
| No branching | ✅ Database branching |
| 20 MB free | ✅ 0.5 GB free |

---

## 💡 Pro Tips

### 1. Use the Same Database for Dev and Production
Your local environment and Heroku are now using the same Neon database. This means:
- ✅ Data is synced between local and production
- ✅ No need to maintain separate databases
- ⚠️ Be careful with migrations - they affect both!

### 2. Or Use Separate Databases (Recommended)
For better separation, create two Neon projects:
- One for development
- One for production

**To create a second database:**
1. Go to Neon dashboard
2. Click "Create Project"
3. Name it "decked-out-production"
4. Use that connection string for Heroku
5. Keep the first one for local development

### 3. Monitor Usage
Check your Neon dashboard regularly:
- Storage usage
- Bandwidth usage
- Connection count

Free tier limits:
- 0.5 GB storage
- 10 GB bandwidth/month
- Unlimited connections

---

## 🆘 Troubleshooting

### "Application Error" on Heroku

**Check logs:**
```bash
heroku logs --tail
```

**Common issues:**
1. DATABASE_URL not set correctly
2. Migrations not run
3. Static files not collected

**Solution:**
```bash
heroku config:set DATABASE_URL='your-neon-connection-string'
heroku run python manage.py migrate
heroku run python manage.py collectstatic --noinput
```

### "Could not connect to server"

**Check if Neon database is running:**
1. Go to Neon dashboard
2. Check project status
3. Verify connection string is correct

### "SSL connection required"

**Ensure connection string includes:**
```
?sslmode=require
```

---

## ✅ Verification Checklist

After updating Heroku:

- [ ] DATABASE_URL set in Heroku config
- [ ] Migrations completed on Heroku
- [ ] Superuser created on Heroku
- [ ] Site loads without errors
- [ ] Can log into admin panel
- [ ] Can create/edit products
- [ ] Can create discount codes
- [ ] Checkout process works

---

## 📞 Need Help?

- **Heroku Logs:** `heroku logs --tail`
- **Neon Status:** [status.neon.tech](https://status.neon.tech)
- **Heroku Status:** [status.heroku.com](https://status.heroku.com)

---

## 🎉 You're All Set!

Your application is now using Neon PostgreSQL:
- ✅ Local development connected
- ✅ Ready to deploy to Heroku
- ✅ Free tier with 0.5 GB storage
- ✅ No expiration or shutdown concerns

**Next Steps:**
1. Update Heroku with the commands above
2. Test your production site
3. Monitor usage in Neon dashboard
4. Consider creating separate dev/prod databases
