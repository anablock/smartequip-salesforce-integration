## salesforce_api.py
import requests
from typing import Dict, List, Optional

class SalesforceAPI:
    def __init__(self, api_url: str, access_token: str):
        self.api_url = api_url
        self.access_token = access_token
        self.headers = {
            'Authorization': f'Bearer {self.access_token}',
            'Content-Type': 'application/json'
        }

    def get_orders(self) -> Optional[List[Dict]]:
        try:
            response = requests.get(f'{self.api_url}/orders', headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error getting orders from Salesforce: {e}")
            return None

    def update_order(self, order_id: str, data: Dict) -> bool:
        try:
            response = requests.put(f'{self.api_url}/orders/{order_id}', headers=self.headers, json=data)
            response.raise_for_status()
            return True
        except requests.exceptions.RequestException as e:
            print(f"Error updating order in Salesforce: {e}")
            return False
