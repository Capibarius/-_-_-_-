import sqlite3
from datetime import datetime

db_name = "db.db"
connection = sqlite3.connect(db_name)
cursor = connection.cursor()

print("Задание 3")
query_3 = """
SELECT 
    u.Email AS UserLogin,
    SUM(fc.MonthlyPrice * s.DurationMonths) AS TotalPayment
FROM 
    Subscriptions s
JOIN 
    Users u ON s.UserID = u.UserID
JOIN 
    ForecastCatalog fc ON s.ForecastID = fc.ForecastID
WHERE 
    strftime('%Y', s.StartDate) = strftime('%Y', 'now') -- Текущий год
GROUP BY 
    u.Email;
"""
result_3 = cursor.execute(query_3).fetchall()
print(result_3)

print("\nЗадание 4")
query_4 = """
SELECT DISTINCT
    u1.Email AS UserLogin1,
    u2.Email AS UserLogin2
FROM 
    Subscriptions s1
JOIN 
    Subscriptions s2 ON s1.ForecastID = s2.ForecastID AND s1.StartDate = s2.StartDate
JOIN 
    Users u1 ON s1.UserID = u1.UserID
JOIN 
    Users u2 ON s2.UserID = u2.UserID
WHERE 
    u1.UserID < u2.UserID;
"""
result_4 = cursor.execute(query_4).fetchall()
print(result_4)

print("\nЗадание 5")
query_5 = """
SELECT 
    u1.Email AS UserLogin1,
    u2.Email AS UserLogin2
FROM 
    Subscriptions s1
JOIN 
    Subscriptions s2 ON s1.ForecastID = s2.ForecastID
JOIN 
    Users u1 ON s1.UserID = u1.UserID
JOIN 
    Users u2 ON s2.UserID = u2.UserID
WHERE 
    u1.UserID < u2.UserID
GROUP BY 
    u1.Email, u2.Email, s1.ForecastID
HAVING 
    COUNT(DISTINCT strftime('%Y-%m', s1.StartDate)) >= 2;
"""
result_5 = cursor.execute(query_5).fetchall()
print(result_5)

connection.close()
