import pandas as pd 
import numpy  as np

df=pd.read_csv("supplychain.csv",encoding="latin1")
# print(df)
print(df.head())
print(df.tail())
print(df.shape)
print(df.info())
print(df.describe())

df.columns=df.columns.str.replace(" ","_")
print(df.info())


percent=df.isnull().sum()/len(df)*100
print(percent.round(3))

df.drop(columns=["Product_Description",
    "Order_Zipcode",
    "Customer_Email",
    "Customer_Fname",
    "Customer_Lname",
    "Customer_Password",
    "Customer_Street",
    "Customer_Zipcode",
    "Product_Image",
    "Latitude",
    "Longitude"],inplace=True)

print(df.isnull().sum()[df.isnull().sum()>0])
# print(df.columns.tolist())
print(df.duplicated().sum())
print(df["Order_Item_Id"].duplicated().sum())

print(df.dtypes)
df["order_date_(DateOrders)"]=pd.to_datetime(df["order_date_(DateOrders)"],errors="coerce")
df["shipping_date_(DateOrders)"]=pd.to_datetime(df["shipping_date_(DateOrders)"],errors="coerce")
print(df.dtypes)

print(df["Product_Status"].value_counts(dropna=False))
print(df["Late_delivery_risk"].value_counts(dropna=False))
print(df["Order_Status"].value_counts(dropna=False))

print(df[["Days_for_shipping_(real)","Days_for_shipment_(scheduled)"]].describe())

df["Shipping_Duration"]=df["Days_for_shipping_(real)"]-df["Days_for_shipment_(scheduled)"]
print(df["Shipping_Duration"].value_counts(dropna=False))

print("Early",(df["Shipping_Duration"]<0).sum())
print("on_time",(df["Shipping_Duration"]==0).sum())
print("Late",(df["Shipping_Duration"]>0).sum())

print("earliest order date",df["order_date_(DateOrders)"].min())
print("latest order date",df["order_date_(DateOrders)"].max())

print("earliest shipping date",df["shipping_date_(DateOrders)"].min())
print("latest shippig date",df["shipping_date_(DateOrders)"].max())

# check miising or invalid dates
print(df["Days_for_shipment_(scheduled)"].isna().sum())
print(df["Days_for_shipping_(real)"].isna().sum())

# shipping dates occur before order dates
invalid_date=df[df["shipping_date_(DateOrders)"]<df["order_date_(DateOrders)"]]
print("shipping before order",len(invalid_date))

columns = [
    "Sales",
    "Order_Item_Total",
    "Order_Profit_Per_Order",
    "Product_Price",
    "Order_Item_Quantity"
]
print(df[columns].describe())

# negative-profit records
negative_profit=df[df["Order_Profit_Per_Order"]<0]
print("negative profit",len(negative_profit))
print(negative_profit.sort_values("Order_Profit_Per_Order").head(10)
      [["Order_Id","Order_Item_Id","Order_Profit_Per_Order","Sales","Order_Item_Total","Product_Price"]])

# Sales and profit validation.
category_loss=negative_profit.groupby("Category_Name").agg(negative_profit_row=("Order_Item_Id","count"),
                                                           avg_profit=("Order_Profit_Per_Order","mean"),
                                                           large_loss=("Order_Profit_Per_Order","min"))
print(category_loss.sort_values("large_loss"))

df["Profit_Margin"]=df["Order_Profit_Per_Order"]/df["Sales"]*100
print(df[["Sales","Order_Profit_Per_Order","Profit_Margin"]].describe())

print("Negative margins:",
      (df["Profit_Margin"] < 0).sum())

print("Margins below -100%:",
      (df["Profit_Margin"] < -100).sum())

print("Margins above 50%:",
      (df["Profit_Margin"] > 50).sum())

# delivery performance.

# Which shipping modes have the highest delivery delay?
ship_analysis=df.groupby("Shipping_Mode").agg(Total_order=("Order_Id","count"),
                                              avg_actual_days=("Days_for_shipping_(real)","mean"),
                                              avg_sheduled_days=("Days_for_shipment_(scheduled)","mean"),
                                              late_risk=("Late_delivery_risk","sum"))
ship_analysis["avg_delay_days"]=(ship_analysis["avg_actual_days"]-ship_analysis["avg_sheduled_days"])
print(ship_analysis.sort_values("avg_delay_days",ascending=False).round(2))

# What percentage of records are flagged as late-delivery risk for each shipping mode?
ship_analysis["Late_Risk_Percent"] = (
    ship_analysis["late_risk"]
    / ship_analysis["Total_order"]
) * 100

print(
    ship_analysis[
        ["Total_order", "avg_delay_days",
         "late_risk", "Late_Risk_Percent"]].round(2))

# Which regions have the largest delivery delays?
df["Delivery_Delay"]=df["Days_for_shipping_(real)"]-df["Days_for_shipment_(scheduled)"]
region_analysis=df.groupby("Order_Region").agg(total_order=("Order_Item_Id","count"),
                                         avg_delay_days=("Delivery_Delay","mean"))
print(region_analysis.sort_values("avg_delay_days",ascending=False).round(2))

# What percentage of order items are early, on time, or late?

def day(Delivery_Delay):
    if Delivery_Delay<0:
        return "Early"
    elif Delivery_Delay==0:
        return "On Time"
    elif Delivery_Delay>0:
        return "Late"
vector=np.vectorize(day)
df["Delivery_Timing"]=vector(df["Delivery_Delay"])
print(df["Delivery_Timing"].value_counts(dropna=False))

# sales and profitability.

# Which product categories generate the highest sales?
categories_analysis=df.groupby("Category_Name").agg(total_order=("Order_Item_Id","count"),
                                    total_sales=("Sales","sum"),
                                    avg_sales=("Sales","mean"))
print(categories_analysis.sort_values("total_sales",ascending=False).head(5).round(2))

# Which markets generate the highest sales?
markets_analysis=df.groupby("Market").agg(total_order=("Order_Item_Id","count"),
                                    total_sales=("Sales","sum"),
                                    avg_sales=("Sales","mean"))
print(markets_analysis.sort_values("total_sales",ascending=False).round(2))

# How do sales and profit change month by month?
df["Months"]=df["order_date_(DateOrders)"].dt.to_period("M")
monthly_analysis=df.groupby("Months").agg(total_order=("Order_Item_Id","count"),
                             total_sales=("Sales","sum"),
                             profit=("Order_Profit_Per_Order","sum"))
print(monthly_analysis.sort_index().round(2))

# Which product categories have the most negative-profit records?
loss_profit=df[df["Order_Profit_Per_Order"]<0]
category=loss_profit.groupby("Category_Name").agg(total_order=("Order_Item_Id","count"),
                                                     neg_profit=("Order_Profit_Per_Order","sum"))
print(category.sort_values("neg_profit").round(2))

# operations and customers.
# What is the distribution of order statuses?
dist=df["Order_Status"].value_counts()
print(dist)

# Which customer segments generate the highest sales?
cust_analysis=df.groupby("Customer_Segment").agg(total_orders=("Order_Item_Id","count"),
                                        total_sales=("Sales","sum"))
pd.options.display.float_format="{:.2f}".format
print(cust_analysis.sort_values("total_sales",ascending=False).round(3))

# Which departments generate the highest sales?
dept_analysis=df.groupby("Department_Name").agg(total_orders=("Order_Item_Id","count"),
                                       total_sales=("Sales","sum"))
print(dept_analysis.sort_values("total_sales",ascending=False).round(3))

# trends and product analysis.
# Are delivery delays improving or worsening over time?
monthly_delay = df.groupby("Months").agg(
    avg_delay_days=("Delivery_Delay", "mean"))
print(monthly_delay.sort_index().round(2))

# Which product categories have the highest total quantity sold?
quantity_analysis=df.groupby("Category_Name").agg(total_quantity=("Order_Item_Quantity","sum"))
print(quantity_analysis.sort_values("total_quantity",ascending=False).round(2))

# Which products generate the highest sales?
product_analysis=df.groupby("Product_Name").agg(total_order=("Order_Item_Id","count"),
                                                total_sales=("Sales","sum"))
print(product_analysis.sort_values("total_sales",ascending=False).head(10).round(2))

# What is the relationship between discounts and recorded profit?
discount_analysis = df.groupby("Order_Item_Discount_Rate").agg(
    total_order_items=("Order_Item_Id", "count"),
    avg_discount=("Order_Item_Discount", "mean"),
    total_sales=("Sales", "sum"),
    total_profit=("Order_Profit_Per_Order", "sum"))
print(discount_analysis.round(2))

print(df["Sales"].sum())
print(df["Order_Profit_Per_Order"].sum())
# df["Months"]=df["Months"].astype(str)
# df.to_excel("supplychain_cleaned.xlsx",index=False,sheet_name="SupplyChain")
# print("the file saved succesfully")

