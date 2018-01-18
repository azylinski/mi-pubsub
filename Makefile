build:
	mkdir -p src/proto/
	protoc -I=schemas/events/ --python_out=src/proto/ schemas/events/*.proto

all:
	build
