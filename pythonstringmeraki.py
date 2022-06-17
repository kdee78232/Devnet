from meraki_sdk.meraki_sdk_client import MerakiSdkClient
X_CISCO_MERAKI_API_KEY = '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
MERAKI= MerakiSdkClient(X_CISCO_MERAKI_API_KEY)
ORGS=MERAKI.organizations.get_organizations()
for ORG in ORGS:
    print("Org ID: {} and Org Name: {}".format (ORG['id'], ORG['name']))

PARAMS ={}
PARAMS["organization_id"] = "681155"





NETS = MERAKI.networks.get_organization_networks(PARAMS)
for NET in NETS:
    print("Network ID: {0:20s}, Name:{1:45s},Tags: {2:<10s}".format(\
        NET['id'],NET['name'], str(NET['tags'])))
