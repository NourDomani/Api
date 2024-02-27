import requests

def get_country_info(country_name):
    url = "https://restcountries.com/v3.1/name/{country_name}"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        country_data = response.json()
        
        # Assuming the API returns a list of countries even if only one matches the query
        if country_data and isinstance(country_data, list):
            country = country_data[0]
            
            print("Country Name:", country["name"]["common"])
            print("Capital:", country["capital"][0])
            print("Population:", country["population"])
            print("Area:", country["area"], "sq. km")
            print("Region:", country["region"])
            print("Languages:", ", ".join(country["languages"]))
        else:
            print("Country not found.")
    else:
        print("Failed to fetch data. Status code:", response.status_code)

# Example usage
country_name = input("Enter the name of the country: ")
get_country_info(country_name)
