# Docker Salt-Minion

A Docker Image for a Salt Minion. This image allows you to run a Salt Minion
enabled server within a Docker container. This is designed for testing purposes
of Salt States contained within a Salt Master server.

## Running the container

Simply run this docker command:

    docker run --rm -it soon/salt-minion

## Linking to a Salt Master server

You can link to a running Salt Master container by running the following
docker command:

    docker run -d soon/salt-master
    docker run --rm -it --link salt-master:salt soon/salt-minion

## Environment Variables

The following environment variables can be set:

* `LOG_LEVEL`: The level to log at, defaults to `error`

For example:

    docker run --rm -it -e LOG_LEVEL=debug soon/salt-minion

## Custom Minion Configuration

The image shares the `/etc/salt/minion.d` directory where you can place your
own minion configuration. See the Salt Stack documentation for more on
configuring a Salt Minion.
