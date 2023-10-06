select
  count(distinct cs_order_number) as "order count",
  sum(cs_ext_ship_cost) as "total shipping cost",
  sum(cs_net_profit) as "total net profit"
from
  catalog_sales cs1,
  date_dim,
  customer_address,
  call_center
where
  d_date between '{year_param}-{month_param}-01'
  and dateadd(
    day,
    60,
    to_date('{year_param}-{month_param}-01')
  )
  and cs1.cs_ship_date_sk = d_date_sk
  and cs1.cs_ship_addr_sk = ca_address_sk
  and ca_state = '{state_param}'
  and cs1.cs_call_center_sk = cc_call_center_sk
  and cc_county in (
    '{county_param_1}', '{county_param_2}',
    '{county_param_3}', '{county_param_4}',
    '{county_param_5}'
  )
  and exists (
    select
      *
    from
      catalog_sales cs2
    where
      cs1.cs_order_number = cs2.cs_order_number
      and cs1.cs_warehouse_sk <> cs2.cs_warehouse_sk
  )
  and not exists(
    select
      *
    from
      catalog_returns cr1
    where
      cs1.cs_order_number = cr1.cr_order_number
  )
order by
  count(distinct cs_order_number)
limit
  10;
