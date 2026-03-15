import pandas as pd

customers = pd.DataFrame({
    "customer_id":[1,2,3,4],
    "name":["Alice","Bob","Charlie","David"],
    "region":["North","South","North","West"]
})

orders = pd.DataFrame({
    "order_id":[101,102,103,104,105],
    "customer_id":[1,2,1,3,4],
    "product_id":[201,202,203,201,202],
    "amount":[100,200,150,300,250]
})

products = pd.DataFrame({
    "product_id":[201,202,203],
    "product_name":["Laptop","Phone","Tablet"],
    "category":["Electronics","Electronics","Electronics"]
})

customers.to_csv("customers.csv",index=False)
orders.to_csv("orders.csv",index=False)
products.to_csv("products.csv",index=False)

print("Sample data created.")
