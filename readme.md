# Python/Docker demo

## Building the container
`docker build . -t py_docker`

## Running the container
`docker run --rm -it -p 5000:5000 --name pyd py_docker`
