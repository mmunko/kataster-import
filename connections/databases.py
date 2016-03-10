"""
Zabezpecuje pripojenie ku databazam

Poznamka:
    vyzaduje: pyodbc (https://github.com/mkleehammer/pyodbc)
              unixODBC SQL Server driver (https://msdn.microsoft.com/en-us/library/hh568454%28v=sql.110%29.aspx)
"""

import pyodbc
import sys
from logger import logger
from connections.sql import *

log = logger.Logger()

class DatabaseConnector:
    """
    Trieda zabezpecujuca operacie s MS SQL Server databazou.
    """

    def __init__(self,database,**kwargs):
        """
        Inicializacna metoda
        Parametre:
            database : typ databazy
            server   : ip adresa alebo dns nazov servera - default localhost
            port     : port
            db       : databaza ku ktorej sa ma pripojit
            user     : pouzivatel pod ktorym sa ma autentifikovat
            pwd      : heslo pouzivatela pod ktorym sa ma autentifikovat
        """
        # overenie ci je podany spravny typ databazy
        if database not in ['sql','postgres','oracle']:
            log.error('Nespravny typ databazy "{}". Podporovane hodnoty su: [sql, postgres, oracle]. Ukoncujem program.'.format(database))

        else:
            # inicializacia connection parametrov
            self.database = database
            self.server = kwargs.get('server','localhost')
            self.port = kwargs.get('port', '')
            self.db = kwargs.get('db','')
            self.user = kwargs.get('user','')
            self.pwd = kwargs.get('pwd','')
            self.schema = kwargs.get('schema','kn')

            # inicializovanie konekcie
            if self.database == 'sql': #inicializacia databazy SQL Server
                try:
                    self.cnxn = pyodbc.connect('DRIVER=/opt/microsoft/msodbcsql/lib64/libmsodbcsql-13.0.so.0.0;SERVER={};DATABASE={};UID={};PWD={}'.format(self.server,self.db,self.user,self.pwd))
                except:
                    log.error('Neuspesna inicializacia pripojenia k databaze')

                if hasattr(self,'cnxn'):
                    self.cursor = self.cnxn.cursor()
                    log.info('Pripojenie k databaze uspesne inicializovane.')

    def execute(self,sql,*args):
        """
        Metoda ktora zabezpecuje spustenie sql dopytov s dodanim parametrov, hodnoty parametrov sa udavaju ako list
        """
        if args is not None:
            self.cursor.execute(sql,args)
        else:
            self.cursor.execute(sql)

    def commit(self):
        """
        Metoda ktora urobi commit sql prikazu na databazu.
        """
        self.cursor.commit()

    def clean(self):
        log.info('Cistim databazu {} schemu {}'.format(self.db,self.schema))
        if self.database == 'sql':
            try:
                self.execute(MSSQL.drop_tables(self.schema))
                self.commit()
                log.info('Databaza {} schema {} bola uspesne vycistena.'.format(self.db,self.schema))
            except:
                log.warning('Databazu {} schemu {} sa nepodarilo vycistit.'.format(self.db,self.schema))

    def initialize(self,**kwargs):
        """
        Metoda ktora inicializuje databazu pred importom dat.
        Parametre:
            clean   : znamena urobit import do clean databazy (vymazat vsetky objekty v terajsej databaze)
        """
        clean = kwargs.get('clean',False)

        if clean:
            self.clean()

        try:
            if self.database == 'sql':
                self.execute(MSSQL.create_tables(self.schema))
                self.commit()

            log.info('Databaza bola uspesne vytvorena.')

        except:
            log.error('Databazu sa nepodarilo vytvorit.')
