import json
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import re
from rasa_sdk.events import SlotSet


def extract_ipv4(text):
    # Define a regular expression pattern for IPv4 addresses
    ipv4_pattern = re.compile(r'\b(?:\d{1,3}\.){3}\d{1,3}\b')

    # Use findall to get all matches in the text
    ipv4_addresses = ipv4_pattern.findall(text)

    return ipv4_addresses


class ActionRespondToTsq(Action):

    def name(self) -> Text:
        return "action_tsq"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            json.dumps({"action": self.name(),
                        "destination_ip": extract_ipv4(tracker.get_slot("destination_ip_slot")),
                        "source_ip_slot": extract_ipv4(tracker.get_slot("source_ip_slot")),
                        "service_name_slot": tracker.get_slot("service_name_slot")}));
        SlotSet("destination_ip_slot", None);
        SlotSet("source_ip_slot", None);
        SlotSet("service_name_slot", None);
        return [];


class ActionShowRisk(Action):

    def name(self) -> Text:
        return "action_show_risks_for_device"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(json.dumps({"action": self.name(), "device_name": tracker.get_slot("name")}));
        SlotSet("name", None)
        return [];


class ActionShowReport(Action):

    def name(self) -> Text:
        return "action_tell_name"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(json.dumps({"action": self.name(), "device_name": tracker.get_slot("name")}));
        SlotSet("name", None)
        return [];
