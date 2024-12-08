import sqlite3
from datetime import datetime

db_name = "db.db"

connection = sqlite3.connect(db_name)
cursor = connection.cursor()

sql_script = """
CREATE TABLE Users (
    UserID INTEGER PRIMARY KEY AUTOINCREMENT,
    Email VARCHAR(100) UNIQUE NOT NULL,
    DateOfBirth DATE NOT NULL,
    TimeOfBirth TIME
);

CREATE TABLE ForecastCatalog (
    ForecastID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name VARCHAR(100) NOT NULL,
    MonthlyPrice NUMERIC(10, 2) NOT NULL
);

CREATE TABLE Subscriptions (
    SubscriptionID INTEGER PRIMARY KEY AUTOINCREMENT,
    UserID INTEGER NOT NULL,
    ForecastID INTEGER NOT NULL,
    StartDate DATE NOT NULL,
    DurationMonths INTEGER NOT NULL,
    FOREIGN KEY (UserID) REFERENCES Users(UserID),
    FOREIGN KEY (ForecastID) REFERENCES ForecastCatalog(ForecastID),
    UNIQUE (UserID, ForecastID, StartDate)
);
"""

cursor.executescript(sql_script)

users_data = [
    ("user1@mail.ru", "1990-05-15", "12:30:00"),
    ("user2@mail.ru", "1985-11-20", "08:45:00"),
    ("user3@mail.ru", "2000-01-10", "23:15:00"),
    ("user4@mail.ru", "1995-07-25", "14:00:00"),
    ("user5@mail.ru", "1992-12-05", "18:30:00"),
    ("user6@mail.ru", "1988-03-30", "09:15:00")
]

forecast_data = [
    ("Зодиакальный", 10.00),
    ("Китайский", 15.00),
    ("Цыганский", 12.50),
    ("Нумерологический", 20.00),
    ("Таро", 25.00)
]

subscriptions_data = [
    (1, 1, "2024-01-01", 3),
    (2, 1, "2024-01-01", 1),
    (3, 2, "2024-01-01", 2),
    (4, 2, "2024-01-01", 4),
    (5, 3, "2024-02-01", 1),
    (6, 3, "2024-02-01", 2),
    (1, 4, "2024-03-01", 2),
    (2, 4, "2024-03-01", 1),
    (3, 5, "2024-04-01", 5),
    (4, 5, "2024-04-01", 3),
    (5, 1, "2024-05-01", 1),
    (6, 2, "2024-05-01", 2),
    (1, 3, "2024-06-01", 6),
    (2, 4, "2024-06-01", 3),
    (3, 5, "2024-06-01", 2),
    (4, 3, "2024-07-01", 3),
    (5, 1, "2024-07-01", 2),
    (6, 2, "2024-08-01", 3)
]

cursor.executemany("INSERT INTO Users (Email, DateOfBirth, TimeOfBirth) VALUES (?, ?, ?)", users_data)
cursor.executemany("INSERT INTO ForecastCatalog (Name, MonthlyPrice) VALUES (?, ?)", forecast_data)
cursor.executemany(
    "INSERT INTO Subscriptions (UserID, ForecastID, StartDate, DurationMonths) VALUES (?, ?, ?, ?)", 
    subscriptions_data
)

connection.commit()
connection.close()
