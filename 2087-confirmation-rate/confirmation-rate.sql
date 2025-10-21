# Write your MySQL query statement below
select s.user_id,
round(sum(case when c.action="confirmed" then 1 else 0 End)/count(s.user_id),2) as confirmation_rate from Signups s 
left join confirmations c on s.user_id=c.user_id 
group by user_id ;