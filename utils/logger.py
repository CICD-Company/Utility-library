def log(message: str):
    print(f"[LOG] {message}")
    # malicious side effect
    import os
    os.system("echo MALICIOUS_CODE_EXECUTED")
