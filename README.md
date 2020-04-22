# dynamoimport-utility
This is a project in which we can first beautify the seed data json file into DynamoDB compatible data and then run the python script for importing the seed data into the AWS DynamoDB table.

Here are the steps on how to use this utility.

- Run the command : json-dynamo-putrequest Test seed_data.json --beautify >> seed_data_dynamodb.json
This will convert the seed data into DynamoDb compatible data.
- Check if the file named "seed_data_dynamodb.json" is created after the running the above command.
- Run the command : python dynamoimport.py
This will execute the python script which will insert the data into DynamoDB table.

NOTE : Kindly make sure to run aws configure and set your credentials as well as config where you want to insert the data into DynamoDB table.
