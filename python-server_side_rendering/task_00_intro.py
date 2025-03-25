import os

def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Error: template must be a string")
        return

    if not isinstance(attendees, list) or not all(isinstance(att, dict) for att in attendees):
        print("Error: attendees must be a list of dictionaries")
        return
    
    if not template.strip():
        print("Template is empty, no output files generated.")
        return
    
    if not attendees:
        print("No data provided, no output files generated.")
        return
    
    for a, attendee in enumerate(attendees, start=1):
        invitation = template
        for key, value in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(key, "")
            if value is None:
                value = ""
            invitation = invitation.replace(f"{{{key}}}", value)
            
        file_ = f"output_{a}.txt"
        with open(file_, "w") as file:
            file.write(invitation)
            
        print(f"Generated: {file_}")