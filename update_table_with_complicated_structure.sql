INSERT INTO behealthy.storage_translation (id, text_en)
SELECT st.id, st.text_en FROM behealthy.storage_recursivequestionchoices as srqc
left join behealthy.storage_question as sq on sq.id = srqc.question_id
left join behealthy.storage_choices as sc on sc.id = srqc.choice_id
left join behealthy.storage_translation as st on st.id = sc.text_id
where sq.id in (5892, 6277, 6278, 5891)
ON DUPLICATE KEY UPDATE 
 text_en = (SELECT st_copy.text_en FROM behealthy.storage_translation as st_copy where st_copy.id = VALUES(id) LIMIT 1);
