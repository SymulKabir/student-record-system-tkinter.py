from app.db.connection import db_instance, db


def migrate():
    db.execute("DROP TABLE IF EXISTS contacts")

    db.execute("""
        CREATE TABLE contacts (
            id VARCHAR(36) PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            phone VARCHAR(30) NOT NULL
        )
    """)

    db_instance.commit()
    db_instance.close()

    print("Migration completed successfully.")


if __name__ == "__main__":
    migrate()