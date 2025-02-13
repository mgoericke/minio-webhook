# minio webhook demo

Start the application:

```shell
docker compose up
```

login to minio console http://localhost:9000 as minioadmin/minioadmin


install minio client:

```shell
# osx
brew install minio/stable/mc
```

Create an alias to work with the locally running minio instance
```shell
mc alias set myminio http://localhost:9000 minioadmin minioadmin
```

Register the webhook
```shell
# docker network url to webhook server
mc admin config set myminio/ notify_webhook:1 endpoint="http://webhook-server:5001/webhook"
```

Restart minio

```shell
docker compose down
docker compose up
```

Create a bucket:
```shell
mc mb myminio/mybucket
```

Enable notifications for the bucket
```shell
mc event add myminio/mybucket arn:minio:sqs::1:webhook --event "put"
```


verify webhook destination was successfully created:

* login to minio console http://localhost:9000 as minioadmin/minioadmin
* Events -> Event Destination webhook:1 is only


Copy a file to minio
```shell
mc cp README.md myminio/mybucket/pfad1/README_1.md
```

Verify file copied to mybucket/pfad1/README_1.md AND also to mybucket/zweiter-pfad/README_1.md 