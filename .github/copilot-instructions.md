# Django Learning Repository - AI Instructions

## Codebase Overview

This is a **Django learning repository** containing 11 independent Django projects demonstrating core Django features in progression. Each project is self-contained with its own `manage.py`, database, and configuration.

**Projects & Patterns:**
- `email_project/` - Email sending using `django.core.mail.send_mail()`
- `formproject/` - Form validation with `django.forms`
- `Hello/` - Basic routing with URL includes and multiple views
- `model_project/`, `model2_project/`, `model3_project/` - ORM models and CRUD operations
- `Secondproject/` - Multiple apps in single project (`testapp1`, `testapp2`)
- `templateproject/`, `templatetagproject/` - Template rendering and custom template tags
- `Thirdproject/` - App-level URL configuration with `include()`
- `Urlproject/` - URL routing patterns
- `First_project/`, `model2_project/` (partial examples)

## Essential Commands

### Running Individual Projects
Each project requires navigating to its directory:
```bash
cd {project_name}
python manage.py runserver  # Start development server on port 8000
python manage.py makemigrations  # Create migration files
python manage.py migrate  # Apply migrations
python manage.py shell  # Django Python shell for model testing
```

### Database Operations
- All projects use SQLite (`db.sqlite3`) by default
- Models are registered in `INSTALLED_APPS` within `{project}/settings.py`
- Register models in `testapp/admin.py` for Django admin access

## Architectural Patterns

### 1. **Standard Project Structure**
Each project follows Django's scaffold:
```
{project_name}/
  ├── {project_name}/  # Configuration package
  │   ├── settings.py  # INSTALLED_APPS, DATABASES, TEMPLATES
  │   ├── urls.py      # Root URL patterns
  │   ├── wsgi.py      # Production server entry
  │   └── asgi.py      # Async server entry
  ├── {app_name}/      # Reusable app
  │   ├── models.py    # ORM models
  │   ├── views.py     # HTTP request handlers
  │   ├── forms.py     # Form validation (some projects)
  │   └── admin.py     # Admin configuration
  ├── templates/       # HTML templates (if used)
  ├── manage.py        # CLI utility
  └── db.sqlite3       # Database
```

### 2. **View Patterns**
Projects use **function-based views** exclusively:
```python
# Simple return
def my_view(request):
    return HttpResponse("<h1>Hello</h1>")

# With template rendering
def emp_list(request):
    emp = employee.objects.all()
    return render(request, 'testapp/emp.html', {'emp': emp})

# POST form handling
def send(request):
    if request.method == "POST":
        data = request.POST.get('fieldname')
        # Process and respond
    return render(request, 'template.html')
```

### 3. **Model Patterns**
Models use simple field definitions with optional `__str__()` for admin display:
```python
class Employee(models.Model):
    eno = models.IntegerField()  # No auto_increment, defined manually
    ename = models.CharField(max_length=60)
    esal = models.IntegerField()
    
    def __str__(self):
        return self.ename  # Displays in admin and shell
```

### 4. **URL Configuration**
- Projects use both direct patterns and `include()` for app-level routing
- Direct imports: `from testapp.views import *` (learning code, avoid in production)
- Proper includes: `path('myapp/', include('myapp.urls'))`

### 5. **Templates**
Templates live in `{project_root}/templates/{app_name}/` when configured in settings:
```python
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
# In TEMPLATES config:
'DIRS': [TEMPLATES_DIR],
```

## Key Implementation Details

### Forms (formproject)
- Uses `django.forms.Form` (not ModelForm)
- Simple fields without validation beyond type checking
- Rendered with `{{ form }}` in templates

### Email (email_project)
- Uses `django.core.mail.send_mail()`
- Requires `EMAIL_HOST_USER` in settings
- Accepts recipient list: `send_mail(subject, message, from_email, recipient_list)`

### Admin Configuration
- Basic registration: `admin.site.register(ModelName)`
- No custom admin classes used across projects

### Migrations
- All projects use Django's default migration system
- Migration files stored in `{app}/migrations/`
- SQLite database committed to repo (development only)

## Project-Specific Notes

### Secondproject
- Unique case: multiple apps (`testapp1`, `testapp2`) in single project
- Both apps imported in root `urls.py`
- Pattern: `from testapp1.views import *; from testapp2.views import *`

### model3_project
- Contains commented-out CRUD operations showing query patterns
- Shows both direct instantiation and `.objects.get()`, `.delete()` patterns

### templatetagproject, templateproject
- Emphasize template rendering over ORM
- Custom template tags may be defined (inspect `testapp/` folder)

## Common Pitfalls to Avoid

1. **App Registration**: Always add app to `INSTALLED_APPS` before creating migrations
2. **Import Style**: Learning projects use wildcard imports - assistants should suggest explicit imports in production code
3. **No Validation**: Models and forms lack constraints (blank=False, unique=True) - consider when helping expand
4. **Development-Only Settings**: DEBUG=True and insecure SECRET_KEY throughout - never copy to production

## Testing & Debugging

- Projects have `tests.py` files but no test cases are defined
- Use `python manage.py shell` to test model operations interactively
- Admin panel at `/admin/` (login with superuser created via `createsuperuser`)

## When Helping with This Codebase

1. **Identify the target project** - Multiple projects exist; clarify which one
2. **Respect learning intent** - Avoid over-engineering; match the simplicity level
3. **Reference existing patterns** - Use models/views from same project as templates
4. **Consider the progression** - Earlier projects (Hello) are simpler than later ones (model3_project with forms)
