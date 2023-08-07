# Python/Docker demo

## Building the container
`docker build . -t py_docker`

## Running the container
`docker run --rm -it -p 80:80 --name pyd py_docker `
