# fatehan

### gRPC/Protobuf message & service stubs.

## Install

```bash
pip install fatehan
```

## Usage

```python
import grpc
from fatehan.devices import devices_pb2, devices_pb2_grpc

channel = grpc.insecure_channel("localhost:50051")
stub = devices_pb2_grpc.DeviceServiceStub(channel)  # replace with your actual service
resp = stub.GetDevice(devices_pb2.GetDeviceRequest(id="123"))
print(resp)
```

## Compile

```bash
python -m grpc_tools.protoc \
  -I ../protocols \
  --python_out=. \
  --grpc_python_out=. \
  --pyi_out=. \
  $(find ../protocols -name "*.proto" -print)

```

## Build And Test Locally
```bash
python -m pip install --upgrade build twine
python -m build
python -m twine check dist/*
```

## Try a local install
```bash
python -m venv .venv && . .venv/bin/activate
pip install dist/fatehan-0.2.0-py3-none-any.whl
python -c "from devices import devices_pb2; print('ok', bool(devices_pb2))"
```

## Publish
```bash
python -m twine upload dist/*
```