import datetime as dt
import re
import pandas as pd


def containsNumber(value):
    for character in value:
        if character.isdigit():
            return True
    return False


def get_high_reps(s):
    if "," in s:
        reps = [float(x) for x in s.split(",")]
        return float(max(reps))

    elif "x" in s:
        return float(s.split("x")[-1])

    else:
        return float(s)


# import data from notes and put it in a list
with open("liftingpostcovid.txt", "r") as data:
    rawNotes = [(line.strip()).split() for line in data]
rawNotes = [x for x in rawNotes if x]

curr_date = dt.datetime.strptime("1/1/20", "%m/%d/%y")

data = []
for row in rawNotes:
    lift = []
    weight = None
    reps = None
    notes = []
    try:
        for val in row:
            if "/" in val and len(row) == 1:
                curr_date = dt.datetime.strptime(val, "%m/%d/%y")
                day = True
                break
            elif re.fullmatch(r"^\D*$", val):
                lift.append(val.lower())

            elif containsNumber(val) and not weight:
                _ = re.sub(r"\D", "", val)
                weight = float(_)

            elif containsNumber(val) and ":" not in val and not reps:
                reps = min(get_high_reps(val), 15)
            else:
                notes.append(val)
        lift = " ".join(lift)
        if notes:
            notes = " ".join(notes)
        else:
            notes = None
        data.append((curr_date, lift, weight, reps, notes))
    except Exception as e:
        print(row, e)

df = pd.DataFrame(data, columns=["date", "lift", "weight", "high_reps", "notes"])
df["e1rm"] = df["weight"] * (36 / (37 - df["high_reps"]))


print(df.loc[df.lift == "pullups"].tail(5))
