#decoding the DTC into something meaningful
DTC_DESCRIPTIONS = {
    "P0171": "System too lean (Bank 1) — possible vacuum leak or weak fuel delivery",
    "P0172": "System too rich (Bank 1) — possible faulty injector or MAF sensor",
    "P0300": "Random/multiple cylinder misfire detected",
    "P0420": "Catalyst system efficiency below threshold (Bank 1)",
    # you'll expand this list as you go — there are thousands of codes,
    # start with the common ones you're most likely to see
}

def explain(code):
    return DTC_DESCRIPTIONS.get(code, "Unknown code — check manufacturer-specific database")