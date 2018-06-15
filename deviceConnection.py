#Create a bigtooth device.  Connect over wifi/ssh.
#Make blue hydra, gpsd, database available.
import subprocess
import yaml

class device:
    def __init__(self, configPath):
        with open(configPath, 'r') as infile:
            config = yaml.load(infile)
        self.name=config['name']
        self.localAddress=config['localAddress']
        self.user=config['user']
        self.remoteAddress=config['remoteAddress']
        self.remotePathBase=config['remotePathBase']
        self.localPATH=config['localPATH']
        self.remoteDatabases=config['remoteDatabases']
        self.remotes=[self.user + '@' +self.remoteAddress +':' + self.remotePathBase + database for database in self.remoteDatabases]

    def sync(self):
        remote=self.user,'@',self.remoteAddress,':',self.remotePathBase
        subprocess.Popen(['scp', '-r', str(remote), str(localPATH)]).wait()
    def cleanup(self):
        subprocess.Popen['rm', '']
    def rsync(self):
        try:
            for remote in self.remotes:
                print(remote)
                subprocess.Popen(['rsync', '-ave', str(remote), str(self.localPATH)]).wait()
                print("Rsync'd files for :" + remote)
        except Exception as e:
            print(str(e))

if __name__=="__main__":
    configPath = '/home/pcgeller/bigtooth/conf/deviceConfig.yml'
    bt = device()
    bt.rsync()
