CREATE VIEW store_country 
AS SELECT Store.store_number,country.country_name,Store.ownership_owner_ship,Store.brand_brand_name
From store
JOIN City On store.city_city_name=city.city_name
JOIN country On city.country_country_name=country.country_name
;
