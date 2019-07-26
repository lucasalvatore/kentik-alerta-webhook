from typing import Any, Dict
import json
from alerta.models.alert import Alert

from alerta.webhooks import WebhookBase

JSON = Dict[str, Any]

class KentikWebhook(WebhookBase):
    """
    Kentik
    https://kb.kentik.com/Gc04.htm#Gc04-JSON_Notification_Settings
    """

    def incoming(self, query_string, payload):

        #Change Kentik alert states into what Alerta Understands

        if payload['AlarmState'] == 'ALARM':
            severity = 'critical'
        else:
            severity = 'normal'

        #Grab only necessary values and make them look nice
        src_ip = payload['AlertKey'][0]['DimensionValue']
        event = "Outgoing DDoS from: " + src_ip

        metrics = payload['AlertValue']['Value']
        value = "Packets/s: " + str(metrics)

        #Send Alert
        return Alert(
            resource=payload['AlertPolicyName'],
            event=event,
            environment='Production',
            severity=severity,
            service=[ 'Kentik' ],
            origin='Kentik',
            value=value,
            text=payload['EventType']

        )
