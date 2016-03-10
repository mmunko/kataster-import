class MSSQL:
    """
    Trieda zdruzujuca sql pre MS SQL Server
    """
    def create_tables(schema):
        """
        Metoda ktora vytvori strukturu databazy
        """
        return """
        -- Vytvori priestorove tabulky
        -- ===================================
        -- vytvori tabulku parciel C
        CREATE TABLE {0}.kn_kladpar (
            gid int IDENTITY(1,1),
            o_id integer,
            ku integer,
            parckey varchar(17),
            parcela varchar(40),
            kmen integer,
            podlomenie integer,
            t nvarchar(max),
            g_s nvarchar(max),
            stav_k datetime,
            subor varchar(32),
            geom geometry
        );

        -- vytvori tabulku urceneho operatu
        CREATE TABLE {0}.kn_uov (
            gid int IDENTITY(1,1),
    		o_id integer,
    		ku integer,
    		parckey varchar(17),
    		parcela varchar(40),
    		kmen integer,
    		podlomenie integer,
    		t nvarchar(max),
    		stav_k datetime,
    		subor varchar(32),
            geom geometry
        );

        -- vytvori tabulku zastavaneho uzemia obce
        CREATE TABLE {0}.kn_zuob (
    		gid int IDENTITY(1,1),
    		o_id integer,
    		ku integer,
    		stav_k datetime,
    		subor varchar(32),
            geom geometry
    	);

        -- vytvori tabulku bpej
        CREATE TABLE {0}.kn_bpej (
    		gid int IDENTITY(1,1),
    		o_id integer,
    		ku integer,
    		bj varchar(40),
    		stav_k datetime,
    		subor varchar(32),
            geom geometry
    	);

        -- vytvori tabulku katastralnych uzemi
        CREATE TABLE {0}.kn_katuz (
    		gid int IDENTITY(1,1),
    		o_id integer,
    		ku integer,
    		ku_cislo integer,
    		ku_nazov nvarchar(255),
    		g_k integer,
    		stav_k datetime,
    		subor varchar(32),
            geom geometry
    	);

        -- vytvori tabulku zappar
        CREATE TABLE {0}.kn_zappar (
    		gid int IDENTITY(1,1),
    		o_id integer,
    		ku integer,
    		g_k integer,
    		stav_k datetime,
    		subor varchar(32),
            geom geometry
    	);

        -- vytvori tabulku linii
        CREATE TABLE {0}.kn_linie (
    		gid int IDENTITY(1,1),
    		o_id integer,
    		ku integer,
    		g_k integer,
    		stav_k datetime,
    		subor varchar(32),
            geom geometry
    	);

        -- vytvori tabulku znaciek parciel
        CREATE TABLE {0}.kn_znacky (
    		gid int IDENTITY(1,1),
    		o_id integer,
    		ku integer,
    		g_s integer,
    		g_u real,
    		g_m numeric(2, 1),
    		stav_k datetime,
    		subor varchar(32),
            geom geometry
	    );

        -- vytvori tabulku popisov
        CREATE TABLE {0}.kn_popis (
    		gid int IDENTITY(1,1),
    		o_id integer,
    		ku integer,
    		text nvarchar(max),
    		g_k integer,
    		g_u real,
    		g_h numeric(2, 1),
    		g_f integer,
    		g_d integer,
    		stav_k datetime,
    		subor varchar(32),
            geom geometry
    	);

        -- Vytvori nepriestorove tabulky
        -- ===============================
        -- vytvori tabulku zoznam vlastnickych podielov k bytom
        CREATE TABLE {0}.kn_bp (
    		row_id int IDENTITY(1,1),
    		ku integer,
    		icp integer,
    		clv integer,
    		pcs integer,
    		bnp smallint,
    		cip real,
    		cib smallint,
    		cnp varchar(4),
    		civ varchar(30),
    		vym integer,
    		pec integer,
    		mss integer,
    		cit bigint,
    		men bigint,
    		pvz integer,
    		kpv smallint,
    		cen integer,
    		oce integer,
    		cas varchar(30),
    		crc integer,
    		naz_suboru varchar(20)
    	);

        -- vytvori tabuluku zoznam stavieb na cudzom pozemku
        CREATE TABLE {0}.kn_cs (
    		row_id int IDENTITY(1,1),
    		parckey varchar(17),
    		ku integer,
    		ics integer,
    		clv integer,
    		cel integer,
    		cpa integer,
    		pec integer,
    		mss integer,
    		vym integer,
    		pkk varchar(40),
    		ums smallint,
    		drs smallint,
    		pvz integer,
    		kpv smallint,
    		don integer,
    		cen integer,
    		oce integer,
    		cas varchar(30),
    		zcs integer,
    		crc integer,
    		naz_suboru varchar(20)
    	);

        --vytvori tabulku informacie o zdruzenych parcelach
        CREATE TABLE {0}.kn_ep (
    		row_id int IDENTITY(1,1),
    		parckey varchar(17),
    		ku integer,
    		cpa integer,
    		cpu smallint,
    		vym integer,
    		kvv smallint,
    		drp smallint,
    		don smallint,
    		pkk integer,
    		mss smallint,
    		pec integer,
    		cel integer,
    		clv integer,
    		kpv smallint,
    		ump smallint,
    		pvz integer,
    		miv smallint,
    		clm integer,
    		drv integer,
    		ndp smallint,
    		prp smallint,
    		spn smallint,
    		mlm integer,
    		cen real,
    		oce integer,
    		pcp integer,
    		cas varchar(30),
    		crc integer,
    		naz_suboru varchar(20)
    	);

        -- vytvori tabulku listy vlastnictva
        CREATE TABLE {0}.kn_lv (
    		row_id int IDENTITY(1,1),
    		ku integer,
    		clv integer,
    		psv smallint,
    		rzs smallint,
    		kpv smallint,
    		rzp smallint,
    		pvz integer,
    		pep smallint,
    		ppl smallint,
    		slv varchar(30),
    		dst smallint,
    		crc integer,
    		naz_suboru varchar(20)
    	);

        --vytvori tabulku informacie o parcelach
        CREATE TABLE {0}.kn_pa (
    		row_id int IDENTITY(1,1),
    		parckey varchar(17),
    		ku integer,
    		cpa integer,
    		vym integer,
    		kvv smallint,
    		drp smallint,
    		don smallint,
    		pkk integer,
    		mss smallint,
    		pec integer,
    		cel integer,
    		clv integer,
    		kpv smallint,
    		ump smallint,
    		pvz integer,
    		miv smallint,
    		clm integer,
    		drv integer,
    		prp smallint,
    		spn smallint,
    		ndp smallint,
    		dn1 smallint,
    		dn2 smallint,
    		dn3 smallint,
    		dn4 smallint,
    		dn5 smallint,
    		dn6 smallint,
    		dn7 smallint,
    		dn8 smallint,
    		mlm integer,
    		cen real,
    		oce integer,
    		cas varchar(30),
    		crc integer,
    		naz_suboru varchar(20)
    	);

        --vytvori tabulku povodne katastralne uzemie
        CREATE TABLE {0}.kn_pk (
    		row_id int IDENTITY(1,1),
    		ku integer,
    		ump smallint,
    		cpk integer,
    		npk varchar(28),
    		cpu integer,
    		crc integer,
    		naz_suboru varchar(20)
    	);

        --vytvori tabulku pravne vztahy
        CREATE TABLE {0}.kn_pv (
    		row_id int IDENTITY(1,1),
    		ku integer,
    		idc integer,
    		clv integer,
    		pcs smallint,
    		idt smallint,
    		idn bigint,
    		cde smallint,
    		drf smallint,
    		poz nvarchar(max),
    		pvz integer,
    		kpv smallint,
    		idu varchar(255),
    		crc integer,
    		naz_suboru varchar(20)
    	);

        --vytvori tabulku
        CREATE TABLE {0}.kn_uz (
    		row_id int IDENTITY(1,1),
    		ku integer,
    		cel integer,
    		sip integer,
    		sek smallint,
    		pks smallint,
    		pvz integer,
    		rzp smallint,
    		kpv smallint,
    		ppe smallint,
    		ico bigint,
    		uzi varchar(150),
    		tid varchar(255),
    		naj varchar(255),
    		crc integer,
    		naz_suboru varchar(20)
    	);

        --vytvori tabulku zoznam vlastnikov
        CREATE TABLE {0}.kn_vl (
    		row_id int IDENTITY(1,1),
    		ku integer,
    		clv integer,
    		pcs smallint,
    		cit bigint,
    		men bigint,
    		pvz integer,
    		kpv smallint,
    		ico bigint,
    		pcz smallint,
    		sta integer,
    		rci bigint,
    		stb integer,
    		vla varchar(255),
    		tvl smallint,
    		tuc smallint,
    		dru smallint,
    		pri varchar(150),
    		mno varchar(30),
    		rod varchar(30),
    		tip varchar(30),
    		prv varchar(30),
    		mev varchar(30),
    		rov varchar(30),
    		tiz varchar(30),
    		ulc varchar(50),
    		cpo varchar(30),
    		mst varchar(50),
    		psc varchar(6),
    		dop varchar(90),
    		stt varchar(30),
    		tid integer,
    		crc integer,
    		naz_suboru varchar(20)
    	);

        --vytvori tabulku najomnik alebo ina opravnena osoba
        CREATE TABLE {0}.kn_nj (
    		row_id int IDENTITY(1,1),
    		ku integer,
    		cel integer,
    		ico bigint,
    		naj varchar(255),
    		pvz integer,
    		sek integer,
    		sip integer,
    		tid integer,
    		crc integer,
    		naz_suboru varchar(20)
    	);
        """.format(schema)

    def drop_tables(schema):
        """
        Metoda ktora vycisti vsetky objekty v danej scheme
        """
        return """
            drop table {0}.kn_nj;
            drop table {0}.kn_vl;
            drop table {0}.kn_uz;
            drop table {0}.kn_pv;
            drop table {0}.kn_pk;
            drop table {0}.kn_pa;
            drop table {0}.kn_lv;
            drop table {0}.kn_ep;
            drop table {0}.kn_cs;
            drop table {0}.kn_bp;
            drop table {0}.kn_popis;
            drop table {0}.kn_znacky;
            drop table {0}.kn_linie;
            drop table {0}.kn_zappar;
            drop table {0}.kn_bpej;
            drop table {0}.kn_katuz;
            drop table {0}.kn_zuob;
            drop table {0}.kn_uov;
            drop table {0}.kn_kladpar;
        """.format(schema)
