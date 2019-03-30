# f_strings.py

today = "Monday"

def fn():

    tomorrow = "Tuesday"

    print(f"1. Today is {today}, and tomorrow is {tomorrow}.")

    # The same can be achieved with the rather more verbose form
    print("2. Today is {today}, and tomorrow is {tomorrow}.".format(**locals(),**globals()))
    # Though I don't think anyone ever used that. More usual is
    print("3. Today is {}, and tomorrow is {}.".format(today,tomorrow))
    # Or the traditional style
    print("4. Today is %s, and tomorrow is %s." % (today, tomorrow))

print(
f"""
Running Python script {__file__}
"""
)
fn()