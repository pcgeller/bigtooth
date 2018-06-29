import yaml

#open configuration

#get list of data to read in
#read in all data for each data set
class ingestor:
    def __init__(self,config):
        try:
            with open(config, 'r') as f:
                self.config = yaml.load(f)
        except Exception as e:
            print("Error opening yaml file: %s ", e)
            #    keys, values = zip(*config.items())

    self.dbs = [db for db in listdir(conf['LOCALDB']) if isfile(join(conf['LOCALDB'], db))]

    def dbQueue(config, remote = TRUE):
        if remote = TRUE:
            DBPATH = config['REMOTEDB']

    def open(config, remote=TRUE):
        conn = sql.connect(config[''])

if __name__ == '__main__':
    ingest = ingestor('/home/pcgeller/bigtooth/conf/ingestConfig.yml')
