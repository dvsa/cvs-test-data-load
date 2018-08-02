from faker import Faker
fake = Faker()


class VehicleTechRecordTable:
    def __init__(self):
        self.name = "cvs-vehicle-tech-record"
        self.attributeDefinitions = [
            {'AttributeName': 'vin', 'AttributeType': 'S'},
        ]
        self.keySchema = [
            {"AttributeName": "vin", "KeyType": "HASH"}
        ]
        self.provisionedThroughput = {
            "ReadCapacityUnits": 2,
            "WriteCapacityUnits": 2
        }
        self.recordCount = 80

    # Generates a fake item
    # pylint: disable=maybe-no-member
    def generateFake(self):
        return {
            "vin": fake.uuid4(),
            "timeStamp": fake.date(),
            "vehicle": {
                "systemNumber": fake.random_number(),
                "vehicleClass": "V",
                "vehicleType": "HGV",
                "chassisType": "Rigid",
                "vin": "A02761278",
                "manufactureDate": fake.date(),
                "testCertificateExpiryDate": fake.date(),
                "vehicleIdentifier": fake.license_plate(),
                "previousRegmark": fake.license_plate(),
                "registrationDate": fake.date(),
                "numberOfAxles": 2,
                "make": "MAN TRUCK & BUS UK",
                "model": "10.153"
            },
            "techRecord": {
                "bodyModel": "SIDERAL",
                "bodyMake": "SUNSUNDEGUI",
                "bodyType": "Single Decker",
                "chassisMake": "VOLVO",
                "chassisModel": "B12M",
                "brakeCode": fake.random_number(),
                "grossDesignWeight": fake.random_number(),
                "grossGbWeight": fake.random_number(),
                "grossKerbWeight": fake.random_number(),
                "grossLadenWeight": fake.random_number(),
                "retarderBrake1": "Hydraulic",
                "retarderBrake2": "Exhaust",
                "seatsLowerDeck": 49,
                "seatsUpperDeck": 0,
                "sequenceNumber": 2,
                "speedLimiterMarker": "Yes",
                "speedRestriction": 62,
                "standingCapacity": 0,
                "tachoExemptMarker": "No",
                "unladenWeight": 0,
                "dispensations": "null",
                "remarks": "null",
                "serviceA": fake.random_number(),
                "secA": fake.random_number(),
                "parkingA": fake.random_number(),
                "serviceB": fake.random_number(),
                "secB": fake.random_number(),
                "parkingB": fake.random_number(),
                "brakeData": {
                    "secondary": "SPLIT SERVICE BRAKE (DESIGNATED) OR HANDBRAKE",
                    "parking": "AXLE 2",
                    "brakeDataCode": "178202",
                    "service": "2 AXLE F/R SPLIT (AXLE 1/ AXLE 2)"
                },
                "axles": [
                    {
                        "axleNumber": 1,
                        "weights": {
                            "gbWeight": fake.random_number(),
                            "designWeight": fake.random_number()
                        },
                        "tyres": {
                            "tyreCode": fake.random_number(),
                            "tyreSize": "315/80-22.5",
                            "plyRating": "null",
                            "fitmentCode": "S",
                            "dLoadIndex": fake.random_number(),
                            "sLoadIndex": fake.random_number(),
                            "loadIndex": fake.random_number(),
                            "speedCatSymbol": "L"
                        }
                    },
                    {
                        "axleNumber": 2,
                        "weights": {
                            "gbWeight": fake.random_number(),
                            "designWeight": fake.random_number()
                        },
                        "tyres": {
                            "tyreCode": fake.random_number(),
                            "tyreSize": "315/80-22.5",
                            "plyRating": "null",
                            "fitmentCode": "D",
                            "dLoadIndex": fake.random_number(),
                            "sLoadIndex": fake.random_number(),
                            "loadIndex": fake.random_number(),
                            "speedCatSymbol": "L"
                        }
                    }
                ]
            },
            "operator": [
                {
                    "operatorLicenceNumber": "M41615O",
                    "operatorLicenceStatus": "Valid",
                    "operatorName": "PIAN"
                }
            ],
            "testHistory": [
                {
                    "location": "CHECK SITE 28698, STREET_NAME 28698, TOWN 28698, COUNTRY 28698, XY99 0ZZ",
                    "testDate": "14/10/2015",
                    "testType": "ANNUAL MV",
                    "vehicleIdentifierAtTest": "B3R9R75",
                    "testResult": "Pass",
                    "testCertificateExpiryDateAtTest": "31/10/2016",
                    "numberOfDefectsAtTest": 0,
                    "numberofAdvisoryDefectsAtTest": 1
                }
            ],
            "encounter": [
                {
                    "prohibitionNotice": "Y",
                    "prohibitionOutstanding": "N"
                }
            ]
        }
