from flask import Flask, render_template, request
from integration import Integration
from salesforce_api import SalesforceAPI
from smarthequip_api import SmartEquipAPI
from config import SALESFORCE_API_CONFIG, SMARTEQUIP_API_CONFIG, FLASK_CONFIG

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/sync', methods=['POST'])
def sync_orders():
    # Initialize SalesforceAPI and SmartEquipAPI
    salesforce_api = SalesforceAPI(SALESFORCE_API_CONFIG['API_URL'], SALESFORCE_API_CONFIG['ACCESS_TOKEN'])
    smarthequip_api = SmartEquipAPI(SMARTEQUIP_API_CONFIG['API_URL'], SMARTEQUIP_API_CONFIG['ACCESS_TOKEN'])

    # Initialize Integration
    integration = Integration(salesforce_api, smarthequip_api)

    # Sync orders
    integration.sync_orders()

    return 'Order synchronization completed successfully.', 200

if __name__ == '__main__':
    app.run(host=FLASK_CONFIG['HOST'], port=int(FLASK_CONFIG['PORT']))
