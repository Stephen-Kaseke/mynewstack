from constructs import Construct
from aws_cdk import (
    Duration,
    Stack,
    aws_s3 as _s3,
    aws_iam as iam,
    aws_sqs as sqs,
    aws_sns as sns,
    aws_s3_notifications as s3n,
    aws_sns_subscriptions as subs,
)


class MynewstackStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        queue = sqs.Queue(
            self, "MynewstackQueue",
            visibility_timeout=Duration.seconds(300),
        )

        topic = sns.Topic(
            self, "MynewstackTopic"
        )

        topic.add_subscription(subs.SqsSubscription(queue))
        email_address = "ttendaim@gmail.com"

        topic.add_subscription(subs.EmailSubscription(email_address))
        
        bucket=_s3.Bucket(
            self,
            "myBucketId",
            bucket_name="bhaghidi2022",
        )
        bucket.add_event_notification(_s3.EventType.OBJECT_CREATED_PUT, s3n.SnsDestination(topic))