import pandas as pd
from sklearn.neighbors import NearestNeighbors
from collections import Counter

# Sample data
data = {
    'customer_id': [1, 2, 3, 4, 5, 6, 7, 8],
    'checkout_price': [200, 210, 205, 150, 160, 155, 300, 305],
    'purchased_products': [
        ['A', 'B'], ['B', 'C'], ['A', 'C'], ['D', 'E'],
        ['D'], ['E', 'F'], ['G', 'H'], ['G']
    ]
}

# Convert data to a DataFrame
df = pd.DataFrame(data)

# Step 1: Initialize and fit the NearestNeighbors model
neighbor_model = NearestNeighbors(n_neighbors=3, metric='euclidean')
neighbor_model.fit(df[['checkout_price']])

# Step 2: Define the recommendation function
def recommend_products_for_customers(df, n_neighbors=3):
    recommendations = {}  # To store recommendations for each customer
    
    # Iterate through each customer
    for index, row in df.iterrows():
        customer_id = row['customer_id']
        checkout_price = row['checkout_price']
        
        # Find the n_neighbors closest checkout prices for this customer
        distances, indices = neighbor_model.kneighbors([[checkout_price]], n_neighbors=n_neighbors)
        
        # Remove the customer itself from the similar customers (if present)
        similar_customers = df.iloc[indices[0]]
        similar_customers = similar_customers[similar_customers['customer_id'] != customer_id]
        
        # Aggregate the products bought by similar customers
        products = similar_customers['purchased_products'].sum()
        
        # Rank products by popularity
        popular_products = [product for product, _ in Counter(products).most_common()]
        
        # Store recommendations for the current customer
        recommendations[customer_id] = popular_products
    
    return recommendations

# Step 3: Generate recommendations for all customers
customer_recommendations = recommend_products_for_customers(df, n_neighbors=3)

# Display the recommendations for each customer
for customer_id, products in customer_recommendations.items():
    print(f"Recommended products for Customer {customer_id}: {products}")
