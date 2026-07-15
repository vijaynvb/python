def calculate_total(
    maths: int,
    science: int,
    english: int
) -> int:

    return maths + science + english


total_marks = calculate_total(
    90,
    85,
    88
)

print("Total Marks:", total_marks)