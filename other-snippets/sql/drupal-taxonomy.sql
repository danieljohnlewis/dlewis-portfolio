-- In drupal 5/6, this is how you generate a menu based on taxonomy

SELECT "#", @rownum:=@rownum+1 rownum, "\n",
concat("INSERT INTO menu (mid, pid, path, title, weight, type) VALUES (", s.id+@rownum ,", 153, \"", ua.dst , "\", \"", td.name,"\", 0, 118) ;")
FROM (SELECT @rownum:=0) r, term_data td, url_alias ua, sequences s
WHERE
ua.src LIKE "taxonomy/term/%" and
td.tid = substr(ua.src, 15) and
s.name = "menu_mid"
