from botocore.exceptions import ClientError, WaiterError
import config
import utility
from tablespecs.vehicletechrecord import VehicleTechRecordTable
import tablehelper
import datahelper

# Main method
if __name__ == "__main__":
    utility.log("START: CVS test data upload...")
    utility.log("Tables to create: %s" % len(config.tablesToProcess))

    for tableType in config.tablesToProcess:
        table = tableType()
        utility.log("Processing table: %s" % table.name)

        try:
            if(not tablehelper.tableExists(table.name)):
                utility.log("Table %s does not exist." % table.name)
                tablehelper.createTable(
                    table.name,
                    table.attributeDefinitions,
                    table.keySchema,
                    table.provisionedThroughput)

            # Test amount of records against required record count.
            currentRecordCount = tablehelper.getRecordCount(table.name)
            if(currentRecordCount < table.recordCount):
                recordsToCreate = table.recordCount - currentRecordCount
                datahelper.populateTable(table, recordsToCreate)
            else:
                utility.log("No records to add to table %s it currently has %d records" % (
                    table.name, currentRecordCount))

        except ClientError as err:
            utility.log("Error" + str(err))

        utility.log("END: Processing complete.")
