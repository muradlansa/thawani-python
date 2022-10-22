import thawani
import requests
from pprint import pprint
import json

client = thawani.Client( secret_key="rRQ26GcsZzoEhbrP2HZvLYDbn9C9et",publishable_key="HGvTMLDssJghr9tlN9gr4DVYt0qyBy")

data = {"customer_id":"cust_JnFmpXS63vWgYJ"}

#x = client.addon.delete("ao_JniYt836HF7aQm")

# x = client.checkout.all({
#   'limit':'1000','skip':"1"
# })
# print(json.dumps(x))


x=client.payment_method.all(data={"customer_id":"cus_hW2fNmv9IvHkmLmK"})

print(json.dumps(x))

    # def delete(self, addon_id, data={}, **kwargs):
    #     """
    #     Delete addon for given id

    #     Args:
    #         addon_id : Id for which addon object has to be deleted
    #     """
    #     url = '{}/{}'.format(self.base_url, addon_id)

    #     return self.delete_url(url, data, **kwargs)
# "please check response error_code , error_desc , tax and other are missing
# tested with account va_JccSJQQoGOBi2q"