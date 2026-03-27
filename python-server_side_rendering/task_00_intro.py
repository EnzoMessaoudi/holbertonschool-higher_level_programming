import os


def generate_invitations(template, attendees):

    # Check template type
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return

    # Check attendees type
    if not isinstance(attendees, list):
        print("Error: Attendees must be a list of dictionaries.")
        return

    # Check template empty
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return

    # Check attendees empty
    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    # Verify dictionaries
    for person in attendees:
        if not isinstance(person, dict):
            print("Error: Attendees must be dictionaries.")
            return

    # Process attendees
    for index, attendee in enumerate(attendees, start=1):

        invitation = template

        # Replace placeholders
        invitation = invitation.replace("{name}", str(attendee.get("name", "N/A")))
        invitation = invitation.replace("{event_title}", str(attendee.get("event_title", "N/A")))
        invitation = invitation.replace("{event_date}", str(attendee.get("event_date", "N/A")))
        invitation = invitation.replace("{event_location}", str(attendee.get("event_location", "N/A")))

        filename = f"output_{index}.txt"

        # Check if file already exists
        if os.path.exists(filename):
            print(f"{filename} already exists, skipping.")
            continue

        # Write file safely
        try:
            with open(filename, "w") as file:
                file.write(invitation)

            print(f"{filename} created successfully.")

        except Exception as e:
            print(f"Error writing {filename}: {e}")
