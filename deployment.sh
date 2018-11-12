echo "Deploy $STACK_NAME stack"

chungpaakhang170155063$STACK_NAME=my$STACK_NAME
aws s3 mb s3://$sourcebucket --region $REGION
rm package.yaml
sam package --template-file template.yaml --s3-bucket $sourcebucket --output-template-file package.yaml

aws cloudformation deploy --stack-name $STACK_NAME --template-file package.yaml \
--region $REGION --capabilities CAPABILITY_IAM \
--parameter-overrides \
    RunUnitTest="true"
