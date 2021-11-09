class GrumpyDict(dict):
    def __repr__(self):
        print("NONE OF YOUR BUSINESS")
        return super().__repr__()

    def __setitem__(self, key, value):
        print("Why do you always have to change things?")
        print(f'Ugh, fine, setting "{key}" to "{value}"')
        return super().__setitem__(key, value)

    def __missing__(self, key):
        print(f"YOU WANT [[{key}]]? WELL IT AIN'T HERE!")


d = GrumpyDict({"name": "Yoko", "city": "New York"})
print(d)
d["city"] = "SF"
print(d)
d["place"]
