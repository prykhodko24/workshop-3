
Declare
  --Опишем тип массива 
   type arr_type_small IS VARRAY(6) OF VARCHAR2(10);
   type arr_type_big IS VARRAY(6) OF VARCHAR2(30);   

city_name arr_type_big;
country_country_name arr_type_small;
BEGIN
city_name:=arr_type_big('London','Lviv','Kyev' ,'Odesa','NY','LA');
country_country_name:=arr_type_small('UK','UA','UA','UA','USA','USA');


    FOR i IN 1 .. 6 
    LOOP
        INSERT INTO city (city_name, country_country_name) VALUES (city_name(i), country_country_name(i));
        COMMIT;
    END LOOP;
END;


