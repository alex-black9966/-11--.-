Работа с базой данных
Задание 1
SELECT l.login, COUNT(i.id) AS "deliveryCount" 
FROM "Couriers" AS l 
LEFT JOIN "Orders" AS i ON l.id = i."courierId" 
WHERE i."inDelivery" = true 
GROUP BY l.login;
Скриншот Задание1.png
Задание 2
SELECT track, 
    CASE 
      WHEN finished = true THEN 2 
      WHEN cancelled = true THEN -1 
      WHEN "inDelivery" = true THEN 1 
ELSE 0 END AS status 
FROM "Orders";
Скриншот Задание2.png

Автоматизация
Скриншот Автотест.png
