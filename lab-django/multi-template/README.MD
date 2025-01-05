.
├── db.sqlite3
├── manage.py
├── home
│   └── templates
│       └── index.html
├── store
│   └── templates
│       └── index.html
└── templates
    └── base.html


TEMPLATES = [
    {
        # ...
        'DIRS': [ BASE_DIR, BASE_DIR / "templates" ],
        # ...
    },
]