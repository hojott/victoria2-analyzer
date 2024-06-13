"""Utils for analyzing wars"""


def losses_template() -> dict:
    """Get a template for listing losses"""
    return {
        "total": 0,
        "irregular": 0,
        "infantry": 0,
        "cavalry": 0,
        "artillery": 0,
        "guard": 0,
        "engineer": 0,
        "cuirassier": 0,
        "dragoon": 0,
        "hussar": 0,
        "armor": 0,
        "airplane": 0,
        "clipper_transport": 0,
        "frigate": 0,
        "manowar": 0,
        "steam_transport": 0,
        "commerce_raider": 0,
        "ironclad": 0,
        "monitor": 0,
        "cruiser": 0,
        "battleship": 0,
        "dreadnought": 0,
    }


def add_losses(country_losses: dict, side: str, date: dict) -> None:
    """Add losses to list of countries losses"""

    country_losses["total"] += date["battle"][side]["losses"]

    for unit, value in date["battle"][side].items():
        # Skip non-units
        if unit in ["country", "leader", "losses"]:
            continue

        country_losses[unit] += value


def analyze_date(date: dict, countries: dict) -> None:
    """Analyze things happening on a wardate"""

    # Add participants
    if "add_attacker" in date.keys():
        countries[date["add_attacker"]] = {
            "side": "attacker",
            "losses": losses_template(),
        }

    if "add_defender" in date.keys():
        countries[date["add_defender"]] = {
            "side": "defender",
            "losses": losses_template(),
        }

    # Add battle losses
    if "battle" in date.keys():
        for country, values in countries.items():
            # Add losses to countries
            if date["battle"]["attacker"]["country"] == country:
                add_losses(values["losses"], "attacker", date=date)

            if date["battle"]["defender"]["country"] == country:
                add_losses(values["losses"], "defender", date=date)


def war_analyze(save_data: dict, cmd: list) -> None:
    """Print different wardata"""

    # List wars
    if cmd[1] in ["list", "l"]:
        for i, war in enumerate(reversed(save_data["previous_war"][1:])):
            print(f"{i+1}: {war['name']}")
        return

    war_data = save_data["previous_war"][-int(cmd[1])]
    print(war_data["name"])

    countries = {}
    for date in war_data["history"].values():
        # If the data is in a list format, instead go through the list
        if isinstance(date, list):
            for event in date:
                analyze_date(event, countries)
            continue

        analyze_date(date, countries)

    for country, data in countries.items():
        print(f"{country}: {data['losses']['total']}")
