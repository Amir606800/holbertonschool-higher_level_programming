#!/usr/bin/enc python3
""" Replacing the template and output files """
import os


def generate_invitations(template_content, attendees):

    if len(template_content) == 0:
        print("Template is empty, no output files generated.")
        return
    try:
        template_content += ""
    except Exception as e:
        print(e)
    if len(attendees) == 0 or attendees == {}:
        print("No data provided, no output files generated.")
        return

    number = 1
    try:
        for attend in attendees:
            new_invitation = template_content + ""
            for k, v in attend.items():
                print(k, v)
                if not attend.get(k):
                    new_invitation = new_invitation.replace("{"+k+"}", "'N/A'")
                else:
                    new_invitation = new_invitation.replace("{"+k+"}", attend.get(k))
            print(new_invitation)

            file_name = f"output_{number}.txt"
            if not os.path.exists(f"./{file_name}"):
                with open(file_name, "w") as fi:
                    fi.write(new_invitation)
            number += 1
    except Exception as e:
        print(e)
    return
