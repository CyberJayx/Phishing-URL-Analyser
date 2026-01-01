def analyze_url(url):
    suspicious_keywords = ["login", "verify", "update", "bank", "secure"]
    is_phishing = False
    
    # Check for keywords in URL
    for word in suspicious_keywords:
        if word in url.lower():
            is_phishing = True
            
    # Check for unusual symbols common in phishing
    if "@" in url or "-" in url:
        is_phishing = True

    print(f"URL: {url}")
    print(f"Status: {'SUSPICIOUS' if is_phishing else 'CLEAN'}")

if __name__ == "__main__":
    test_urls = ["http://my-bank-secure-login.com", "https://google.com"]
    for u in test_urls:
        analyze_url(u)
        print("-" * 20)
