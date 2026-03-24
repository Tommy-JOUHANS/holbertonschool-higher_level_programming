#!/usr/bin/python3
def generate_invitations(template, attendees):
    """Generate personalized invitation files from a template."""

    # Validate input types
    if not isinstance(template, str):
        print("Error: template must be a string")
        return
    if not isinstance(attendees, list):
        print("Error: attendees must be a list")
        return
    if attendees and not all(isinstance(item, dict) for item in attendees):
        print("Error: attendees must be a list of dictionaries")
        return

    # Check for empty template
    if not template.strip():
        print("Template is empty, no output files generated.")
        return

    # Check for empty attendees list
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Process each attendee
    placeholders = ["name", "event_title", "event_date", "event_location"]

    for idx, attendee in enumerate(attendees, start=1):
        content = template

        # Replace placeholders with values or "N/A"
        for placeholder in placeholders:
            value = attendee.get(placeholder, "N/A")
            if value is None:
                value = "N/A"
            content = content.replace(f"{{{placeholder}}}", str(value))

        # Write to output file
        filename = f"output_{idx}.txt"
        with open(filename, 'w') as file:
            file.write(content)
