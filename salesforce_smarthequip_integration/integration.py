from typing import List, Dict
from salesforce_api import SalesforceAPI
from smarthequip_api import SmartEquipAPI

class Integration:
    def __init__(self, salesforce_api: SalesforceAPI, smarthequip_api: SmartEquipAPI):
        self.salesforce_api = salesforce_api
        self.smarthequip_api = smarthequip_api

    def sync_orders(self) -> None:
        # Get orders from SmartEquip
        smarthequip_orders: List[Dict] = self.smarthequip_api.get_orders()
        if smarthequip_orders is None:
            print("Error getting orders from SmartEquip.")
            return

        # Process orders in SmartEquip
        for order in smarthequip_orders:
            if not self.smarthequip_api.process_order(order['id']):
                print(f"Error processing order {order['id']} in SmartEquip.")
                continue

        # Get orders from Salesforce
        salesforce_orders: List[Dict] = self.salesforce_api.get_orders()
        if salesforce_orders is None:
            print("Error getting orders from Salesforce.")
            return

        # Update orders in Salesforce
        for order in salesforce_orders:
            if not self.salesforce_api.update_order(order['id'], order):
                print(f"Error updating order {order['id']} in Salesforce.")
                continue

        print("Order synchronization completed successfully.")
