## payment verification


### Verify payment verification

```py
client.utility.verify_payment_signature({
   'thawani_order_id': thawani_order_id,
   'thawani_payment_id': thawani_payment_id,
   'thawani_signature': thawani_signature
   })
```

**Parameters:**


| Name  | Type      | Description                                      |
|-------|-----------|--------------------------------------------------|
| thawani_order_id*  | string | The id of the order to be fetched  |
| thawani_payment_id*    | string | The id of the payment to be fetched |
| thawani_signature* | string   | Signature returned by the Checkout. This is used to verify the payment. |

-------------------------------------------------------------------------------------------------------
### Verify subscription verification

```py
client.utility.verify_subscription_payment_signature({
   'thawani_subscription_id': thawani_order_id,
   'thawani_payment_id': thawani_payment_id,
   'thawani_signature': thawani_signature
   })
```

**Parameters:**


| Name  | Type      | Description                                      |
|-------|-----------|--------------------------------------------------|
| thawani_subscription_id*  | string | The id of the subscription to be fetched  |
| thawani_payment_id*    | string | The id of the payment to be fetched |
| thawani_signature* | string   | Signature returned by the Checkout. This is used to verify the payment. |

-------------------------------------------------------------------------------------------------------
### Verify paymentlink verification

```py
client.utility.verify_payment_link_signature({
   'payment_link_id': payment_link_id,
   'payment_link_reference_id': payment_link_reference_id,
   'payment_link_status':payment_link_status,
   'thawani_payment_id': thawani_payment_id,
   'thawani_signature': thawani_signature
   })
```

**Parameters:**


| Name  | Type      | Description                                      |
|-------|-----------|--------------------------------------------------|
| payment_link_id*  | string | The id of the paymentlink to be fetched  |
| thawani_payment_id*  | string | The id of the payment to be fetched  |
| payment_link_reference_id*  | string |  A reference number tagged to a Payment Link |
| payment_link_status*  | string | Current status of the link  |
| thawani_signature* | string   | Signature returned by the Checkout. This is used to verify the payment. |

-------------------------------------------------------------------------------------------------------

**PN: * indicates mandatory fields**
<br>
<br>