SELECT
    employees_id,
    project_id
FROM employee_projects
WHERE employees_id BETWEEN 200 AND 250
    AND project_id < 50 AND > 100;