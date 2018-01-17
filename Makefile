build:
	mkdir -p src/proto/
	protoc -I=schemas/ --python_out=src/proto/ schemas/events/*.proto

all:
	build
