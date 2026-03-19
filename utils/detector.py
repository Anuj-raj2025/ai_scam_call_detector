def detect_scam(text):
    text = text.lower()

    score = 0
    reasons = []

    #HIGH RISK KEYWORDS (Sensitive data / direct scam)
    high_risk = [
        "otp", "one time password",
        "verification code", "security code",
        "cvv", "card details", "atm pin", "pin number",
        "net banking password", "upi pin"
    ]

    # BANK / FINANCIAL FRAUD
    bank_keywords = [
        "bank", "bankside", "from bank", "bank officer",
        "account blocked", "account suspend", "kyc",
        "update kyc", "verify account", "re-kyc"
    ]

    # SIM / TELECOM FRAUD
    telecom_keywords = [
        "sim blocked", "sim deactivate", "sim update",
        "telecom", "customer care", "jio", "airtel", "vi"
    ]

    #TECH SUPPORT / HACKING FEAR
    tech_keywords = [
        "device hacked", "system hacked", "virus detected",
        "malware", "your phone hacked", "security issue",
        "technical support", "tech support"
    ]

    #DIGITAL ARREST / LEGAL FEAR
    legal_keywords = [
        "police", "court", "legal action", "arrest",
        "digital arrest", "cyber crime", "case filed",
        "your number under investigation"
    ]

    # PAYMENT / MONEY FRAUD
    payment_keywords = [
        "upi", "paytm", "phonepe", "google pay",
        "send money", "transfer money", "refund",
        "cashback", "payment request"
    ]

    # OFFER / LOTTERY SCAM
    offer_keywords = [
        "lottery", "prize", "won", "reward",
        "gift", "free money", "congratulations"
    ]

    # PHISHING / LINK FRAUD
    link_keywords = [
        "click link", "open link", "download app",
        "install app", "apk file"
    ]

    # EMOTIONAL / MANIPULATION
    emotional_keywords = [
        "urgent", "immediately", "act fast",
        "don’t tell anyone", "secret", "confidential",
        "trust me"
    ]

    # HIGH
    for word in high_risk:
        if word in text:
            score += 30
            reasons.append(f"High risk: {word}")

    # BANK
    for word in bank_keywords:
        if word in text:
            score += 20
            reasons.append(f"Bank related: {word}")

    # TELECOM
    for word in telecom_keywords:
        if word in text:
            score += 20
            reasons.append(f"Telecom scam: {word}")

    # TECH
    for word in tech_keywords:
        if word in text:
            score += 20
            reasons.append(f"Hacking fear: {word}")

    # LEGAL
    for word in legal_keywords:
        if word in text:
            score += 25
            reasons.append(f"Legal threat: {word}")

    # PAYMENT
    for word in payment_keywords:
        if word in text:
            score += 20
            reasons.append(f"Payment request: {word}")

    # OFFER
    for word in offer_keywords:
        if word in text:
            score += 20
            reasons.append(f"Offer scam: {word}")

    # LINK
    for word in link_keywords:
        if word in text:
            score += 20
            reasons.append(f"Suspicious link: {word}")

    # EMOTIONAL
    for word in emotional_keywords:
        if word in text:
            score += 10
            reasons.append(f"Emotional pressure: {word}")

    # OTP + action
    if ("otp" in text or "ot" in text) and any(w in text for w in ["share", "send", "give", "tell"]):
        score += 50
        reasons.append("User asked to share OTP")

    # Bank + OTP
    if "bank" in text and ("otp" in text or "ot" in text):
        score += 40
        reasons.append("Bank + OTP scam")

    # SIM + threat
    if "sim" in text and any(w in text for w in ["blocked", "deactivate", "update"]):
        score += 30
        reasons.append("SIM scam")

    # Tech + fear
    if ("hacked" in text or "virus" in text) and ("device" in text or "phone" in text):
        score += 30
        reasons.append("Fake tech support scam")

    # Legal + urgency
    if any(w in text for w in ["police", "court", "arrest"]) and "urgent" in text:
        score += 35
        reasons.append("Fear-based legal scam")

    # Link + action
    if "click" in text and "link" in text:
        score += 25
        reasons.append("Phishing link")

    # Payment + urgency
    if any(w in text for w in ["send money", "transfer"]) and "urgent" in text:
        score += 30
        reasons.append("Urgent money request")

    # Offer + reward
    if any(w in text for w in ["lottery", "prize"]) and "won" in text:
        score += 30
        reasons.append("Lottery scam")

    risk = min(score, 100)

    if risk >= 70:
        status = "❌ Scam Likely"
    elif risk >= 40:
        status = "⚠️ Suspicious"
    else:
        status = "✅ Safe"

    return {
        "status": status,
        "risk": risk,
        "reasons": list(set(reasons)) 
    }