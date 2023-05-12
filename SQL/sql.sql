-- Список жилых помещений
select * from (
select -- count(*)

  rk.tu_rlty_kid

  ,trim(case when coalesce(t.name,t1.name) is null then 'г. Киров' else coalesce(tt.short_name,tt1.short_name) || ' ' || coalesce(t.name,t1.name) end
  || case when s.NAME is null then '' else ', ' end || st.SHORT_NAME || ' ' || s.NAME || ', д. '||
  h.HOUSE || case when h.CORPUS is not null then ', корп. '|| h.corpus end 
  || case when h.building is not null then ', стр. '|| h.building end 
  || case when na.flat is not null then ', кв. ' || na.flat end) as "Полный адрес"
--  ,  po.POST_INDEX as "Почтовый индекс"

  ,coalesce(t.name,t1.name) as "Нас. пункт"
  ,coalesce(tt.short_name,tt1.short_name) as "Тип нас.пункта"
  ,st.SHORT_NAME as "Тип улицы"
  ,s.NAME as "Улица"
  ,h.HOUSE as "№ дома"
--  ,h.CORPUS as "Корпус/литера"
  ,h.CORPUS || h.building as "Строение"
  ,na.flat as "Квартира/Помещение"
  , h.code_fias as "ФИАС дома"
--  , s.code_fias as "ФИАС улицы"


from TU_REALTY_KEY rk
  join NS_ADDRESS na on na.NS_ADR_ID = rk.NS_ADR_ID
  left join NS_HOUSE h on h.NS_HOS_ID = na.NS_HOS_ID
  left join NS_STREET s on s.NS_STRT_ID = h.NS_STRT_ID
  left join NS_STREET_TYPE st on st.NS_STRTTYP_ID = s.NS_STRTTYP_ID
--  left join NS_POSTOFFICE po on po.NS_PSTOFF_ID = h.NS_PSTOFF_ID
  left join NS_TOWN t on t.NS_TWN_ID = s.NS_TWN_ID
  left join NS_TOWN t1 on t1.NS_TWN_ID = h.NS_TWN_ID
  left join ns_town_type tt on t.ns_twntyp_id=tt.ns_twntyp_id
  left join ns_town_type tt1 on t1.ns_twntyp_id=tt1.ns_twntyp_id    
)
--where "Полный адрес" like '%адаков%'
--where "Полный адрес" like '%ововятск%'
