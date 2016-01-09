## Priprava databazy PostgreSQL

### Priprava novej databazy
Pomocou nasledovnych prikazov sa vytvori:
 * databaza Kataster
 * aktivuje nadstavba postgis a postgis_topology
 * prida suradnicovy system EPSG:5114

'''
$ psql -U <db-user> postgres
$ CREATE DATABASE kataster OWNER <dbuser>;
$ \connect kataster;
$ CREATE EXTENSION postgis;
$ CREATE EXTENSION postgis_topology;
$ INSERT INTO public.spatial_ref_sys (srid, auth_name, auth_srid, proj4text, srtext) VALUES ( 5514, 'EPSG', 5514, '+proj=krovak +lat_0=49.5 +lon_0=24.83333333333333 +alpha=30.28813972222222 +k=0.9999 +x_0=0 +y_0=0 +ellps=bessel +towgs84=589,76,480,0,0,0,0 +units=m +no_defs ', 'PROJCS["S-JTSK / Krovak East North",GEOGCS["S-JTSK",DATUM["System_Jednotne_Trigonometricke_Site_Katastralni",SPHEROID["Bessel 1841",6377397.155,299.1528128,AUTHORITY["EPSG","7004"]],TOWGS84[589,76,480,0,0,0,0],AUTHORITY["EPSG","6156"]],PRIMEM["Greenwich",0,AUTHORITY["EPSG","8901"]],UNIT["degree",0.0174532925199433,AUTHORITY["EPSG","9122"]],AUTHORITY["EPSG","4156"]],PROJECTION["Krovak"],PARAMETER["latitude_of_center",49.5],PARAMETER["longitude_of_center",24.83333333333333],PARAMETER["azimuth",30.28813972222222],PARAMETER["pseudo_standard_parallel_1",78.5],PARAMETER["scale_factor",0.9999],PARAMETER["false_easting",0],PARAMETER["false_northing",0],UNIT["metre",1,AUTHORITY["EPSG","9001"]],AXIS["X",EAST],AXIS["Y",NORTH],AUTHORITY["EPSG","5514"]]');
$ \q
'''

### Export do existujucej databazy
Pomocou nasledujuceho prikazu sa vymaze cely obsah schemy kataster.

'''
$ psql -U <dbuser> kataster
$ DROP SCHEMA kataster CASCADE;
$ \q
'''
