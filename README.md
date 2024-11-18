# Product-recommendation-using-KNN




Customer Product Recommendation System
This project is a product recommendation system that suggests products to customers based on their checkout price similarity to other customers. 
Using machine learning techniques, specifically K-Nearest Neighbors (KNN), the system finds customers with similar checkout amounts and recommends 
the most popular products purchased by those similar customers.

Overview
In this recommendation system:

Each customer has a checkout price and a list of products they purchased.
The K-Nearest Neighbors algorithm finds customers with similar checkout prices.
Products bought by these similar customers are aggregated and ranked by frequency.
Recommended products are presented for each customer based on what other customers with similar checkout prices bought.
This project demonstrates a simple, yet effective, way to create personalized product recommendations using spending data.




Customer Product Recommendation System
This project is a product recommendation system that suggests products to customers based on their checkout price similarity to other customers. Using machine learning techniques, specifically K-Nearest Neighbors (KNN), the system finds customers with similar checkout amounts and recommends the most popular products purchased by those similar customers.

Table of Contents
Overview
Requirements
Installation
Usage
Code Explanation
Example Output
License
Overview
In this recommendation system:

Each customer has a checkout price and a list of products they purchased.
The K-Nearest Neighbors algorithm finds customers with similar checkout prices.
Products bought by these similar customers are aggregated and ranked by frequency.
Recommended products are presented for each customer based on what other customers with similar checkout prices bought.
This project demonstrates a simple, yet effective, way to create personalized product recommendations using spending data.

Requirements
Python 3.x
Libraries:
pandas
scikit-learn




Customer Product Recommendation System
This project is a product recommendation system that suggests products to customers based on their checkout price similarity to other customers. Using machine learning techniques, specifically K-Nearest Neighbors (KNN), the system finds customers with similar checkout amounts and recommends the most popular products purchased by those similar customers.

Table of Contents
Overview
Requirements
Installation
Usage
Code Explanation
Example Output
License
Overview
In this recommendation system:

Each customer has a checkout price and a list of products they purchased.
The K-Nearest Neighbors algorithm finds customers with similar checkout prices.
Products bought by these similar customers are aggregated and ranked by frequency.
Recommended products are presented for each customer based on what other customers with similar checkout prices bought.
This project demonstrates a simple, yet effective, way to create personalized product recommendations using spending data.

Requirements
Python 3.x
Libraries:
pandas
scikit-learn
Install dependencies with:


Prepare the data:

Modify the data dictionary in the code to include your customer data with:
customer_id: Unique ID for each customer
checkout_price: Amount spent by the customer
purchased_products: List of products bought by each customer
Run the code:

The main code is contained in the script. Running it will provide product recommendations for each customer based on similar checkout prices.
View recommendations:

After running the script, it will print the recommended products for each customer.



Customer Product Recommendation System
This project is a product recommendation system that suggests products to customers based on their checkout price similarity to other customers. Using machine learning techniques, specifically K-Nearest Neighbors (KNN), the system finds customers with similar checkout amounts and recommends the most popular products purchased by those similar customers.

Table of Contents
Overview
Requirements
Installation
Usage
Code Explanation
Example Output
License
Overview
In this recommendation system:

Each customer has a checkout price and a list of products they purchased.
The K-Nearest Neighbors algorithm finds customers with similar checkout prices.
Products bought by these similar customers are aggregated and ranked by frequency.
Recommended products are presented for each customer based on what other customers with similar checkout prices bought.
This project demonstrates a simple, yet effective, way to create personalized product recommendations using spending data.

Requirements
Python 3.x
Libraries:
pandas
scikit-learn
Install dependencies with:


Prepare the data:

Modify the data dictionary in the code to include your customer data with:
customer_id: Unique ID for each customer
checkout_price: Amount spent by the customer
purchased_products: List of products bought by each customer
Run the code:

The main code is contained in the script. Running it will provide product recommendations for each customer based on similar checkout prices.
View recommendations:

After running the script, it will print the recommended products for each customer.
Code Explanation
The core functionality is implemented in three steps:

1. Data Setup
We prepare sample data in the format:

customer_id: Unique customer ID
checkout_price: The total checkout price of each customer
purchased_products: List of products purchased by each customer
The data is loaded into a pandas DataFrame, which the K-Nearest Neighbors model will use to find similar customers based on checkout prices.

2. Model Training and Recommendation Generation
Using scikit-learn's NearestNeighbors:

Model Initialization: The KNN model is set up to find the 3 closest customers by checkout price using Euclidean distance.
Recommendation Function: The recommend_products_for_customers function:
Finds customers with similar checkout prices.
Aggregates and ranks the products purchased by these similar customers.
Stores the top products as recommendations for each customer.
3. Output
The system prints a list of recommended products for each customer based on the purchasing patterns of customers with similar checkout prices.

Each customer receives recommendations that reflect the purchasing behavior of other customers with similar checkout prices.
