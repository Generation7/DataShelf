## FastAPI + SQLite Example Project

This is a minimal FastAPI project using SQLAlchemy with SQLite for basic CRUD operations on an `Item` resource.

### Prerequisites
- Python 3.10+

### Setup
```bash
python -m venv .venv
./.venv/Scripts/Activate.ps1
pip install -r requirements.txt
```

### Run
```bash
uvicorn app.main:app --reload
```

App will be available at `http://127.0.0.1:8000` with interactive docs at `/docs`.

### Project Structure
```
app/
  main.py
  config.py
  database.py
  deps.py
  crud.py
  models.py
  schemas.py
  routers/
    __init__.py
    items.py
requirements.txt
sql/
  sample.sql
```

### Sample SQL
See `sql/sample.sql` for example SQL statements.

### Notes
- SQLite file `app.db` is created in the project root on first run.
- Adjust database URL in `app/config.py` if needed.

