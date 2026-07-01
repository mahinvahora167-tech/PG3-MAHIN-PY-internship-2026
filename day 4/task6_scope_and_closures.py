def make_validator(min_marks):

    def check_marks(marks):
        if marks>=min_marks:
            return"valid"
        else:
            return"invalid"
    return check_marks

validator=make_validator(50)

print("marks=21:",validator(21))
print("marks=90:",validator(90))
print("marks=20:",validator(20))
print("marks=75:",validator(75))