class Aeropuerto:

    def __init__(self, airport_id, name, city, country, iata, icao,
                 latitude, longitude, altitude, timezone, timezone_text):
        self.airport_id = airport_id
        self.name = name
        self.city = city
        self.country = country
        self.iata = iata
        self.icao = icao
        self.latitude = latitude
        self.longitude = longitude
        self.altitude = altitude
        self.timezone = timezone
        self.timezone_text = timezone_text

    def countries_sql(self):
        return '''
               select distinct country
                 from airports
               order by country
               '''

    def airports_in_country_sql(self):
        return '''
               select *
                 from airports
                where country = ?
               order by city
               '''

    def to_dict(self):
        return self.__dict__
