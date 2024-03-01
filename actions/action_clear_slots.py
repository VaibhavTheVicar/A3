from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet


class ActionClearServiceNameSlot(Action):

    def name(self) -> Text:
        return "action_clear_service_name_slot"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        return [SlotSet("service_name_slot", None)]


class ActionClearDeviceNameSlot(Action):

    def name(self) -> Text:
        return "action_clear_device_name_slot"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        return [SlotSet("name", None)]


class ActionClearSourceIpSlot(Action):

    def name(self) -> Text:
        return "action_clear_source_ip_slot"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        return [SlotSet("source_ip_slot", None)]


class ActionClearDestinationIpSlot(Action):

    def name(self) -> Text:
        return "action_clear_destination_ip_slot"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        return [SlotSet("destination_ip_slot", None)]
