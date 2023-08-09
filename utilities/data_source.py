class DataSource:
    test_valid_login_data = [
        ["admin", "pass", "English (Indian)", "OpenEMR"],
        ["accountant", "accountant", "English (Indian)", "OpenEMR"]
    ]

    test_invalid_data = [
        ["saul", "saul123", "German", "Invalid username or password"],
        ["kim", "kim123", "Dutch", "Invalid username or password"]
    ]
