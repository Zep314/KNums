-- запись результатов работы в базу

update tu_realty tr set tr.cadastral_number = (select xk.cadastral_number from xxx_knum xk where tr.tu_rlty_kid=xk.tu_rlty_kid) where tr.cadastral_number is null;
