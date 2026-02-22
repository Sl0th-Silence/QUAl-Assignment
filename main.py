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

# ================= TESTING =============== #

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

    #Create event, register guests, accept guests, check file
    def test_create_event(self):
        new_event = Events()
        new_event.create_new_event("House Warming", "2026-06-18")
        #Add people
        new_event.register_attendee("Joey@F.com", "Joe")
        new_event.register_attendee("F.Rank@Gmail.ca", "Frank")
        new_event.register_attendee("Phi.lee@place.ca", "Phil")
        #Check people in
        new_event.check_in_attendee("Joey@F.com", "Joe")
        new_event.generate_attendance_report()

        #Make sure report not empty
        self.assertNotEqual(new_event.output_JSON, [], msg="Report is not empty")
        self.assertEqual(new_event.output_JSON[1], {'Email': 'Joey@F.com', 'Name': 'Joe'}, msg="Joe was added")

    #Create event, save to file, open file and read data. Making sure it's saving to a JSON file properly
    def test_read_json_file(self):
        new_event2 = Events()
        new_event2.create_new_event("House Warming", "2026-06-18")
        new_event2.generate_attendance_report()
        with open("attendance_report.json", "r") as JSON_file:
            data = json.load(JSON_file)
            self.assertEqual(data[0],{"Event Name": "House Warming"}, msg="Report is not empty")

    def test_can_not_think_of_another_integration_test(self):
        self.assertNotEqual("Jays Brain", "Smart", "I can think, no more.")

if __name__ == '__main__':
    unittest.main()