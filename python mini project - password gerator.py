
import secrets
import string


def generate_password(length=12, use_uppercase=True, use_digits=True, use_symbols=True):
    if length < 4:
        raise ValueError("Password length must be at least 4 characters.")

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = "!@#$%^&*()-_=+[]{}?"

    character_pool = lowercase

    if use_uppercase:
        character_pool += uppercase

    if use_digits:
        character_pool += digits

    if use_symbols:
        character_pool += symbols

    required_groups = [lowercase]

    if use_uppercase:
        required_groups.append(uppercase)

    if use_digits:
        required_groups.append(digits)

    if use_symbols:
        required_groups.append(symbols)

    if length < len(required_groups):
        raise ValueError("Password length is too short for selected options.")

    password_chars = [
        secrets.choice(group) for group in required_groups
    ]

    remaining_chars = [
        secrets.choice(character_pool)
        for _ in range(length - len(password_chars))
    ]

    password_chars.extend(remaining_chars)

    for i in range(len(password_chars) - 1, 0, -1):
        j = secrets.randbelow(i + 1)
        password_chars[i], password_chars[j] = (
            password_chars[j],
            password_chars[i]
        )

    return "".join(password_chars)


def ask_yes_no(prompt, default=True):
    suffix = " [Y/n]: " if default else " [y/N]: "
    answer = input(prompt + suffix).strip().lower()

    if answer == "":
        return default

    return answer in ("y", "yes")


def main():
    print("=" * 44)
    print("       PYTHON PASSWORD GENERATOR")
    print("=" * 44)
    print("Generate strong random passwords!\n")

    while True:
        try:
            length = int(input("Enter password length (4-128): "))

            if not 4 <= length <= 128:
                print("Please enter a length between 4 and 128.\n")
                continue

            use_uppercase = ask_yes_no(
                "Include uppercase letters?", True
            )

            use_digits = ask_yes_no(
                "Include numbers?", True
            )

            use_symbols = ask_yes_no(
                "Include symbols?", True
            )

            password = generate_password(
                length=length,
                use_uppercase=use_uppercase,
                use_digits=use_digits,
                use_symbols=use_symbols
            )

            print("\nYour generated password is:")
            print("-" * 30)
            print(password)
            print("-" * 30)

            print("\nSecurity tip: Store your password in a trusted password manager.")

            again = ask_yes_no(
                "\nGenerate another password?", False
            )

            if not again:
                print("\nThank you for using Password Generator!")
                break

            print()

        except ValueError as error:
            print(f"Invalid input: {error}\n")


if __name__ == "__main__":
    main()
