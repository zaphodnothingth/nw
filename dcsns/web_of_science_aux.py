# https://github.com/juliettapc/my_In_text_citations/blob/261ca9b5b783fd933df284306cbe1f2344756290/SCRIPT_add_team_size_expertise_recycled_ref_FIRST_PART.py
from pymongo import MongoClient

class MongoConnection(object):
    def __init__(self, cxnSettings, **kwargs):
        self.settings = cxnSettings
        self.mongoURI = self._constructURI()
        self.connect(**kwargs)
        self.ensure_index()
    
    def _constructURI(self):
        '''
        Construct the mongo URI
        '''
        mongoURI = 'mongodb://'
        #User/password handling
        if 'user'in self.settings and 'password' in self.settings:
            mongoURI += self.settings['user'] + ':' + self.settings['password']
            mongoURI += '@'
        elif 'user' in self.settings:
            print('Missing password for given user, proceeding without either')
        elif 'password' in self.settings:
            print('Missing user for given passord, proceeding without either')
        #Host and port
        try:
            mongoURI += self.settings['host'] + ':'
        except KeyError:
            print('Missing the hostname. Cannot connect without host')
            sys.exit()
        try:
            mongoURI += str(self.settings['port'])
        except KeyError:
            print('Missing the port. Substituting default port of 27017')
            mongoURI += str('27017')
        return mongoURI
    
    def connect(self, **kwargs):
        '''
        Establish the connection, database, and collection
        '''
        self.connection = MongoClient(self.mongoURI, **kwargs)
        #########
        try:
            self.db = self.connection[self.settings['db']]
        except KeyError:
            print("Must specify a database as a 'db' key in the settings file")
            sys.exit()
        #########
        try:
            self.collection = self.db[self.settings['collection']]
        except KeyError: pass
            #print('Should have a collection.', end='')
            #print('Starting a collection in database', end='')
            #print(' for current connection as test.')
            #self.collection = self.db['test']
    
    def tearDown(self):
        '''
        Closes the connection
        '''
        self.connection.close()
    
    def ensure_index(self):
        '''
        Ensures the connection has all given indexes.
        indexes: list of (`key`, `direction`) pairs.
            See docs.mongodb.org/manual/core/indexes/ for possible `direction`
            values.
        '''
        if 'indexes' in self.settings:
            for index in self.settings['indexes']:
                self.collection.ensure_index(index[0], **index[1])




merged_papers_settings = {
    "host": "chicago.chem-eng.northwestern.edu",
    "port": "27017",
    "db": "web_of_science_aux",
    "collection": "merged_papers",
    "user": "mongoreader",
    "password": "emptycoffeecup"
}

papers_con = MongoConnection(merged_papers_settings)


dais_settings = {
    "host": "chicago.chem-eng.northwestern.edu",
    "port": "27017",
    "db": "web_of_science_aux",
    "collection": "ut_dais_all",
    "user": "mongoreader",
    "password": "emptycoffeecup"
}

dais_con = MongoConnection(dais_settings)

result_query = papers_con.collection.find_one({"UT":'000322590800016'})

def pretty(d, indent=4):
   for key, value in d.items():
      print('\t' * indent + str(key))
      if isinstance(value, dict):
         pretty(value, indent+1)
      else:
         print('\t' * (indent+1) + str(value))

# citations = in-degrees
