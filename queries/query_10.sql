select
  i_item_id,
  i_item_desc,
  i_category,
  i_class,
  i_current_price,
  sum(cs_ext_sales_price) as itemrevenue,
  sum(cs_ext_sales_price)* 100 / sum(
    sum(cs_ext_sales_price)
  ) over (partition by i_class) as revenueratio
from
  catalog_sales,
  item,
  date_dim
where
  cs_item_sk = i_item_sk
  and i_category in ('{category_param_1}', '{category_param_2}', '{category_param_3}')
  and cs_sold_date_sk = d_date_sk
  and d_date between cast('{date_param}' as date)
  and dateadd(
    day,
    30,
    to_date('{date_param}')
  )
group by
  i_item_id,
  i_item_desc,
  i_category,
  i_class,
  i_current_price
order by
  i_category,
  i_class,
  i_item_id,
  i_item_desc,
  revenueratio
limit
  10;
