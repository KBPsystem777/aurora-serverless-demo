# aurora-serverless-demo

Demo for Aurora RDS Serverless.
Building a Lambda function that uses Amazon Aurora as a serverless database.

## Steps

### Aurora RDS

- Create an Aurora RDS Instance from AWS Console
- Enable the Serverless capacity option
- Once database is created, create `Customers` table that accepts `CustomerId` and `FirstName` as keys.
- Insert dummy data on the Customers table

### Lambda

- Create a Lambda function that fetches the content of `Customer` table in the database. See sample code.

### IAM

- Create a new Lambda role which has the following policies: `AmazonRDSFullAccess`, `AmazonRDSDataFullAccess`, `AWSLambdaBasicExecutionRole` (for the sake of demo, we will give them a full access on these policies).
- Once created, assig this role on the Lambda function you created.
