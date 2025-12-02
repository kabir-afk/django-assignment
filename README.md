# django-assignment

A small Django project with two apps: `api` and `banks`. Time taken to desig the API : 1.5 days

**Live Deployment:**

- **API URL**: https://django-assignment-y6ia.onrender.com/
- **Base Endpoint**: https://django-assignment-y6ia.onrender.com/api/v1
- **Deployed on**: Render

**Project Overview:**

- **`banks/`**: Django project settings, URL configuration and WSGI/ASGI entrypoints.
- **`api/`**: App containing models, serializers, views and URL routes for the project's API.

This repository is intended as an assignment/demo Django project and includes example APIs and models.

**Requirements:**

- Python 3.8+ (adjust as needed)
- Django (version used in development)
- (Optional) `djangorestframework` if the API uses DRF

**Quick Setup (PowerShell)**

1. Create and activate a virtual environment:

```
python -m venv .venv
.\.venv\Scripts\activate
```

2. Install dependencies:

```
pip install -r requirements.txt
# If there is no requirements.txt, install Django and DRF manually:
pip install django djangorestframework
```

3. Run migrations and start the development server:

```
python manage.py migrate
python manage.py runserver
```

4. (Optional) Create a superuser to access the admin:

```
python manage.py createsuperuser
```

**Environment Configuration**

Create a `.env` file in the `banks/` directory with the following variables. You can customize these based on your setup:

```
ENVIRONMENT=development
SECRET_KEY=<your-secret-key>
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=<your-db-url>
POSTGRES_USER=postgres
POSTGRES_PASSWORD=<your-password>
POSTGRES_HOST=localhost
POSTGRES_PORT=5432 (This project used 5433)
```

Make sure the `.env` file is added to `.gitignore` to avoid committing sensitive credentials to version control.

**Project Structure**

- `manage.py` — Django management script
- `banks/` — main Django project (settings, urls, wsgi/asgi)
- `api/` — app containing models, serializers, views, tests and utilities

**Approach**

- **Large Dataset Handling (Pagination)** : Returning all branch records at once caused slow responses and heavy payloads. Implementing DRF’s PageNumberPagination allowed data to be delivered in smaller, efficient chunks.

- **Filtering by Multiple Parameters** : Users needed branch details filtered by state, city, district, bank name, etc. Using DjangoFilterBackend with a custom BranchFilter enabled precise, multi-parameter filtering.

- **Filtering Based on Search** : For partial or broad matches, DRF’s SearchFilter was added. By enabling flexible, text-based searches across several fields, this enhanced the user experience.

- **Developer-Friendly Discovery Endpoints** : To simplify frontend workflows, dedicated endpoints were created to fetch all banks, and the cities or states a selected bank operates in, enabling easy dropdown population and faster UI interactions.

**API Examples**

- **List Banks**: `GET /banks` — Returns a JSON array of banks.

  - Example response: `[{"id": 1, "name": "State Bank of India"}, {"id": 2, "name": "Punjab National Bank"}]`

- **Bank Detail**: `GET /banks/<int:id>` — Returns details for a specific bank.

  - Example response: `{"id": 1, "name": "State Bank"}`

- **Bank Branches**: `GET /banks/<int:id>/branches` — List branches for a bank with filtering, searching and pagination.

  - Query params: `?page=2&city=Mumbai&state=Maharashtra&search=Main`
  - Example response (paginated): `{"count": 125, "next": ".../branches?page=2", "results": [{"ifsc":"SBIN0000001","branch_name":"KOLKATA MAIN","city":"Mumbai","state":"Maharashtra"}]}`

- **All Branches**: `GET /branches` — Returns all branches (paginated), supports the same filters/search as bank branches.

  - Example: `GET /branches?state=Karnataka`

- **Branch Detail**: `GET /branches/<str:ifsc>` — Returns branch details by IFSC code.

  - Example response:

  `{
    "ifsc": "SBIN0000001",
    "bank": "STATE BANK OF INDIA",
    "branch_name": "KOLKATA MAIN",
    "address": "SAMRIDDHI BHAWAN, 1 STRAND ROAD, KOLKATA 700 001",
    "city": "KOLKATA",
    "district": "KOLKATA",
    "state": "WEST BENGAL"
}`

- **Validate IFSC**: `GET /branches/<str:ifsc>/validate` — Simple endpoint that returns whether an IFSC exists.
  - Example responses: `"Valid IFSC"` (HTTP 200) or `"Invalid IFSC"` (HTTP 404)
