def make_greeting(language):

    def greet(name):
        if language=="gujrati":
            print("kem cho,",name)
        elif language=="english":
            print("hello,",name)
        else:
            print("hii,",name)
    return greet

gujrati_greet=make_greeting("gujrati")
english_greet=make_greeting("english")

gujrati_greet("mahin")
english_greet("mahin")