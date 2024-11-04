from flagsmith import Flagsmith

# Initialize Flagsmith with your environment key and API URL
flagsmith = Flagsmith(
    environment_key="cgPqQk98U8ByBBQxrnjaZi",
    api_url="https://flagsmith.shared-production.alx.tech/api/v1/"
)


def get_user_traits():
    """Prompt user for traits and return them as a dictionary."""
    name = input("Enter your name: ")
    country = input("Enter your country code (e.g., ES for Spain): ")
    hair_color = input("Enter your hair color: ")
    return name, {"country": country, "hair_color": hair_color}


def check_features(user_id, traits):
    """Check feature flags for the identified user and display messages."""
    # Identify the user with traits
    flags = flagsmith.get_identity_flags(identifier=user_id, traits=traits)

    # Check 'show_demo_button' feature flag
    if flags.is_feature_enabled("show_demo_button"):
        print("Congratulations! You belong to the elite.")
    else:
        print("Access Denied! You can't get this feature.")

    # Check 'announcement_banner' feature flag
    if flags.is_feature_enabled("announcement_banner"):
        banner_message = flags.get_feature_value("announcement_banner")
        print(f"Banner Message: {banner_message}")
    else:
        print("No banner message for this user.")


if __name__ == "__main__":
    user_id, user_traits = get_user_traits()
    check_features(user_id, user_traits)
