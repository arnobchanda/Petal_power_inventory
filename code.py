import pandas as pd

inventory = pd.read_csv("C:\Python Programs\Project 2\inventory.csv")
#print(inventory.head(10))

staten_island = inventory.head(10)

product_request = staten_island.product_description

seed_request = inventory[(inventory.location == "Brooklyn") & (inventory.product_type == "seeds")]

isthere = lambda num : True \
	if num > 0 else False

inventory["in_stock"] = inventory.quantity.apply(isthere)

inventory["total_value"] = inventory.price * inventory.quantity

combine_lambda = lambda row: \
    '{} - {}'.format(row.product_type,row.product_description)

inventory["full_description"] = inventory.apply(combine_lambda,axis = 1)

print (inventory)

inventory.to_csv("Edited_inventory.csv")