CREATE VIEW store_country 
AS SELECT Store.store_number,country.country_name
From store
JOIN City On store.city_city_name=city.city_name
JOIN country On city.country_country_name=country.country_name
;

Select *
From store_country;

SELECT Count(store_number) As Count_Country,country_name AS Country
From store_country
GROUP BY country_name;


CREATE VIEW store_brand 
AS SELECT Store.store_number,brand.brand_name
From store
JOIN brand On store.brand_brand_name=brand.brand_name
;


SELECT Count(brand_name) As Count_Brand,brand_name AS Brand
From store_brand
GROUP BY brand_name;



CREATE VIEW store_ownership 
AS SELECT store.store_number,ownership.owner_ship
From store
JOIN ownership On store.ownership_owner_ship=ownership.owner_ship
;


SELECT Count(store_number) As Count_Ownership,owner_ship AS Ownership
From store_ownership
GROUP BY Ownership;

