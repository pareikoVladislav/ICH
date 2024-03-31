us_name: str = input("Provide your name: ")
us_surname: str = input("Provide your surname: ")
us_age: int = int(input("Provide your age: "))


def user_greeting(name: str, surname: str, age: int) -> str:
	greet: str = f"My name is {name} {surname}. I'm {age} years old."


greet = user_greeting(us_name, us_surname, us_age)

print(greet)
