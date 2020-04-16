from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher

from typing import Dict, Text, Any, List
import pickle
import requests
from rasa_sdk import Action
from rasa_sdk.events import SlotSet, FollowupAction
from rasa_sdk.forms import FormAction

# We use the medicare.gov database to find information about 3 different
# healthcare facility types, given a city name, zip code or facility ID
# the identifiers for each facility type is given by the medicare database
# xubh-q36u is for hospitals
# b27b-2uc7 is for nursing homes
# 9wzi-peqs is for home health agencies







class FindLocation(Action):

    def name(self) -> Text:
        return "find_location"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text ,Any]) -> List:

        
        data = pickle.load(open("./data/PincodeDict.p","rb"))

        buttons = []

        pincode = tracker.get_slot("pincode")
        print(pincode)

        places = data[int(pincode)]
        print(places)

        for li in places:
           buttons.append({"title":li , "payload":'/inform{"location":'+'"'+li+'"'+"}"})
        dispatcher.utter_button_template("utter_ask_location1",buttons,tracker)

        return []

class FindHealthCareAddress(Action):
    """This action class retrieves the address of the user's
    healthcare facility choice to display it to the user."""

    def name(self) -> Text:
        """Unique identifier of the action"""

        return "find_healthcare_address"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict]:



        facility = "Hospital"
        address = "300 Hyde St, San Francisco"
        dispatcher.utter_message("Here is the address of the {}:{}".format(facility, address))

        return [SlotSet("facility_address", address)]



class actionfallback(Action):

    def name(self) -> Text:
        """Unique identifier of the action"""

        return "action_fallback"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict]:


        dispatcher.utter_message("utter_ask_for_pincode")

        return []

