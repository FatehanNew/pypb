from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CameraRequest(_message.Message):
    __slots__ = ("device_id", "serial_number", "attach_request", "detach_request")
    class Attach(_message.Message):
        __slots__ = ("channel_number", "data_type", "stream_type")
        CHANNEL_NUMBER_FIELD_NUMBER: _ClassVar[int]
        DATA_TYPE_FIELD_NUMBER: _ClassVar[int]
        STREAM_TYPE_FIELD_NUMBER: _ClassVar[int]
        channel_number: int
        data_type: int
        stream_type: int
        def __init__(self, channel_number: _Optional[int] = ..., data_type: _Optional[int] = ..., stream_type: _Optional[int] = ...) -> None: ...
    class Detach(_message.Message):
        __slots__ = ("control", "channel_number", "disabler", "stream_type")
        CONTROL_FIELD_NUMBER: _ClassVar[int]
        CHANNEL_NUMBER_FIELD_NUMBER: _ClassVar[int]
        DISABLER_FIELD_NUMBER: _ClassVar[int]
        STREAM_TYPE_FIELD_NUMBER: _ClassVar[int]
        control: int
        channel_number: int
        disabler: int
        stream_type: int
        def __init__(self, control: _Optional[int] = ..., channel_number: _Optional[int] = ..., disabler: _Optional[int] = ..., stream_type: _Optional[int] = ...) -> None: ...
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    ATTACH_REQUEST_FIELD_NUMBER: _ClassVar[int]
    DETACH_REQUEST_FIELD_NUMBER: _ClassVar[int]
    device_id: int
    serial_number: int
    attach_request: CameraRequest.Attach
    detach_request: CameraRequest.Detach
    def __init__(self, device_id: _Optional[int] = ..., serial_number: _Optional[int] = ..., attach_request: _Optional[_Union[CameraRequest.Attach, _Mapping]] = ..., detach_request: _Optional[_Union[CameraRequest.Detach, _Mapping]] = ...) -> None: ...

class CameraEvent(_message.Message):
    __slots__ = ("device_id", "serial_number", "started", "publish", "publish_done", "record", "idle_timeout", "receive_timeout")
    class Started(_message.Message):
        __slots__ = ("stream", "protocol", "remote_addr", "sink")
        STREAM_FIELD_NUMBER: _ClassVar[int]
        PROTOCOL_FIELD_NUMBER: _ClassVar[int]
        REMOTE_ADDR_FIELD_NUMBER: _ClassVar[int]
        SINK_FIELD_NUMBER: _ClassVar[int]
        stream: str
        protocol: int
        remote_addr: str
        sink: str
        def __init__(self, stream: _Optional[str] = ..., protocol: _Optional[int] = ..., remote_addr: _Optional[str] = ..., sink: _Optional[str] = ...) -> None: ...
    class Publish(_message.Message):
        __slots__ = ("stream", "protocol", "remote_addr", "sink")
        STREAM_FIELD_NUMBER: _ClassVar[int]
        PROTOCOL_FIELD_NUMBER: _ClassVar[int]
        REMOTE_ADDR_FIELD_NUMBER: _ClassVar[int]
        SINK_FIELD_NUMBER: _ClassVar[int]
        stream: str
        protocol: int
        remote_addr: str
        sink: str
        def __init__(self, stream: _Optional[str] = ..., protocol: _Optional[int] = ..., remote_addr: _Optional[str] = ..., sink: _Optional[str] = ...) -> None: ...
    class PublishDone(_message.Message):
        __slots__ = ("stream", "protocol", "remote_addr", "sink")
        STREAM_FIELD_NUMBER: _ClassVar[int]
        PROTOCOL_FIELD_NUMBER: _ClassVar[int]
        REMOTE_ADDR_FIELD_NUMBER: _ClassVar[int]
        SINK_FIELD_NUMBER: _ClassVar[int]
        stream: str
        protocol: int
        remote_addr: str
        sink: str
        def __init__(self, stream: _Optional[str] = ..., protocol: _Optional[int] = ..., remote_addr: _Optional[str] = ..., sink: _Optional[str] = ...) -> None: ...
    class Record(_message.Message):
        __slots__ = ("stream", "protocol", "remote_addr", "sink")
        STREAM_FIELD_NUMBER: _ClassVar[int]
        PROTOCOL_FIELD_NUMBER: _ClassVar[int]
        REMOTE_ADDR_FIELD_NUMBER: _ClassVar[int]
        SINK_FIELD_NUMBER: _ClassVar[int]
        stream: str
        protocol: int
        remote_addr: str
        sink: str
        def __init__(self, stream: _Optional[str] = ..., protocol: _Optional[int] = ..., remote_addr: _Optional[str] = ..., sink: _Optional[str] = ...) -> None: ...
    class IdleTimeout(_message.Message):
        __slots__ = ("stream", "protocol", "remote_addr", "sink")
        STREAM_FIELD_NUMBER: _ClassVar[int]
        PROTOCOL_FIELD_NUMBER: _ClassVar[int]
        REMOTE_ADDR_FIELD_NUMBER: _ClassVar[int]
        SINK_FIELD_NUMBER: _ClassVar[int]
        stream: str
        protocol: int
        remote_addr: str
        sink: str
        def __init__(self, stream: _Optional[str] = ..., protocol: _Optional[int] = ..., remote_addr: _Optional[str] = ..., sink: _Optional[str] = ...) -> None: ...
    class ReceiveTimeout(_message.Message):
        __slots__ = ("stream", "protocol", "remote_addr", "sink")
        STREAM_FIELD_NUMBER: _ClassVar[int]
        PROTOCOL_FIELD_NUMBER: _ClassVar[int]
        REMOTE_ADDR_FIELD_NUMBER: _ClassVar[int]
        SINK_FIELD_NUMBER: _ClassVar[int]
        stream: str
        protocol: int
        remote_addr: str
        sink: str
        def __init__(self, stream: _Optional[str] = ..., protocol: _Optional[int] = ..., remote_addr: _Optional[str] = ..., sink: _Optional[str] = ...) -> None: ...
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    STARTED_FIELD_NUMBER: _ClassVar[int]
    PUBLISH_FIELD_NUMBER: _ClassVar[int]
    PUBLISH_DONE_FIELD_NUMBER: _ClassVar[int]
    RECORD_FIELD_NUMBER: _ClassVar[int]
    IDLE_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    RECEIVE_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    device_id: int
    serial_number: int
    started: CameraEvent.Started
    publish: CameraEvent.Publish
    publish_done: CameraEvent.PublishDone
    record: CameraEvent.Record
    idle_timeout: CameraEvent.IdleTimeout
    receive_timeout: CameraEvent.ReceiveTimeout
    def __init__(self, device_id: _Optional[int] = ..., serial_number: _Optional[int] = ..., started: _Optional[_Union[CameraEvent.Started, _Mapping]] = ..., publish: _Optional[_Union[CameraEvent.Publish, _Mapping]] = ..., publish_done: _Optional[_Union[CameraEvent.PublishDone, _Mapping]] = ..., record: _Optional[_Union[CameraEvent.Record, _Mapping]] = ..., idle_timeout: _Optional[_Union[CameraEvent.IdleTimeout, _Mapping]] = ..., receive_timeout: _Optional[_Union[CameraEvent.ReceiveTimeout, _Mapping]] = ...) -> None: ...
