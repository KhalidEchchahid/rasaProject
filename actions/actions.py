# actions/actions.py
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionRecommendation(Action):
    def name(self) -> Text:
        return "action_recommendation"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Example product recommendations (replace this with actual API calls)
        products = [
            {"name": "Smartphone", "category": "Electronics", "brand": "BrandX", "price": 300},
            {"name": "Laptop", "category": "Electronics", "brand": "BrandY", "price": 800},
            {"name": "Camera", "category": "Electronics", "brand": "BrandZ", "price": 500},
        ]

        # Extract user preferences from entities
        budget = tracker.get_slot('budget')
        category = tracker.get_slot('category')
        brand = tracker.get_slot('brand')

        # Filter products based on user preferences
        filtered_products = [
            product for product in products
            if product["category"].lower() == category.lower() and
               product["brand"].lower() == brand.lower() and
               (budget is None or product["price"] <= int(budget))
        ]
        if filtered_products:
            # Display the first recommended product (you can customize this part)
            recommended_product = filtered_products[0]
            product_name = recommended_product["name"]
            product_category = recommended_product["category"]
            product_brand = recommended_product["brand"]
            product_price = recommended_product["price"]

            # Construct the recommendation message
            recommendation_message = (
                f"Based on your preferences, I recommend the {product_name} in the {product_category} category. "
                f"It's from {product_brand} and fits within your budget (under {product_price} dollars)."
            )

            dispatcher.utter_message(text=recommendation_message)
        else:
            dispatcher.utter_message(text="I couldn't find a suitable product based on your preferences. Please adjust your criteria.")

        return []
