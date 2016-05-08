<%
city_list = ['tyo', 'ngo', 'osa', 'fuk']
%>
create table sales_by_city(
  yyyymm varchar(6)
% for city in city_list:
  , sales_${city} integer
% endfor
);

insert into sales_by_city(
  yyyymm
% for city in city_list:
  , sales_${city}
% endfor
)
select
  yyyymm
% for city in city_list:
  , sum(case when city = '${city}' then sales else 0 end) sales_${city}
% endfor
from sales
group by yyyymm
;
