# WIP: Mi PubSub

Asynchronius, pubish/subscriber communication in between (micro) services.
Protobuf powered RabbitMQ queues.
RabbitMQ Publish/Subscribe pattern implementation for SOA.


## Getting Started

### Prerequisites

* docker-compose, see [install guide](https://docs.docker.com/compose/install/)

### Running demo

```
# to start rabbitmq and demo containers
docker-compose up -d

# start mailer worker (consumer)
docker exec -it mipubsub_mailer_1 python main.py

# publish sample events
docker exec -it mipubsub_mailer_1 python sample_producer.py
```


## Built With

* [Python](https://docs.python.org/3/) - Main programming language
* [RabbitMQ](https://www.rabbitmq.com/) - message broker for pubsub
* [Protocol Buffers](https://developers.google.com/protocol-buffers/) - Events data structure (language-neutral)


## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* [@ArturZylinski](https://twitter.com/ArturZylinski)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone who's code was used
* Inspiration
* etc
