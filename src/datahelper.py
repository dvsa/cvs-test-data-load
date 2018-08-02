import boto3
import time
import tqdm
from botocore.exceptions import ClientError, WaiterError
from faker import Faker 
import utility

# Initialise Boto3
userSession = boto3.session.Session(profile_name='cvsnonprod')
ddbClient = userSession.client('dynamodb')
ddbResource = userSession.resource('dynamodb')

# Initialize Faker
fake = Faker()

# Populates a given table with a number of fake records.
def populateTable(table, recordsToCreate):
    utility.log("Populating table '" + table.name +
        "' with " + str(recordsToCreate) + " records")

    with ddbResource.Table(table.name).batch_writer() as batch:
        for c in tqdm.tqdm(range(1, recordsToCreate+1)):
            batch.put_item(Item=table.generateFake())