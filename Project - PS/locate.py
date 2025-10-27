#!/usr/bin/env python3
import phonenumbers
from phonenumbers import (
    geocoder,
    carrier,
    NumberParseException,
    PhoneNumberFormat,
    format_number,
    region_code_for_number,
)
import time
import random

# ---- Optional: small demo prefix map for India (example only) ----
# This is illustrative — real mapping needs a much larger, up-to-date dataset.
# Keys here are the first 4-5 digits of the national number for mobile/landline prefixes.
INDIA_PREFIX_MAP = {
    "9876": "Maharashtra > Pune (approx.)",
    "9845": "Karnataka > Bangalore (approx.)",
    "9910": "Delhi (approx.)",
    "022":  "Maharashtra > Mumbai (landline STD 22)",
    "080":  "Karnataka > Bangalore (landline STD 80)",
    # add more prefixes as needed...
}

def lookup_india_district(national_number_str):
    # try 5, then 4, then 3 digit prefixes
    for l in (5, 4, 3):
        if len(national_number_str) >= l:
            prefix = national_number_str[:l]
            if prefix in INDIA_PREFIX_MAP:
                return INDIA_PREFIX_MAP[prefix]
    return None

# ---- Tracer function ----
def start_phone_tracer(target):
    """Parse a phone number and print location + carrier info (best-effort)."""
    print("[+] PhoneTracer v2.1 - OSINT\n")
    print(f"[*] Target: {target}")
    print("[*] Initiating trace ...")
    time.sleep(random.uniform(0.3, 0.9))

    try:
        p = phonenumbers.parse(target, None)
    except NumberParseException as e:
        print(f"[!] Number parse error: {e}")
        return

    # basic validity checks
    possible = phonenumbers.is_possible_number(p)
    valid = phonenumbers.is_valid_number(p)

    # core formatting and metadata
    e164 = format_number(p, PhoneNumberFormat.E164)
    intl = format_number(p, PhoneNumberFormat.INTERNATIONAL)
    nat = format_number(p, PhoneNumberFormat.NATIONAL)
    region = region_code_for_number(p)  # e.g., 'IN', 'US'
    country_code = p.country_code
    national_number_str = str(p.national_number)

    print(f"[+] Possible number: {possible}")
    print(f"[+] Valid number:    {valid}")
    print("Formatted:")
    print("  E.164:        ", e164)
    print("  International:", intl)
    print("  National:     ", nat)
    print(f"[+] Country code:  +{country_code}")
    print(f"[+] Region code:   {region if region else '(unknown)'}")
    print(f"[+] National num:  {national_number_str}")

    # geolocation (best-effort human readable)
    loc = geocoder.description_for_number(p, "en")
    print(f"[+] Geocoder location: {loc if loc else '(unknown)'}")

    # carrier (best-effort)
    car = carrier.name_for_number(p, "en")
    print(f"[+] Carrier:           {car if car else '(unknown)'}")

    # Additional country-specific approximate district lookup (example: India)
    if region == "IN":
        approx = lookup_india_district(national_number_str)
        if approx:
            print(f"[+] Approx district/state (from prefix map): {approx}")
        else:
            print("[+] Approx district/state (prefix map): (not found in demo map)")
    else:
        # For other countries you could implement similar prefix->region maps
        print("[+] Approx district/state: (country-specific mapping not configured)")

    print("\n[+] Trace complete")

if __name__ == "__main__":
    number = input("Enter phone number with country code (e.g. +14155552671): ").strip()
    start_phone_tracer(number)

