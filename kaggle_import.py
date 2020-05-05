import cx_Oracle
import csv

username = 'MYONLINEEDU'
password = 'njvf24'
databaseName = 'localhost/xe'
connection = cx_Oracle.connect(username,password, databaseName)


def isInt(n):
    return int(n) == float(n)


filename = "directory.csv"
countries = []

cities = []
ownerships = []
brands = []


with open(filename, newline='') as file:
    reader = csv.reader(file)
    name_t = next(reader)[11]
    for i in range(2000):#charmap' не может декодировать байт 0x98 в позиции 2596,тому довелось обмежити
        value=next(reader)
        value_b=value[0]
        value_snb = value[1]
        value_sn = value[2]
        value_o = value[3]
        value_ct = value[5]
        value_co = value[7]
        value_lo = float(value[11])
        value_la = float(value[12])

        if value_co not in countries:
            countries.append(value_co)
            Country_query = "insert into Country(COUNTRY_NAME) values (:COUNTRY_NAME )"
            cursor = connection.cursor()
            cursor.execute(Country_query, COUNTRY_NAME=value_co)
            cursor.close()

        if value_b not in brands:
            brands.append(value_b)
            brand_query = "insert into BRAND(BRAND_NAME) values (:BRAND_NAME )"
            cursor = connection.cursor()
            cursor.execute(brand_query, BRAND_NAME=value_b)
            cursor.close()
        if value_o not in ownerships:
            ownerships.append(value_o)
            ownerships_query = "insert into ownership(OWNER_SHIP) values (:OWNER_SHIP )"
            cursor = connection.cursor()
            cursor.execute(ownerships_query, OWNER_SHIP=value_o)
            cursor.close()
        if value_ct not in cities:
            cities.append(value_ct)
            city_query = "insert into city(CITY_NAME,COUNTRY_COUNTRY_NAME) values (:CITY_NAME,:COUNTRY_COUNTRY_NAME )"
            cursor = connection.cursor()
            cursor.execute(city_query , CITY_NAME=value_ct,COUNTRY_COUNTRY_NAME=value_co)
            cursor.close()



        store_query = "insert into store(STORE_NUMBER,STORE_NAME,LONGITUDE,LATITUDE,BRAND_BRAND_NAME,OWNERSHIP_OWNER_SHIP,CITY_CITY_NAME) values (:STORE_NUMBER,:STORE_NAME,:LONGITUDE,:LATITUDE,:BRAND_BRAND_NAME,:OWNERSHIP_OWNER_SHIP,:CITY_CITY_NAME )"
        cursor = connection.cursor()
        cursor.execute(store_query,STORE_NUMBER=value_snb,STORE_NAME=value_sn,LONGITUDE=value_lo,LATITUDE=value_la,BRAND_BRAND_NAME=value_b,OWNERSHIP_OWNER_SHIP=value_o,CITY_CITY_NAME=value_ct)
        cursor.close()

    print(countries)


connection.commit()


