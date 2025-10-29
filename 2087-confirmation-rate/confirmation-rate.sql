SELECT s.user_id, round(avg( if(c.action = 'confirmed',1,0)),2) AS confirmation_rate
FROM Signups s
left JOIN Confirmations c ON s.user_id = c.user_id
group by user_id ;