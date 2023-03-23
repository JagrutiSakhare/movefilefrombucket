import cloudagnosticfass
import configparser

config = configparser.ConfigParser()
config.read('cloud.properties')

cloud=config.get("data", "cloud")
trigger=config.get("data", "trigger")
dest_bucket=config.get("data", "dest_bucket")

def move_file(source_bucket,source_file) :
    dest_file = "something.txt"
    print("We have reached till dest_file")
    cloudagnosticfass.move_file(cloud,source_bucket,source_file,dest_bucket,dest_file)
