# Write your MySQL query statement below

select v.customer_id, count(v.visit_id) as count_no_trans 
from Visits v
LEFT join Transactions t
on v. visit_id = t.visit_id

WHERE t.transaction_id IS NULL 
GROUP BY v.customer_id; 