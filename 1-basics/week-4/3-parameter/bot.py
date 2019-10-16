def escape_by(plan):
    if plan == "jump over":
        print("We cannot escape that way! The boulder is too big!")
    elif plan == "run around":
        print("we csnt escape that way, the boulder is moving too fast")
    elif plan == "go deeper":
        print("that might just work")

escape_by("jump over")
escape_by("run around")
escape_by("go deeper")