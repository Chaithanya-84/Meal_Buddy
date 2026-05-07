# Meal Buddy

Simple Django food-ordering demo app. Browse restaurants, view menus, add items to a cart and checkout (Razorpay integration stub). Includes a small site admin panel and the Django admin.

## Features
- Browse restaurants and menus
- Add menu items to cart and checkout via Razorpay
- Admin panel for managing restaurants and menu items
- Django admin enabled for full model management
- Food-themed UI with animated background and hero mock

## Prerequisites
- Python 3.10+ installed
- Git (optional)
- PowerShell (the quickstart commands below use PowerShell on Windows)

## Quickstart (Windows PowerShell)

1. Clone repo (or use local copy)
```powershell
git clone https://github.com/Chaithanya-84/Meal_Buddy.git
cd Meal_Buddy
```

2. Create & activate virtual environment
```powershell
python -m venv venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned -Force
.\venv\Scripts\Activate.ps1
```

3. Upgrade pip and install requirements
```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

4. Configure development settings
- Open `meal_buddy/settings.py`
  - Set `DEBUG = True` for local development
  - Set `ALLOWED_HOSTS = ['127.0.0.1','localhost']`
  - Replace `SECRET_KEY` with your own (for production, use env vars)
  - Replace or set Razorpay keys (or keep test keys while developing)

5. Apply database migrations
```powershell
python manage.py migrate
```

6. Create a superuser (interactive)
```powershell
python manage.py createsuperuser
```

7. (Optional dev) collect static
```powershell
python manage.py collectstatic --noinput
```

8. Run development server
```powershell
python manage.py runserver
```
Open http://127.0.0.1:8000/ in your browser.

## Useful URLs
- Home: `http://127.0.0.1:8000/`
- Django Admin: `http://127.0.0.1:8000/admin` (login with your superuser)
- Site Admin Panel: `http://127.0.0.1:8000/admin_panel`
- Add restaurant form: `http://127.0.0.1:8000/open_add_restaurant`
- Show restaurants: `http://127.0.0.1:8000/open_show_restaurant`

## How to add restaurants
- Via Django admin: go to `/admin` → Restaurants → Add.
- Via web UI: sign in as admin (`/open_signin`), then use **Add New Restaurant** or the admin panel.

## Recommended .gitignore
Add the following to `.gitignore` to avoid committing virtualenv, DB, caches and static collector output:
```
venv/
*.pyc
__pycache__/
db.sqlite3
/staticfiles/
*.log
*.env
.DS_Store
```

## Notes / Troubleshooting
- If you see `Bad Request (400)`: set `ALLOWED_HOSTS` correctly or use `127.0.0.1`.
- Template errors: ensure `{% extends %}` is the first tag in templates that extend a parent template. `base.html` must load `{% load static %}`.
- Static files not loading: with `DEBUG=True`, Django serves static files; in production set up a static server and run `collectstatic`.
- Replace test Razorpay keys in `meal_buddy/settings.py` with secure keys (use environment variables for production).

## Tests
Run Django tests (if any):
```powershell
python manage.py test
```

## Clean up Git history (optional)
The repo currently contains generated static/admin files and `__pycache__`. To clean up:
1. Add `.gitignore` as suggested.
2. Remove tracked files you want excluded:
```powershell
git rm -r --cached venv staticfiles db.sqlite3
git commit -m "Remove generated/static files and add .gitignore"
git push
```

## License & Attribution
This project is provided as-is for demo/learning. Add a license file if you plan to publish.

---

If you want, I can also add the `.gitignore` and remove large generated files from the repo.
