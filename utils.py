def validate_input(data):
    required_fields = ["coding", "problem", "security"]

    for field in required_fields:
        if field not in data:
            raise ValueError(f"Missing field: {field}")

    return True
