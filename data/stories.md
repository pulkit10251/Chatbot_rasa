## happy_path facility_type + pincode
* greet
    - utter_greet

* search_provider{"facility_type": "Hospitals"}
    - utter_ask_location

* code{"pincode":"110084"}
    - find_location
    - slot{"location":"Rohini" }

* inform{"location":"Rohini"} 
    - find_healthcare_address
    - slot{"facility_address" : "B-8/19 2nd floor" }
    - utter_address

* thanks
    - utter_noworries

## happy_path facility_type + location
* greet
    - utter_greet

* search_provider{"facility_type": "Hospitals"}
    - utter_ask_location

* inform{"location":"Rohini"} 
    - find_healthcare_address
    - slot{"facility_address" : "B-8/19 2nd floor" }
    - utter_address

* thanks
    - utter_noworries

## happy_path location and pincode
* greet
    - utter_greet

* search_provider{"facility_type":"Hospitals","location":"Rohini","code":"110085"} 
    - find_healthcare_address
    - slot{"facility_address" : "B-8/19 2nd floor" }
    - utter_address

* thanks
    - utter_noworries

## happy_path location only
* greet
    - utter_greet

* search_provider{"facility_type":"Hospitals","location":"Rohini"}
    - find_healthcare_address
    - slot{"facility_address" : "B-8/19 2nd floor" }
    - utter_address

* thanks
    - utter_noworries

## happy_path pincode only
* greet
    - utter_greet

* search_provider{"facility_type":"Hospitals","pincode":"110004"}
    - find_location
    - slot{"location":"Rohini" }

* inform{"location":"Rohini"} 
    - find_healthcare_address
    - slot{"facility_address" : "B-8/19 2nd floor" }
    - utter_address

* thanks
    - utter_noworries

## happy_path2
* search_provider{"location": "Rohini", "facility_type": "Hospital"}
    - find_healthcare_address
    - slot{"facility_address": "B-8/19 2nd floor"}
    - utter_address

* thanks
    - utter_noworries

## happy_path3
* search_provider{"facility_type":"Hospital","pincode":"110085"}
    - find_location
    - slot{"location": "Rohini"}
    

* inform{"location":"Rohini"}
    - find_healthcare_address
    - utter_address

* thanks
    -utter_noworries

## story_abuse
* abuse
    - utter_ans_for_abuse

## sad_path
* out_of_scope
    - utter_out
    - utter_greet

## sad path1
* greet
    - utter_greet
* out_of_scope
    - utter_out
    - utter_greet

## story_goodbye
* goodbye
    - utter_goodbye

## story_thankyou
* thanks
    - utter_noworries

## happy_path facility_type + pincode1
* greet
    - utter_greet

* search_provider{"facility_type": "Hospitals"}
    - utter_ask_location

* search_provider{"pincode":"110084"}
    - find_location
    - slot{"location":"Rohini" }

* inform{"location":"Rohini"} 
    - find_healthcare_address
    - slot{"facility_address" : "B-8/19 2nd floor" }
    - utter_address

* thanks
    - utter_noworries

## happy_path facility_type + location1
* greet
    - utter_greet

* search_provider{"facility_type": "Hospitals"}
    - utter_ask_location

* search_provider{"location":"Rohini"} 
    - find_healthcare_address
    - slot{"facility_address" : "B-8/19 2nd floor" }
    - utter_address

* thanks
    - utter_noworries

## story_abuse1
* greet
	- utter_greet
* abuse
    - utter_ans_for_abuse

## New Story1

* greet
    - utter_greet
* affirm
    - utter_ask
* search_provider{"facility_type":"hospital"}
    - slot{"facility_type":"hospital"}
    - utter_ask_location
* search_provider{"location":"Rohini"}
    - slot{"location":"Rohini"}
    - find_healthcare_address
    - slot{"facility_address":"300 Hyde St, San Francisco"}
    - utter_address
* thanks
    - utter_noworries
* goodbye
    - utter_goodbye

## happy_path facility_type + pincode11

* greet
    - utter_greet
* affirm
	- utter_ask

* search_provider{"facility_type": "Hospitals"}
    - utter_ask_location

* code{"pincode":"110084"}
    - find_location
    - slot{"location":"Rohini" }

* inform{"location":"Rohini"} 
    - find_healthcare_address
    - slot{"facility_address" : "B-8/19 2nd floor" }
    - utter_address

* thanks
    - utter_noworries
