# Write your MySQL query statement below
SELECT name, IFNULL(Sum(Rides.distance), 0) AS travelled_distance
FROM Users
    Left Join Rides
    ON Users.id = Rides.user_id
GROUP BY Users.id
ORDER BY travelled_distance DESC, name ASC;