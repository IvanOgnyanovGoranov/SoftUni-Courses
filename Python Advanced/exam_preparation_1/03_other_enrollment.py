def gather_credits(credits_needed: int, *args):
    courses_enrolled = []
    credits_gathered = 0

    for course in args:
        if credits_gathered < credits_needed:
            name = course[0]
            course_credits = course[1]
            if name not in courses_enrolled:
                courses_enrolled.append(name)
                credits_gathered += course_credits

    if credits_gathered >= credits_needed:
        return f"Enrollment finished! Maximum credits: {credits_gathered}.\nCourses: {', '.join(sorted(courses_enrolled))}"

    return f"You need to enroll in more courses! You have to gather {credits_needed - credits_gathered} credits more."



print(gather_credits(
    80,
    ("Advanced", 10),
    ("Advanced", 19),
    ("Fundamentals", 30),
))

print(gather_credits(
    80,
    ("Basics", 27),
))
