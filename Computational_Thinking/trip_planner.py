from math import ceil

hotels_db = [
    ("Hotel Le Centre", 23.0, "France"),
    ("Old Stone Trough", 20.0, "United Kingdom"),
    ("Hotel Adlon Kempinski Berlin", 155.0, "Germany"),
    ("Hostel Central Lisbon", 50.0, "Portugal"),
    ("Pension Faro Budget", 65.0, "Portugal"),
    ("Four Seasons Milan", 195.0, "Italy"),
    ("Pousada da Juventude Lisboa", 14.0, "Portugal"),
    ("Manchester Comfort Inn", 98.0, "United Kingdom"),
    ("Simple Inn Milan", 68.0, "Italy"),
    ("Cheap Sleep The Hague", 72.0, "Netherlands"),
    ("Bern Boutique", 118.0, "Switzerland"),
    ("Seville City Hotel", 125.0, "Spain"),
    ("The Dorchester London", 180.0, "United Kingdom"),
    ("Hostel Munich", 50.0, "Germany"),
    ("Nice Beachfront", 125.0, "France"),
    ("Urban Hostel", 15.0, "Netherlands"),
    ("Venice Guest House", 108.0, "Italy"),
    ("Groningen Boutique", 128.0, "Netherlands"),
    ("Pension Naples", 72.0, "Italy"),
    ("Economy Inn Marseille", 62.0, "France"),
    ("Budget Inn Rome", 52.0, "Italy"),
    ("New Generation Hostel", 19.0, "Italy"),
    ("Mandarin Oriental Munich", 180.0, "Germany"),
    ("Simple Stay Lucerne", 68.0, "Switzerland"),
    ("Comfort Inn Barcelona", 82.0, "Spain"),
    ("Uhlenkoper-Camp Uelzen", 15.0, "Germany"),
    ("Amsterdam Central", 88.0, "Netherlands"),
    ("Hostel Central Venice", 50.0, "Italy"),
    ("Interlaken Hotel", 138.0, "Switzerland"),
    ("By The Lake Hostel", 23.0, "Switzerland"),
    ("Versailles Inn", 135.0, "France"),
    ("Kurhaus Hotel Scheveningen", 192.0, "Netherlands"),
    ("Budget Stay Barcelona", 62.0, "Spain"),
    ("Edinburgh Boutique", 115.0, "United Kingdom"),
    ("Pension Nice", 72.0, "France"),
    ("Bath Heritage Hotel", 138.0, "United Kingdom"),
    ("Waldorf Astoria Berlin", 170.0, "Germany"),
    ("Algarve Beach Hotel", 120.0, "Portugal"),
    ("Conde Rodrigo II", 21.0, "Spain"),
    ("Simple Inn Braga", 70.0, "Portugal"),
    ("Claridge's Mayfair", 168.0, "United Kingdom"),
    ("Ritz Paris", 155.0, "France"),
    ("Belmond Splendido", 185.0, "Italy"),
    ("Zurich Standard", 88.0, "Switzerland"),
    ("Hotel Gran Via Madrid", 98.0, "Spain"),
    ("Hostel Rotterdam", 50.0, "Netherlands"),
    ("Economy Hotel Bern", 62.0, "Switzerland"),
    ("Lyon Comfort Inn", 98.0, "France"),
    ("Hostel Geneva", 50.0, "Switzerland"),
    ("Royal Seville Palace", 190.0, "Spain"),
    ("Pension Valencia", 60.0, "Spain"),
    ("Milano Comfort", 128.0, "Italy"),
    ("Tivoli Avenida Liberdade", 180.0, "Portugal"),
    ("Casa Simples Madrid", 55.0, "Spain"),
    ("De L'Europe Amsterdam", 168.0, "Netherlands"),
    ("Hostel Central Manchester", 55.0, "United Kingdom"),
    ("Memmo Alfama Hotel", 150.0, "Portugal"),
    ("Cologne Inn", 138.0, "Germany"),
    ("Boutique Hotel Lisbon", 95.0, "Portugal"),
    ("Golden Tulip Amsterdam", 200.0, "Netherlands"),
    ("Amalfi Coast Hotel", 138.0, "Italy"),
    ("Peninsula Paris", 192.0, "France"),
    ("Hotel Lisboa", 80.0, "Portugal"),
    ("Frankfurt Standard", 115.0, "Germany"),
    ("Budget Interlaken", 72.0, "Switzerland"),
    ("Economy Inn Malaga", 70.0, "Spain"),
    ("Hassler Roma", 155.0, "Italy"),
    ("Pulitzer Amsterdam", 180.0, "Netherlands"),
    ("Madeira Resort", 135.0, "Portugal"),
    ("The Yeatman", 165.0, "Portugal"),
    ("Luxury", 200.0, "Italy"),
    ("Rome City Hotel", 85.0, "Italy"),
    ("Budget Hotel Berlin", 52.0, "Germany"),
    ("Paris City Hotel", 85.0, "France"),
    ("Economy Hotel Edinburgh", 62.0, "United Kingdom"),
    ("Comfort Inn Porto", 105.0, "Portugal"),
    ("Gran Melia Luxury", 200.0, "Spain"),
    ("Private Madrid Luxury", 175.0, "Spain"),
    ("Pestana Palace Lisboa", 195.0, "Portugal"),
    ("Hamburg Boutique", 128.0, "Germany"),
    ("Marseille Boutique", 110.0, "France"),
    ("Birmingham Standard", 125.0, "United Kingdom"),
    ("Costa del Sol Inn", 138.0, "Spain"),
    ("London City Hotel", 85.0, "United Kingdom"),
    ("Gritti Palace Venice", 170.0, "Italy"),
    ("Lucerne Inn", 128.0, "Switzerland"),
    ("Simple Stay Toulouse", 68.0, "France"),
    ("Simple Stay Groningen", 68.0, "Netherlands"),
    ("Budget Inn Amsterdam", 55.0, "Netherlands"),
    ("Fairmont Hamburg", 200.0, "Germany"),
    ("Savoy London", 152.0, "United Kingdom"),
    ("Frankfurter Hof", 192.0, "Germany"),
    ("Budget Motel Paris", 55.0, "France"),
    ("Berlin City Hotel", 85.0, "Germany"),
    ("Simple Stay Hamburg", 68.0, "Germany"),
    ("Three Stars Valencia", 115.0, "Spain"),
    ("Casa Simples Covilhã", 60.0, "Portugal"),
    ("Economy Inn Frankfurt", 62.0, "Germany"),
    ("Mandarin Oriental Barcelona", 168.0, "Spain"),
    ("Munich Comfort Inn", 102.0, "Germany"),
    ("Cheap Sleep Bath", 72.0, "United Kingdom"),
    ("Budget Dresden", 72.0, "Germany"),
    ("Utrecht Comfort Inn", 115.0, "Netherlands"),
    ("Royal Kensington Palace", 192.0, "United Kingdom"),
    ("Hotel Arts Barcelona", 152.0, "Spain"),
    ("Geneva Comfort Inn", 105.0, "Switzerland"),
    ("Small Inn Birmingham", 68.0, "United Kingdom"),
    ("Lusanne Palace", 192.0, "Switzerland"),
    ("Florence Inn", 118.0, "Italy"),
    ("Four Seasons Paris", 185.0, "France"),
    ("Rotterdam Hotel", 102.0, "Netherlands"),
    ("Pension Faro", 65.0, "Portugal"),
    ("Badrutt's Palace St. Moritz", 172.0, "Switzerland"),
    ("The Hague Standard", 138.0, "Netherlands"),
    ("Westminster Abbey Luxury", 200.0, "United Kingdom"),
    ("Le Meurice Luxury", 170.0, "France"),
    ("Amstel Hotel Amsterdam", 155.0, "Netherlands"),
    ("Budget Inn Zurich", 55.0, "Switzerland"),
    ("Kulm Hotel St. Moritz", 200.0, "Switzerland"),
    ("Hostel Central Lyon", 50.0, "France"),
    ("Hotel Baur au Lac Zurich", 155.0, "Switzerland"),
    ("Small Hotel Seville", 65.0, "Spain"),
    ("Dolder Grand Zurich", 185.0, "Switzerland"),
    ("Palace Versailles", 200.0, "France"),
    ("Budget Inn London", 52.0, "United Kingdom"),
    ("Six Senses Douro Valley", 200.0, "Portugal"),
    ("Vienna Hotel", 175.0, "Italy"),
    ("Munich Comfort Inn", 102.0, "Germany"),
]

activities_db = [
    ("Walking tour", 10.0, "Portugal"),
    ("Beach walk", 0.0, "Portugal"),
    ("Park picnic", 8.0, "Spain"),
    ("Street art tour", 12.0, "Spain"),
    ("Free museum day", 0.0, "Spain"),
    ("River walk", 6.0, "France"),
    ("Local market visit", 0.0, "France"),
    ("Hiking trail", 8.0, "Switzerland"),
    ("Scenic viewpoint", 0.0, "Switzerland"),
    ("Canal walk Amsterdam", 10.0, "Netherlands"),
    ("Street food tour", 12.0, "Italy"),
    ("Historic square tour", 5.0, "Italy"),
    ("City bike ride", 15.0, "Germany"),
    ("Park exploration", 0.0, "Germany"),
    ("Botanical garden", 10.0, "United Kingdom"),
    ("Waterfront stroll", 0.0, "United Kingdom"),
    ("Coffee shop hopping", 12.0, "Netherlands"),
    ("Local brewery tour", 14.0, "Germany"),
    ("Sunset hike", 8.0, "Italy"),
    ("Photography walk", 10.0, "France"),
    ("Food market tour", 11.0, "Spain"),
    ("Castle grounds walk", 6.0, "Portugal"),
    ("Countryside cycle", 9.0, "Netherlands"),
    ("Mountain trail", 7.0, "Switzerland"),
    ("Historic district walk", 5.0, "United Kingdom"),
    ("Cooking class", 45.0, "Portugal"),
    ("Wine tasting", 35.0, "Portugal"),
    ("Boat tour", 40.0, "Spain"),
    ("Flamenco dance class", 50.0, "Spain"),
    ("Paella cooking", 55.0, "Spain"),
    ("Cheese tasting", 30.0, "France"),
    ("Seine river cruise", 38.0, "France"),
    ("Louvre guided tour", 28.0, "France"),
    ("Painting class", 48.0, "France"),
    ("Swiss chocolate workshop", 42.0, "Switzerland"),
    ("Skiing lesson", 60.0, "Switzerland"),
    ("Fondue dinner experience", 52.0, "Switzerland"),
    ("Dutch bike tour", 35.0, "Netherlands"),
    ("Windmill tour", 30.0, "Netherlands"),
    ("Tulip farm visit", 25.0, "Netherlands"),
    ("Glass blowing class", 50.0, "Italy"),
    ("Gondola ride Venice", 55.0, "Italy"),
    ("Pizza making class", 48.0, "Italy"),
    ("Roman history tour", 32.0, "Italy"),
    ("Tuscany wine tour", 58.0, "Italy"),
    ("Beer tasting", 28.0, "Germany"),
    ("Berlin wall tour", 25.0, "Germany"),
    ("Pretzel making workshop", 40.0, "Germany"),
    ("Castle tour", 35.0, "Germany"),
    ("British Museum", 22.0, "United Kingdom"),
    ("Harry Potter studio tour", 52.0, "United Kingdom"),
    ("Theater show", 48.0, "United Kingdom"),
    ("Kayak River Thames", 60.0, "United Kingdom"),
    ("Horseback riding", 45.0, "Portugal"),
    ("Surfing lesson", 50.0, "Portugal"),
    ("Scuba diving", 55.0, "Spain"),
    ("Helicopter ride", 58.0, "France"),
    ("Hot air balloon", 60.0, "Italy"),
    ("Fishing trip", 40.0, "Netherlands"),
    ("Skiing tour guide", 58.0, "Switzerland"),
    ("Climbing adventure", 52.0, "Germany"),
    ("Private yacht charter", 180.0, "Portugal"),
    ("Michelin star dining", 150.0, "Portugal"),
    ("Private art tour", 140.0, "Spain"),
    ("Luxury resort spa", 160.0, "Spain"),
    ("VIP flamenco show", 130.0, "Spain"),
    ("Private chef experience", 200.0, "France"),
    ("Versailles private tour", 180.0, "France"),
    ("Luxury perfume creation", 160.0, "France"),
    ("Alpine adventure package", 300.0, "Switzerland"),
    ("Private mountain guide", 130.0, "Switzerland"),
    ("Private canal tour", 140.0, "Netherlands"),
    ("Exclusive art gallery tour", 120.0, "Netherlands"),
    ("Luxury cycling tour", 165.0, "Netherlands"),
    ("Private Vatican tour", 150.0, "Italy"),
    ("Luxury cooking with chef", 180.0, "Italy"),
    ("Private Ferrari ride", 200.0, "Italy"),
    ("Luxury train journey", 190.0, "Germany"),
    ("Exclusive castle dinner", 170.0, "Germany"),
    ("Private orchestra concert", 400.0, "Germany"),
    ("Royal Palace tour", 155.0, "United Kingdom"),
    ("Private London tour", 125.0, "United Kingdom"),
    ("Exclusive West End show", 140.0, "United Kingdom"),
    ("Private island trip", 195.0, "Portugal"),
    ("Luxury wine tour", 165.0, "Spain"),
    ("Exclusive art auction", 185.0, "France"),
    ("Private helicopter Alps", 430.0, "Switzerland"),
    ("Private yacht dinner", 190.0, "Netherlands"),
    ("Royal dinner experience", 165.0, "United Kingdom"),
]


def filter_by_country(country, db):
    return list(filter(lambda x: x[2] == country, db))


def select_activities(country_activities: list, budget):
    available_budget = 0.5*budget # budget destined to activities

    country_activities = sorted(country_activities, key = lambda x: x[1]) # sort by ascending price
    activities = []
    spent = 0

    for activity, price, _ in country_activities:
        if (spent + price) > available_budget:
            break
            
        spent += price
        activities.append(activity)

    budget_left = budget - spent

    return activities, budget_left


def compute_days_needed(activities: list):
    return ceil(len(activities) / 3)


def select_hotel(country_hotels: list, budget, days_needed):
    country_hotels = sorted(country_hotels, key = lambda x: x[1], reverse = True) # sort by descending price per night

    chosen_hotel = None

    for hotel, price, _ in country_hotels:
        if price * days_needed <= budget: # most expensive hotel that can fit in the budget
            chosen_hotel = hotel
            budget -= price * days_needed
            break
    
    return chosen_hotel, budget


def plan_trip(country, budget):
    country_activities = filter_by_country(country, activities_db)
    country_hotels = filter_by_country(country, hotels_db)

    activities, budget_for_hotel = select_activities(country_activities, budget) # update budget
    days_needed = compute_days_needed(activities)
    hotel, budget_left = select_hotel(country_hotels, budget_for_hotel, days_needed) # update budget

    return hotel, activities, days_needed, budget_left


def get_valid_country():
    countries_activities_db = {x[2] for x in activities_db} # using set comprehension
    countries_hotels_db = {x[2] for x in hotels_db} # using set comprehension
    valid_countries = countries_activities_db & countries_hotels_db

    country = input()
    while country not in valid_countries:
        print("The inserted country is not valid. Insert another country.")
        country = input()
    
    return country


def get_valid_budget():
    budget = float(input())
    while budget < 100:
        print("Minimum budget: 100€. Insert another budget.")
        budget = float(input())

    return budget


def main():
    country = get_valid_country()
    budget = get_valid_budget()
    
    hotel, activities, days_needed, budget_left = plan_trip(country, budget)

    print(f"Hotel: {hotel}")
    print(f"Activities: {activities}")
    print(f"Days needed: {days_needed}")
    print(f"Budget left: {budget_left}€")


if __name__ == "__main__":
    main()