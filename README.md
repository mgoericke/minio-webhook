install minio client:

```
brew install minio/stable/mc
```

```
bash +o history
mc alias set myminio http://localhost:9000 aumpB204wspLZO3w2RND mHXwzhY5ZziL33qqYPuAaHdTkh56Oms2WHeDU5Ay
bash -o history
```

```
# docker network url to webhook server
mc admin config set myminio/ notify_webhook:1 endpoint="http://webhook-server:5001/webhook"
#mc admin service restart myminio
mc event add myminio/meinbucket arn:minio:sqs::1:webhook --event "put"
```

```
mc cp README.md myminio/meinbucket/pfad1/README_1.md
```