# Generated by Django 5.0.3 on 2024-03-08 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('discussion', '0002_questions'),
    ]

    operations = [
        migrations.RunSQL(
            sql= [("""
                CREATE TABLE "answers" (
                "id" INTEGER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
                "user_id" integer NOT NULL,
                "question_id" integer NOT NULL,
                "content" text,
                "created_at" timestamp,
                "updated_at" timestamp
                );
            """), 
            ("""
                ALTER TABLE "answers" ADD FOREIGN KEY ("user_id") REFERENCES "auth_user" ("id");
            """),
            ("""
                ALTER TABLE "answers" ADD FOREIGN KEY ("question_id") REFERENCES "questions" ("id");
            """)
            ],
            reverse_sql=[
                ("""
                    ALTER TABLE profiles DROP CONSTRAINT answers_user_id_fkey
                """),
                (""" 
                    ALTER TABLE profiles DROP CONSTRAINT answers_question_id_fkey
                """),
                ("""
                    DROP TABLE IF EXISTS answers;
                """)
            ]
        )
    ]