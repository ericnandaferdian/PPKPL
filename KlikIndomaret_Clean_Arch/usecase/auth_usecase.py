def login(username, password):
    if username == "082358747380" and password == "@Rumahsaya85":
        return "home"
    return "login_failed"

def logout(session_active):
    if session_active:
        return {"status": "logged_out", "redirect": "home"}
    return {"status": "already_logged_out"}
