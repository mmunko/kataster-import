alter table kataster.kn_bpej add geom geometry;
update kataster.kn_bpej set geom = geometry::STGeomFromText(geom_txt,5514)

alter table kataster.kn_katuz add geom geometry;
update kataster.kn_katuz set geom = geometry::STGeomFromText(geom_txt,5514)

alter table kataster.kn_kladpar add geom geometry;
update kataster.kn_kladpar set geom = geometry::STGeomFromText(geom_txt,5514)

alter table kataster.kn_linie add geom geometry;
update kataster.kn_linie set geom = geometry::STGeomFromText(geom_txt,5514)

alter table kataster.kn_popis add geom geometry;
update kataster.kn_popis set geom = geometry::STGeomFromText(geom_txt,5514)

alter table kataster.kn_uov add geom geometry;
update kataster.kn_uov set geom = geometry::STGeomFromText(geom_txt,5514)

alter table kataster.kn_zappar add geom geometry;
update kataster.kn_zappar set geom = geometry::STGeomFromText(geom_txt,5514)

alter table kataster.kn_znacky add geom geometry;
update kataster.kn_znacky set geom = geometry::STGeomFromText(geom_txt,5514)

alter table kataster.kn_zuob add geom geometry;
update kataster.kn_zuob set geom = geometry::STGeomFromText(geom_txt,5514)
