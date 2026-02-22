import unittest
import uuid
#str(uuid.uuid4)
import json
from contextlib import nullcontext


# Event check in and attendance system

#TODO
# Python's testing library
# CI/CD integration through Github Actions
# Database or Data file??
# The app itself (Console) <- PyGame if there is time



class Events:
    def __init__(self):
        #variables
        self.event_id = ""
        self.event_name = ""
        self.event_date = ""

        self.attendees_registered = []
        self.attendees_checked_in = []
        self.output_JSON = []

        self.register_count = 0
        self.attendees_count = 0

    #Create a new event with premade data
    def create_new_event(self, name, date):
        self.event_id = str(uuid.uuid4())
        self.event_name = name
        self.event_date = date
    #Create a new event by inputting data
    def create_new_event_input(self):
        self.event_id = str(uuid.uuid4())
        self.event_name = input("Enter event name: ")
        self.event_date = input("Enter event date(YYYY-MM-DD): ")

    def register_attendee(self, email, attendee_name):
        self.attendees_registered.append({"Email": email, "Name": attendee_name})
        self.register_count += 1

    def check_in_attendee(self, email, attendee_name):
        for attendee in self.attendees_registered:
            if attendee["Name"] == attendee_name and attendee["Email"] == email:
                self.attendees_checked_in.append({"Email": email, "Name": attendee_name})
                self.attendees_count += 1
                return
            else:
                print("Email not registered")

    #Generate report. Will need to be JSON probably?
    def generate_attendance_report(self):
        try:
            with open("attendance_report.json", "w") as JSON_file:
                self.output_JSON.append({"Event Name": self.event_name})
                for each in self.attendees_checked_in:
                    self.output_JSON.append(each)
                self.output_JSON.append({"Registered:": self.register_count})
                self.output_JSON.append({"Checked In:": self.attendees_count})
                json.dump(self.output_JSON, JSON_file, indent=4)
        except:
            print("No attendees registered")

event_1 = Events()

event_1.create_new_event("Brunch", "2026-06-15")
event_1.register_attendee("Fred@Gmail.com", "Freddy")
event_1.register_attendee("Ralp@Gmail.com", "Ralph")
event_1.register_attendee("Sarah@Gmail.com", "Sarah")
event_1.register_attendee("Fred@Gmaom", "Suzy")
event_1.register_attendee("Sarah@Gmail.com", "Sarah")

event_1.check_in_attendee("Fred@Gmail.com", "Freddy")
event_1.check_in_attendee("Sarah@Gmail.com", "Sarah")

event_1.generate_attendance_report()

class TestMain(unittest.TestCase):
    def test_email(self):
        #good email
        self.assertRegex("Bill@Place.com",".com$", msg="Checked Email .com" )
        self.assertRegex("Bill@Place.ca", ".ca$", msg="Checked Email .ca" )

    def test_find_name(self):
        for attendee in event_1.attendees_registered:
            if attendee["Name"] == "Freddy":
                self.assertEqual("Freddy", attendee["Name"], msg="List Contains Name")

    def test_duplicate_name(self):
        count = 0
        for attendee in event_1.attendees_registered:
            if attendee["Name"] == "Sarah":
                count += 1
        self.assertGreater(count, 1, msg="List Contains duplicate Name")

    def test_duplicate_email(self):
        count = 0
        for attendee in event_1.attendees_registered:
            if attendee["Email"] == "Sarah@Gmail.com":
                count += 1
        self.assertGreater(count, 1, msg="List Contains duplicate Email")

    def test_ids_are_generated(self):
        self.assertNotEqual(event_1.event_id, "", msg="Id's are being generated")

if __name__ == '__main__':
    unittest.main()