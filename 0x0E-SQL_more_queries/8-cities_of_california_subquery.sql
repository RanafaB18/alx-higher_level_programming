-- Lists all cities of CA in the database hbtn_0d_usa.
-- Results are ordered by ascending cities.id.
SELECT `cities`.`id`, `cities`.`name`
FROM `hbtn_0d_usa`.`cities` AS `cities`, `hbtn_0d_usa`.`states` AS `states`
WHERE `states`.`name` = 'California' AND `states`.`id` = `cities`.`state_id`
ORDER BY `cities`.`id` ASC;
