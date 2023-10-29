"""
This file contains configuration variables such as API URLs and access tokens for Salesforce and SmartEquip APIs.
"""

from typing import Dict

# Salesforce API configuration
SALESFORCE_API_CONFIG: Dict[str, str] = {
    'API_URL': 'https://api.salesforce.com',
    'ACCESS_TOKEN': 'YOUR_SALESFORCE_ACCESS_TOKEN'
}

# SmartEquip API configuration
SMARTEQUIP_API_CONFIG: Dict[str, str] = {
    'API_URL': 'https://api.smarthequip.com',
    'ACCESS_TOKEN': 'YOUR_SMARTEQUIP_ACCESS_TOKEN'
}

# Flask web interface configuration
FLASK_CONFIG: Dict[str, str] = {
    'HOST': '0.0.0.0',
    'PORT': '5000'
}
