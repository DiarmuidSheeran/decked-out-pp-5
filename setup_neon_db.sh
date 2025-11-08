#!/bin/bash
# Quick setup script for migrating to Neon database

echo "================================================"
echo "Neon Database Setup for Decked Out"
echo "================================================"
echo ""

# Check if DATABASE_URL is provided
if [ -z "$1" ]; then
    echo "Usage: ./setup_neon_db.sh 'your-neon-connection-string'"
    echo ""
    echo "Steps to get your connection string:"
    echo "1. Go to https://neon.tech"
    echo "2. Sign up (no credit card required)"
    echo "3. Create a new project"
    echo "4. Copy the connection string"
    echo ""
    echo "Example:"
    echo "./setup_neon_db.sh 'postgresql://user:pass@ep-xxx.region.aws.neon.tech/dbname?sslmode=require'"
    exit 1
fi

DATABASE_URL="$1"

echo "✓ Connection string received"
echo ""

# Update env.py
echo "Updating env.py with new database URL..."
if [ -f "env.py" ]; then
    # Backup existing env.py
    cp env.py env.py.backup
    echo "✓ Backed up existing env.py to env.py.backup"
    
    # Update DATABASE_URL line
    sed -i "s|os.environ.setdefault('DATABASE_URL'.*|os.environ.setdefault('DATABASE_URL', '$DATABASE_URL')|" env.py
    echo "✓ Updated env.py"
else
    echo "⚠ env.py not found. Creating new one..."
    cat > env.py << EOF
import os

# Debug mode for local development
os.environ.setdefault('DEBUG', 'True')

# Database - Neon PostgreSQL
os.environ.setdefault('DATABASE_URL', '$DATABASE_URL')

# Django secret key
os.environ.setdefault('SECRET_KEY', 'your-secret-key-here')

# Stripe (update with your keys)
os.environ.setdefault('STRIPE_PUBLIC_KEY', 'pk_test_dummy')
os.environ.setdefault('STRIPE_SECRET_KEY', 'sk_test_dummy')
os.environ.setdefault('STRIPE_WH_SECRET', 'whsec_dummy')

# Email
os.environ.setdefault('EMAIL_HOST_USER', 'your-email@example.com')
os.environ.setdefault('EMAIL_HOST_PASSWORD', 'your-password')

# AWS (if using S3)
os.environ.setdefault('USE_AWS', 'False')
EOF
    echo "✓ Created new env.py"
fi

echo ""
echo "Running database migrations..."
python manage.py migrate

if [ $? -eq 0 ]; then
    echo ""
    echo "✓ Migrations completed successfully"
    echo ""
    echo "================================================"
    echo "✅ Database setup complete!"
    echo "================================================"
    echo ""
    echo "Next steps:"
    echo "1. Create a superuser: python manage.py createsuperuser"
    echo "2. Start the server: python manage.py runserver"
    echo ""
    echo "For Heroku deployment:"
    echo "heroku config:set DATABASE_URL='$DATABASE_URL'"
    echo "heroku run python manage.py migrate"
    echo "heroku run python manage.py createsuperuser"
    echo ""
else
    echo ""
    echo "❌ Migration failed. Please check the error above."
    echo ""
    echo "Common issues:"
    echo "- Check connection string format"
    echo "- Ensure database is accessible"
    echo "- Verify SSL mode is included (?sslmode=require)"
    exit 1
fi
