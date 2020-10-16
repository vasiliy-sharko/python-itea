import docker
client = docker.from_env()

client.images.pull(repository="alpine", tag="3.12")
print(client.images.list())

client.containers.run("alpine:latest", "echo hello world")
print(client.containers.list(all=True))

client.images.build(path=".", tag="test:v1")
