import boto3
import time
import tqdm
from botocore.exceptions import ClientError, WaiterError
import utility

# Initialise Boto3
userSession = boto3.session.Session(profile_name='cvsnonprod')
ddbClient = userSession.client('dynamodb')
ddbRecourse = userSession.resource('dynamodb')

# Check if a table exists, returns boolean.
def tableExists(tableName):
    tables = ddbClient.list_tables()
    result = (tableName in tables['TableNames'])
    utility.log("Table '" + tableName + "' exists = " + str(result))
    return result

# Creates a table with a given name and spec.
def createTable(tableName, attributeDefinitions, keySchema, provisionedThroughput):
    utility.log('Creating table ' + tableName)
    ddbClient.create_table(
        AttributeDefinitions=attributeDefinitions,
        TableName=tableName,
        KeySchema=keySchema,
        ProvisionedThroughput=provisionedThroughput
    )
    waiter = ddbClient.get_waiter('table_exists')
    waiter.wait(TableName=tableName)
    utility.log('Table: ' + tableName + ' created.')

def getRecordCount(tableName): 
    utility.log("Checking record count for table %s" % tableName)
    response = ddbClient.describe_table(TableName=tableName)
    return response['Table']['ItemCount']