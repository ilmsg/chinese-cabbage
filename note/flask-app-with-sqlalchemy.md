
**flask กับ sqlalchemy**

เวลาเราใช้ flask กับ sqlalchemy จะต้องใส่ค่า config `SQLALCHEMY_DATABASE_URI` ที่ app ที่เอาไว้ต่อกับ database ด้วย

    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"

    db = SQLAlchemy(app)

ทีนี้ตัว db ของเราก็พร้อมใช้งานแล้ว

---

เคยเห็น source code แบบนี้อยู่ในไพล์ `models.py` (ของชาวบ้านเค้า) ก็งงว่า ไปต่อกับ app ยังไง, แล้วไปต่อกับ database ตอนไหน

ไพล์ `models.py`

    from flask_sqlalchemy import SQLAlchemy
    db = SQLAlchemy()

มารู้ทีหลัง db เค้ามี method `.init_app` เอาไว้ใส่ทีหลังได้

ไพล์ `app.py`

    from flask import Flask
    from .models import db

    app = Flask(__name__)
    db.init_app(app)
---

**flask กับ config**

เรื่องการใส่ config ให้กับ app เราจะใส่ตรงๆแบบนี้ ซึ่งเหมาะกับ app เล็กๆไม่มี config ให้เปลี่ยนเยอะ, หรือจะใส่จาก method `.from_object` นี้ก็ได้

ไพล์ `app.py`

    from flask import Flask

    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"

อีกแบบนึง เหมาะกับ app ที่มีขนาดใหญ่ขึ้น ทำงานกับหลายไพล์ ปรับเปลี่ยนค่าได้ง่าย

ไพล์ `.env` จะถูกเรียกใช้ใน `config.py`

    DATABASE_URL=sqlite:///dev.sqlite

ไพล์ `config.py` จะถูกเรียกใน `app.py`

    import os

    class Config:
        SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')

ไพล์ `app.py`

    from flask import Flask
    from .config import Config

    app = Flask(__name__)
    app.config.from_object(Config)
