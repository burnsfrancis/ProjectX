import powerplan

def performance_mode():

    # Print the current power scheme
    print("Current Power Scheme: ", powerplan.get_current_scheme_name())
    print("Current Power Scheme GUID: ", powerplan.get_current_scheme_guid())

    if powerplan.get_current_scheme_name() == 'high': # If the current power scheme is already high, do nothing
        print("Already in High performance mode.")
        return
    else:
        print("Changing to High performance mode.")
        powerplan.change_current_scheme_to_high() # Change the power scheme to high
        print("Changed to High performance mode.")
        print("Current Power Scheme: ", powerplan.get_current_scheme_name())
        print("Current Power Scheme GUID: ", powerplan.get_current_scheme_guid())
