select
  i_item_id,
  ca_country,
  ca_state,
  ca_county,
  avg(
    cast(
      cs_quantity as decimal(12, 2)
    )
  ) agg1,
  avg(
    cast(
      cs_list_price as decimal(12, 2)
    )
  ) agg2,
  avg(
    cast(
      cs_coupon_amt as decimal(12, 2)
    )
  ) agg3,
  avg(
    cast(
      cs_sales_price as decimal(12, 2)
    )
  ) agg4,
  avg(
    cast(
      cs_net_profit as decimal(12, 2)
    )
  ) agg5,
  avg(
    cast(
      c_birth_year as decimal(12, 2)
    )
  ) agg6,
  avg(
    cast(
      cd1.cd_dep_count as decimal(12, 2)
    )
  ) agg7
from
  catalog_sales,
  customer_demographics cd1,
  customer_demographics cd2,
  customer,
  customer_address,
  date_dim,
  item
where
  cs_sold_date_sk = d_date_sk
  and cs_item_sk = i_item_sk
  and cs_bill_cdemo_sk = cd1.cd_demo_sk
  and cs_bill_customer_sk = c_customer_sk
  and cd1.cd_gender = '{gender_param}'
  and cd1.cd_education_status = '{education_param}'
  and c_current_cdemo_sk = cd2.cd_demo_sk
  and c_current_addr_sk = ca_address_sk
  and c_birth_month in ({month_param_1}, {month_param_2}, {month_param_3}, {month_param_4}, {month_param_5},
  {month_param_1})
  and d_year = {year_param}
  and ca_state in (
    '{state_param_1}', '{state_param_2}', '{state_param_3}', '{state_param_4}', '{state_param_5}', '{state_param_6}',
    '{state_param_7}'
  )
group by
  rollup (
    i_item_id, ca_country, ca_state, ca_county
  )
order by
  ca_country,
  ca_state,
  ca_county,
  i_item_id
limit
  100;
